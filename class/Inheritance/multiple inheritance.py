class base1:
    def a(self):
        return 20

class base2:
    def b(self):
        return 30

class sum(base1,base2):
    def sum(self):
        print(self.a() + self.b())

class sub(base1,base2):
    def sub(self):
        print(self.a() - self.b())

s=sum()
s.sum()

f=sub()
f.sub()