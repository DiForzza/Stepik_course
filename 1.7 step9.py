from string import ascii_lowercase, digits
import re

class CardCheck:
    NUMBER_CORRECT = r'\d{4}-\d{4}-\d{4}-\d{4}'
    NAME_CORRECT = r'[A-Z\0-9]*\s[A-Z\0-9]*'

    def __init__(self):
        pass

    @classmethod
    def check_card_number(cls, number):
        match = re.fullmatch(cls.NUMBER_CORRECT, number)
        return True if match else False

    @classmethod
    def check_name(cls, name):
        match = re.fullmatch(cls.NAME_CORRECT, name)
        if match and len(match[0].split()) <= 2:
            return True
        else:
            return False


cc = CardCheck()
is_number = CardCheck.check_card_number('1234-1a34-1234-1234')
is_name = CardCheck.check_name('ASDASASD FSAFSA')
print(is_name)
#a = '3210-3452-8752-3874'
#match = re.fullmatch(r'\d{4}-\d{4}-\d{4}-\d{4}', a)
#print(match[0] if match else 'Not found')


# Подвиг 8. Объявите класс CardCheck для проверки корректности информации на пластиковых картах. Этот класс должен иметь следующие методы:
#
# check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True,
# если номер в верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
# check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True, если имя записано верно и False - в противном случае.
#
# Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами. Например, SERGEI BALAKIREV.
#
# Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):
#
# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# Для проверки допустимых символов в классе должен быть прописан атрибут:
#
# CHARS_FOR_NAME = ascii_lowercase.upper() + digits
# Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod).
#
# P.S. В программе только объявить класс. На экран ничего выводить не нужно.