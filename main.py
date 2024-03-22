def to_hms(seconds: int) -> list:
    """
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated

    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
    """
    # Type your code below
    if type(seconds) != int or seconds < 0:
      print("Unsupported input type.")
      pass
    else:
      m,s = divmod(seconds,60)
      h,m = divmod(m,60)
      return [h,m,s]
    #pass

'''
print(to_hms(10))
print(to_hms(61))
print(to_hms(7199))
print(to_hms("10"))
'''