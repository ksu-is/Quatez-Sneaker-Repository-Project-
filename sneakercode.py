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
