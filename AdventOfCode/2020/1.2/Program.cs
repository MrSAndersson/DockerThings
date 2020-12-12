using System;
using System.IO;

namespace _1._2
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

                            FileStream filestreamInner2 = new FileStream("input/input.txt", FileMode.Open, FileAccess.Read);
                            using (StreamReader readerInner2 = new StreamReader(filestreamInner2))
                            {
                                string value3;

                                while ((value3 = readerInner2.ReadLine()) != null)
                                {
                                    if ((value1 != value2) && (value1 != value3) && (value2 != value3) && 
                                        Int32.Parse(value1) + Int32.Parse(value2) + Int32.Parse(value3) == 2020)
                                    {
                                        Console.WriteLine(String.Format("{0} + {1} + {2} = 2020\n{0} * {1} * {2} = {3}",
                                            value1, value2, value3, Int32.Parse(value1) * Int32.Parse(value2) * Int32.Parse(value3)));
                                    }
                                }
                            }
                        }
                    }
                }

            }
        }
    }
}
