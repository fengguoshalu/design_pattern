class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("装扮的{}".format(self.name))


class Finery(Person):

    def __init__(self, person):
        self.person = person

    def show(self):
        if self.person is not None:
            self.show()


class TShirts(Finery):
    def show(self):
        print("大T恤，7470")
        self.person.show()


class BigTrouser(Finery):
    def show(self):
        print("穿了卫衣, 法国士兵")
        self.person.show()


class Shoes(Finery):
    def show(self):
        print("穿了破球鞋，跳走了")
        self.person.show()


class Hat(Finery):
    def show(self):
        print("戴了个帽子")
        self.person.show()


if __name__ == '__main__':
    p = Person("fy")
    ts = TShirts(p)
    ts.show()
    print("--"*10)
    bt = BigTrouser(p)
    bt.show()
    print("--" * 10)
    sh = Shoes(p)
    hat = Hat(sh)
    hat.show()