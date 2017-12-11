class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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

    def mult(self,m):
        li = [ m*i for i in self.coordinates ]
        return Vector(li)
v1 = Vector((1.671,-1.012,-0.318))
v2 = Vector((1,2,3))

print v1.sum(v2)
