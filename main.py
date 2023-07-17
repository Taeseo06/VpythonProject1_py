from tkinter import *
from vpython import *

root = Tk()
root.title('물리운동 시뮬레이터')
root.geometry("900x600+450+300")
# 시작 버튼을 만듭니다.
btn_motion1 = Button(root, text="포물선 운동", width = 7, height = 2, relief = "solid", overrelief= "solid")
btn_motion1.place(x=400, y=20)



# 포물선을 그리는 함수를 만듭니다.
def draw_parabola(): # 운동1 - 포물선 운동
  # 포물선운동
  ball = sphere(radius = 0.2) # 물체 반지름
  ground = box(pos=vec(0, -4, 0), size=vec(15, -0.01, 5))
  ball.pos = vec(-2, 0, 0)
  ball.v = vec(1, 1, 0)  # y값 0 : 제자리에서 포물선 운동, 1 : 위로 올라갔다가 떨어지는 포물선운동r
  ball.a = vec(0, -0.35, 0)
  attach_trail(ball, type='points', pps=5)

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
    tracker = 1

    settingWindow = Toplevel(root)
    settingWindow.title(f'{text} 시뮬레이션 환경 설정창')
    settingWindow.geometry("500x900+290+200")

    btn_start = Button(settingWindow, text="시뮬레이션 시작") # 시뮬레이션 시작버튼
    btn_tracker = Button(settingWindow, text = "운동 크래커 스위치")

    lb_tracker = Label(settingWindow, text = "현재상태 : " + "ON" if tracker else "OFF")



    btn_start.pack()
    btn_tracker.pack(side="left")
    lb_tracker.pack(side="right")


    def tracker_witch():
        print("test111")

    # def tracker_switch():



    btn_start.config(command=draw_parabola)
    btn_tracker.config(command=tracker_switch)



# 모션1 버튼 - 포물선운동 콜백함수
def motion1_callback():
  btn_motion1.destroy()
  # global new
  # new = Toplevel()
  setting_window("포물선운동")



  # draw_parabola() # 포물선 운동

btn_motion1.config(command=motion1_callback)

root.mainloop()
