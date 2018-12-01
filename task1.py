from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію


def addUserProduct(user_name, bank_name, money):
        from data import dataset
        if user_name in dataset and bank_name not in dataset[user_name]:
            dataset[user_name].update(bank_name, money)
            return dataset
        elif user_name in dataset and bank_name in dataset[user_name]:
            banks = dataset[user_name][bank_name]
            banks.append(money)
            return dataset
        elif user_name not in dataset:
            dataset[user_name]=dict()
            dataset[user_name][bank_name]=[money]
            return dataset





# addUserProduct(user_name, bank_name, money):
#     dataset[user_name].update("bank_name": "money")
#
#
# #Додати існуючому користувачу нову покупку нового продукту
# addUserProduct(?,?,?)
#
# #Додати існуючому користувачу нову покупку існуючого продукту
# addUserProduct(?,?,?)
#
# print(dataset)
#
#
# print("\n\n")