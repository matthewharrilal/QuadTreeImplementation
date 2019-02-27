from point import Point
import random

class RegionNode(object):
    def __init__(self, x, y):  # User passes in an array of points that they want
        # Center point in which the sub quadrants are based off of
        self.center = Point(x, y)

        self.points = []  # Made array because didn't have position of an initializer point

        self.capacity = 0  # Represents counter for when to subdivide

        # List of 0 or 4 Region objects that are children of this Region
        self.children = [None] * 4

        self.isDivided = False # So depending if capacity is full check for available spots without subdividing first

    def insert(self, point):
        '''Inserts point inside region that contains that coordinate space'''
        # TODO: move code from QuadTree.insert() - replace region with self
        # occuring at a point in time where we know the regions capacity is over 0 because we are being handed off here
 
        if self.capacity == 0:  # Meaning that we found a valid region
            self.points.append(point)
            self.capacity += 1
            return 


        if self.capacity > 0: # Meaning that there is already a point in the region
            if self.isDivided == False:  # Meaning that we haven't subdivided the region
                self.subdivide()
                self.isDivided = True   # Mark that this region has been divided

            quadrant = self.region_index(point)
            subregion = self.children[quadrant]  # Find the subregion that corresponds to the quadrant and use that as self

            subregion.insert(point)
            
            

    def subdivide(self):
        '''Splits the region into 4 separate quadrants based of center point of the region'''
        # Can do so by updating the center of the children region objects to be half the region's x and y coordinate

        # Northwest Region
        self.children[0] = RegionNode(self.center.x // 2, (self.center.y + self.center.y // 2))

        # Northeast Region
        self.children[1] = RegionNode((self.center.x + self.center.x // 2), (self.center.y + self.center.y // 2))
        
        # Southeast region
        self.children[2] = RegionNode((self.center.x + self.center.x // 2), self.center.y // 2)
       

        # Southwest region
        self.children[3] = RegionNode(self.center.x // 2, self.center.y // 2)
    

    def region_index(self, point):
        '''Return an index in range [0...3] (0: NW, 1: NE, 2: SE, 3: SW) that specifies which
        subregion (child) the given point belongs to relative to this region's center.'''
        # Not handling edge case where data lies directly on the axis
      
        # SELF NOT REFERRING TO THE NEW REGION
        if point.x < self.center.x and point.y > self.center.y:
            return 0  # Representing the Northwest region

        elif point.x >= self.center.x and point.y >= self.center.y:

            return 1  # Representing NE region

        elif point.x > self.center.x and point.y < self.center.y:
            return 2  # Representing the SE region

        else:
            return 3  # Representing the southwest region


class QuadTree(object):
    def __init__(self, x, y, point_collection=None):
        self.root_region = RegionNode(x, y)

        if point_collection is not None:
            for point in point_collection:
                self.insert(point)


    # SOMETHING WRONG WITH THE ACT OF REASSIGNING POINTS
    def insert(self, point, region=None):
        '''Inserts point inside region that contains that coordinate space'''

        # Meaning that the point can lie in the root region
        if self.root_region.capacity == 0: 
            self.root_region.points.append(point)
            self.root_region.capacity += 1
            return self.root_region

        else:  # Meaning that there is no room and pass of the insertion to the region class
            self.root_region.points.append(point) # Append point and then leave the insertion function of the point to rebalance and place in correct region

            for existing_point in self.root_region.points:
                # print("Existing point ", existing_point.x, existing_point.y)
                self.root_region.insert(existing_point)


        # # else:  # len(region.point) >= region.capacity
        # if region.capacity > 0 :  # Meaning that there is already a point in there
         
        #     if region.isDivided == False:

        #         region.subdivide()  # Subdivide into four different quadrants
        #         region.isDivided = True
        #         # Add the point to this region's points before moving them
        #         # region.points.append(point)
        #         # TODO: move all points in region.points into 4 subregions you just made
        #         # for point in region.points:
        #         #     # move point into the correct subregion
        #         #     quadrant = region.region_index(point)
        #         #     subregion = region.children[quadrant]
        #         #     self.insert(point, subregion)
        #         #     NEW CODE: subregion.insert(point)


        #     quadrant = region.region_index(point)
        #     subregion = region.children[quadrant]
        #     self.insert(point, subregion)
            

    def contains(self, point):
        '''Returns true if point is contained inside the quad tree'''
        region = self.root_region # Representing the starting region
        # Already been subdivided

        # Iterate through the regions until we find the point

        while region is not None: # If the region exists
            
            quadrant = region.region_index(point) # Find the corresponding quadrant


            if len(region.points) > 0: # If the region contains a point
                

                if region.points[0].x == point.x and region.points[0].y == point.y: # If the coordinates match
                    return True   
            
            region = region.children[quadrant]
        return False

    def pathway(self, point):
        '''Finds pathway through quadrants'''
        region = self.root_region
        pathway = ""

        # First lets check if point exists before we find the pathway
        if self.contains(point) is False:
            return "No pathway available"

        while region is not None: # If the region exists

            if point.x == region.points[0].x and point.y == region.points[0].y:
                # If we found the pathway but remains in the root region ... no concatenation to pathway
                
                return "Point lies in root region" if pathway == "" else pathway

            quadrant = region.region_index(point)
            pathway += str("Quadrant -> {} ".format(quadrant)) # Only add pathway if index of quadrant exists

            region = region.children[quadrant] # Keep going until you find specific quadrant that contains point
            
        return pathway

# Second element not working as a result of the subdivide
quad_tree = QuadTree(100, 100, [Point(150, 150),Point(60, 120), Point(120, 140)])
points_array = []

# for i in range(20):
#     random_x = random.randint(0,1000)
#     random_y = random.randint(0,1000)
#     points_array.append(Point(random_x, random_y))
#     quad_tree.insert(Point(random_x, random_y))


# for point in points_array:
#     print(quad_tree.pathway(point))
#     print("")

print(quad_tree.pathway(Point(150, 150)))
print("")

print(quad_tree.pathway(Point(60, 120)))
print("")

print(quad_tree.pathway(Point(120, 140)))
print("")

# print(quad_tree.pathway(Point(40, 40)))
# print("")

# print(quad_tree.pathway(Point(95, 120)))
# print("")