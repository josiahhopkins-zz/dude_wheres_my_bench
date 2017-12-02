
import boto3

if __name__ == "__main__":
    fileName='evan.jpg'
    bucket='whereismybenchbruh'

    client=boto3.client('rekognition')
    botoclient=boto3.client('s3')

    botoclient.upload_file(fileName, bucket, fileName)

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}},MinConfidence=75)

    print('Detected labels for ' + fileName)


    for label in response['Labels']:
        if(label['Name'] == 'Human'):
            print('true I see human')
            print (label['Name'] + ' : ' + str(label['Confidence']))
            break;
