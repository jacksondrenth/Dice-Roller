from PIL import Image, ImageTk
import random
import tkinter as tk
import tkinter.ttk as ttk
import os

# chooses picture
def pic_choice(image):
    dir_path = 'dies/'

    file_names = os.listdir(dir_path)

    random_file = random.choice(file_names)

    img = Image.open(dir_path + random_file)

    img = img.resize((width, height))

    img_tk = ImageTk.PhotoImage(img)

    image.config(image=img_tk)

    image.image = img_tk


# simulates a roll
def dice_roll(i, image1, image2):
    if i < 10:
        pic_choice(image1)
        pic_choice(image2)
        root.after(200, dice_roll, i+1, image1, image2)

# set dimensions
width, height = 200, 200

# tk start
root = tk.Tk()

style = ttk.Style()
style.configure('TButton', font =('calibri', 10, 'bold'), borderwidth='4')

# window fixtures
root.title('D6 Roller')
root.configure()

# picture
img2 = Image.open('dies/S1.png')
img2 = img2.resize((width, height))
img_tk2 = ImageTk.PhotoImage(img2)
label2 = ttk.Label(root, image=img_tk2)
label2.grid(row=0, column=0)

# picture 2
img3 = Image.open('dies/S1.png')
img3 = img3.resize((width, height))
img_tk3 = ImageTk.PhotoImage(img3)
label3 = ttk.Label(root, image=img_tk3)
label3.grid(row=0, column=1)

# button
button = ttk.Button(root, text="Roll D6", style='TButton', command=lambda: dice_roll(0, label2, label3))
button.grid()
button.config(width=20, padding=20)


root.mainloop()
