import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw
import os

def create_drawing_canvas(width, height):
    # Setting a width and heigth for canvas
    local_width, local_height = 500, 500
    
    # Setting up canvas for drawing
    root = tk.Tk()
    root.title("Drawing Message")
    
    canvas_frame = tk.Frame(root, borderwidth=2, relief='sunken')
    canvas_frame.pack(padx=10, pady=10)
    
    canvas = tk.Canvas(canvas_frame, width=local_width, height=local_height, bg='white')
    canvas.pack()
    
    last_x, last_y = None, None
    
    drawing_image = Image.new("RGB", (local_width, local_height), "white")
    draw_context = ImageDraw.Draw(drawing_image)
    
    def draw(event):
        nonlocal last_x, last_y
        if last_x is not None and last_y is not None:
            canvas.create_line(last_x, last_y, event.x, event.y, fill='black', width=10, capstyle=tk.ROUND, smooth=tk.TRUE)
            draw_context.line([(last_x, last_y), (event.x, event.y)], fill="black", width=10)
        last_x, last_y = event.x, event.y
    
    def reset_coords(event):
        nonlocal last_x, last_y
        last_x, last_y = None, None
    
    def clear_canvas():
        canvas.delete("all")
        
        nonlocal drawing_image, draw_context
        drawing_image = Image.new('RGB', (local_width, local_height), 'white')
        draw_context = ImageDraw.Draw(drawing_image)
        
    def save_canvas_as_jpg():
        folder = "output"
        file_path = "output/secret_message.jpg"

        if not os.path.exists(folder):
            os.mkdir(folder)    

        if file_path:
            try:
                # Resizing the canvas to fit the image
                new_size = (width, height)
                resized_image = drawing_image.resize(new_size)
                resized_image.save(file_path, "JPEG", quality=95)
                # print(f'image saved successfully to {file_path}')
            except Exception as e:
                print(f"Error saving image: {e}")
        root.destroy()
    
    canvas.bind("<B1-Motion>", draw)
    canvas.bind("<ButtonRelease-1>", reset_coords)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)
    
    clear_button = tk.Button(button_frame, text='Clear Canvas', command=clear_canvas)
    clear_button.pack(side=tk.LEFT, padx=5)

    save_button = tk.Button(button_frame, text="Save image", command=save_canvas_as_jpg)
    save_button.pack(side=tk.LEFT, padx=5)

    root.mainloop()


if __name__ == "__main__":
    # Testing if this works
    canvas_width = 900
    canvas_height = 500

    create_drawing_canvas(canvas_width, canvas_height)