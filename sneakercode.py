#Sneaker flashcard welcome page
import tkinter as tk
from tkinter import messagebox
from PIL import image, ImageTK
import requests
from io import BytesIO

def show_image():
  response = requests.get("https://github.com/ksu-is/Quatez-Sneaker-Repository-Project-/blob/main/Image%204-5-25%20at%2010.36%20AM.JPG")
  img_data = responses.content
  img = Image.open(BytesIO(img_data))
  img.show()

def main():
  root = tk.Tk() 
  root.title(" Sneaker Flash Card Game")

welcome_label = tk.Label(root, text "READY TO PLAY?!", font=("Helvetica", 24))
welcome_label.pack(pady=20)

click_here_button = tk.Button(root, text="Click Here", command=show_image)
    click_here_button.pack(pady=10)



root.mainloop()

if __name == "__main__" 
  welcome_page()










#Sneaker flashcard welcome page
import tkinter as tk
from tkinter import messagebox
import PIL
from PIL import Image, ImageTk
import requests
from io import BytesIO

def show_image():
  url="https://raw.githubusercontent.com/ksu-is/Quatez-Sneaker-Repository-Project-/main/Image%204-5-25%20at%2010.36%20AM.JPG"
  responses = requests.get(url)
  img_data = responses.content
  img = image.open(BytesIO(img_data))
  img.show()

#def main():
root = tk.Tk() 
root.title("Sneaker Flash Card Game")


#welcome_label.pack(pady=20)
# Welcome Message
welcome_label = tk.Label(root, text="READY TO PLAY?!", font=("Helvetica", 24))

click_here_button = tk.Button(root, text="Click Here", command=show_image)
click_here_button.pack(pady=10)



root.mainloop()

if __name__ == "__main__":
   show_image()

