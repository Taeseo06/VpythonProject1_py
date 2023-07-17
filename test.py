# def draw_parabola(): # 운동1 - 포물선 운동
#   # 포물선운동
#   ball = sphere(radius = 0.2) # 물체 반지름
#   ground = box(pos=vec(0, -4, 0), size=vec(15, -0.01, 5))
#   ball.pos = vec(-2, 0, 0)
#   ball.v = vec(1, 1, 0)  # y값 0 : 제자리에서 포물선 운동, 1 : 위로 올라갔다가 떨어지는 포물선운동r
#   ball.a = vec(0, -0.35, 0)
#   attach_trail(ball, type='points', pps=5)
#
#   t = 0
#   dt = 0.01
#   while ball.pos.y > ground.pos.y:
#     rate(1 / dt)
#     ball.v = ball.v + ball.a * dt
#     ball.pos = ball.pos + ball.v * dt
#     t = t + dt
#   # 아래는 포물선 운동 그래프 구현
#   motion_graph = graph(title='position-time', xtitle='t', ytitle='y')
#   g_bally = gcurve()
#
#   motion_graph = graph(title='velocity-time', xtitle='t', ytitle='vy')
#   g_ballvy = gcurve(color=color.green)
#
#   while ball.pos.y > ground.pos.y:
#     rate(1 / dt)
#     ball.v = ball.v + ball.a * dt
#     ball.pos = ball.pos + ball.v * dt
#     g_bally.plot(pos=(t, ball.pos.y))
#     g_ballvy.plot(pos=(t, ball.v.y))
#     t = t + dt
#
#   max_y = ball.pos.y
#   max_t = t
#   while ball.pos.y > ground.pos.y:
#     rate(1 / dt)
#     if ball.pos.y > max_y:
#       max_y = ball.pos.y
#       max_t = t
#     ball.v = ball.v + ball.a * dt
#     ball.pos = ball.pos + ball.v * dt
#     g_bally.plot(pos=(t, ball.pos.y))
#     g_ballvy.plot(pos=(t, ball.v.y))
#     t = t + dt
#   print('max_y:', max_y)
#   print('max_t:', max_t)