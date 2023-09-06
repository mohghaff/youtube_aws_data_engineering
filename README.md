 YouTube Videos Data Analysis on AWS
Overview
This project focuses on the secure management, streamlined processing, and in-depth analysis of structured and semi-structured YouTube video data. The analysis is centered around video categories and trending metrics based on countries.

Project Goals
Data Ingestion: Developed a robust mechanism to ingest data from various sources.

ETL System: Transformed raw data into a structured format suitable for analysis.

Data Lake: Established a centralized repository to store data from multiple sources efficiently.

Scalability: Ensured the system can handle increasing data volumes effectively.

Cloud Infrastructure: Utilized AWS (Amazon Web Services) cloud services for processing large datasets.


Services Utilized
Amazon S3
Amazon Simple Storage Service (Amazon S3) was employed as an object storage service. 

AWS IAM
AWS Identity and Access Management (IAM) was used for secure management of access to AWS services and resources. It ensured that only authorized users and services can interact with the AWS infrastructure.


AWS Glue
AWS Glue is a serverless data integration service that simplifies data discovery, preparation, and combination for analytics, machine learning, and application development. It played a key role in the ETL (Extract, Transform, Load) process.

AWS Lambda
AWS Lambda enables serverless computing, allowing for code execution without the need to manage servers. It played a role in transforming json files into parquet files as part of data processing.

AWS Athena
AWS Athena is an interactive query service for data stored in Amazon S3. It eliminated the need to load data into a separate database, enabling ad-hoc querying of data in its native format.

Dataset Used
The project leverages a dataset obtained from Kaggle, containing statistics in CSV format. The dataset encompasses daily statistics of popular YouTube videos spanning several months. Key data points include video title, channel title, publication time, tags, views, likes, dislikes, description, and comment count. Additionally, a category_id field, specific to each region, is available in a linked JSON file.
