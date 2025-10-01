# Overview
- `Computational Geometry Group Project 1.pdf` - Group presentation; covers how the algorithm works in general
- `convexhull.py` - main code for computing the convex hull of a set of 2D points using the gift wrapping algorithm

# How to Run the Code
1. Download the `convexhull.py` script
2. Run the script from the command line with `python path/to/file/convexhull.py`, a new window should open
3. Click `Plot Random Points` to generate a series of 50 points, or create your own points by clicking, or perform a combination of the two options. Re-clicking a point will remove it from the set. 
4. Click `Computer Convex Hull (Gift Wrapping)` when ready

# How does the code work?
- Define window and create list where the points will be stored
- Store the points as coordinate pairs so that we have their locations
- Pick the point with the lowest x-value (tiebreak by lowest y-value). We know this is a hull point because if it weren't, there would be a point with lower coordinates.
- Check the angle of each point, using the cross product to determine the greatest angle. Vectors extend from the current point to the last hull point and to the prospective points. Add the point with the largest angle, and if points are collinear, select the farther one.
- Continue adding hull points until we reach the starting point.

