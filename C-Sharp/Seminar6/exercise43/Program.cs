/*
Задача 43: Напишите программу, которая найдёт точку пересечения двух прямых,
заданных уравнениями y = k1 * x + b1, y = k2 * x + b2;
значения b1, k1, b2 и k2 задаются пользователем.

b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)
*/

//Если k1 = k2 , то прямые параллельны и отрезки пересекаться не могут. 
//Вычисляем точку пересечения прямых:  
// x = ( b2 - b1 ) / ( k1 -  k2 )
// y = k1 x + b1.

void intersectionPoint(double num1, double numk1, double num2, double numk2)
{
    if (numk1 == numk2)
    {
        Console.WriteLine("Прямые параллельны и отрезки пересекаться не могут.");
    }
    else
    {
        Console.WriteLine($"x = {(num2 - num1) / (numk1 - numk2)}");
        Console.WriteLine($"y = {((num2 - num1) / (numk1 - numk2)) * numk1 + num1}");
    }

}
double b1 = new Random().Next(-10, 10);
double k1 = new Random().Next(-10, 10);
double b2 = new Random().Next(-10, 10);
double k2 = new Random().Next(-10, 10);

intersectionPoint( b1, k1, b2, k2);
Console.WriteLine($"b1 = {b1}, k1 = {k1}, b2 = {b2}, k2 = {k2}");
