class base:
    def a(self):
        return 20
    def b(self):
        return 30
class sum(base):
    def sum(self):
        print(self.a() + self.b())

class mul(base):
    def mul(self):
        print(self.a() * self.b())

s=sum()
s.sum()

m=mul()
m.mul()