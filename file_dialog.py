from tkinter import *
from tkinter import filedialog
from pathlib import Path
from os.path import join
from PIL import Image, ImageTk


# root = Tk()
# root.geometry("+0+0")


def open_img():
    global img_tk # to ensure that img can be shown and not be thrown to garbage collector.

    init_dir = join(Path.home(), "Pictures")
    file_type_tups = (
        ("jpg image files", "*.jpg"),
        ("jpeg image files", "*.jpeg"),
        ("png image files", "*.png"),
        ("all files", "*.*")
    )

    top = Toplevel()
    top.withdraw() # hide the window
    top.geometry("+0+0")
    top.title("Image")

    top.filename = filedialog.askopenfilename(
        initialdir=init_dir,
        title="Select A Image File",
        filetypes=file_type_tups
    )
    
    img = Image.open(top.filename)
    img.thumbnail((1280, 720))
    img_tk = ImageTk.PhotoImage(img)
    img_label = Label(
        top,
        image=img_tk
    )
    img_label.pack()
    
    top.deiconify() # unhide/show again the window
    top.attributes('-topmost',True) # to stay the window on top of other windows


# btn = Button(
#     root,
#     text="Open Image",
#     command=open_img
# )
# btn.pack()


# root.mainloop()
