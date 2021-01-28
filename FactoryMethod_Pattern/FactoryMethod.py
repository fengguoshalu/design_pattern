

class LeiFeng:
    def sweep(self):
        print("扫地")

    def wash(self):
        print("洗衣服")


class Student(LeiFeng):
    def sweep(self):
        print("Student Sweep")


class Volunteer(LeiFeng):
    def sweep(self):
        print("Volunteer Sweeping....")

    def wash(self):
        print("Volunteer Washing....")


class LeiFengFactory:
    def create_leifeng(self):
        temp = LeiFeng()
        return temp


class StudentFactory(LeiFengFactory):
    def create_leifeng(self):
        temp = Student()
        return temp


class VolunteerFactory(LeiFengFactory):
    def create_leifeng(self):
        temp = Volunteer()
        return temp


if __name__ == '__main__':
    sf = StudentFactory()
    s = sf.create_leifeng()
    s.sweep()

    vf = VolunteerFactory()
    v = vf.create_leifeng()
    v.sweep()

