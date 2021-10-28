import argparse
import csv
import configparser
import time
import sys

sys.path.insert(0, 'HitData.py')
from HitData import HitData

config = configparser.ConfigParser()
config.read('config.conf')
EXPECTED_COLUMNS = config['mapping']['known_columns'].split('\n')
MANDATORY_COLUMNS = set(['event_list', 'product_list', 'referrer'])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', help='Hit data file to be processed', required=True)
    args = parser.parse_args()
    file = args.filename

    try:
        with open(file) as tsv_file:
            reader = csv.DictReader(tsv_file, delimiter='\t')
            obj = HitData(reader)
            print('Extra columns in file', set(obj.columns) - set(EXPECTED_COLUMNS))
            missing_cols = set(EXPECTED_COLUMNS) - set(obj.columns)
            print('Missing columns in file', missing_cols)

            for col in MANDATORY_COLUMNS:
                if col in missing_cols:
                    raise ValueError('Mandatory field for processing HitData is missing')

            start = time.time()
            obj.merge_referrer_purchase()
            obj.build_referrer_revenue()
            end = time.time()
            print("Took %f ms" % ((end - start) * 1000.0))
            obj.write_output()

    except IOError as e:
        print('Provided filename/file location is not valid -->', e)


if __name__ == '__main__':
    main()