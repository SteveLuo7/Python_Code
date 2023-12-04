from captcha.image import ImageCaptcha
from PIL import Image
import random
import string

def generate_captcha():
    # Generate a random string for the CAPTCHA
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Create an ImageCaptcha object
    captcha = ImageCaptcha()

    # Generate the CAPTCHA image
    image = captcha.generate(captcha_text)

    # Save the image to a file
    image_path = f'captcha_{captcha_text}.png'
    captcha.write(captcha_text, image_path)

    # Open and display the generated image (optional)
    Image.open(image_path).show()

if __name__ == "__main__":
    generate_captcha()
