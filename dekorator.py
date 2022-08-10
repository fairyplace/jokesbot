def decorator(func):
    def msg():
        print('start')
        func()
        print('end')
    return msg

def greet():
    print('hello')

d = decorator(greet)

print(d)