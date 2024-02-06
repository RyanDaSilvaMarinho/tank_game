from bullet import bullet
from tank import tank

a = tank('a')
b = tank('b')

bullet1 = bullet('bullet',a)
bullet1.scope()
bullet1.shoot(b)
bullet1.destroy()

a.movement('shoot tank b')
b.movement('tank b exploded')
a.print_movement()