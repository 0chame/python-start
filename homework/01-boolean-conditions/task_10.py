# ДЗ 1, задача 10 «Допуск к экзамену» (★★☆)
# Задачник, задача 2.2.11: https://python-theory-makarov.vercel.app/zadachnik/2-2/index.html#p11
#
# Студента допускают к экзамену, если посещаемость не ниже 75%, сдано не меньше 8 лабораторных
# работ и нет долга по оплате. Вводятся посещаемость в процентах, число сданных работ и сумма
# долга. Выведите результат каждой проверки и общий ответ.
#
# Решение
posesh = int(input("Посешаемость, %: "))
sdano = int(input("Сдано лабораторных: "))
dolg = int(input("Долг по оплате, руб.: "))

posesh_dopysk = posesh >= 75
sdano_zachet = sdano >= 8
net_dolga = dolg == 0
dopysk = posesh_dopysk and sdano_zachet and net_dolga

print(f"Посещаемость: {posesh_dopysk}")
print(f"Лабораторная: {sdano_zachet}")
print(f"Нет долга: {net_dolga}")
print(f"Допущен: {dopysk}")