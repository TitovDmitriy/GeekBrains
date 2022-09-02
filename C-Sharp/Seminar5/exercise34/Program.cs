/*Задача 34: Задайте массив заполненный случайными положительными
 трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.

[345, 897, 568, 234] -> 2*/

int[] array = new int[8];
Console.Write("[");
for (int i = 0; i < array.Length; i++)
{
    array[i] = new Random().Next(100, 1000);

}
Console.Write("{0}", String.Join("; ", array));
int count = 0;
for (int j = 0; j < array.Length; j++)
{
    if (array[j] % 2 == 0)
    {
        count++;
    }
}
Console.Write("]");
Console.Write(" -> " + count);