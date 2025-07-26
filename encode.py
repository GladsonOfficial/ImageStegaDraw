from PIL import Image
import logging

def get_image_dimensions(file_path):
    img = Image.open(file_path)
    return img.size

def encode_image(image_file, message_file, output_file):
    img = Image.open(image_file)
    message = Image.open(message_file)

    img_width, img_height = img.size
    mes_width, mes_height = message.size

    img_pixels = img.load()
    msg_pixels = message.load()

    # This condition should never get satisfied, if it does, then issue is from where this code is called
    if (img_width != mes_width and img_height != mes_height):
        logging.error(f"The dimensions of image and message don't match")
        return
    
    # iterating through all pixels
    for y in range(img_height):
        for x in range(img_width):
            current_img_pixel = img_pixels[x, y]
            current_msg_pixel = msg_pixels[x, y]

            # Setting 2 least significant bit to 0
            new_img_pixel = (current_img_pixel[0]&0b11111100, current_img_pixel[1]&0b11111100, current_img_pixel[2]&0b11111100, 255)

            # Setting 2 least significant bit to 1 if message pixel is white
            if (current_msg_pixel[0] > 150):
                new_img_pixel = (current_img_pixel[0]|0b00000011, current_img_pixel[1]|0b00000011, current_img_pixel[2]|0b00000011, 255)
            
            # replacing the existing pixel with modified pixel
            img_pixels[x, y] = new_img_pixel


    img.save(output_file) 
             
    