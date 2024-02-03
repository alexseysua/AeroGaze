from PIL import Image

def get_image_dimensions(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e:
        print(f"Error: {e}")
        return None

# Replace 'your_photo.jpg' with the path to your photo
photo_path = '/home/abinashlingank/Pilote/RasYolo/pic.png'

dimensions = get_image_dimensions(photo_path)

if dimensions:
    width, height = dimensions
    print(f"Width: {width}px, Height: {height}px")
