#
# Functions
#

def to_json(title, message=None):
    return {
        str(title): message
    }


def part_of(obj, list_obj):
    for o in list_obj:
        if o is obj:
            return True
    return False
