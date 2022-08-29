// Задача 25: Напишите цикл, который принимает на вход два числа (A и B) 
//   и возводит число A в натуральную степень B.
//   3, 5 -> 243 (3⁵)
//   2, 4-> 16

Console.WriteLine("Введите число A: ");
int num1 = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Введите число B: ");
int num2 = Convert.ToInt32(Console.ReadLine());
int step = num1;

for (int i = 1; i < num2; i++)
{
    step *= num1;
}
Console.WriteLine("Число " + num1 + " в степени " + num2 + " = " + step);