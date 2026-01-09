class IOString():

    def __init__(self):
        self.str1 = "test"

    def inp(self):
        self.str1 = input("Input a string: ")
    
    def up(self):
        print(self.str1.upper())

a = IOString()
a.inp()
a.up()