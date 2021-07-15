# Building a Low-Code Image Processing Application with  Bubble.io and AWS Rekognition

This is the companion code for our YouTube tutorial on building an
image-processing application with Bubble.io and AWS Rekognition.  The code here
is a lambda function that will take a base64 encoded image from Bubble (via API
Gateway), and return the number of cats the Rekognition API detects.

You can find the tutorial video on YouTube: https://www.youtube.com/watch?v=63XAZfruLJY

The rest of this README is an overview of what is covered in the tutorial video.

## 1. Orientation to Service/API
    - Try demo in browser
    - Rekognition developer guide
        - https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-dg.pdf
    - boto3 (python client) guide to Rekognition
        - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html

## 2. Write Lambda function

- IAM role needs:
    - Full access to Rekognition
    - Read access to S3 (if using)
    - Cloudwatch logs (default for lambda)

- 3 second timeout, probably want to increase

## 3. Create API w/ API Gateway
- Lambda proxy integration

## 4. Add API from (3) to Bubble
- Bubble API connector

## 5. Count Cats
- Profit

## 6. Tips
- CloudWatch needed when troubleshooting API gateway
- Pricing - Rekognition is free-tier eligible (5k images/mo)
- Limit file size before upload - compresses, much faster
- Larger images sometimes benefit from image downscaling
(in Bubble: select 'Limit image size before upload')

