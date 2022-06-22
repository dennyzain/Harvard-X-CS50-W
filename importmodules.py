# called a function from another file
import functions
# or 
# from functions import square

for i in range(10):
    print(f'the square of {i} is {functions.square(i)}')