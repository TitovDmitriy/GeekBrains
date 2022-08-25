/*Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 3D пространстве.

A (3,6,8); B (2,1,-7), -> 15.84
A (7,-5, 0); B (1,-1,9) -> 11.53*/

/*Сообщение для преподавателя! В первом примере ошибка, если решать по формуле
 √(x2-x1)^2)+(y2-y1)^2+(z2-z1)^2. Тогда получаем: 5,196152422706632, 
 тогда как второй пример проходит проверку: 11,532562594670797 */

Console.WriteLine("Введите Х1: ");
int x1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите Y1: ");
int y1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите Z1: ");
int z1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите Х2: ");
int x2 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите Y2: ");
int y2 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите Z2: ");
int z2 = Convert.ToInt32(Console.ReadLine());

double distance = Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2) 
+ Math.Pow(z2 - z1, 2));
Console.WriteLine(distance);