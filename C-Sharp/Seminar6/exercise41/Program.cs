/*Задача 41: Пользователь вводит с клавиатуры M чисел. 
Посчитайте, сколько чисел больше 0 ввёл пользователь.
0, 7, 8, -2, -2 -> 2
1, -7, 567, 89, 223-> 3*/

Console.Write("Введите колличество чисел: ");
int  M = int.Parse(Console.ReadLine());

void PositiveNumbers(int num)
{
    int count = 0;
    for (int i = 0; i < num; i++)
    {
        Console.Write($"Введите число {i+1}: ");
        int index = int.Parse(Console.ReadLine());
        if (index > 0)
            count++;
    }
    Console.WriteLine($"Чисел больше нуля: {count}");
}

PositiveNumbers(M);