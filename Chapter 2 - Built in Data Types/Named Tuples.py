vision = (9.5, 8.8)
print vision

print vision[0]                 # left eye (implicit postional reference)
print vision[1]                 # right eye (implicit postional reference)


from collections import namedtuple

Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8)
print '\n', vision[0]
print vision.left               # same as vision[0] but explicit
print vision.right              # same as vision[1] but explicit


Vision = namedtuple('Vision', ['left', 'combined', 'right'])
vision = Vision(9.5, 9.2, 8.8)
print '\n', vision.left
print vision.right
print vision.combined


