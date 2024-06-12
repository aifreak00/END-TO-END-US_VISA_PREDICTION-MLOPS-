# from us_visa.pipline.training_pipeline import TrainPipeline


# pipline  = TrainPipeline()
# pipline.run_pipeline()

# from us_visa.configuration.mongo_db_connection import MongoDBClient

# ins = MongoDBClient()

# import os

# # Print the value of MONGODB_URL
# print("MONGODB_URL:", os.getenv("MONGODB_URL"))

# from pymongo import MongoClient
# import os

# # Retrieve the MongoDB URL from the environment variable
# mongodb_url = os.getenv("MONGODB_URL")

# # Connect to the MongoDB instance
# client = MongoClient(mongodb_url)

# # Example: List databases to verify connection
# print(client.list_database_names())



# import boto3
# import os

# def test_aws_credentials():
#     try:
#         # Create an S3 client
#         s3 = boto3.client('s3')
        
#         # List S3 buckets
#         response = s3.list_buckets()
        
#         # Print the bucket names
#         print("S3 Buckets:")
#         for bucket in response['Buckets']:
#             print(f"  {bucket['Name']}")
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     # Print AWS credentials to verify they are set correctly
#     print("AWS_ACCESS_KEY_ID:", os.getenv("AWS_ACCESS_KEY_ID"))
#     print("AWS_SECRET_ACCESS_KEY:", os.getenv("AWS_SECRET_ACCESS_KEY"))

#     # Test AWS credentials by listing S3 buckets
#     test_aws_credentials()

# from us_visa.pipline.prediction_pipeline import USvisaData, USvisaClassifier

# usvisa_data = USvisaData(
#                         continent= 'Asia',
#                         education_of_employee = 'Doctorate',
#                         has_job_experience = 'Y',
#                         requires_job_training = 'N',
#                         no_of_employees= 20000,
#                         company_age= 100,
#                         region_of_employment = 'Northeast',
#                         prevailing_wage= 10000,
#                         unit_of_wage= 'Year',
#                         full_time_position= 'Y',
#                         )

# usvisa_data = USvisaData(
#                         continent= 'Asia',
#                         education_of_employee = 'Doctorate',
#                         has_job_experience = 'N',
#                         requires_job_training = 'Y',
#                         no_of_employees= 15000,
#                         company_age= 10,
#                         region_of_employment = 'West',
#                         prevailing_wage= 1000,
#                         unit_of_wage= 'Hour',
#                         full_time_position= 'N',
#                         )
# usvisa_df = usvisa_data.get_usvisa_input_data_frame()

# model_predictor = USvisaClassifier()

# value = model_predictor.predict(dataframe=usvisa_df)[0]

# print(value)

# import os

# def check_aws_credentials():
#     access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
#     secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

#     if not access_key_id or not secret_access_key:
#         raise EnvironmentError("AWS credentials are not set properly.")
    
#     print(f"AWS_ACCESS_KEY_ID: {access_key_id}")
#     print(f"AWS_SECRET_ACCESS_KEY: {secret_access_key}")

# # Ensure to call this function before the code that requires AWS credentials
# check_aws_credentials()

# from dotenv import load_dotenv
# import os

# load_dotenv()

# def check_aws_credentials():
#     access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
#     secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

#     if not access_key_id or not secret_access_key:
#         raise EnvironmentError("AWS credentials are not set properly.")
    
#     print(f"AWS_ACCESS_KEY_ID: {access_key_id}")
#     print(f"AWS_SECRET_ACCESS_KEY: {secret_access_key}")

# # Ensure to call this function before the code that requires AWS credentials
# check_aws_credentials()
