import json
import boto3
import pprint
import urllib.request

def lambda_handler(event, context):

    def detect_labels():

        # 1. create a client object, to connect to rekognition
        client=boto3.client('rekognition')

        # 2. set parameters of image url, which will be sent to Rekognition
        url = event['body']
        img_path = '/tmp/image'

        # 3. Download image to lambda temporary storage
        image = urllib.request.urlopen(url).read()

        # 4. call Rekognition, store result in 'response'
        response = client.detect_labels(
                Image={
                    'Bytes': image
                    },
                MaxLabels=20,
                )

        # 5. extract number of cats
        for label in response['Labels']:
            # if 'Name' in label.keys() and label['Name'] == 'Cat':
            if label['Name'] == 'Cat':
                response['cat_count'] = len(label['Instances'])

                # 5.a Optional - Add a 'conservative cutoff'
                # response['convervative_cat_count'] = \
                # len([instance for instance in label['Instances'] if instance['Confidence'] > 70])

        #6. Return response from function
        return response


    # Call detect_labels
    response = detect_labels()

    # Return results to API gateway
    return {
        'statusCode': 200,
        'body': json.dumps(response)
        }

