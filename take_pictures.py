import picamera
import time
import os
# import <josiah>
# import <evan>
# import <phansa>

def main():
    camera = picamera.PiCamera()
    image_pth = 'image.jpg'
    try:
        while True:
            occupied = False
            send_to_aws = False
            camera.capture(image_pth)
            print('Taking picture at', time.gmtime().tm_min)
            # send_to_aws = <josiah>.picture(image_pth)
            print('Should I send this to aws?', send_to_aws)
            if send_to_aws:
                print('Sending to aws')
                # occupied = <phansa>.send_to_aws()
                print('Is it occupied?', occupied)
                if not occupied:
                    print('Sending out text')
                    # <evan>.send_text()
            time.sleep(3)
    except KeyboardInterrupt:
        print('interrupted!')

main()
