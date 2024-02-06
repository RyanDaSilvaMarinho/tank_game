from tank import tank
class bullet:

    def __init__(self, name, tank):
        self.name = name
        self.tank = tank

    def scope(self):
        print("tank in sight")

    def shoot(self, tank):
        self.tank = tank

    def destroy(self):
        self.tank.print_name()