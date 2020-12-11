using System;
using System.IO;

namespace _2._2
{
    class CompareResult
    {
        public Boolean isSimilar { get; set; } = false;
        public string commonName { get; set; } = "";
    }

    class Program
    {
        static void Main(string[] args)
        {
            FileStream filestream = new FileStream("input/input.txt", FileMode.Open);
            using (StreamReader reader = new StreamReader(filestream))
            {
                string line;
                int lineNr = 0;
                while ((line = reader.ReadLine()) != null)
                {
                    lineNr++;
                    FileStream compareFileStream = new FileStream("input/input.txt", FileMode.Open);
                    using (StreamReader compareReader = new StreamReader(compareFileStream))
                    {
                        // Skip lines until we're after 'line'
                        for (int x = 0; x < lineNr; x++)
                        {
                            compareReader.ReadLine();
                        }

                        string compareLine;
                        while ((compareLine = compareReader.ReadLine()) != null)
                        {
                            // Compare 'line' and 'compareLine'
                            CompareResult result = CompareLines(line, compareLine);
                            if (result.isSimilar)
                            {
                                Console.WriteLine(result.commonName);
                            }
                        }
                    }
                }
            }
        }

        private static CompareResult CompareLines(string line, string compareLine)
        {
            char[] lineArray = line.ToCharArray();
            char[] compareLineArray = compareLine.ToCharArray();
            int diffCount = 0;
            int diffPosition = 0;
            CompareResult result = new CompareResult();

            for (int x = 0; x < line.Length; x++)
            {
                if (lineArray[x] != compareLineArray[x])
                {
                    diffCount++;
                    diffPosition = x;
                }
            }
            if (diffCount == 1)
            {
                result.isSimilar = true;
                result.commonName = line.Remove(diffPosition, 1);
                return result;
            }
            else
            {
                return result;
            }
        }
    }
}
