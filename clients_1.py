import json
import csv
from datetime import datetime, date
import re


class Client:
    def __init__(self, name, surname, birthday, bonuses):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.bonuses = bonuses

    @staticmethod
    def verification_client(name, surname, birthday, bonuses):
        if not (0 <= bonuses <= 10000000):
            return False
        if not (re.match(r'^[А-Яа-яЁё\s]+$', name) and re.match(r'[А-Яа-яЁё\s]+$', surname)):
            return False
        try:
            birth_date = datetime.strptime(birthday, '%d.%m.%Y').date()
            current_date = date.today()
            if birth_date > current_date or birth_date.year < 1950:
                return False
        except ValueError:
            return False
        return True


def cvs_to_json(file):
    processed_rec = 0  # Обработанные клиенты
    missing_res = 0  # Пропущенные клиенты
    with open(file, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        clients = []
        for row in csv_reader:
            try:
                name = row['Name'].lower()
                surname = row['Surname'].lower()
                birthday = row['Birthday']
                bonuses = int(row['Bonuses'])
                if Client.verification_client(name, surname, birthday, bonuses):
                    clients.append({
                        'name': name,
                        'surname': surname,
                        'birthday': birthday,
                        'bonuses': bonuses
                    })
                    processed_rec += 1
                else:
                    missing_res += 1
            except (ValueError, KeyError):
                missing_res += 1

        with open('clients.json', 'w', encoding='utf-8') as json_file:
            json.dump({'clients': clients}, json_file, ensure_ascii=False, indent=2)

    print(f"Было обработано (клиентов): {processed_rec} \nБыло пропущено (клиентов)Ж {missing_res}")


cvs_to_json('clients.cvs')
