
class tank:

    def __init__(self, name):
        self.name = name
        self.movements = []

    def movement(self, move):
        self.movements.append(move)

    def print_movement(self):
        print(self.movements)

    def print_name(self):
        print(self.name)