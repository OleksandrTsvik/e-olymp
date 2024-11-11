using System;
using System.Text.RegularExpressions;

class Solution
{
    public static void Main(string[] args)
    {
        string pattern = Console.ReadLine();
        int n = int.Parse(Console.ReadLine());

        string patternEscape = Regex.Escape(pattern).Replace(@"\*", ".*");
        Regex regex = new Regex($"^{patternEscape}$", RegexOptions.Compiled);

        for (int i = 0; i < n; i++)
        {
            string fileName = Console.ReadLine();

            if (regex.IsMatch(fileName))
            {
                Console.WriteLine(fileName);
            }
        }
    }
}
