using System;

class Solution
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        int[] a = new int[n];
        int max = 0, index = 0;

        string[] num = Console.ReadLine().Split(' ');
        for (int i = 0; i < n; i++)
        {
            a[i] = int.Parse(num[i]);
        }

        for (int i = 0; i < n; i++)
        {
            if (a[i] > max)
            {
                max = a[i];
                index = i + 1;
            }
        }

        Console.WriteLine($"{max} {index}");
    }
}
