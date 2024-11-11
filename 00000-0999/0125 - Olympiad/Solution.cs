using System;

class Solution
{
    static void Main(string[] args)
    {
        string[] st1 = Console.ReadLine().Split();
        string[] st2 = Console.ReadLine().Split();

        int h1 = int.Parse(st1[0]); int h2 = int.Parse(st2[0]);
        int m1 = int.Parse(st1[1]); int m2 = int.Parse(st2[1]);
        int s1 = int.Parse(st1[2]); int s2 = int.Parse(st2[2]);

        s1 += m1 * 60 + h1 * 3600;
        s2 += m2 * 60 + h2 * 3600;

        int result = s2 - s1;
        int h = result / 3600; result -= h * 3600;
        int m = result / 60; result -= m * 60;
        int s = result;

        Console.WriteLine($"{h} {m} {s}");
    }
}
