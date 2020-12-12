using System;
using System.IO;

namespace _1._1
{
    class Program
    {
        static void Main(string[] args)
        {
            FileStream filestreamOuter = new FileStream("input/input.txt", FileMode.Open, FileAccess.Read);
            using (StreamReader readerOuter = new StreamReader(filestreamOuter))
            {
                string value1;

                while ((value1 = readerOuter.ReadLine()) != null)
                {

                    FileStream filestreamInner = new FileStream("input/input.txt", FileMode.Open, FileAccess.Read);
                    using (StreamReader readerInner = new StreamReader(filestreamInner))
                    {
                        string value2;
                        
                        while ((value2 = readerInner.ReadLine()) != null)
                        {
                            if (value1 != value2 && Int32.Parse(value1)+Int32.Parse(value2) == 2020)
                            {
                                Console.WriteLine(String.Format("{0} + {1} = 2020.\n{0} * {1} = {2}", 
                                    value1, value2, Int32.Parse(value1) * Int32.Parse(value2)));
                            }
                        }
                    }
                }

            }
        }
    }
}
