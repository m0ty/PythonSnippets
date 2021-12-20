"""
An automated cutting machine is used to cut rods into segments.
The cutting machine can only hold a rod of minLength or more.
A rod is marked with the necessary cuts and their lengths are given
as an array in the order they are marked.
Determine if it is possible to plan the cuts so the last cut is from a rod at least minLength units long.

Example:
lengths = [4, 3, 2]
minLength = 7

The rod is initially sum(lengths) = 4 + 3 + 2 = 9 units long.
First cut off the segment of length 4 + 3 = 7 leaving a rod 9 - 7 = 2.
Then check that the length 7 rod can be cut into segments of lengths 4 and 3.
Since 7 is greater than or equal to minLength = 7,
the final cut can be made. Return "Possible".
"""

min_length = 7

