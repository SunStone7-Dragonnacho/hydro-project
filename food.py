class Food:

    def __init__(self, name, type, origin):
        self.name = name   
        self.type = type 
        self.origin = origin

    @property
    def menu_list(self):
        return '{} is {} from {}'.format(self.name, self.type, self.origin)

    def __repr__(self):
        return 'Food("{}", "{}", "{}")'.format(self.name, self.type, self.origin)

food = Food("Burger", "Fast Food", "America")
print(food.__repr__())