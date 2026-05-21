from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk(screenName="Amőba", baseName="Amőba", className='Tk', useTk=1)
root.title("Amőba")
frm = ttk.Frame(root, padding=15)
ttk.Label(frm, text="Amőba.")
jatekos = "X"
stop = False
def clicked(k, n):
    global jatekos
    if jatekos == "X" and statusz[k][n] == 0 and stop == False:
        felulet[k][n].config(text = "X")
        statusz[k][n] = "X"
        jatekos = 'O'
    
    elif jatekos == "O" and statusz[k][n] == 0 and stop == False:
        felulet[k][n].config(text = "O")
        statusz[k][n] = "O"
        jatekos = "X"

    nyerte()

def nyerte():
    global stop
    
    i = 0
    while i < 3:
        if statusz[i][0] == statusz[i][1] == statusz[i][2] != 0:
            stop = True

            nyer = messagebox.showinfo("Nyertes", statusz[i][0] + "Nyert")
            break
        elif statusz [0][i] == statusz[1][i] == statusz[2][i] != 0:
            stop = True

            nyer = messagebox.showinfo("Nyertes", statusz[0][i] + "Nyert")
            break

        elif statusz[0][0] == statusz[1][1] == statusz[2][2] !=0:
            stop = True

            nyer = messagebox.showinfo("Nyertes", statusz[0][0] + "Nyert")
            break

        elif statusz[0][2] == statusz[1][1] == statusz[2][0] !=0:
            stop = True

            nyer = messagebox.showinfo("Nyertes", statusz[0][2] + "Nyert")
            break

        elif statusz[0][0] and statusz[0][1] and statusz[0][2] and statusz[1][0] and statusz[1][1] and statusz[1][2] and statusz[2][0] and statusz[2][1] and statusz[2][2] != 0:
            stop = True

            nyer = messagebox.showinfo("Döntetlen", "Döntetlen")
    i += 1

root.resizable(0,0)

felulet = [[0,0,0], [0,0,0], [0,0,0]]

statusz = [[0,0,0], [0,0,0], [0,0,0]]
i = 0
j = 0
while i < 3:
    j = 0
    while j < 3:
        felulet[i][j] = Button(height=5, width=10, text="", font = ("Oswald","25"), command = lambda k = i, n = j : clicked(k, n))
        felulet[i][j].grid(row = i, column = j)
        j += 1
    i += 1
root.mainloop()

