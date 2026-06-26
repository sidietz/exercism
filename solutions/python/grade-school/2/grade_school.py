"""
implements grade_school
"""

def mysort(mymap):
    """
    basic bubble sort
    """
    tmp = list(mymap.keys())
    tmp.sort()

    for i in range(len(tmp)):
        for j in range(len(tmp)):
            if mymap[tmp[i]] < mymap[tmp[j]]:
                t = tmp[i]
                tmp[i] = tmp[j]
                tmp[j] = t
            if mymap[tmp[i]] == mymap[tmp[j]]:
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
        self.student_map = {}
        self.bitmap = []

    

    def add_student(self, name, grade):

        if name in self.student_map.keys():
            self.bitmap.append(False)
        else:
            self.student_map[name] = grade
            self.bitmap.append(True)
        return self.bitmap

    def roster(self):
        tmp = list(self.student_map.keys())
        tmp.sort()
        return mysort(self.student_map)

    def grade(self, grade_number):
        tmp = []
        for k, v in self.student_map.items():
            if v == grade_number:
                tmp.append(k)
        tmp.sort()
        return tmp

    def added(self):
        return self.bitmap