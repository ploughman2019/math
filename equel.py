#-*- coding: UTF-8 -*-
import random
f = open("math_level1.txt", "w")
for i in range(0, 99):

        A = random.randint(1, 99)
        B = random.randint(1, 99)
        if A > B:
            Num1 = A
            Num2 = B
        else:
            Num1 = B
            Num2 = A
        operators = ["+", "-", "x", "÷"]
        j = random.randint(0, 3)
        if j ==0:
            answer = Num1 + Num2
        elif j == 1:
            answer = Num1 - Num2
        elif j == 2:
            answer = Num1 * Num2
        else:
            answer = Num1 // Num2
            answer_modulus = Num1 % Num2
        if j == 3:
            txt = "{}{}{} = {} ... {}\n"
            f.write(txt.format(Num1, operators[j], Num2, answer, answer_modulus))
        else:
            txt = "{}{}{} = {}\n"
            f.write(txt.format(Num1, operators[j], Num2, answer))
f.close()

