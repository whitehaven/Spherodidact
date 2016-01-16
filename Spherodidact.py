import pyglet
import primitives

frame_rate = 120.0

window = pyglet.window.Window()
circle = primitives.Circle(x=200, y=200, z=0, width=50, color=(1, 0, 0, 1), stroke=25, rotation=0.0,
                           style=pyglet.gl.GLU_FILL)


@window.event
def on_draw():
    window.clear()
    circle.render()


def update_positions(dt):
    circle.x += 10 * dt


pyglet.clock.schedule_interval(update_positions, 1 / frame_rate)

pyglet.app.run()
