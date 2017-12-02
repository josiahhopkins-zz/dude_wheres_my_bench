import boto3

def check_human(image_pth)
    fileName=image_pth
    bucket='whereismybenchbruh'

    client=boto3.client('rekognition')
    botoclient=boto3.client('s3')

    botoclient.upload_file(fileName, bucket, fileName)

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}},MinConfidence=75)
    
    for label in response['Labels']:
        if(label['Name'] == 'Human'):
            print('true I see human')
            print (label['Name'] + ' : ' + str(label['Confidence']))
            return True
            break;
