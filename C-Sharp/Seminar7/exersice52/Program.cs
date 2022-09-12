/*Задайте двумерный массив из целых чисел. Найдите среднее арифметическое 
элементов в каждом столбце.

Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.  */


int[,] matrix = new int[5, 3]; //задаем размер матрицы
for (int i = 0; i < matrix.GetLength(0); i++)
{
    for (int j = 0; j < matrix.GetLength(1); j++)
    {
        matrix[i, j] = new Random().Next(0, 11);
        Console.Write(matrix[i, j] + "\t");
    }
    Console.WriteLine();
}
Console.WriteLine();
for (int j = 0; j < matrix.GetLength(1); j++)//меняем местами i и j в цикле, иначе программа считает среднее арифметическое строки
{
    int sum = 0;
    double count = 0;
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        sum += matrix[i, j];
        count++;
    }
    Console.WriteLine($"Среднее арифметическое {j} столбца = {sum / count}");
}



