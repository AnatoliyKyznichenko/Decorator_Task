"""Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов
будет показывать в консоли сообщение "Покупайте наших котиков!"
и возвращать результат запущенной функции. 1.2 Параметризовать декоратор таким образом,
чтобы сообщение, печатаемое перед выполнением функции можно было задавать как параметр во время декорирования."""


# def cat_message(message='Покупайте наших котиков'):
#     def decorator(function):
#         def wrapper(*args):
#             print(message)
#             result = function(*args)
#             return result
#         return wrapper
#     return decorator
#
#
# @cat_message("Спасибо за поддержку наших котиков!")
# def func(a, b):
#     return a + b
#
#
# result = func(3, 5)
# print("Результат функции:", result)


# """Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае
# успешного выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы
# выполнение функции было повторено ещё раз с теми же самыми аргументами, но не более 10 раз.
# Если после последней попытки функцию так и не удастся выполнить успешно, то бросать исключение.
# 2.2 Параметризовать декоратор таким образом, чтобы количество попыток выполнения функции можно было задавать
# как параметр во время декорирования."""
#
#
#
#
# def func(a, b, i=0):
#     if i == 10:
#         print("Превышено максимальное количество попыток.")
#         return
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         return a + b
#     else:
#         print('Вы ввели не корректные данные')
#         func(a, b, i + 1)
#
#
#
# print(func('jdfjg', 'hfsdjkhf'))