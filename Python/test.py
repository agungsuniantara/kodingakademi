def scholarship(cgpa, year, program):
    """
    Determines if a student is eligible for a scholarship based on their CGPA, year of study, and program.

    >>> scholarship(4.0, 2, "CS")
    True
    >>> scholarship(3.8, 3, "cs")
    True
    >>> scholarship(3.7, 1, "CS")
    False
    >>> scholarship(3.6, 2, "CS")
    False
    >>> scholarship(4.0, 2, "BIO")
    False
    """
    
    if cgpa >= 3.7 and (year == 2 or year == 3) and program.lower() == "cs":
        return True
    else:
        return False

# Remove or comment out this line for doctest
# scholarship(2,10,"BIO")
