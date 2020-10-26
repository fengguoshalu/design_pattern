

class Subject:
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("真实的请求")


class Proxy(Subject):
    def __init__(self, real_subject=RealSubject()):
        self.real_subject = real_subject

    def request(self):
        if self.real_subject is None:
            self.real_subject = RealSubject()
        self.real_subject.request()


if __name__ == '__main__':
    proxy = Proxy()
    proxy.request()