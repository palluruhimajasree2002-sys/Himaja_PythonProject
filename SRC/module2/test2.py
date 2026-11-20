def welcome():
    print("welocme to python")

def my_decorater(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@my_decorater
def addition():
    print("welcome")

addition()
welcome()


