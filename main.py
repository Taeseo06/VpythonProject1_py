from tkinter import *
from vpython import *
from tkinter import ttk
import tkinter.messagebox as msgbox
import tkinter.font

root = Tk()
root.title('물리운동 시뮬레이터')
root.geometry("900x600+450+300")

# 시작 버튼을 만듭니다.
btn_motion1 = Button(root, text="포물선 운동", width = 7, height = 2, relief = "solid", overrelief= "solid")
btn_motion1.place(x=400, y=20)

btn_motion2 = Button(root, text="자유낙하 운동", width = 7, height = 2, relief = "solid", overrelief= "solid")
btn_motion2.place(x=400, y=80)

btn_motion3 = Button(root, text="등속 운동", width = 7, height = 2, relief = "solid", overrelief= "solid")
btn_motion3.place(x=400, y=140)

btn_motion4 = Button(root, text="등가속도 운동", width = 7, height = 2, relief = "solid", overrelief= "solid")
btn_motion4.place(x=400, y=200)

btn_motion5 = Button(root, text="원 운동", width = 7, height = 2, relief = "solid", overrelief= "solid")
btn_motion5.place(x=400, y=260)



# 포물선을 그리는 함수를 만듭니다.
def draw_parabola(setting): # 운동1 - 포물선 운동

    root.destroy()

    canvas(width=1300, height=900)

    # 포물선운동
    ball = sphere(radius = setting['radius']) # 물체 반지름
    # ground = box(pos=vec(0, -4, 0), size=vec(15, -0.01, 5))
    ground = box(pos=vec(0, -4, 0), size=vec(15, -0.01, 5))
    ball.pos = vec(-2, 0, 0)
    ball.v = vec(1, 1, 0) # 물체의 속도를 나타내는 벡터 -> y값 0 : 제자리에서 포물선 운동, 1 : 위로 올라갔다가 떨어지는 포물선운동
    # ball.v = vec(2, 1, 0)  # y축 방향으로 2m/s의 속도로 운동
    ball.a = vec(0, -0.3, 0) # 물체의 가속도를 나타내는 벡터 -> y값 : 중력의 정도

    # ball.a = vec(0, -9.8, 0)  # 물체의 가속도를 나타내는 벡터 -> y값 : 중력의 정도
    # ball.a = vec(2, -0.35, 0) # 물체의 가속도를 나타내는 벡터 -> y값 : 중력의 정도

    if setting['tracker'] == 1: # setting[tracker] 값에 따라 attach_trail 의 색상을 조정해서 가시/비가시로 구현함
        tracker_color = color.red
    else :
        tracker_color = color.black
    attach_trail(ball, type='points', pps=6, color=tracker_color)


    t = 0
    dt = 0.01
    while ball.pos.y > ground.pos.y:
        rate(1 / dt)
        ball.v = ball.v + ball.a * dt
        ball.pos = ball.pos + ball.v * dt
        t = t + dt
    # 아래는 포물선 운동 그래프 구현
    motion_graph = graph(title='position-time', xtitle='t', ytitle='y')
    g_bally = gcurve()

    motion_graph = graph(title='velocity-time', xtitle='t', ytitle='vy')
    g_ballvy = gcurve(color=color.green)

    while ball.pos.y > ground.pos.y:
        rate(1 / dt)
        ball.v = ball.v + ball.a * dt
        ball.pos = ball.pos + ball.v * dt
        g_bally.plot(pos=(t, ball.pos.y))
        g_ballvy.plot(pos=(t, ball.v.y))
        t = t + dt

    max_y = ball.pos.y
    max_t = t
    while ball.pos.y > ground.pos.y:
        rate(1 / dt)
        if ball.pos.y > max_y:
            max_y = ball.pos.y
            max_t = t

        ball.v = ball.v + ball.a * dt
        ball.pos = ball.pos + ball.v * dt
        g_bally.plot(pos=(t, ball.pos.y))
        g_ballvy.plot(pos=(t, ball.v.y))
        t = t + dt
    print('max_y:', max_y)
    print('max_t:', max_t)


def setting_window(text): # 시뮬레이션 환경설정 윈도우 - (생성)

    setting = {'tracker' : 1,
               'radius' : 0.2,
               'gravity_speed' : 0.35}

    settingWindow = Toplevel(root)
    settingWindow.title(f'{text} 시뮬레이션 환경 설정창')
    settingWindow.geometry("500x900+290+200")

    btn_start = Button(settingWindow, text="시뮬레이션 시작", fg="red", font=tkinter.font.Font(weight="bold", size=15)) # 시뮬레이션 시작버튼
    btn_tracker = Button(settingWindow, text = "운동 크래커 스위치", fg='blue', font=tkinter.font.Font(weight='bold')) # 운동 트랙커 스위치 (on/off)
    lb_tracker = Label(settingWindow, text = "현재상태 : " + ("ON" if setting['tracker'] else "OFF")) # 트랙커 상태 표시라벨
    lb_radius = Label(settingWindow, text="운동할 원의 반지름을 설정해주세요") # 반지름 설정 라벨
    spin_radius = Spinbox(settingWindow, from_=0.1, to=1.0, increment=.1, textvariable=setting['radius'], width=10) # 반지름 설정 스핀박스
    lb_gravity_speed = Label(settingWindow, text="중력 가속도를 설정해주세요") # 중력가속도 설정 라벨

    combobox_var = StringVar()
    combo_gravity_speed = ttk.Combobox(settingWindow, state="readonly", textvariable=combobox_var, values=['-9.8', '-5', '-2', '-1', '기본 : 0.35', '1', '2', '5', '9.8'], width=10) # 중력가속도 설정 콤보박스



    btn_start.pack()
    btn_tracker.place(x=125, y=70)
    lb_tracker.place(x=290, y=73)

    lb_radius.place(x=155, y=120)
    spin_radius.place(x=193, y=140)

    lb_gravity_speed.place(x=170, y=190)
    combo_gravity_speed.place(x=165, y=230)


    def tracker_switch():
        nonlocal setting
        if setting['tracker'] == 1: # 1(on) -> 0 (off)
            setting['tracker'] -= 1
            btn_tracker.config(fg='black', font=tkinter.font.Font(weight="normal"))
        else: # 0 (off) -> 1 (on)r
            setting['tracker'] += 1
            btn_tracker.config(fg='blue', font=tkinter.font.Font(weight="bold"))
        lb_tracker.config(text="현재상태 : " + ("ON" if setting['tracker'] else "OFF"))



    def get_radius():
        nonlocal setting
        try:
            number = float(spin_radius.get())
            setting['radius'] = number
        except ValueError:
            print("반지름-올바른 숫자를 입력해주세요.")

    def on_combobox_select(event):
        nonlocal setting
        setting['gravity_speed'] = combobox_var.get()
        # print(f'현재 중력가속도 : {setting['gravity_speed']}')

        # if gravity_speed == '기본속도':
        # result_label.config(text="Selected value: " + gravity_speed)

    btn_start.config(command=lambda: draw_parabola(setting))
    btn_tracker.config(command=tracker_switch)
    spin_radius.config(command=get_radius)
    # combo_speed.config(command=)
    combo_gravity_speed.bind("<<ComboboxSelected>>", on_combobox_select)

btn_motion1.config(command=lambda: setting_window("포물선운동")) # 메뉴 포물선 운동 버튼 피드백 함수 설정

root.mainloop()