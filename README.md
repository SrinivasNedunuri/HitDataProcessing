Hitdata processing to analyze search engine and keyword performance
==============================
Hit data is the dataset that captures the clicks and user sessions from search event to purchase event. Analyzing hit data is crucial for e-commerce companies to analyze how well a search engine, a keyword or a combination of both are performing in terms of revenue, number of orders etc. Mining hit data and anlyzing it can help companies make informed decisions on marketing spend, product stocking, popular products etc.
This project is focused on answering one such business question - 
How much revenue is the client getting from external Search Engines, such as Google, Yahoo and MSN, and which keywords are performing the best based on revenue?

Data Overview
------------
![image](https://user-images.githubusercontent.com/54639431/139508834-361a6d67-985f-444b-a6e8-7f4d4815594f.png)

Getting Started
------------
Tools used for development, continous integration and deployment:
1. python 3.7: This project built using only inbuilt modules hence no extra package installations are required
2. GitHub: Workflow scripts for Continous Integration and Continous Deployments
3. AWS account
4. EC2 free tier account: For hosting the application
5. AWS Code deploy: Integrates with GitHub to continously deploy the repo whenever code is pushed into main branch

Running application 

`python3 HDataProcessing.py -f input/data[4][63][84][3][80].tsv`

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
        
Application Overview
------------
1. HitDataProcessor class is designed in such a way that it would work with any HitData with referrer urls and product attributes.
2. For now, the application can answer only How much revenue is the client getting from external Search Engines, such as Google, Yahoo and
MSN, and which keywords are performing the best based on revenue? But it can be further enhanced to answer even more questions. 
3. For finding out the class functionalities and attributes pleasse go through the HDataProcessing.py. It is all nicely documented with docstrings.
4. There are couple of assumption in the implementation one is no overlapping sessions for an ip (i.e) if a session starts, new session cannot be started until
   first session(that involves purchase event) ends for an ip and the other data is ordered by hit_gmt_time in ascending order.
 
TO DO:
------------
1. Unit test cases
2. Serverless deployment
3. Business problem presenation

