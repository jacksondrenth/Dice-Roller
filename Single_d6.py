from PIL import Image, ImageTk
import random
import tkinter as tk
import tkinter.ttk as ttk
import os


def pic_choice(image):
    dir_path = 'dies/'

    file_names = os.listdir(dir_path)

    random_file = random.choice(file_names)

    img = Image.open(dir_path + random_file)

    img = img.resize((width, height))

    img_tk = ImageTk.PhotoImage(img)

    image.config(image=img_tk)

    image.image = img_tk



def dice_roll(i, image):
    if i < 10:
        pic_choice(image)
        root.after(200, dice_roll, i+1, image)


width, height = 200, 200

# tk start
root = tk.Tk()

style = ttk.Style()
style.configure('TButton', font =('calibri', 10, 'bold'), borderwidth='4')

# window fixtures
root.title('D6 Roller')
root.configure()

# picture
img = Image.open('dies/S1.png')
img = img.resize((width, height))
img_tk = ImageTk.PhotoImage(img)
label = ttk.Label(root, image=img_tk)
label.grid(row=0, column=0)

# button
button = ttk.Button(root, text="Roll D6", style='TButton', command=lambda: dice_roll(0, label))
button.grid()
button.config(width=20, padding=20)


root.mainloop()
