def filter_integers(real_numbers):
# Генератор списка, который возвращает только целые числа из списка вещественных чисел
    return [number for number in real_numbers if number == int(number)]
# Запрос ввода вещественных чисел у пользователя
input_numbers = input("Введите вещественные числа через пробел: ")
# Преобразование введенных данных в список вещественных чисел
real_numbers = list(map(float, input_numbers.split()))
# Фильтрация списка, оставляя только целые числа
integers_only = filter_integers(real_numbers)
# Вывод результата
print("Список целых чисел:", integers_only)
