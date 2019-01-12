using System;
using System.Collections.Generic;
using System.IO;

namespace _3._1
{

    class Coordinate : IEquatable<Coordinate>
    {
        public Coordinate(int x, int y)
        {
            this.x = x;
            this.y = y;
        }

        public int x { get; set; }
        public int y { get; set; }


        public bool Equals(Coordinate other)
        {
            return this.x == other.x &&
                   this.y == other.y;
        }
    }

    class Claim
    {
        public int xOrigin { get; set; }
        public int yOrigin { get; set; }

        //TODO Make sure xEnd and yEnd are Origin + Lenght
        public int xEnd { get; set; }
        public int yEnd { get; set; }

        public List<Coordinate> CheckOverlap(Claim otherClaim, List<Coordinate> overlaps)
        {
            for (int x = xOrigin; x < xEnd; x++)
            {
                for (int y = yOrigin; y < yEnd; y++)
                {
                    if (otherClaim.xOrigin <= x && x <= otherClaim.xEnd &&
                        otherClaim.yOrigin <= y && y <= otherClaim.yEnd)
                    {
                        Coordinate overlap = new Coordinate(x, y);
                        if (!overlaps.Contains(overlap))
                        {
                            overlaps.Add(overlap);
                        }
                    }
                }
            }
            return overlaps;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Coordinate> overlaps = new List<Coordinate>();
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
