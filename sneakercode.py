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

def welcome_page():
  root = tk.Tk() 
  root.title(" Sneaker Flash Card Game")

label = tk.Label(root, text="Ready to Play?!", font=("Helvetica, 24))
label.pack(pady=20)

start_button = tk.Button(root, text-"Click Here", command = root.quit font="Helvetica", 16))
start_button.pack(pady=10

root.mainloop()

if __name == "__main__" 
  welcome_page()
