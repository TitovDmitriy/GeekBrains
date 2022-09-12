/*Задача 50. Напишите программу, которая на вход принимает 
позиции элемента в двумерном массиве, и возвращает значение 
этого элемента или же указание, что такого элемента нет.

Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4

17 -> такого числа в массиве нет*/

Console.WriteLine("Введите позицию строки: ");
int RowsPosition = int.Parse(Console.ReadLine());
Console.WriteLine("Введите позицию столбца: ");
int ColumnsPosition = int.Parse(Console.ReadLine());
int[,] matrix = new int[5, 5];
for (int i = 0; i < matrix.GetLength(0); i++)
{
    for (int j = 0; j < matrix.GetLength(1); j++)
    {
        matrix[i, j] = new Random().Next(0, 11);
        Console.Write(matrix[i, j] + "\t");
    }
    Console.WriteLine();
}
if (RowsPosition < 0 | RowsPosition > matrix.GetLength(0) - 1 | ColumnsPosition < 0 |
 ColumnsPosition > matrix.GetLength(1) - 1)
{
    Console.WriteLine($"строка {RowsPosition}, столбец {ColumnsPosition} -> такого числа в массиве нет");
}
else
{
    Console.WriteLine("Элемент с такими значениями = {0}", matrix[RowsPosition, ColumnsPosition]);
}




