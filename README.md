Hitdata processing to analyze search engine and keyword performance
==============================
Hit data is the dataset that captures the clicks and user sessions from search event to purchase event. Analyzing hit data is crucial for e-commerce companies to analyze how well a search engine, a keyword or a combination of both are performing in terms of revenue, number of orders etc. Mining hit data and anlyzing it can help companies make informed decisions on marketing spend, product stocking, popular products etc.
This project is focused on answering one such business question - 
How much revenue is the client getting from external Search Engines, such as Google, Yahoo and MSN, and which keywords are performing the best based on revenue?

Data Overview
------------
![image](https://user-images.githubusercontent.com/54639431/139508834-361a6d67-985f-444b-a6e8-7f4d4815594f.png)

Development
------------
class: HitDataProcessor
    A class to represent Hitdata file object and process it
    Attributes: dict_reader_obj (:obj:csv.DictReader): iterator yields each row as ordered dictionary.
                output_header (list) : Desired output header
                product_attr (list): List of product attributes
                event_list (dict): event description by event_id
                client (str): client website.
                output_f (str): output file name
    Methods: 
                write_output - Method to write out list of rows to an output path specified
                Args:
                    list_of_rows (list) : list of tuples
--------
Getting Started
------------
Tools used for development, continous integration and deployment:
1. python 3.7: This project built using only inbuilt modules hence no extra package installations are required
2. GitHub: Workflow scripts for Continous Integration and Continous Deployments
3. AWS account
4. EC2 free tier account: For hosting the application
5. AWS Code deploy: Integrates with GitHub to continously deploy the repo whenever code is pushed into main branch

Running application 

`python3 - HDataProcessing.py -f input/data[4][63][84][3][80].tsv`

Project Organization
------------

    ├── README.md         
    ├── input
    │   └── data[4][63][84][3][80]                      
    ├── output                    
    ├── HDataProcessing.py <- main excecutable
    ├── config.conf        
    ├── appspec.yml        <- Application specification file in yaml format for codedeploy to deploy the code in aws ec2
    │
    └── .github         
        │
        ├── workflows           
            └── main.yml   <- Workflow script for github action CI/CD
        


