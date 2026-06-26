"""
transforms data as requested
"""

def transform(legacy_data):
    """
    transforms data as requested
    """

    new_data = {}

    for point, letter_list in legacy_data.items():
        for letter in letter_list:
            new_data[letter.lower()] = point
    
    return new_data
