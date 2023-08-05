# import tkinter as tk
#
# def get_number():
#     try:
#         number = int(entry.get())
#         print("입력한 숫자:", number)
#     except ValueError:
#         print("올바른 숫자를 입력해주세요.")
#
# root = tk.Tk()
# root.title("숫자 입력")
# root.geometry("300x100")
#
# label = tk.Label(root, text="숫자를 입력하세요:")
# label.pack()
#
# entry = tk.Entry(root)
# entry.pack()
#
# button = tk.Button(root, text="확인", command=get_number)
# button.pack()
#
# root.mainloop()



----------

import tkinter as tk

root = tk.Tk()

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing name and password
name_var = tk.StringVar()
passw_var = tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():
  name = name_var.get()
  password = passw_var.get()

  print("The name is : " + name)
  print("The password is : " + password)

  name_var.set("")
  passw_var.set("")


# name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
# passw_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))
passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

sub_btn = tk.Button(root, text='Submit', command=submit)
# method
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()

#ticky=tk.W+tk.E+tk.N+tk.S



-----


def motion1_callback():
  setting = {'tracker': 1, 'radius': 0.2}
  setting_window("포물선운동", setting)
  draw_parabola(setting)


(lambda setting: draw_parabola(setting))(setting)
