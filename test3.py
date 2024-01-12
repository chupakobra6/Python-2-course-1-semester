import datetime

persons = dict(Леонов={"06.12.2002", "isip_i.m.leonov@mpt.ru"}, Андреева={"13.12.2006", "isip_i.m.andreeva@mpt.ru"},
               Зуев={"07.03.2005", "isip_i.m.zuev@mpt.ru"}, Давыдов={"14.07.2003", "isip_i.m.davidov@mpt.ru"},
               Шевцова={"16.02.2002", "isip_i.m.shevcova@mpt.ru"}, Аксёнов={"07.04.2002", "isip_i.m.aksenov@mpt.ru"},
               Филиппов={"14.06.2006", "isip_i.m.philippov@mpt.ru"},
               Ситников={"03.05.2000", "isip_i.m.sitnikova@mpt.ru"},
               Моисеева={"31.07.2002", "isip_i.m.moiseeva@mpt.ru"}, Козин={"18.01.2003", "isip_i.m.kozin@mpt.ru"})

inputday = input("Введите дату рождения (в формате ДД.ММ.ГГГГ): ")
inputday = inputday.split(".")

for i in range(len(inputday)):
    inputday[i] = int(inputday[i])

inputday = datetime.date(inputday[2], inputday[1], inputday[0])

values = []

for i in persons.values():
    value = list(i)
    for j in value:
        if not "@" in j:
            date = j.split(".")

            for k in range(len(date)):
                date[k] = int(date[k])

            date = datetime.date(date[2], date[1], date[0])

            if date > inputday:
                for key in persons.keys():
                    if j in persons[key]:
                        print(f"{key} - родился(ась) позже введённой даты")
