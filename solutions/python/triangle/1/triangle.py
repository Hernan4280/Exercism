def equilateral(sides):
    side_a, side_b, side_c  = sorted(sides)
    return (side_a + side_b >= side_c) & (0 not in sides) & (side_a == side_b == side_c)


def isosceles(sides):
    side_a, side_b, side_c  = sorted(sides)
    two_equal_sides = side_a == side_b or side_b == side_c or side_a == side_c
    return (side_a + side_b >= side_c) & (0 not in sides) & two_equal_sides


def scalene(sides):
    side_a, side_b, side_c  = sorted(sides)
    return (side_a + side_b >= side_c) & (0 not in sides) & (len(set(sides)) == 3)
