from time import sleep
# import picamera
import sys
sys.path.append("..")
from Constants import focalLength, sensorDim, imgDim
from Constants import flightHeight

def capture_image(file_path):
    with picamera.PiCamera() as camera:
        # Adjust camera settings as needed
        # camera.resolution = (width, height)
        # camera.rotation = 180 # If your camera is upside down, you can rotate the image
        
        # Capture an image
        camera.capture(file_path)
        print("Image captured successfully!")

def getGSD():
    GSDh =  (flightHeight * sensorDim[0]) / (focalLength * imgDim[0])
    GSDw =  (flightHeight * sensorDim[1]) / (focalLength * imgDim[1])
    return GSDh, GSDw

# print(getGSD())