import math
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def exercise2():
    x = input('Input x = ')
    if not is_number(x):
        print('x must be a number')
        return

    x = float(x)
    acti_fun = input('Input activation Function (sigmoid|relu|elu): ')

    if acti_fun == 'sigmoid':
        result = 1 / (1 + math.exp(-x))
    elif acti_fun == 'relu':
        result = max(0, x)
    elif acti_fun == 'elu':
        alpha = 0.01
        result = alpha * (math.exp(x) - 1) if x <= 0 else x
    else:
        print(f'{acti_fun} is not supported')
        return

    print(f'{acti_fun}: f({x}) = {result}')

exercise2()
