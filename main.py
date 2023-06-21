from tkinter import *
from vpython import *

#포물선운동
ball = sphere(radius = 0.2)
ground = box(pos = vec(0, -4, 0), size = vec(15, -0.01, 5))
ball.pos = vec(-2, 0, 0)
ball.v = vec(1, 1, 0) # y값 0 : 제자리에서 포물선 운동, 1 : 위로 올라갔다가 떨어지는 포물선운동
ball.a = vec(0, -0.35, 0)
attach_trail(ball, type = 'points', pps = 5)

t = 0
dt = 0.01
while ball.pos.y > ground.pos.y:
    rate(1 / dt)
    ball.v = ball.v + ball.a * dt
    ball.pos = ball.pos + ball.v * dt
    t = t + dt
# 아래는 포물선 운동 그래프 구현
motion_graph = graph(title = 'position-time', xtitle = 't', ytitle = 'y')
g_bally = gcurve()

motion_graph = graph(title = 'velocity-time', xtitle = 't', ytitle = 'vy')
g_ballvy = gcurve(color = color.green)

while ball.pos.y > ground.pos.y:
    rate(1 / dt)
    ball.v = ball.v + ball.a * dt
    ball.pos = ball.pos + ball.v * dt
    g_bally.plot(pos = (t, ball.pos.y))
    g_ballvy.plot(pos = (t, ball.v.y))
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
    g_bally.plot(pos = (t, ball.pos.y))
    g_ballvy.plot(pos = (t, ball.v.y))
    t = t + dt
print('max_y:', max_y)
print('max_t:', max_t)

# sample
# a = box()



#myBall = sphere(color = color.red, radius = 2)
#myBox = box(pos = vec(5, 0, 0), color = color.blue, size = vec(0.5, 4, 1))
#myBall.color = color.green
#myBox.pos.x = 10
#
#myCylinder = cylinder(size = vec(3, 1, 3))
#
#r = vector(3, -4, 5)
#r_arrow = arrow(pos = vector(0, 0, 0), axis = r, shaftwidth = 0.2)

#
#x = vector(10, 0, 0)
#y = vector(0, 10, 0)
#z = vector(0, 0, 10)
#
#x_arrow = arrow(axis = x, shaftwidth = 0.1)
#y_arrow = arrow(axis = y, shaftwidth = 0.1)
#z_arrow = arrow(axis = z, shaftwidth = 0.1)


#r = vector(6, 8, 0)
#r_mag = mag(r)
#r_hat = norm(r)
#r_hat_mag = mag(r_hat)
#r_arrow = arrow(pos = vec(-5, 0, 0), axis = r, color = color.red, shaftwidth = 0.2)
#r_hat_arrow = arrow(axis = r_hat,
#color = color.cyan,
#shaftwidth = 0.2)
#print("r: ", r)
#print("r_mag: ", r_mag)
#print("r_hat_mag: " ,r_hat_mag)
#print("r_hat: ", r_hat)

#a = vector(3, 4, 0)
#b = vector(5, 1, 0)
#a_arrow = arrow(pos = vector(0, 0, 0), axis = a, shaftwidth = 0.2, color = color.blue)
#b_arrow = arrow(pos = vector(3, 4, 0), axis = b, shaftwidth = 0.2, color = color.green)
#c = a + b
#c_arrow = arrow(pos = vector(0, 0, 0), axis = c, shaftwidth = 0.2, color = color.red)

#a = vector(3, 4, 0)
#b = vector(5, 1, 0)
#a_arrow = arrow(pos = vector(0, 0, 0), axis = a, shaftwidth = 0.2, color = color.blue)
#b_arrow = arrow(pos = vector(0, 0, 0), axis = b, shaftwidth = 0.2, color = color.green)
#d = a - b
#d_arrow = arrow(pos = b, axis = d,
#shaftwidth = 0.2, color = color.red)


#a = box(pos = vec(0, 0, 0))
#b = sphere(pos = vec(2, 1, 0), radius = 1, color = color.yellow)
#a.pos, a.color = a.pos + vec(5, 1, 0), color.red
#b.pos, bradius, b.color = vec(0, 0, 0), 3, color.blue
#print(a.pos, b.pos, b.radius, sep='\n')
#
# a = box(pos = vec(0, 0, 0))
# b = sphere(pos = vec(2, 1, 0), radius = 1, color = color.yellow)

#
# ball = sphere(radius = 00.2)
# ball.pos = vec(-2, 0, 0)
# ball.v = vec(0.9, 0.2, 2)
# attach_arrow(ball, "v", shaftwidth=0.1, color = color.green)
# # print('initial ball pos:', ball.pos)
# # scene.waitfor('click')
# t = 0
# dt = 0.01
# while t < 4:
#     rate(100)
#     ball.pos = ball.pos + ball.v * dt
#     # print('t:', t)
#     # print('ball pos:', ball.pos)
#     # print(ball.v)
#     t = t + dt

# ball = sphere(radius = 0.2)
# ball.pos = vec(-2, 0, 0)
# ball.v = vec(0, 0, 0)
# ball.a = vec(0.35, 0, 0)
# t = 0
# dt = 1
# attach_arrow(ball, "v", shaftwidth=0.1, color=color.green)
# attach_arrow(ball, 'a', shaftwidth=0.05, color=color.red)
#
# while t < 4:
#     rate(100)
#     ball.v = ball.v + ball.a * dt
#     ball.pos = ball.pos + ball.v * dt
#     # print('t:', t)
#     # print('ball pos:', ball.pos)
#     # print(ball.v)
#     t = t + dt


# ball = sphere(radius = 0.2)
# ball.pos = vec(-2, 0, 0)
# ball.v = vec(0, 0, 0)
# ball.a = vec(0.35, 0, 0)
# t = 0
# dt = 0.01
# attach_arrow(ball, 'v', shaftwidth=0.1, color=color.green)
# attach_arrow(ball, 'a', shaftwidth=0.05, color=color.red)
# attach_trail(ball, type = "points", pps = 5)
#
# while t < 4:
#     rate(100)
#     ball.v = ball.v + ball.a * dt
#     ball.pos = ball.pos + ball.v * dt
#     t += 1


# ball = sphere(radius = 0.2, pos = vec(0, 3, 0))
# ball.v = (0, -0.1, 0)
# attach_arrow(ball, 'v', shaftwidth=0.1, color=color.red)
#
# dt = 0.01
# t = 0
# while t < 4:
#     rate(100)

#자유낙하운동
# ball = sphere(radius = 0.2)
# ground = box(pos = vec(0, -4, 0), size = vec(15, -0.01, 5))
#
# ball.pos = vec(0, 5, 0)
# ball.v = vec(0, 0, 0)
# ball.a = vec(0, -0.35, 0)
# attach_trail(ball, type = 'points', pps = 5)
# t = 0
# dt = 0.01
# dt2 = vec(0, -0.001, 0)
#
# while ball.pos.y > ground.pos.y:
#     rate(100)
#     ball.v = ball.v + ball.a * dt
#     ball.pos = ball.pos + ball.v * dt
#     t = t + dt

