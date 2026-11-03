# ДЗ 1, задача 5 «Сданные экзамены» (★★★)
# Задачник, задача 2.1.13: https://python-theory-makarov.vercel.app/zadachnik/2-1/index.html#p13
#
# Студент сдал три экзамена. Экзамен сдан, если балл не меньше 40. Вводятся три балла. Выведите,
# сколько экзаменов сдано и сданы ли все три.
#
# Решение
Exams_passed = 0

ball_1 = int(input("Баллы за первый экзамен: "))
if ball_1 >= 40:
    Exams_passed = Exams_passed + 1
else:
    Exams_passed = Exams_passed + 0

ball_2 = int(input("Балл за второй экзамен: "))
if ball_2 >= 40:
    Exams_passed = Exams_passed + 1
else:
    Exams_passed = Exams_passed + 0

ball_3 = int(input("Балл за третий экзамен: "))
if ball_3 >= 40:
    Exams_passed = Exams_passed + 1
else:
    Exams_passed = Exams_passed + 0

print(f"Сдано экзаменов: {Exams_passed}")
print(f"Сессия закрыта: {Exams_passed == 3}")