# Build-an-image-labels-generator-using-Amazon-Rekognition

2.1 Project Overview
In this project, you'll create an image labels generator using Amazon Rekognition. Amazon Rekognition is a service that makes it easy to add image and video analysis to your applications. You will use Amazon S3 to store images and AWS CLI to interact with AWS services.

2.2A Create S3 Bucket and Upload Images
Create an S3 bucket:

Sign in to the AWS Management Console.
Navigate to the S3 service.
Click on "Create bucket."
Enter a unique name for your bucket (e.g., my-image-labels-bucket).
Select the region.
Leave the other settings as default and click "Create bucket."
Upload images to the S3 bucket:

Open your newly created bucket.
Click on "Upload."
Add files and select the images you want to upload.
Click "Upload."

2.2B Install and Configure AWS CLI
Install AWS CLI:

Follow the instructions to install AWS CLI from the official AWS documentation: AWS CLI Installation.
Configure AWS CLI:

Open your terminal or command prompt.
Run aws configure.
Enter your AWS Access Key ID, AWS Secret Access Key, default region name (e.g., us-west-2), and default output format (e.g., json).

2.2C Import Libraries
In your Python script, you'll need to import the necessary libraries. Create a new Python file (e.g., image_labels_generator.py) and add the following imports:

python code
    
2.2D Define Functions
Detect Labels Function:
This function uses the Amazon Rekognition detect_labels API to detect labels in an image stored in your S3 bucket.

2.2E Final Code
Combine all parts into your Python script:

python:

import boto3
import json

def detect_labels(bucket, key):
    client = boto3.client('rekognition')
    
    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key,
            }
        },
        MaxLabels=10,
        MinConfidence=75
    )
    
    return response['Labels']

def print_labels(image, labels):
    print(f"Labels for {image}:")
    for label in labels:
        print(f"  Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%")
    print()

def main():
    bucket = 'codepen-kattyan'  # Your S3 bucket name
    image_keys = ['image1.jpg', 'image2.jpg', 'image3.jpg']  # List of image file names

    print("Available images:")
    for index, key in enumerate(image_keys):
        print(f"{index + 1}. {key}")

    choice = int(input("Enter the number of the image you want to process: ")) - 1

    if 0 <= choice < len(image_keys):
        selected_image = image_keys[choice]
        print(f"\nProcessing image: {selected_image}\n")
        labels = detect_labels(bucket, selected_image)
        print_labels(selected_image, labels)
    else:
        print("Invalid choice. Please select a valid number from the list.")

if __name__ == "__main__":
    main()
    
2.2F Running Your Project
Step-by-Step Instructions:
1. Run the script:

Open your terminal or command prompt.
Navigate to the directory containing your image_labels_generator.py script.
Run the script by executing: python image_labels_generator.py.

2. Output:

The script will print the labels and confidence scores for the specified image. For example:

Label: Person, Confidence: 99.24%
Label: Human, Confidence: 99.24%
Label: Clothing, Confidence: 97.56%
Label: Apparel, Confidence: 97.56%
...

2.3 Conclusion & Clean-up
Conclusion:
You've successfully created an image labels generator using Amazon Rekognition.
You learned how to create an S3 bucket, upload images, configure AWS CLI, and use the Rekognition service to detect labels in images.
Clean-up:
Delete the images from your S3 bucket:

Navigate to your S3 bucket in the AWS Management Console.
Select the images you uploaded.
Click on "Delete" to remove them.
Delete the S3 bucket:

If you no longer need the S3 bucket, you can delete it by selecting the bucket and clicking on "Delete bucket."
Clean up AWS resources:

Ensure no unwanted AWS resources are running to avoid unnecessary charges.
By following these steps, you will have a functioning image labels generator using Amazon Rekognition and understand the process of interacting with AWS services through Python and the AWS CLI.
