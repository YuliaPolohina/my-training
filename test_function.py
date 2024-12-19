def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

#inner_function() - при вызове функции происходит ошибка name 'inner_function' is not defined, т.к. имя не срабатывает вне функции 
test_function()
