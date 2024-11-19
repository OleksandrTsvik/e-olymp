using System;

class Solution
{
    static void Main(string[] args)
    {
        var a = new BigInteger(Console.ReadLine());
        var b = new BigInteger(Console.ReadLine());

        if (a > b)
        {
            Console.WriteLine($"{a.Number} > {b.Number}");
        }
        else if (a < b)
        {
            Console.WriteLine($"{a.Number} < {b.Number}");
        }
        else
        {
            Console.WriteLine($"{a.Number} == {b.Number}");
        }
    }
}

class BigInteger
{
    private readonly string _number;

    public BigInteger(string number)
    {
        _number = number;
    }

    public string Number => _number;
    public int CountDigits => _number.Length;

    public char this[int key]
    {
        get => _number[key];
    }

    public static bool operator >(BigInteger a, BigInteger b)
    {
        if (a.CountDigits > b.CountDigits)
        {
            return true;
        }

        if (a.CountDigits < b.CountDigits)
        {
            return false;
        }

        for (int i = 0; i < a.CountDigits; i++)
        {
            if (CharToInt(a[i]) == CharToInt(b[i]))
            {
                continue;
            }

            return CharToInt(a[i]) > CharToInt(b[i]);
        }

        return false;
    }

    public static bool operator <(BigInteger a, BigInteger b)
    {
        return b > a;
    }

    private static int CharToInt(char digit)
    {
        return digit - '0';
    }
}
