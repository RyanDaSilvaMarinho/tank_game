from bullet import bullet
from tank import tank

a = tank('tank a')
b = tank('tank b')

bullet1 = bullet('bullet',a)
bullet1.scope()
bullet1.shoot(b)
bullet1.destroy()

a.movement('tank a turn left')
b.tank_status('tank b is reaching tank a')
a.tank_status('shoot tank b')
b.movement('tank b exploded')
a.print_movement()
b.print_tank_status()
a.print_tank_status()
b.print_movement()

