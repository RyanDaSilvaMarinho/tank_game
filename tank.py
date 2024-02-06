
class tank:

    def __init__(self, name):
        self.name = name
        self.movements = []
        self.tank_action = []
    def movement(self, move):
        self.movements.append(move)
    def tank_status(self, move):
        self.tank_action.append(move)
    def print_tank_status(self):
        print(self.tank_action)
    def print_movement(self):
        print(self.movements)

    def print_name(self):
        print(self.name)