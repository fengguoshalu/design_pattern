import abc


class Observer(metaclass=abc.ABCMeta):
    def __init__(self, name, subscribe):
        self.name = name
        self.subscribe = subscribe

    @abc.abstractmethod
    def update(self):
        pass


class StockObserver(Observer):

    def update(self):
        print("{}, {}, 别看股票了，去工作".format(self.name, self.subscribe.action))


class NBAObserver(Observer):

    def update(self):
        print("{}, {}, 别看NBA了，去工作".format(self.name, self.subscribe.action))


class SecretaryBase(metaclass=abc.ABCMeta):
    def __init__(self):
        self.observers = []

    @abc.abstractmethod
    def Attach(self, new_observer):
        pass

    @abc.abstractmethod
    def Notify(self):
        pass


class Secretary(SecretaryBase):

    def Attach(self, new_observer):
        self.observers.append(new_observer)

    def Notify(self):
        for i in self.observers:
            i.update()


if __name__ == '__main__':
    p = Secretary()
    s1 = StockObserver("风行", p)
    n1 = NBAObserver("钢背", p)

    p.Attach(s1)
    p.Attach(n1)

    p.action = "Boss 来了"
    p.Notify()