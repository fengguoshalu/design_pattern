
class CashSuper:

    def accept_cash(self, money):
        return 0


class CashNormal(CashSuper):

    def accept_cash(self, money):
        return money


class CashRebate(CashSuper):

    def __init__(self, discount):
        self._discount = discount

    def accept_cash(self, money):
        return money * self._discount


class CashReturn(CashSuper):

    def __init__(self, total, ret):
        self.total = total
        self.ret = ret

    def accept_cash(self, money):
        if money >= self.total:
            money -= self.ret
        return money


class CashContext:
    def __init__(self, cashSuper):
        self.cs = cashSuper

    def get_result(self, money):
        return self.cs.accept_cash(money)


if __name__ == '__main__':
    while True:
        money = float(input("money="))
        strategy = {
            1: CashContext(CashNormal()),
            2: CashContext(CashRebate(0.8)),
            3: CashContext(CashReturn(200, 100))
        }
        ctype = int(input("type:[1]normal, [2]rebate, [3]return :"))
        if ctype in strategy:
            ss = strategy[ctype]
        else:
            ss = strategy[2]
        print("final pay:", ss.get_result(money))
