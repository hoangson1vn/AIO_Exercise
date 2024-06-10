import random
import math

def exercise3():
    number_sample = input('Input number of samples (integer number) which are generated: ')
    if not number_sample.isdigit():
        print('number of samples must be an integer number')
        return

    number_sample = int(number_sample)

    loss_name = input('Input loss name (MAE|MSE|RMSE): ')
    if loss_name not in ['MAE', 'MSE', 'RMSE']:
        print(f'{loss_name} is not a supported loss function')
        return

    total_loss = 0
    for i in range(number_sample):
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)

        if loss_name == 'MAE':
            loss = abs(pred - target)
        elif loss_name == 'MSE':
            loss = (pred - target) ** 2
        elif loss_name == 'RMSE':
            loss = (pred - target) ** 2

        total_loss += loss
        print(f'loss name: {loss_name}, sample: {i}, pred: {pred:.6f}, target: {target:.6f}, loss: {loss:.6f}')

    if loss_name == 'MAE':
        final_loss = total_loss / number_sample
    elif loss_name == 'MSE':
        final_loss = total_loss / number_sample
    elif loss_name == 'RMSE':
        final_loss = math.sqrt(total_loss / number_sample)

    print(f'final {loss_name}: {final_loss:.6f}')

exercise3()
