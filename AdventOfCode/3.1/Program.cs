using System;
using System.IO;

namespace _3._1
{

    class Claim
    {
        public int xOrigin { get; set; }
        public int yOrigin { get; set; }

        //TODO Make sure xEnd and yEnd are Origin + Lenght
        public int xEnd { get; set; }
        public int yEnd { get; set; }

        public void CheckOverlap(Claim otherClaim)
        {
            for (int x = xOrigin; x < xEnd; x++)
            {
                for (int y = yOrigin; y < yEnd; y++)
                {
                    if (otherClaim.xOrigin <= x && x <= otherClaim.xEnd &&
                        otherClaim.yOrigin <= y && y <= otherClaim.yEnd)
                    {
                        //TODO have a list, check if the position is present and add if not
                    }
                }
            }
        }
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
                    //TODO Parse all lines and save as claims in a list
                }

                //TODO Go through each combination
            }
        }
    }
}
