int num = new Random().Next(0, 100000);
int num1 = num;
if(num > 99 && num < 1000)
{
    Console.WriteLine(num1 + " " + (num % 100)  % 10);
}
if(num > 1000)
{
    Console.WriteLine(num1 + " " + (num % 1000)  / 100);
}
else
{
    Console.WriteLine(num1 + " третьей цифры нет");
}

