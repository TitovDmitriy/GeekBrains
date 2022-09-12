/*Напишите программу, которая принимает на вход пятизначное число
 и проверяет, является ли оно палиндромом.
 14212 -> нет
12821 -> да
23432 -> да*/

Console.WriteLine("Введите пятизначное число: ");
string ? number = Console.ReadLine();

//создаём массив, в который посимвольно передаём элементы строки
char[]  obrnumber = number.ToCharArray();

//переворачиваем массив
Array.Reverse(obrnumber);

//создаём переменную, в которую записываем все элементы массива,
//т.к. строку и массив сравнивать нельзя
string reversenumber = new string(obrnumber);

if (number == reversenumber)
{
    Console.WriteLine("Yes");
}
else
{
    Console.WriteLine("No");
}