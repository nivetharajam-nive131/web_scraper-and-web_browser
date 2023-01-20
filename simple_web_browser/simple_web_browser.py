import tkinter as tk
import webbrowser
from PIL import Image, ImageTk

def open_url():
    webbrowser.open(entry.get())

root = tk.Tk()
root.title("Web Browser")

# Add background image
image = Image.open("websitelogo.png")
image = image.resize((400, 300), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create search box
entry = tk.Entry(root, font=("Arial", 18), width=30)
entry.pack()

# Create "Go" button
button = tk.Button(root, text="Go", font=("Arial", 18), width=10, command=open_url)
button.pack()

root.mainloop()
