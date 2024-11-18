using System;

class FenwickTree
{
    private readonly long[] _fenwickTree;

    public FenwickTree(long size)
    {
        _fenwickTree = new long[size];
    }

    public long GetSum(long stopIndex)
    {
        long sum = 0;

        for (long i = stopIndex; i >= 0; i = (i & (i + 1)) - 1)
        {
            sum += _fenwickTree[i];
        }

        return sum;
    }

    public long GetSum(long startIndex, long stopIndex)
    {
        return GetSum(stopIndex) - GetSum(startIndex);
    }

    public void SetItem(long index, long value)
    {
        long currentValue = GetSum(index) - GetSum(index - 1);
        AddToItem(index, value - currentValue);
    }

    public void AddToItem(long index, long value)
    {
        for (long i = index; i < _fenwickTree.Length; i |= i + 1)
        {
            _fenwickTree[i] += value;
        }
    }
}

class Solution
{
    static void Main(string[] args)
    {
        string[] data = Console.ReadLine().Split();

        long arraySize = long.Parse(data[0]);
        long requestCount = long.Parse(data[1]);

        var fenwickTree = new FenwickTree(arraySize);

        for (long i = 0; i < requestCount; i++)
        {
            data = Console.ReadLine().Split();

            char requestType = char.Parse(data[0]);
            long a = long.Parse(data[1]);
            long b = long.Parse(data[2]);

            if (requestType == 'A')
            {
                fenwickTree.SetItem(a - 1, b);
            }
            else
            {
                Console.WriteLine(fenwickTree.GetSum(a - 2, b - 1));
            }
        }
    }
}
