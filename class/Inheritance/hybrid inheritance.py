class base:
    def a(self):
        return 20

    def b(self):
        return 30
class derieved1(base):
    def sum(self):
        return(self.a() + self.b())

class derieved2(base):
    def sub(self):
        return(self.a() - self.b())

class last_derieved(derieved1,derieved2):
    def avg(self):
        print(self.sum() + self.sub())

l=last_derieved()
l.avg()