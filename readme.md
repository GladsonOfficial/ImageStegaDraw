# ImageStegaDraw
A terminal-based tool that lets you draw and hide secret messages inside images using Least Significant Bit (LSB) steganography via an interactive pop-up drawing window.

## About the project
This project is for beginners getting into cybersecurity. This is a very good way to practically see how image steganography works, with a very easy to use interface. User can upload a picture and draw a secret message and they will have a image with the secret message hidden in it. This tool uses Least Significant Bit Steganography to hide message.


## Usage
You can either install all the dependency and run the python file (recommended) or run the executable file.

### Running the Python File (Recommended)
**(Optional)** Create a virtual environment by writing the following line in the terminal
>python -m venv .venv

Install the dependancies by writing following in terminal
> pip install -r requirements.txt

Now run the main.py using
> python main.py

### Hiding Message
When you start the tool, it will ask if you want to encrypt or decrypt, Press 'E' to encrypt. Write the path to the image in the field. Draw a secret message in the window that pops up and then press the "Save Image" button. The secret message and image with secret message hidden in it can be found in the output folder.

### Extracting Message
Start the program and press 'D' to to decrypt. Enter the path of the file with the secret message embedded in it. Now enter the path where you want the extracted message to be, leave it blank to save at the default location (output/secret_message.png). Now you can see the hidden message extracted out of the image in the output folder.

## How This Tool Works
This tool works using LSB Steganography. Image is basically a collection of pixels. Some images don't fall in this description but we will leave it for now. Each pixel consists of a Red, Green and Blue data.
Changing the LSB (Least Significant Bit) changes the color of the pixel slightly but it is not apparent.

We store the data in this bit. In this tool we are using the least 2 bits. To hide a secret message, we first resize the secret message to match the dimensions of the image.

Now if the secret message has a black pixel then we change the least 2 bits of the image to 0, 
Now if the secret message has a white pixel then we change the least 2 bits of the image to 1.

To extract the secret message, we do the opposite. We check the least 2 bits of pixel and if they are 0, we turn the pixel to black and if they are 1 we turn the pixel to white.


## Technology Used
**Core Language**: Python 3.12.4\
**Libraries used**: Pillow, Tkinter, pyinstaller