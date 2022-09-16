/*
Задача 66: Задайте значения M и N. Напишите программу, которая найдёт 
сумму натуральных элементов в промежутке от M до N.

M = 1; N = 15 -> 120
M = 4; N = 8. -> 30
*/
Console.WriteLine("Введите число M: ");
int M = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число N: ");
int N = Convert.ToInt32(Console.ReadLine());

Console.WriteLine($"M = {M}; N = {N} -> {NaturalSum(M, N)}");

int NaturalSum(int M, int N)
{
    if (M == N)
        return N;
    return M + NaturalSum(M + 1, N);
}
