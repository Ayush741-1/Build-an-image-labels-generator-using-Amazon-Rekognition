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
    image_keys = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg', 'image6.jpg']  # List of image file names

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
