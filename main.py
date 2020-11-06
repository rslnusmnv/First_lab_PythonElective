import string
import random
from random import randint


# Функция генерации электронных почт
def generateRandomMail(number: int):
    domain = ['yandex.ru', 'mail.ru', 'ssau.ru', 'gmail.com', 'rambler.ru', 'yahoo.com']
    mails = []
    for i in range(number):
        result = ""
        numberSymbols = randint(3, 12)
        for i in range(numberSymbols):
            result += random.choice(string.ascii_letters.lower())
        result += "@"
        result += random.choice(domain)
        mails.append(result)
    return mails


# Генерация и сохранения электронных почт в текстовый файл с названием "emails.txt"
number = 0
while number < 50:
    number = int(input("Введите количество генерируемых электронных почт: "))
emailsList = generateRandomMail(number)
print("Электронные почты сгенерированы")
emailsFile = open('emails.txt', 'w')
for item in emailsList:
    emailsFile.write("%s\n" % item)
emailsFile.close()
print("Сгенерированные электронные почты записаны в текстовый файл 'emails.txt'")


# Открытие файла с электронными почтами
emailsFile = open('emails.txt', 'r')
emailsForAnalyze = emailsFile.read()
emailsForAnalyze = emailsForAnalyze.splitlines()
print("Текстовый файл 'emails.txt' открыт")

# Выделение доменных имен
splitedEmails = []
for element in emailsForAnalyze:
    splitedEmails.append(element.split('@'))
domains = []
for i in range(len(splitedEmails)):
    domains.append(splitedEmails[i][1])
print("Выделены домены электронных почт")

# Сохранение доменов в текстовый файл "domains.txt"
domainsFile = open('domains.txt', 'w')
for item in domains:
    domainsFile.write("%s\n" % item)
domainsFile.close()
print("Выделенные домены записаны в текстовый файл 'domains.txt'")