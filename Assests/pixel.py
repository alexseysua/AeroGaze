import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

class ImageViewer:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.image)

        # Get image dimensions
        width, height = self.image.size

        # Draw x-axis
        self.ax.axhline(y=height/2, color='red', linestyle='--', linewidth=2)
        self.ax.axhline(y=743.0, color='pink', linestyle='--', linewidth=2)

        # Draw y-axis
        self.ax.axvline(x=width/2, color='blue', linestyle='--', linewidth=2)
        self.ax.axvline(x=787.5, color='pink', linestyle='--', linewidth=2)

        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.on_click)

    def on_click(self, event):
        if event.inaxes == self.ax:
            x, y = int(event.xdata), int(event.ydata)
            pixel_value = self.image.getpixel((x, y))
            print(f"Clicked at (x={x}, y={y}), Pixel Value: {pixel_value}")

if __name__ == "__main__":
    # Replace 'your_photo.jpg' with the path to your photo
    photo_path = '/home/abinashlingank/Main/Pilote/Rasyolo/runs/detect/exp55/quad3.jpg'

    viewer = ImageViewer(photo_path)
    plt.show()
