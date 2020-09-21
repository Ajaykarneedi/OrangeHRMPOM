
class one:

    def pri(self):
        x = 7
        print(x)
        print ("Inside Class One")

class two(one):

    def print(self):
        x = "In Second class"
        print(x)
        print("Inside Class Two")

class three(one):

    def pri(self):
        x = "In third class"
        print(x)
        print("Inside Class Three")


o = two
o.pri(two)

o = three
o.pri(three)

