""" Функция 'расход_топлива': displacement-литраж;
                              mileage-километраж;
                              kilometers-километры;
                              consumption-расход."""

import sys


def fuel_consumption():
    print('Введите кол-во израсходованных литров:')
    displacement = float(sys.stdin.readline())
    print('Введите кол-во пройденных километров:')
    mileage = float(sys.stdin.readline())
    print('Введите кол-во км на которое Вы хотите расчитать расход топлива:')
    kilometers = float(sys.stdin.readline())
    consumption = (displacement / mileage) * kilometers
    return 'Ваша машина потребляет %s литров на %s км' % (consumption, kilometers)


print(fuel_consumption())
