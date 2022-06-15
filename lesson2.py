transactions = {
    "1":{
        "add":True,
        "sum":2,
        "person":{
            "name":"Petro",
        }
    },
    "2":{
        "add":True,
        "sum":2,
        "person":{
            "name":"Petro",
            "male":True
        }
    },
    "3":{
        "add":False,
        "sum":2,
        "person":{
            "name":"Petro",
            "male":True
        }
    },
    "4":{
        "add":False,
        "sum":2,
        "person":{
            "name":"Petro",
            "male":True
        }
    }
}

total_amount = 0
for transaction in transactions.values():
    # if transaction['add']:
    #     if "male" in transaction["person"].keys():
    #        total_amount += transaction["sum"]
    if transaction["add"] and "male" in transaction["person"].keys():
        total_amount += transaction["sum"]
print(total_amount)



# Добавить сумму транзакции, если add = True и среди продуктов есть "Хлеб"
# Должно выйти 172
sum = 0
transactions_homework = [
    {
        "add":True,
        "amount":69,
        "products":[
            "Хлеб",
            "Масло",
            "Сок",
        ]
    },
    {
        "add":True,
        "amount":30,
        "products":[
            "Сок",
        ]
    },
    {
        "add":True,
        "amount":94,
        "products":[
            "Мука",
            "Хлеб",
            "Масло",
        ]
    },
    {
        "add":False,
        "amount":24,
        "products":[
            "Конфеты",
            "Хлеб",
        ]
    },
    {
        "add":True,
        "amount":9,
        "products":[
            "Хлеб",
            "Шоколад",
            "Гречка",
        ]
    },
    {
        "add":True,
        "amount":91,
        "products":[
            "Апельсин",
            "Гречка",
        ]
    },
    {
        "add":True,
        "amount":84,
        "products":[
            "Помидоры",
            "Сок",
        ]
    },
    {
        "add":False,
        "amount":45,
        "products":[
            "Хлеб",
            "Гречка",
        ]
    },
    {
        "add":True,
        "amount":9,
        "products":[
            "Лимон",
            "Сок",
        ]
    },
]

for transaction in transactions_homework:
    if transaction["add"] and "Хлеб" in transaction["products"]:
        sum += transaction["amount"]
print(sum)