import string
import random
from random import randint


def generateRandomMail(number: int):
    domains = ['yandex.ru', 'mail.ru', 'ssau.ru', 'gmail.com', 'rambler.ru', 'yahoo.com']
    mails =[]
    for i in range(number):
        result = ""
        numberSymbols = randint(3, 12)
        for i in range(numberSymbols):
            result += random.choice(string.ascii_letters)
        result += "@"
        result += random.choice(domains)
        mails.append(result)
    return mails
