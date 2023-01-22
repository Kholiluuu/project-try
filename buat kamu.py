import turtle as tur
import colorsys as cs

tur.setup(600,600)
tur.speed(0)
tur.tracer(100)
tur.width(2)
tur.screensize(50)
tur.bgcolor('black')
for j in range(25):
    for i in range (15):
        tur.color(cs.hls_to_rgb(i/15,j/25,1))
        tur.right(90)
        tur.circle(200-j*4,80)
        tur.left(90)
        tur.circle(200-j*4,80)
        tur.right(100)
        tur.circle(5,24)
tur.hideturtle()
tur.done
