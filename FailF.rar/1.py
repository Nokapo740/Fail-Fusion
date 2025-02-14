import tkinter as tk
from tkinter import filedialog
from PIL import Image

def convert_to_jpg():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if output_path:
            img.convert('RGB').save(output_path, 'JPEG')
            label_result.config(text=f"Saved as: {output_path}")

def convert_to_png():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if output_path:
            img.save(output_path, 'PNG')
            label_result.config(text=f"Saved as: {output_path}")

app = tk.Tk()
app.title("Image Converter")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

btn_convert_to_jpg = tk.Button(frame, text="Конвертировать в JPG", command=convert_to_jpg)
btn_convert_to_jpg.pack(side=tk.LEFT, padx=5, pady=5)

btn_convert_to_png = tk.Button(frame, text="Конвертировать в PNG", command=convert_to_png)
btn_convert_to_png.pack(side=tk.LEFT, padx=5, pady=5)

label_result = tk.Label(app, text="")
label_result.pack(pady=5)

app.mainloop()
        