try:
    class MyCustomException(Exception):
        def __init__(self, value):
            self.value = value

    raise (MyCustomException(10))

except MyCustomException as error:
    print('A New Exception occurred:', error.value)
