import picamera
# import <josiah class>

def main():
    camera = picamera.PiCamera()
    image_pth = 'image.jpg'
    try:
        while True:
            camera.capture(image_pth)
            # <josiah>.picture(image_pth)
            time.sleep(2)
    except KeyboardInterrupt:
        print('interrupted!')

main()
