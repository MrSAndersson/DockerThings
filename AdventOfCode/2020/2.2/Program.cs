using System;
using System.IO;

namespace _2._2
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

                    int pos1 = Convert.ToInt32(substrings[0])-1;
                    int pos2 = Convert.ToInt32(substrings[1])-1;
                    char character = Convert.ToChar(substrings[2]);
                    string password = substrings[4];

                    if (character == password[pos1] ^ character == password[pos2])
                    {
                        validPassCount++;
                    }

                }

                Console.WriteLine(validPassCount);
            }

        }
    }
}
