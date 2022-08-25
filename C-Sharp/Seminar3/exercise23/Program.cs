/*Напишите программу, которая принимает на вход число (N) 
и выдаёт таблицу кубов чисел от 1 до N.
3 -> 1, 8, 27
5 -> 1, 8, 27, 64, 125*/

Console.WriteLine("Введите число: ");
int N = Convert.ToInt32(Console.ReadLine());
for (int i = 1; i <= N; i++)
{
    double result = Math.Pow(i, 3);
    Console.Write(result);
    /* почему-то не сработала конкатенация (result + ' ')
    при вводе 5 получил результат -> 33405996157
    при вводе 3 получил результат -> 334059
    пришлось записать вывод в две строки, но зато результаты стали верными*/
    Console.Write(' ');
}

// тоже решение, но через цикл while
/*int count = 1;
while (count <= N)
{
    Console.Write(Math.Pow(count, 3) + " ");
    count++;
}*/