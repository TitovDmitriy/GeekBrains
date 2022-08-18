int a = new Random().Next(-100, 100);
int b = new Random().Next(-100, 100);
int c = new Random().Next(-100, 100);
int max = a;
if(b > max)
{
    max = b;
}
if(c > max)
{
    max = c;
}
Console.WriteLine(a);
Console.WriteLine(b);
Console.WriteLine(c);
Console.Write("max = ");
Console.WriteLine(max);
