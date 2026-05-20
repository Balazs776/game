from tkinter import *
from tkinter import ttk


root = Tk(screenName="Amőba", baseName="Amőba", className='Tk', useTk=1)
root.title("Amőba")
frm = ttk.Frame(root, padding=15)
ttk.Label(frm, text="Amőba.")

canvas = Canvas(root, width=400, height=400)
canvas.pack()


canvas.create_line(0, 50, 200, 50)
canvas.create_line(0, 100, 200, 100)
canvas.create_line(0, 150, 200, 150)
canvas.create_line(0, 50, 200, 50)
canvas.create_line(50, 100, 200, 100)
canvas.create_line(0, 50, 128, 50)


def left_click(event):
    print(f"Left click at ({event.x}, {event.y})")
root.bind("<Button-1>", left_click)
ttk.Button(frm, text="Kilépés", command=root.destroy)
root.mainloop()
