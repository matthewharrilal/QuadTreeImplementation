class Point(object):
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    def __str__(self):
        return f"({self.x}, {self.y})"

    # def __repr__(self):
        # return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        """Return True if this point is equal to the given other point."""
        # TODO
        pass

    def is_near(self, other, limit=10):
        """Return True if this point is within some limit near the other point.
        Parameter limit is how near the points should be (default 10 pixels)."""
        # TODO
        pass


# if __name__ == "__main__":
#     pt1 = Point(3, 5)
#     print(pt1)
#     # pt1 == pt2
#     # pt1.__eq__(pt2)
#     # Point.__eq__(pt1, pt2)