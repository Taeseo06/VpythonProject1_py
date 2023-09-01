import vpython as vp

# 바닥을 정의합니다.
floor = vp.box(pos=vp.vec(0, -1, 0), size=vp.vec(10, 1, 1), color=vp.color.white)

# 물체를 정의합니다.
ball = vp.sphere(pos=vp.vec(0, 0, 0), radius=1, color=vp.color.red)

# 마우스의 위치를 얻습니다.
def update():
    # 마우스의 위치
    x, y = vp.mouse.pos

    # 마우스와 물체 사이의 거리를 구합니다.
    distance = vp.mag(ball.pos - vp.vec(x, y, 0))

    # 힘을 구합니다.
    force = distance * 0.1

    # 힘을 적용합니다.
    if vp.mouse.left:
        ball.v += force / ball.m * vp.dt
        ball.pos += ball.v * vp.dt

vp.rate(100)
vp.window.run()

while True:
    update()
