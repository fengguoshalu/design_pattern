import abc


class People:
    def __init__(self):
        self._part = []

    def addPart(self, part):
        self._part.append(part)

    def show(self):
        print("\n\n创建一个新的人")
        for i in self._part:
            print(i)


class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def buildhead(self):
        pass

    @abc.abstractmethod
    def buildHand(self):
        pass

    @abc.abstractmethod
    def buildLeg(self):
        pass

    @abc.abstractmethod
    def getResult(self):
        pass


class PeopleBuilder1(Builder):

    # def __init__(self):
    #     super().__init__()
    #     self.people = People()
    def __init__(self):
        self.people = People()

    def buildhead(self):
        self.people.addPart("我来组成头部")

    def buildLeg(self):
        self.people.addPart("我来组成腿部")

    def buildHand(self):
        self.people.addPart("我来组成手部")

    def getResult(self):
        return self.people


class PeopleBuilder2(Builder):

    # def __init__(self):
    #     super().__init__()
    #     self.people = People()
    # self.people = People()

    def __init__(self):
        self.people = People()

    def buildhead(self):
        self.people.addPart("我来组成两个头部")

    def buildLeg(self):
        self.people.addPart("我们要去哪")

    def buildHand(self):
        self.people.addPart("你打我干什么")

    def getResult(self):
        return self.people


class Director:

    def construct(self, pepple_builder):
        pepple_builder.buildhead()
        pepple_builder.buildLeg()
        pepple_builder.buildHand()


if __name__ == '__main__':
    director = Director()
    b1 = PeopleBuilder1()
    b2 = PeopleBuilder2()

    director.construct(b1)
    p1 = b1.getResult()
    p1.show()

    director.construct(b2)
    p2 = b2.getResult()
    p2.show()