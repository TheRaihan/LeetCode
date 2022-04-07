using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] grades = { 30, 23, 12, 54 };
            Array.Sort(grades);

            for (int i = 0; i < grades.Length; i++)
            {
                Console.WriteLine(grades[i]);
            }
);
        }
    }

}