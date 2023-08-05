from tkinter import *
from vpython import *
import tkinter.font

root = Tk()
root.title('물리운동 시뮬레이터')
root.geometry("900x600+450+300")

# 시작 버튼을 만듭니다.
btn_motion1 = Button(root, text="포물선 운동", width = 7, height = 2, relief = "solid", overrelief= "solid")
btn_motion1.place(x=400, y=20)



# 포물선을 그리는 함수를 만듭니다.
def draw_parabola(): # 운동1 - 포물선 운동

    canvas(width=1300, height=900)



    # 포물선운동
    ball = sphere(radius = 0.2) # 물체 반지름
    ground = box(pos=vec(0, -4, 0), size=vec(15, -0.01, 5))
    ball.pos = vec(-2, 0, 0)
    ball.v = vec(1, 1, 0)  # y값 0 : 제자리에서 포물선 운동, 1 : 위로 올라갔다가 떨어지는 포물선운동r
    ball.a = vec(0, -0.35, 0)
    attach_trail(ball, type='points', pps=6, color=color.red)

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
               'radius' : 0.2}

    settingWindow = Toplevel(root)
    settingWindow.title(f'{text} 시뮬레이션 환경 설정창')
    settingWindow.geometry("500x900+290+200")

    btn_start = Button(settingWindow, text="시뮬레이션 시작", fg="red", font=tkinter.font.Font(weight="bold", size=15)) # 시뮬레이션 시작버튼
    btn_tracker = Button(settingWindow, text = "운동 크래커 스위치", fg='blue', font=tkinter.font.Font(weight='bold'))
    lb_tracker = Label(settingWindow, text = "현재상태 : " + ("ON" if setting['tracker'] else "OFF"))
    entry_radius = Entry(settingWindow, textvariable=setting['radius'], font=('calibre', 10, 'normal'))

    btn_start.pack()
    btn_tracker.place(x=125, y=50)
    lb_tracker.place(x=260, y=53)
    entry_radius.place(x=110, y=85)

    def tracker_switch():
        nonlocal setting
        if setting['tracker'] == 1: # 1(on) -> 0 (off)
            setting['tracker'] -= 1
            btn_tracker.config(fg='black', font=tkinter.font.Font(weight="normal"))
        else: # 0 (off) -> 1 (on)
            setting['tracker'] += 1
            btn_tracker.config(fg='blue', font=tkinter.font.Font(weight="bold"))
        lb_tracker.config(text="현재상태 : " + ("ON" if setting['tracker'] else "OFF"))


    # btn_start.config(command=draw_parabola)
    btn_start.config(command=lambda: draw_parabola(setting))
    # btn_start.config(command=((lambda setting: draw_parabola(setting))(setting)))
    btn_tracker.config(command=tracker_switch)



# 모션1 버튼 - 포물선운동 콜백함수
def motion1_callback():
  # btn_motion1.destroy()

  setting_window("포물선운동")




  # draw_parabola() # 포물선 운동

btn_motion1.config(command=motion1_callback)

root.mainloop()