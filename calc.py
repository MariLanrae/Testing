
def summ(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def err(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def calculator():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выход")

    while True:
        choice = input("Введите номер операции: ")

        if choice == '5':
            print("Выход из калькулятора.")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))

                if num1.is_integer():
                    num1 = int(num1)
                if num2.is_integer():
                    num2 = int(num2)

            except ValueError:
                print("Ошибка: введите число.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                res = err(num1, num2)
                if isinstance(res, str):
                    print(res)
                else:
                    print(f"{num1} / {num2} = {res}")
        else:
            print("Ошибка. Пожалуйста, введите номер от 1 до 5.")

        print("-_" * 30)

if __name__ == "__main__":
    calculator()