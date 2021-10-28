from collections import defaultdict
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import csv

class HitData:
    output_header = ['Search Engine Domain', 'Search Keyword', 'Revenue']
    product_attr = ['Category', 'Product Name', 'Number of Items', 'Total Revenue', 'Custom Event',
                    'Merchandising eVar']

    def __init__(self, dict_reader_obj):
        self.client = 'esshopzilla.com'
        self.reader = dict_reader_obj
        self.columns = self.reader.fieldnames
        self.rev_by_ref_keyword = defaultdict(lambda: defaultdict(int))
        self.output_filename = datetime.today().strftime('%Y-%m-%d') + '_SearchKeywordPerformer.tab'
        self.output = []
        self.ip_dict = {}
        self.purchase = defaultdict(list)
        self.referrer = defaultdict(list)

    @staticmethod
    def get_url_domain(parser):
        if parser.netloc.startswith('www.'):
            return parser.netloc[4:]
        else:
            return parser.netloc

    @staticmethod
    def get_url_keyword(parser):
        tags = parse_qs(parser.query)
        keyword = []
        if tags.get('q'):
            keyword = tags['q']
        if tags.get('p'):
            keyword = tags['p']
        return keyword[0].lower()

    @staticmethod
    def get_product_revenue(product_str):
        product_dict = {}
        product_list = product_str.split(';')
        for i in range(len(HitData.product_attr)):
            try:
                product_dict[HitData.product_attr[i]] = product_list[i]
            except IndexError:
                product_dict[HitData.product_attr[i]] = ''
        return product_dict

    def build_referrer(self, ip, referrer_url):
        parse = urlparse(referrer_url)
        domain = self.get_url_domain(parse)
        if domain != self.client:
            keyword = self.get_url_keyword(parse)
            self.referrer[ip].append({'referrer': domain, 'keyword': keyword})

    def build_product_purchase(self, ip, product_list):
        self.purchase[ip].append(self.get_product_revenue(product_list))

    def merge_referrer_purchase(self):
        for row in self.reader:
            if row['event_list'] == '1':
                self.build_product_purchase(row['ip'], row['product_list'])
            else:
                self.build_referrer(row['ip'], row['referrer'])

    def build_referrer_revenue(self):
        for ip, referrers in self.referrer.items():
            num_of_referrers = len(referrers)
            if ip in self.purchase:
                num_of_purchases = len(self.purchase[ip])
                if num_of_referrers == num_of_purchases == 1:
                    try:
                        ref = referrers[0]['referrer']
                        key = referrers[0]['keyword']
                        self.rev_by_ref_keyword[ref][key] += int(self.purchase[ip][0]['Total Revenue'])
                    except ValueError:
                        pass
                else:
                    for referrer in referrers:
                        key = referrer['keyword']
                        for purchase in self.purchase[ip]:
                            if key in purchase['Product Name']:
                                try:
                                    ref = referrer['referrer']
                                    key = referrer['keyword']
                                    self.rev_by_ref_keyword[ref][key] += int(self.purchase[ip]['Total Revenue'])
                                    matched = True
                                except ValueError:
                                    pass
                        if not matched:
                            self.rev_by_ref_keyword[ref][key] += 0

            else:
                for referrer in referrers:
                    self.rev_by_ref_keyword[referrer['referrer']][referrer['keyword']] += 0

    def sort_by_revenue(self):
        lis = self.rev_by_ref_keyword.items()
        for key, value in lis:
            for k, v in value.items():
                self.output.append(tuple([key, k, v]))
        self.output.sort(key=lambda x: x[2], reverse=True)

    def write_output(self):
        self.sort_by_revenue()
        with open(self.output_filename, 'w') as out_file:
            writer_obj = csv.writer(out_file, delimiter='\t')
            writer_obj.writerow(HitData.output_header)
            writer_obj.writerows(line for line in self.output)
