import pyglet
import pyglet2d

frame_rate = 120.0

window = pyglet.window.Window()

circle = pyglet2d.Shape.circle((300, 300), 50)

circle.color = (0, 255, 0)

@window.event
def on_draw():
    window.clear()
    circle.draw()


def update_positions(dt):
    circle.translate((1, 1))


pyglet.clock.schedule_interval(update_positions, 1 / frame_rate)

pyglet.app.run()
