using System;
using System.Diagnostics;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int biggerNumber = 10;
            int smallNumber = 1;

            if (biggerNumber != smallNumber)
            {
                Debug.Print(biggerNumber + "is not equal to " + smallNumber);
            }
        }
    }
}
