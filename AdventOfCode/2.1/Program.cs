using System;
using System.Collections.Generic;
using System.IO;

namespace _2._1
{
    class Program
    {
        static void Main(string[] args)
        {
            FileStream filestream = new FileStream("input/input.txt", FileMode.Open);
            using (StreamReader reader = new StreamReader(filestream))
            {
                string line;
                int triplecounter = 0;
                int doublecounter = 0;
                while ((line = reader.ReadLine()) != null)
                {
                    List<char> triples = ContainsTriple(line);
                    if (triples.Count > 0)
                        triplecounter++;


                    List<char> doubles = ContainsDouble(line, triples);
                    if (doubles.Count > 0)
                        doublecounter++;
                }

                int checksum = doublecounter * triplecounter;
                Console.WriteLine("Checksum is: " + checksum);

            }
        }

        private static List<char> ContainsDouble(string line, List<char> triples)
        {
            List<char> doubles = new List<char>();
            foreach (char x in line)
            {
                int count = 0;
                foreach (char y in line)
                {
                    if (x == y)
                        count++;
                }
                if (count == 2 && !triples.Contains(x))
                    doubles.Add(x);
            }
            return doubles;

        }

        private static List<char> ContainsTriple(string line)
        {
            List<char> triples = new List<char>();
            foreach (char x in line)
            {
                int count = 0;
                foreach (char y in line)
                {
                    if (x == y)
                        count++;
                }
                if (count == 3)
                    triples.Add(x);
            }
            return triples;
        }

    }
}
