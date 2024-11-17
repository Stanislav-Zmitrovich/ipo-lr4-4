# Исходный список вещественных чисел
original_list = [1.5, 2.3, 4.7, 5.0, 6.8]
# Пустой список для хранения целых частей
integer_parts_list = []
# Инициализация индекса
i = 0
# Используем цикл while для обхода элементов списка и добавления их целых частей в новый список
while i < len(original_list):
    integer_parts_list.append(int(original_list[i]))
    i += 1
# Вывод нового списка
print(integer_parts_list)
