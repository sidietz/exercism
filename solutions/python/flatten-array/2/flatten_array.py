"""
flattens a list of nested lists
"""

def flatten(iterable):
    """
    flattens a list of nested lists
    """

    if not iterable and iterable != 0:
        return []

    if isinstance(iterable, list):
        return [a for i in iterable for a in flatten(i)]
    
    return [iterable]

    

    
