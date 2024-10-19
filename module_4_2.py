def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
test_function()
#inner_function() - Выдает ошибку имени.
#Вызов функции test_function(), выводит в консоль - Я в области видимости функции test_function