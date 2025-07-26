from PIL import Image


def decode_image(image_path, output_path):
    img = Image.open(image_path)
    width, height = img.size

    pixels = img.load()

    # iterating through all the pixels
    for y in range(height):
        for x in range(width):
            current_pixel = pixels[x, y]
            new_pixel = (0,0,0,255)
            if current_pixel[0] & 0b00000011 > 2:
                # setting the pixel to to white if there is data on the least significant bit of that pixel
                new_pixel = (255, 255, 255, 255)

            # updating the pixel with new pixel
            pixels[x, y] = new_pixel

    img.save(output_path)        


