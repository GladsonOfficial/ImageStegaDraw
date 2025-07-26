from PIL import Image
FILE_PATH = 'rough/secret_message.jpg'      # Enter the path of file to be analyzed here

img = Image.open(FILE_PATH)        

width, height = img.size
print(f'the dimensions are {width}x{height}')       # The dimension on the picture

pixels = img.load()

csv_file = open('rough/output.csv', 'w')            # output csv file

for y in range(height):
    current_line = ""
    first_column = True
    for x in range(width):
        current_pixel = pixels[x, y]
        hex_code = f'#{hex(pixels[x, y][0])[2:]}{hex(pixels[x, y][1])[2:]}{hex(pixels[x, y][2])[2:]}'   # converting the rgba to hex code
        if first_column:
            current_line += hex_code
        else:
            current_line += ',' + hex_code

    current_line += '\n'                                # moving to next life after completion of the row
    csv_file.write(current_line)                        # writing the line to csv file
        