class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Деление на ноль невозможно"
        
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

calculator = Calculator(num1, num2)

print("Выберите операцию: ")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

if choice == '1':
    print(calculator.num1, "+", calculator.num2, "=", calculator.add())

elif choice == '2':
    print(calculator.num1, "-", calculator.num2, "=", calculator.subtract())

elif choice == '3':
    print(calculator.num1, "*", calculator.num2, "=", calculator.multiply())

elif choice == '4':
    print(calculator.num1, "/", calculator.num2, "=", calculator.divide())

else:
    print("Неверный номер операции.")
