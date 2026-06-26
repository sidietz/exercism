"""
implements grade_school
"""

def mysort(map):
    """
    basic bubble sort
    """
    tmp = list(map.keys())
    tmp.sort()

    for i in range(len(tmp)):
        for j in range(len(tmp)):
            if map[tmp[i]] < map[tmp[j]]:
                t = tmp[i]
                tmp[i] = tmp[j]
                tmp[j] = t
            if map[tmp[i]] == map[tmp[j]]:
                if tmp[i] < tmp[j]:
                    t = tmp[i]
                    tmp[i] = tmp[j]
                    tmp[j] = t
                
    return tmp

class School:
    """
    provides school class
    """
    def __init__(self):
        self.map = {}
        self.bitmap = []

    

    def add_student(self, name, grade):

        if name in self.map.keys():
            self.bitmap.append(False)
        else:
            self.map[name] = grade
            self.bitmap.append(True)
        return self.bitmap

    def roster(self):
        tmp = list(self.map.keys())
        tmp.sort()
        return mysort(self.map)

    def grade(self, grade_number):
        tmp = []
        for k, v in self.map.items():
            if v == grade_number:
                tmp.append(k)
        tmp.sort()
        return tmp

    def added(self):
        return self.bitmap