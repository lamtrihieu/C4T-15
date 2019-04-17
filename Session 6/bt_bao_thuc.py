import pyglet
from datetime import datetime

d_now = datetime.now().strftime("%H:%M")
w_time =  str("20:05")

while True:
    if d_now == w_time :
        music = pyglet.resource.media('sample.mp3')
        music.play()
        pyglet.app.run()
        print("Wake up")
        
    else:
        print("Not yet")
        break



# while True:
#     if date.time ==(19,30,0,0):
#         pyglet.app.run()