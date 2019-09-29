# Janice Cotcher
# Date created: 2019/09/29
# Sierpinski's Triangle
# Code adapted from "Triangle of Sierpinski", Maeln, CC0 1.0 Universal,
# https://www.openprocessing.org/sketch/17026/


def setup():
    size(800, 800)
    # light grey background
    background(200)
    smooth()
    noStroke()
    # draw a static background
    triangleSier(0, 700, 400, 0, 800, 700, 7)


def triangleSier(x1, y1, x2, y2, x3, y3, n):
    """
    Recurvise function to draw iterations of Sierpinski's triangle
    x1, x2, x3 are the x-coordinates of the points of the triangle
    y1, y2, y3 are the y-coordinates of the points of the triangle
    n is the number is iterations"""
    if n > 0:
        # different shade for each size of triangle
        fill(0, float(128/n), 128)
        triangle(x1, y1, x2, y2, x3, y3)
        # define the mid-points of all segments
        # h1, h2, h3 are the mid-points of the x-values
        # w1, w2, w3 are the mid-points of the y-values
        h1 = float((x1+x2)/2.0)
        w1 = float((y1+y2)/2.0)
        h2 = float((x2+x3)/2.0)
        w2 = float((y2+y3)/2.0)
        h3 = float((x1+x3)/2.0)
        w3 = float((y1+y3)/2.0)
        # recursive calls for the function
        triangleSier(x1, y1, h1, w1, h3, w3, n-1)
        triangleSier(h1, w1, x2, y2, h2, w2, n-1)
        triangleSier(h3, w3, h2, w2, x3, y3, n-1)
