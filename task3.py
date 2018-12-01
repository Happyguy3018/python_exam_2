
from data import dataset
import re
from task1 import addUserProduct

#   Написати рекурсивну функцію, що повертає інформацію: хто і скільки грошей витратив на свої покупки.
#   Рекурсивно необхідно пройтись по користувачам та спискам їх товарів.


#product_list - словник з dataset, що зберігає товар та список його покупок (цін)
def recursionByProducts(user_id, banks, money, amount_of_money = 0):
    if money==[]:
        return amount_of_money
    current_money = dataset[user_id][banks[0]]
    current_money=re.findall('\d+', current_money)
    amount_of_money+=current_money
    return recursionByProducts(user_id, banks[1:], amount_of_money)



def recursionByUsers(users_id = list(dataset.keys()), result_dict = dict()):
    if users_id == []:
        return result_dict
    user_id= users_id[0]
    banks = list (dataset[user_id].keys())
    money = recursionByProducts(user_id, banks)

    result_dict[user_id] = money

    return recursionByUsers(users_id[1:], result_dict)

#print("Task 3")

#result = recursionByUsers()
#print(result)

#print("\n\n")



