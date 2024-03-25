import json


inventory = {
    "inventory": [
        {
            "item": "Кисти",
            "category": "Инструменты",
            "quantity": 5,
            "minimum_required": 10
        },
        {
            "item": "Краска акриловая",
            "category": "Материалы",
            "quantity": 20,
            "minimum_required": 15
        }
    ]
}

with open('inventory.json', 'w', encoding='utf-8') as file:
    json.dump(inventory, file)


def product_quantity(data):
    shop_list = {}
    for material in data['inventory']:
        item = material['item']
        quantity = material['quantity']
        min_required = material['minimum_required']
        required = min_required - quantity
        if item not in shop_list:
            if quantity < min_required:
                shop_list[item] = required
    return shop_list


result = product_quantity(inventory)

for items, inventory in result.items():
    print(f"Необходимо закупить:  {items} {inventory} шт.")

with open('inventory.json', 'r', encoding='utf-8') as file:
    inventory = json.load(file)
