using System;
using System.IO;

namespace _2._1
{
    class Program
    {
        static void Main(string[] args)
        {
            FileStream filestream = new FileStream("input/input.txt", FileMode.Open, FileAccess.Read);
            using (StreamReader reader = new StreamReader(filestream))
            {
                int validPassCount = 0;
                string passwordString;
                while ((passwordString = reader.ReadLine()) != null)
                {
                    string[] substrings = passwordString.Split('-', ' ', ':');

                    int min = Convert.ToInt32(substrings[0]);
                    int max = Convert.ToInt32(substrings[1]);
                    char character = Convert.ToChar(substrings[2]);
                    string password = substrings[4];

                    int charCount = 0;

                    foreach (char c in password)
                    {
                        if (c == character)
                        {
                            charCount++;
                        }
                    }

                    if (min <= charCount && charCount <= max)
                    {
                        validPassCount++;
                    }

                }

                Console.WriteLine(validPassCount);
            }

        }
    }
}
