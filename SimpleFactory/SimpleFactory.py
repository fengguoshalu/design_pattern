class Operation:
    def __init__(self):
        self.op1 = 0
        self.op2 = 0

    def get_result(self):
        pass


class OperationAdd(Operation):
    def get_result(self):
        return self.op1 + self.op2


class OperationSub(Operation):
    def get_result(self):
        return self.op1 - self.op2


class OperationMul(Operation):
    def get_result(self):
        return self.op1 * self.op2


class OperationDiv(Operation):
    def get_result(self):
        try:
            result = self.op1 / self.op2
            return result
        except Exception as e:
            print("ERROR:Divided by 0,")
            return 0


class OperationUndef(Operation):
    def get_result(self):
        print("Undefined Operation")
        return 0


class OperationFactory:
    operation = {"+": OperationAdd(), "-": OperationSub(), "*": OperationMul(), "/": OperationDiv()}

    def create_operation(self, ch):
        if ch in self.operation:
            return self.operation[ch]
        else:
            return OperationUndef()


if __name__ == '__main__':
    while True:
        op = input("operator:")
        opa = float(input("a="))
        opb = float(input("b="))
        factory = OperationFactory()
        cal = factory.create_operation(op)
        cal.op1 = opa
        cal.op2 = opb
        print("result=", cal.get_result())
