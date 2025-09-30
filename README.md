# How does the code work?
- Define window and create list where the points will be stored
- Store the points as coordinate pairs so that we have their locations
- Pick the point with the lowest x-value (tiebreak by lowest y-value). We know this is a hull point because if it weren't, there would be a point with lower coordinates.
- Check the angle of each point, using the cross product to determine the greatest angle. Vectors extend from the current point to the last hull point and to the prospective points. Add the point with the largest angle, and if points are collinear, select the farther one.
- Continue adding hull points until we reach the starting point.
- 
https://docs.google.com/presentation/d/1l-9AUQqhrsVREcgN_2FpVNGS6kF1L25B6wkFkumYLfY/edit?usp=sharing  (slideshow)
