/*
Задача 58: Задайте две матрицы. Напишите программу, 
которая будет находить произведение двух матриц.
Например, даны 2 матрицы:
2 4 | 3 4
3 2 | 3 3
Результирующая матрица будет:
18 20
15 18
*/
// int InputInt(string output)
// {
//     Console.Write(output);
//     return int.Parse(Console.ReadLine());
// }

int[,] matrixA = new int[2, 2];
int[,] matrixB = new int[2, 2];
int[,] matrixC = new int[2, 2];

FillArray(matrixA);
Console.WriteLine("Первая матрица:");
PrintArray(matrixA);
Console.WriteLine();

FillArray(matrixB);
Console.WriteLine("Вторая матрица:");
PrintArray(matrixB);
Console.WriteLine();

Console.WriteLine("Произведение двух матриц:");
ResultMatrix(matrixC, matrixA, matrixB);
PrintArray(matrixC);


void FillArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = new Random().Next(0, 11);
        }
    }
}

void PrintArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j] + "\t");
        }
        Console.WriteLine();
    }
}

void ResultMatrix(int [,] arrayC, int [,] arrayA, int [,] arrayB)
{
    for (int i = 0; i < arrayA.GetLength(0); i++)
    {
        for (int j = 0; j < arrayB.GetLength(1); j++)
        {
            for (int k = 0; k < arrayA.GetLength(0); k++)
            {
                arrayC[i, j] = arrayC[i, j] + (arrayA[i, k] * arrayB[k, j]);
            }
        }
    }
}

