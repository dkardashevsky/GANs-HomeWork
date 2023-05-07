import pprint
import random

# Возможные элементы стиля
styles = {
    'Причёска':[
        'Нет волос',
        'Длинные в пучок',
        'Длинные волнистые',
        'Длинные прямые',
        'Короткая волнистые',
        'Короткая прямые',
        'Короткая курчавые'
    ],
    'Цвет волос':[
        'Чёрный',
        'Блонд',
        'Каштановый',
        'Пастельный розовый',
        'Рыжий',
        'Серебристо серый',
    ],
    'Аксесуар':[
        'Нет очков',
        'Круглые очки',
        'Солнцезащитные очки',
    ],
    'Одежда':[
        'Худи',
        'Комбинезон',
        'Футболка с круглым вырезом',
        'Футболка с V-вырезом',
    ],
    'Цвет одежды':[
        'Чёрный',
        'Синий',
        'Серый',
        'Зеленый',
        'Оранжевый',
        'Розовый',
        'Красный',
        'Белый'
    ],
}

# Колличество элементов стиля в наблюдаемых данных
styles_count = {
    'Причёска':[
        7,
        0,
        1,
        23,
        1,
        11,
        7
    ],
    'Цвет волос':[
        7,
        6,
        2,
        3,
        8,
        24,
    ],
    'Аксесуар':[
        11,
        22,
        17,
    ],
    'Одежда':[
        7,
        18,
        19,
        6,
    ],
    'Цвет одежды':[
        4,
        5,
        6,
        8,
        6,
        8,
        7,
        6
    ],
}


# Создаём свой класс исключения для вывода ошибки данных
class DataError(Exception):
    pass

check_data = 0
for s in styles_count['Причёска']:
    check_data += s

# Находим N - колличество всех образцов, которые есть в выборке
print('\nData:')
for k in styles_count:
    summ = 0
    for s in styles_count[k]:
        summ += s
    print(k, summ)
    if check_data != summ:
        raise DataError("Invalid data")

# Создаём словарь вероятностей
prob = {}

# Считаем вероятности встретить элемент
for k in styles:
    prob[k] = []
    summ_k = summ + len(styles[k])
    for n, i_styles in enumerate(styles[k]):
        prob_n = (styles_count[k][n] + 1) / summ_k
        prob[k].append( prob_n )

# Выводим значение вероятностей встретить элемент
print('\nProbabilities:')
pprint.pprint(prob)


feature = 'Аксесуар'
result_style = {}

# Случайно собираем новый стиль
for feature in styles:
    p_acc = prob[feature]
    acc = styles[feature]
    result_style[feature] = random.choices(acc, p_acc)[0]

if result_style['Причёска'] == 'Нет волос':
    result_style.pop('Цвет волос')

# Выводим параметры случайно собранного стиля
print('\nNew style:')
pprint.pprint(result_style)
