def list_transformation():
    # Напишите код для преобразования произвольного списка вида
    # ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины)
    # в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

    list_random = ["2018-01-01", "yandex", "cpc", 100]
    x = {list_random[-2]: list_random[-1]}
    for i in list_random[-3::-1]:
        x = {i: x}
    return x


def visits_from_Russia():
    # Дан список с визитами по городам и странам.
    # Напишите код, который возвращает отфильтрованный
    # список geo_logs, содержащий только визиты из России."

    geo_logs = [
        {"visit1": ["Москва", "Россия"]},
        {"visit2": ["Дели", "Индия"]},
        {"visit3": ["Владимир", "Россия"]},
        {"visit4": ["Лиссабон", "Португалия"]},
        {"visit5": ["Париж", "Франция"]},
        {"visit6": ["Лиссабон", "Португалия"]},
        {"visit7": ["Тула", "Россия"]},
        {"visit8": ["Тула", "Россия"]},
        {"visit9": ["Курск", "Россия"]},
        {"visit10": ["Архангельск", "Россия"]},
    ]

    geo_logs = [i for i in geo_logs for value in i.values() if "Россия" in value]
    return geo_logs


def unique_id():
    # Выведите на экран все уникальные гео-ID из значений словаря ids.
    # Т.е. список вида [213, 15, 54, 119, 98, 35]

    ids = {
        "user1": [213, 213, 213, 15, 213],
        "user2": [54, 54, 119, 119, 119],
        "user3": [213, 98, 98, 35],
    }

    list_ID = list(set([value for i in list(ids.values()) for value in i]))
    return list_ID



if __name__ == '__main__':
    print(f"""=============
Результат функции 'list_transformation':
{list_transformation()}
============
Результат функции 'visits_from_Russia':
{visits_from_Russia()}
============
Результат функции 'unique_id':
{unique_id()}
============
""")
