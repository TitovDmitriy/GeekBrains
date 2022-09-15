/*
Задача 60. Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. 
Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
Массив размером 2 x 2 x 2
66(0,0,0) 25(0,1,0)
34(1,0,0) 41(1,1,0)
27(0,0,1) 90(0,1,1)
26(1,0,1) 55(1,1,1)
*/
int edgecube1 = 2;
int edgecube2 = 2;
int edgecube3 = 2;
int LimitNum = 90;

if (edgecube1 * edgecube2 * edgecube3 > LimitNum)
{
    Console.Write("Превышен предел неповторяющихся двузначных чисел");
    return;
}

int[,,] array = CreateCube(edgecube1, edgecube2, edgecube3);

for (int i = 0; i < array.GetLength(0); i++)
{
    for (int j = 0; j < array.GetLength(1); j++)
    {
        for (int k = 0; k < array.GetLength(2); k++)
        {
            Console.WriteLine($"{array[i, j, k]} ({i},{j},{k})");
        }        
    }
    Console.WriteLine();
}


int[,,] CreateCube(int axis1, int axis2, int axis3)
{
    int[,,] array = new int[axis1, axis2, axis3];
    int[] values = new int[LimitNum];
    int num = 10;
    for (int i = 0; i < values.Length; i++)
        values[i] = num++;

    for (int i = 0; i < values.Length; i++)
    {
        int randomArr = new Random().Next(0, values.Length);
        int temp = values[i];
        values[i] = values[randomArr];
        values[randomArr] = temp;
    }

    int count = 0;

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(2); k++)
            {
                array[i, j, k] = values[count++];
            }
        }
    }
    return array;
}


