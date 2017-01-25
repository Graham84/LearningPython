# map.example.py

print map(lambda *a: a, range(3))                                      # without wrapping in list...
print list(map(lambda *a: a, range(3)))                                # wrapping in list...
print list(map(lambda *a: a, range(3), 'abc'))                         # 2 iterables
print list(map(lambda *a: a, range(3), 'abc', range(4, 7)))            # 3
# map stops at the shortest iterator
print list(map(lambda *a: a, (), 'abc'))                               # empty tuple is shortest
print list(map(lambda *a: a, (1, 2), 'abc'))                           # (1, 2) shortest
print list(map(lambda *a: a, (1, 2, 3, 4), 'abc'))                     # 'abc' shortest


# decorate.sort.undecorate.py
students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

def decorate(student):
    # create a 2-tuple (sum of credits, student) from student dict
    return (sum(student['credits'].values()), student)

def undecorate(decorated_student):
    # discard sum of credits, return original student dict
    return decorated_student[1]

print students[0]
print decorate(students[0])
print students
students = sorted(map(decorate, students), reverse=True)
print students
students = list(map(undecorate, students))
print students
