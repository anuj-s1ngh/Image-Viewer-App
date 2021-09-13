from tkinter import *
from pathlib import Path
from os import listdir, stat
from tkinter import filedialog
from PIL import ImageTk, Image
from file_dialog import open_img


main_window = Tk()
main_window.title("Image Viewer App")
main_window.iconbitmap("image_icon.ico")
main_window.geometry("300x300")


root = Toplevel()
root.title("See Images")
root.withdraw()


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width / 1.25)
window_height = int(screen_height / 1.25)
# Adjust size
root.geometry(f"{window_width}x{window_height}+0+0")
 
# set minimum window size value
# root.minsize(1280, 720)

# set maximum window size value
# root.maxsize(1920, 1080)


def load_images(folder_path):
    global img_list
    picture_folder_path = folder_path
    # picture_folder_path = str(Path.home()).replace("\\", "/") + "/Pictures"
    picture_name_list = listdir(picture_folder_path)
    picture_name_list.sort()
    try:
        img_list = []
        for picture_name in picture_name_list:
            file_ext = Path(picture_name).suffix
            if file_ext == ".png" or file_ext == ".jpeg"  or file_ext == ".jpg":
                img = Image.open(picture_folder_path + "/" + picture_name)
                img.thumbnail((int(screen_width / 1.5), int(screen_height / 1.5)))
                imgTK = ImageTk.PhotoImage(img)
                img_list.append(imgTK)
    except Exception as err:
        print(f"Error While Loading Images From '{folder_path}' : {err}")
    
    return img_list


def ask_for_directory():
    folder_selected = filedialog.askdirectory()
    return folder_selected


def show_initial_img():
    global current_img_num, img_label, img_list, prev_btn, next_btn, folder_path, wait_for_load_lbl, main_window

    folder_path = ask_for_directory()

    root.deiconify()
    root.attributes('-topmost',True)

    wait_for_load_lbl = Label(
        root,
        text="Please Wait While Your Images Are Loading ......"
    )
    wait_for_load_lbl.grid(
        row=0,
        column=0,
        columnspan=3
    )

    returned_img_list = load_images(folder_path)

    if len(returned_img_list) > 0:
        wait_for_load_lbl.destroy()
    else:
        wait_for_load_lbl.destroy()
        no_img_files_lbl = Label(
            root,
            text="!!! No Image Files Found."
        )
        no_img_files_lbl.grid(
            row=0,
            column=0,
            columnspan=3
        )


    current_img_num = 0

    dir_label = Label(
        root,
        text=folder_path
    )
    dir_label.place(
        x=20,
        y=0
    )

    img_label = Label(
        root,
        image=img_list[current_img_num]
    )
    img_label.place(
        x=20,
        y=20
    )
    show_btns()


def show_img(img):
    global img_label, folder_path
    dir_label = Label(
        root,
        text=folder_path
    )
    dir_label.place(
        x=20,
        y=0
    )

    img_label = Label(
        root,
        image=img
    )
    img_label.place(
        x=20,
        y=20
    )


def show_next_img():
    global current_img_num, img_label, img_list, next_btn
    if  current_img_num < len(img_list):
        img_label.place_forget()
        current_img_num += 1
        show_img(img_list[current_img_num])
        show_btns()


def show_prev_img():
    global current_img_num, img_label, img_list, prev_btn
    if current_img_num > 0:
        img_label.place_forget()
        current_img_num -= 1
        show_img(img_list[current_img_num])
        show_btns()


dir_load_btn = Button(
    main_window,
    text="Load Images From A Folder",
    # width=int(screen_width / 15),
    # height=int(screen_height / 15),
    padx=20,
    pady=10,
    width=25,
    command=show_initial_img,
    fg="white",
    bg="blue"
)
dir_load_btn.place(
    relx=0.5,
    rely=0.4,
    anchor=CENTER
)

dir_load_btn = Button(
    main_window,
    text="Load A Image File",
    # width=int(screen_width / 15),
    # height=int(screen_height / 15),
    padx=20,
    pady=10,
    width=25,
    command=open_img,
    fg="white",
    bg="green"
)
dir_load_btn.place(
    relx=0.5,
    rely=0.6,
    anchor=CENTER,
)


def show_btns():
    global current_img_num, img_list

    if current_img_num <= 0:
        prev_btn = Button(
            root,
            text="prev",
            padx=10,
            pady=5,
            state=DISABLED,
            justify="center",
            anchor=W
        )
    else:
        prev_btn = Button(
            root,
            text="prev",
            padx=10,
            pady=5,
            command=show_prev_img,
            justify="center",
            anchor=W
        )
    prev_btn.place(
        x=40,
        y=window_height - 50
    )

    if current_img_num >= len(img_list) - 1:
        next_btn = Button(
            root,
            text="next",
            padx=10,
            pady=5,
            state=DISABLED,
            justify="center",
            anchor=E
        )
    else:
        next_btn = Button(
            root,
            text="next",
            padx=10,
            pady=5,
            command=show_next_img,
            justify="center",
            anchor=E
        )
    next_btn.place(
        x=window_width - 100,
        y=window_height - 50
    )

    status_label = Label(
        root,
        text=f"image {current_img_num + 1} of {len(img_list)}",
        padx=10,
        pady=5,
        justify="center",
        bd=1,
        relief=SUNKEN,
        anchor=S
    )
    status_label.place(
        x=(window_width // 2) - 40,
        y=window_height - 40
    )


root.mainloop()

