import os
import datetime
import time
import sys
from datetime import datetime
from colorama import Fore, Back, Style
import webbrowser

блокнот = " "

print(Fore.GREEN + "Начало загрузки [ ]")
time.sleep(1)
os.system("cls")
print(Fore.GREEN + "Начало загрузки [✓]")
print(Fore.GREEN + "Загрузка функций")

def rabota():
    print(Back.WHITE + Fore.BLACK + "Блокнот")
    print(Back.WHITE + Fore.BLACK + "Калькулятор")
    print(Back.WHITE + Fore.BLACK + "KerBrowser")
    print(Back.WHITE + Fore.BLACK + "Конец работы")
    command = input("Ввод команды: ")
    if command == "Блокнот":
        os.system("cls")
        bloknot()
    elif command == "Калькулятор":
        os.system("cls")
        calcul()
    elif command == "KerBrowser":
        os.system("cls")
        browser()
    elif command == "Конец работы":
        konez()
    else:
        os.system("cls")
        rabota()

def bloknot():
    global блокнот
    if блокнот == " ":
        print("Создан новый временный документ")
        блокнот = input()
        print("Закрытие программы")
        os.system("cls")
        rabota()
    else:
        print(блокнот)
        print("Напишите exit для выхода")
        user_input = input()
        if user_input == "exit":
            os.system("cls")
            rabota()
        else:
            print("Неизвестная команда")
            time.sleep(1)
            os.system("cls")
            bloknot()

def calcul():
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")
    
    num1 = float(input("Введите первое число: "))
    operation = input("Введите операцию: ")
    num2 = float(input("Введите второе число: "))
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ошибка: деление на ноль!")
            time.sleep(2)
            os.system("cls")
            calcul()
            return
    else:
        print("Неизвестная операция!")
        time.sleep(2)
        os.system("cls")
        calcul()
        return
    
    print(f"Результат: {result}")
    time.sleep(2)
    os.system("cls")
    rabota()

def browser():
    user_input = input("Введите запрос: ")
    url = "https://www.google.com/search?q=" + user_input
    webbrowser.open(url)
    time.sleep(1)
    os.system("cls")
    rabota()

def konez():
    sys.exit(0)

print("Загрузка Окончена")
time.sleep(1)
os.system("cls")
rabota()