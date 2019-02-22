from point import Point

class Region(object):
    def __init__(self, x_coordinate, y_coordinate, width, height, points_collection=None): # User passes in an array of points that they want
        # Center point in which the sub quadrants are based off of
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self.width = width
        self.height = height
        self.capacity = 0 # Represents counter for when to subdivide

        if len(points_collection) > 0:
            for point in points_collection:
                self.insert(point)

    def contains(self, point):
        '''Returns true if point is contained inside given region'''
        pass

    def insert(self, point):
        '''Inserts point inside region that contains that coordinate space'''
        pass

    def subdivide(self):
        '''Splits the region into 4 separate quadrants based of center point of the region'''
        pass