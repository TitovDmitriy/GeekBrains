int N = new Random().Next(2, 100);
Console.WriteLine(N);
for (int i = 2; i <= N; i+=2)
{
    Console.Write(i);
    Console.Write(" ");
}

