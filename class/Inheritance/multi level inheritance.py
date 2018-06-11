class base:
    def a(self):
        return 10
    def b(self):
        return 20


class derieved(base):
    def sum(self):
        return(self.a()+self.b())


class finalderieved(derieved):
    def avg(self):
        print(self.sum() / 2)

d=derieved()
d.sum()

f=finalderieved()
f.avg()
