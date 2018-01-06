import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'


    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def sum(self, v):
        li = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        # i=0; j=0;
        # z=[];
        # while(i<len(self.coordinates) and j<len(v.coordinates)):
        #     z.append(self.coordinates[i]+v.coordinates[j])
        #     j+=1;
        #     i+=1;
        # while(j<len(v.coordinates)):
        #     z.append(v.coordinates[j])
        #     j+=1;
        # while(i<len(self.coordinates)):
        #     z.append(self.coordinates[i])
        #     i+=1;
        return Vector(li)

    def diff(self, v):
        li = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        # i=0; j=0;
        # z=[];
        # while(i<len(self.coordinates) and j<len(v.coordinates)):
        #     z.append(self.coordinates[i]-v.coordinates[j])
        #     j+=1;
        #     i+=1;
        # while(j<len(v.coordinates)):
        #     z.append(-1*v.coordinates[j])
        #     j+=1;
        # while(i<len(self.coordinates)):
        #     z.append(self.coordinates[i])
        #     i+=1;
        return Vector(li)

    def scalar_mult(self,m):
        li = [ m*i for i in self.coordinates ]
        return Vector(li)

    def magnitude(self):
        coordinates_squared = [i**2 for i in self.coordinates]
        return math.sqrt(sum(coordinates_squared))

    def normalise(self):
        try:
            magnitude = Decimal(1./self.magnitude())
            return self.scalar_mult(magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot_product(self,v):
        return sum([x*y for x,y in zip(self.coordinates,v.coordinates)])

    def angle_between(self,v, in_degrees=False):
       try:
            u1 = self.normalise()
            u2 = v.normalise()
            angle_in_radians = math.acos(u1.dot_product(u2))

            if in_degrees:
                degrees_per_radian = 180. / math.pi
                return angle_in_radians*degrees_per_radian
            else:
                return angle_in_radians
       except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e
    def is_orthogonal_to(self, v, tolerance = 1e-10):
        return abs(self.dot_product(v)) < tolerance

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_parallel_to(self, v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle_between(v) == 0 or
                self.angle_between(v) == math.pi)

    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.diff(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_parallel_to(self, basis):
        try:
            u = basis.normalise()
            weight = self.dot_product(u);
            return u.scalar_mult(weight);

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e
