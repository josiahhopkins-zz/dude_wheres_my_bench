import picamera
import time
import os
import send_sms
# import <josiah>
# import <phansa>

def main():
    camera = picamera.PiCamera()
    image_pth = 'image{}.jpg'
    counter = 0
    try:
        while True:
            occupied = False
            send_to_aws = False
            camera.capture(image_pth.format(counter%4))
            print('Taking picture at', time.gmtime().tm_min)
            # send_to_aws = <josiah>.picture(image_pth)
            print('Should I send this to aws?', send_to_aws)
            if send_to_aws:
                print('Sending to aws')
                # occupied = <phansa>.send_to_aws()
                print('Is it occupied?', occupied)
                if not occupied:
                    print('Sending out text')
                    send_sms.send()
            counter += 1
            time.sleep(3)
    except KeyboardInterrupt:
        print('interrupted!')

main()
