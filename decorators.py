# decorators

def announce(f):
    def wrapper():
        print('about to run the function...')
        f()
        print('done with the function')
    return wrapper

@announce
def hello():
    print('hello world!')

hello()

# if i run the hello() the announce method automatically invoke and hello method will be parameter

@announce
def greet():
    print('hello nice to meet you!')

greet()