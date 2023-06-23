# №3.  Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

a_1 = ""
a_2 = ""
b_1 = ""
b_2 = ""
fraction_1 = input("Введите первую дробь в виде 'a/b': ")
fraction_2 = input("Введите вторую дробь в виде 'a/b': ")
a_1 = int(fraction_1[0])
a_2 = a_2_2 = int(fraction_1[2])
b_1 = int(fraction_2[0])
b_2 = int(fraction_2[2])
print("Произведение дробей равно: ", a_1 * b_1,"/", a_2 * b_2)

if a_2 != b_2:
    a_1 *= b_2
    a_2 *= b_2
    b_1 *= a_2_2
    b_2 *= a_2_2
    print("Сумма дробей равна: ", a_1 + b_1,"/", a_2)

else:
    print("Cумма дробей равна: ", a_1 + b_1,"/", a_2)

fraction_1 = fractions.Fraction(a_1, a_2)
fraction_2 = fractions.Fraction(b_1, b_2)
print("Произведение дробей равно: ", fraction_1 * fraction_2)
print("Cумма дробей равна: ", fraction_1 + fraction_2)