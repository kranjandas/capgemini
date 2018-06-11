class base:
    def a(self):
        return 10
    def b(self):
        return 20

class derieved(base):
    def product(self):
        print(self.a()*self.b())
    def division(self):
        print(self.a()/self.b())

b=derieved()
b.product()
b.division()