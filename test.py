

import tkinter as tk

def createNewWindow():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()



app = tk.Tk()
buttonExample = tk.Button(app, text="Create new window", command=createNewWindow)
buttonExample.pack()

app.mainloop()

#########################
import tkinter as tk

def on_enter(event):
    label.config(text="마우스 들어감!")
def on_leave(event):
    label.config(text="마우스 나감!")
def button_clicked():
    label.config(text="버튼 클릭됨!")
root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="버튼 위에 마우스를 올리세요.")
label.pack(pady=10)
button = tk.Button(root, text="버튼", command=button_clicked)
button.pack(pady=5)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()




##### 레퍼런스
# https://edward0im.github.io/engineering/2021/09/15/vpython-ex7/
# https://blog.naver.com/gyurse/221034749868
