
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Menu
from build.songutils import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("644x393")
window.configure(bg = "#FFFFFF")

menubar=Menu()
fileMenu=Menu(menubar)
fileMenu.add_command(label="Open Song",command=lambda: loadsingle())
fileMenu.add_command(label="Open Playlist",command=lambda: LoadPlaylist())
menubar.add_cascade(label="File",menu=fileMenu)
window.config(menu=menubar)
menubar.add_command(label="Exit", command=lambda :window.quit())

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 393,
    width = 644,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=0.0,
    y=0.0,
    width=644.0,
    height=393.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=218.0,
    y=154.0,
    width=207.0,
    height=207.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: previousSong(),
    relief="flat"
)
button_3.place(
    x=231.0,
    y=231.0,
    width=49.0,
    height=37.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextSong(),
    relief="flat"
)
button_4.place(
    x=370.0,
    y=231.0,
    width=49.0,
    height=37.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: stop(),
    relief="flat"
)
button_5.place(
    x=304.0,
    y=313.0,
    width=36.0,
    height=36.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pause(),
    relief="flat"
)
button_6.place(
    x=304.0,
    y=171.0,
    width=38.0,
    height=31.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: play(),
    relief="flat"
)
button_7.place(
    x=280.0,
    y=216.0,
    width=84.0,
    height=83.0
)

canvas.create_text(
    157.0,
    44.0,
    anchor="nw",
    text="Python Music Player",
    fill="#FFFFFF",
    font=("Inter Bold", 36 * -1)
)
window.resizable(False, False)
window.mainloop()