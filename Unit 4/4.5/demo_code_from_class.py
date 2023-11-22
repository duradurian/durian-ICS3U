class Vegetable:
    def __init__(self, vegtype):
        self.__vegtype = vegtype

    def message(self):
        print("I'm a vegetable.")

class Potato(Vegetable):
    def __init__(self):
        super().__init__('potato')

    def message(self):
        print("I'm a potato.")

def main():
    v = Vegetable('veggie')
    p = Potato()
    p.message()
    v.message()

# Call the main function.
main()
