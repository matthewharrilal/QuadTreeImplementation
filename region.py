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

        self.depth = 0

    def insert(self, point):
        '''Inserts point inside region that contains that coordinate space'''
      
        if self.capacity == 0:  
            self.points.append(point) 
            self.capacity += 1
            return 


        if self.capacity > 0: # Meaning that there is already a point in the region
            if self.isDivided == False:  # Meaning that we haven't subdivided the region
                
                # You know when you subdivide there is an existing point becuase the capacity is 1 and it hasnt been divided yet therefore 
                self.subdivide()
                self.isDivided = True  

 

                # We can take that existing point
                existing_point = self.points[0]
                existing_quadrant = self.region_index(existing_point)

                self.children[existing_quadrant].points.append(existing_point)
                # print("New existing quadrant %s", existing_quadrant, existing_point.x)
                # self.children[existing_quadrant].capacity  += 1
                self.points = []


            # Find where new point should be inserted
            quadrant = self.region_index(point)
            subregion = self.children[quadrant]  
            subregion.depth = self.depth + 1

            subregion.insert(point)  # Insert the point into the proper subregion
            
            

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
            return 

        else:  # Meaning that there is a point that already exists within the region
            
            if len(self.root_region.points) > 0:  # Meaning we know the capacity is 1 and there is an existing point inside the region
                existing_point = self.root_region.points[0]
                self.root_region.insert(existing_point)  # Rebalance existing point then clear the regions existing point
                self.root_region.insert(point)
                # self.root_region.points = []
                return

            else:  # Meaning that the region had a capacity of 1 but there was no existing point then lets just find a region for the new point
                self.root_region.insert(point)
                return

            
                


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
        if self.contains(point) is False: # We are not getting this so we know after we insert it in the new region and reset the points it not breaking
            return "No pathway available for points Point(%s, %s)", point.x, point.y

        while region is not None: # If the region exists

            if len(region.points) > 0: # Root region no longer contains points but still has capacity which is good

                    if point.x == region.points[0].x and point.y == region.points[0].y:
                        # If we found the pathway but remains in the root region ... no concatenation to pathway
                        
                        return "Point lies in root region" if pathway == "" else pathway

            # elif region.capacity > 0:  # Meaning no point but the capacity is greater than 1 showing there is a path

            quadrant = region.region_index(point)
            pathway += str("Quadrant -> {} ".format(quadrant)) # Only add pathway if index of quadrant exists

            region = region.children[quadrant] # Keep going until you find specific quadrant that contains point
            
        return pathway, region.depth

# Second element not working as a result of the subdivide
# quad_tree = QuadTree(100, 100, [Point(150, 150),Point(120, 140), Point(60, 120),])
quad_tree = QuadTree(100, 100, [Point(50, 50), Point(150, 150),Point(160, 160)])
points_array = []

# for i in range(20):
#     random_x = random.randint(0,1000)
#     random_y = random.randint(0,1000)
#     points_array.append(Point(random_x, random_y))
#     quad_tree.insert(Point(random_x, random_y))


# for point in points_array:
#     print(quad_tree.pathway(point))
#     print("")

print(quad_tree.pathway(Point(50, 50)))
print("")

print(quad_tree.pathway(Point(150, 150)))
print("")

print(quad_tree.pathway(Point(160, 160)))
print("")

# print(quad_tree.pathway(Point(155, 155)))
# print("")

# # print(quad_tree.pathway(Point(95, 120)))
# # print("")