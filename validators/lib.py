
"""
    Написати валідатор ....
    Правило валідації
"""

import  re
import string
def get_user_id():
    user_id=input("Введите id")
    if len(user_id)!=16:
         return  get_user_id()
    if (re.match(r"\d{1,16}", user_id)):
        return user_id
    else:
        return get_user_id()
def get_bank():
    user_bank=input("Введите банк")
    if user_bank[0] not in string.ascii_uppercase:
        return  get_bank()
    if (re.match(r"^\w+[\w+|\d+]$", user_bank)):
        return user_bank
    else:
        return get_bank()
def get_user_money():
    user_money=input("Введите суму кредита")
    if (re.match(r"^\(\d+\.0\sgrn\)$", user_money)):
        return  user_money
    else:
        return get_user_money()