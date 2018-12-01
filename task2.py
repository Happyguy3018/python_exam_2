from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators.lib import get_user_id
from validators.lib import get_bank
from validators.lib import get_user_money

import re
import string
from task1 import addUserProduct


#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник.
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def addUserProductValidator():
    return addUserProduct(get_user_id(), get_bank(), get_user_money())
print(addUserProductValidator())


print("\n\n")