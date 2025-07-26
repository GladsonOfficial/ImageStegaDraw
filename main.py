import os
import draw_message
import encode
import decode
import draw_message

SECRET_MESSAGE_PATH = 'output/secret_message.jpg'
IMAGE_WITH_SECRET_MESSAGE_PATH = 'output/image_with_secret_image.png'

def get_image_from_user():
    while True:
        file_path = input("Enter the file path: ")
    
        if not os.path.exists(file_path):
            print("The path does not exist, please enter correct path")
            continue
         
        return file_path


def encrypt_mode():
    print(f"\n--ENCRYPT--\n")
    file_path = get_image_from_user()
    width, height = encode.get_image_dimensions(file_path)
    draw_message.create_drawing_canvas(width, height)
    encode.encode_image(file_path, SECRET_MESSAGE_PATH, IMAGE_WITH_SECRET_MESSAGE_PATH)
    print(f"The image with secret message can be found at {IMAGE_WITH_SECRET_MESSAGE_PATH}")
    print(f"The secret message is saved in {SECRET_MESSAGE_PATH}, delete it if not required.")
    os.system('pause')


def decrypt_mode():
    print(f"\n--DECRYPT--\n")
    file_path = get_image_from_user()
    while True:
        output_path = input('Enter path for output (default: /output/secret_message.png): ') 
        if output_path == "":
            output_path = 'output/secret_message.png'
            print(f'Using default path: {output_path}')
            if not os.path.exists('output'):
                os.mkdir('output')
            break
        
        if '\\' in output_path or '/' in output_path:
            output_path = output_path.replace('\\', '/')
            folder_path = '/'.join(output_path.split('/')[:-1])
            if not os.path.exists(folder_path):
                print('Path is invalid')
                continue
            break
        
        break    
    
    if output_path[-4:].lower() != ".png":
        output_path += ".png"

    decode.decode_image(file_path, output_path)
    print(f"The decrypted message can be found at {output_path}")
    os.system('pause')

def show_intro():
    print(r"""
|----------------------------------------------------------------------------------------|
|                 _____                                                                  | 
|                |_   _|                                                                 | 
|                  | |  _ __ ___    __ _   __ _   ___                                    | 
|                  | | | '_ ` _ \  / _` | / _` | / _ \                                   |
|                 _| |_| | | | | || (_| || (_| ||  __/                                   |
|                 \___/|_| |_| |_| \__,_| \__, | \___|                                   |
|   _____  _                      ______   __/ |                                         | 
|  /  ___|| |                     |  _  \ |___/                                          | 
|  \ `--. | |_  ___   __ _   __ _ | | | | _ __  __ _ __      __                          |
|   `--. \| __|/ _ \ / _` | / _` || | | || '__|/ _` |\ \ /\ / /                          |
|  /\__/ /| |_|  __/| (_| || (_| || |/ / | |  | (_| | \ V  V /                           | 
|  \____/  \__|\___| \__, | \__,_||___/  |_|   \__,_|  \_/\_/                            | 
|                     __/ |                                                              | 
|                    |___/                                                               | 
|                                                                                        |
|                                                                                        |
|                                                                         - by Virtuosos |
|________________________________________________________________________________________|
          """)



if __name__ == "__main__":
    show_intro()
    while True:
        print("Please choose:")
        mode = input("(E)ncrypt or (D)ecrypt: ")
        if mode.lower() == 'e':
            encrypt_mode()            
            break
        elif mode.lower() == 'd':
            decrypt_mode()    
            break
        else:
            print("invalid choice")
            continue
    