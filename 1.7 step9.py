from string import ascii_lowercase, digits
import re

class CardCheck:
    CHARS_CORRECT = r'\d{4}-\d{4}-\d{4}-\d{4}'

    def __init__(self):
        pass

    @classmethod
    def check_card_number(cls, number):
        match = re.fullmatch(cls.CHARS_CORRECT, number)
        return True if match else False


cc = CardCheck()
print(cc.check_card_number('3210-3952-8752-3474'))
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