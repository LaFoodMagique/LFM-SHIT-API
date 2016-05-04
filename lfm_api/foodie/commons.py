#
# Functions
#

def part_of(obj, list_obj):
    for o in list_obj:
        if o is obj:
            return True
    return False


#
# Marks
#

MARKS = (
    (0, 'Very bad'),
    (1, 'Bad'),
    (2, 'Normal'),
    (3, 'Good'),
    (4, 'Very good'),
)
