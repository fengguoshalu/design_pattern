# 模板方法模式

class Paper:
    def question1(self):
        print("Question1 Choose A, B, C, D")
        self.answer1()

    def question2(self):
        print("Question2 Choose A, B, C, D")
        self.answer2()


class StudetPaper1(Paper):
    def answer1(self):
        print("Studet1 Choose A")

    def answer2(self):
        print("Studet1 Choose C")


class StudetPaper2(Paper):
    def answer1(self):
        print("Studet2 Choose B")

    def answer2(self):
        print("Studet2 Choose D")


if __name__ == '__main__':
    print("*"*20, "Student1", "*"*20)
    studet1 = StudetPaper1()
    studet1.question1()
    studet1.question2()

    print("*" * 20, "Student2", "*" * 20)
    studet2 = StudetPaper2()
    studet2.question1()
    studet2.question2()