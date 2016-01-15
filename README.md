# Spherodidact
A classic balls-that-don't-really-do-anything simulation. A testbed for my upcoming project, Undulation-Devastation, a life simulator.

I'm talking about that first opengl program you did in junior college - you know, built from scratch, with your own bound detection, then collision detection... fun times. Then you messed with the settings - why not some gravity? Hey, why not gravity on the surface of Mars? Why not a white dwarf? And what if you had negative friction? As in, surfaces just accelerated against each other for no reason? Cool.

Anyway, I'm writing this to get a handle on pyglet, then on pymunk. I will tag major milestones along the way.

The finished product will:
### pyglet phase:
- [ ] draw a few different shapes
- [ ] draw a few shapes that have multicolored blending effects
- [ ] move the shapes both linearly and rotationally
### pymunk integration phase:
- [ ] draw a bunch of physicsified circles, squares, and triangles
  - [ ] demonstrate an off-kilter center of mass
  - [ ] demonstrate random colors, including multicolor objects
- [ ] allow them to interact in a gravity environment
- [ ] allow the creation of magical no-gravity shapes
- [ ] allow for the creation of a ghost shape that simply does not collide with other shapes
