from ya_disk import Yandex_Disk
import requests

"""Первое задание"""


url = "https://akabab.github.io/superhero-api/api/all.json"


response = requests.get(url)

data = response.json()

dict_all = {}
for i in data:
    dict_all[i.get("name")] = i.get("powerstats", 0).get("intelligence", 0)


def best_intelligence(dict, *names):
    dic = {}
    for name in names:
        if name not in dict:
            raise KeyError(f"Нет такого имени - {name}")
        dic[name] = dict[name]

    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    best = dic[0][0]
    print(f"Самый умный герой из {names} это: {best}")


best_intelligence(dict_all, "Hulk", "Captain America", "Thanos")
print()


"""Второе задание"""


TOKEN = "y0_AgAAAABZsbK1AADLWwAAAADgniB5WC3hGz18Q6qdhgWfEkPkqkqyjBY"

my_disk = Yandex_Disk(TOKEN)
file = 'test_file.txt'
# Если мы не добавляем второй параметр, то будет создана просто папка!
my_disk.upload_file_to_disk("netology")

my_disk.upload_file_to_disk("netology/test_12_04_23.txt", file)
