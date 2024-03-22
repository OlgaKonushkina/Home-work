import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0 # счетчик для сохранения количества попыток
    predict = np.random.randint(1,101) # загадали список чисел
    left_border = 1 
    right_border = 101
    while number != predict:
        count += 1
        predict = left_border + (right_border-left_border) // 2 # находим число путем деления диапазона пополам
        if predict > number: right_border = predict
        elif predict < number: left_border = predict
        else: break

    return count

print(f'Количество попыток: {random_predict()}')
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)