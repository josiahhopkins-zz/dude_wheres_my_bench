import picamera
import time
import os
import send_sms
import image_processor
# import <josiah>
# import <phansa>

def main():
    camera = picamera.PiCamera()
    image_pth = 'image{}.jpg'
    img_proc = image_processor()
    counter = 0
    try:
        while True:
            occupied = False
            send_to_aws = False
            camera.capture(image_pth.format(counter%5))
            print('Taking picture number', counter, 'at', time.gmtime().tm_min)
            img_proc.add_image(image_pth)
            if counter%5 == 0:
                send_to_aws = img_proc.make_decision()
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
