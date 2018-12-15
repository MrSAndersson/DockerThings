using System;
using System.IO;

namespace _1._1
{
    class Program
    {


        static void Main(string[] args)
        {
            FileStream filestream = new FileStream("input/input.txt", FileMode.Open);
            using (StreamReader reader = new StreamReader(filestream))
            {
                int sum = 0;
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                    string number = line.Substring(1);
                    if (line.StartsWith('+'))
                    {
                        sum += Int32.Parse(number);
                    }
                    else
                    {
                        sum -= Int32.Parse(number);
                    }
                }

                Console.WriteLine("Sum: " + sum);

            }
        }
    }
}
