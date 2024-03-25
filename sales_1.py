import json

sales = {
    "sales": [
        {
            "product": "Футболка",
            "category": "Одежда",
            "quantity": 3,
            "total_price": 1500
        },
        {
            "product": "Чашка",
            "category": "Посуда",
            "quantity": 2,
            "total_price": 700
        }
    ]
}


with open('sales.json', 'w', encoding='utf-8') as write_file:
    json.dump(sales, write_file)

with open("sales.json", "r", encoding="utf-8") as read_file:
    json_data = json.load(read_file)


def calculation_revenue(data):
    end_info = {}
    for sale in data['sales']:
        category = sale['category']
        total_price = sale['total_price'] * sale['quantity']
        if category not in end_info:
            end_info[category] = total_price
        else:
            end_info[category] += total_price
    return end_info


result = calculation_revenue(json_data)

for category, total_price in result.items():
    print(f"Выручка по категории: {category}: {total_price}")
