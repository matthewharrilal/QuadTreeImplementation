from point import Point

class Region(object):
    def __init__(self, width, height, points_collection=None): # User passes in an array of points that they want
        self.width = width
        self.height = height
        self.capacity = 0 # Represents counter for when to subdivide

        if len(points_collection) > 0:
            for point in points_collection:
                self.insert(point)

    # def contains(self, point):
    #     '''Returns true if point is contained inside given region'''
    #     p

