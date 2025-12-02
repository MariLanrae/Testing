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

def calculate(choice, x, y):
    if choice == '1':
        return summ(x, y)
    elif choice == '2':
        return subtract(x, y)
    elif choice == '3':
        return multiply(x, y)
    elif choice == '4':
        return err(x, y)
    else:
        return None

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

            result = calculate(choice, num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                op_symbol = {'1': '+', '2': '-', '3': '*', '4': '/'}[choice]
                print(f"{num1} {op_symbol} {num2} = {result}")
        else:
            print("Ошибка. Пожалуйста, введите номер от 1 до 5.")

        print("-_" * 30)

if __name__ == "__main__":
    calculator()