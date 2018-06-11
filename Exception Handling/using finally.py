try:
    a=eval(input("enter the first number:"))
    b=eval(input("enter the second number:"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("jiban")
finally:
    print("there is no exception")