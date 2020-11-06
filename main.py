import string
import random
from random import randint


# Функция генерации электронных почт
def generateRandomMail(number: int):
    domains = ['yandex.ru', 'mail.ru', 'ssau.ru', 'gmail.com', 'rambler.ru', 'yahoo.com']
    mails = []
    for i in range(number):
        result = ""
        numberSymbols = randint(3, 12)
        for i in range(numberSymbols):
            result += random.choice(string.ascii_letters.lower())
        result += "@"
        result += random.choice(domains)
        mails.append(result)
    return mails


# Генерация и сохранения электронных почт в текстовый файл с названием "emails.txt"
number = int(input("Введите количество генерируемых электронных почт: "))
emailsList = generateRandomMail(number)
print(emailsList)
emails = open('emails.txt', 'w')
for item in emailsList:
    emails.write("%s\n" % item)
emails.close()

# Открытие файла с электронными почтами
emailsFile = open('emails.txt', 'r')
emailsListForAnalyze = emailsFile.read()
emailsListForAnalyze = emailsListForAnalyze.splitlines()
print(emailsListForAnalyze)