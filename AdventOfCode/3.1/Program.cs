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

        public int xOrigin { get; }
        public int yOrigin { get; }

        //TODO Make sure xEnd and yEnd are Origin + Lenght
        public int xEnd { get; }
        public int yEnd { get; }
        public Claim(int xOrigin, int xLength, int yOrigin, int yLength)
        {
            this.xOrigin = xOrigin;
            this.yOrigin = yOrigin;
            this.xEnd = xOrigin + xLength;
            this.yEnd = yOrigin + yLength;
        }

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
                    string[] newClaimSplit = newClaim.Split(' ', 4);
                    string[] x = newClaimSplit[2].Split(',', 2);
                    string y = x[1].Trim(':');
                    int xOrigin = int.Parse(x[0]);
                    int yOrigin = int.Parse(y);
                    string[] lengthSplit = newClaimSplit[3].Split('x', 2);
                    int xLength = int.Parse(lengthSplit[0]);
                    int yLength = int.Parse(lengthSplit[1]);

                    claims.Add(new Claim(xOrigin, xLength, yOrigin, yLength));
                }
            }
            for (int x = 0; x < claims.Count; x++)
            {
                for (int y = x + 1; y < claims.Count; y++)
                {
                    overlaps = claims[x].CheckOverlap(claims[y], overlaps);
                }
            }
        }
    }
}
