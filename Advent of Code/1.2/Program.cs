using System;
using System.Collections.Generic;
using System.IO;

namespace _1._2
{
    class Program
    {


        static void Main(string[] args)
        {
            Console.WriteLine("First recurring frequency: " + RepeatFinder());
        }

        private static int RepeatFinder()
        {
            List<int> known_frequencies = new List<int>();
            int sum = 0;
            while (true)
            {


                FileStream filestream = new FileStream("input/input.txt", FileMode.Open);
                using (StreamReader reader = new StreamReader(filestream))
                {

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

                        if (known_frequencies.Contains(sum))
                        {
                            return sum;
                        }
                        else
                        {
                            known_frequencies.Add(sum);
                        }

                    }
                }

            }
        }
    }
}
