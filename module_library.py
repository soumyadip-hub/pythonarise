print("imported my modeule___________....")

test = 'test string'

def find_index(to_search, target):
    """find out the index of value in sequence"""
    for i,value in enumerate(to_search):
        if value == target:
            return i
    return -1