persons = dict(Леонов={"06.12.2002", "isip_i.m.leonov@mpt.ru"}, Андреева={"13.12.2006", "isip_i.m.andreeva@mpt.ru"},
               Зуев={"07.03.2005", "isip_i.m.zuev@mpt.ru"}, Давыдов={"14.07.2003", "isip_i.m.davidov@mpt.ru"},
               Шевцова={"16.02.2002", "isip_i.m.shevcova@mpt.ru"}, Аксёнов={"07.04.2002", "isip_i.m.aksenov@mpt.ru"},
               Филиппов={"14.06.2006", "isip_i.m.philippov@mpt.ru"},
               Ситников={"03.05.2000", "isip_i.m.sitnikova@mpt.ru"},
               Моисеева={"31.07.2002", "isip_i.m.moiseeva@mpt.ru"}, Козин={"18.01.2003", "isip_i.m.kozin@mpt.ru"})

inputday = input("Введите дату проверки (в формат ДД.ММ.ГГГГ) - ")
inputday = inputday.split(".")

values,  values2, values3, persons2 = [], [], [], []

for i in persons.values():
    values.extend(i)
for i in range(len(values)):
    if "@" not in values[i]:
        values2.append(values[i])

for i in range(len(values2)):
    a = values2[i].split(".")
    day = int(a[0])
    month = int(a[1])
    year = int(a[2])
    day2 = int(inputday[0])
    month2 = int(inputday[1])
    year2 = int(inputday[2])
    if year > year2:
        values3.append(a)
    elif year == year2:
        if month > month2:
            values3.append(a)
        elif month == month2:
            if day > day2:
                values3.append(a)

values.clear()
s = "."
for i in range(len(values3)):
    values.append(s.join(values3[i]))

i = 0
for key in persons:
    if values[i] in persons[key]:
        print(f"{key} - родился(ась) позже введённой даты")
        i += 1
        if i == len(values):
            break
