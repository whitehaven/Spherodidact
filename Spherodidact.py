import pyglet
import primitives

window = pyglet.window.Window()
circle = primitives.Circle(x=200, y=200, z=0, width=50, color=(1, 0, 0, 1), stroke=25, rotation=0.0,
                           style=pyglet.gl.GLU_FILL)


@window.event
def on_draw():
    window.clear()
    circle.render()


pyglet.app.run()
