int a = new Random().Next(-100, 100);
int b = new Random().Next(-100, 100);
int max = a;
if(max > b)
{
    Console.WriteLine(a);
    Console.WriteLine(b);
    Console.Write("max = ");
    Console.WriteLine(max);
}
else
{
    max = b;
    Console.WriteLine(a);
    Console.WriteLine(b);
    Console.Write("max = ");
    Console.WriteLine(max);
}

