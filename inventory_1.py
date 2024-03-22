import json
import yaml

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

with open('inventory.json', 'w', encoding='utf-8') as write_file:
    json.dump(inventory, write_file)

with open('inventory.json', 'r', encoding='utf-8') as read_file:
    json_data = json.load(read_file)


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


result = product_quantity(json_data)

for items, required in result.items():
    print(f"Необходимо закупить {yaml.dump(result, allow_unicode=True, default_flow_style=False)}")
