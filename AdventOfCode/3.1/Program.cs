using System;
using System.IO;

namespace _3._1
{

    class Claim
    {
        public int xOrigin { get; set; }
        public int yOrigin { get; set; }
        public int xLength { get; set; }
        public int yLength { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Claim> claims = new List<Claim>();
            FileStream filestream = new FileStream("input.txt", FileMode.Open);
            using (StreamReader reader = new StreamReader(filestream))
            {
                string newClaim;
                while ((newClaim = reader.ReadLine()) != null)
                {

                }
            }
        }
    }
}
