def square(side):
    area = side * side
    return int(area) + 1 if isinstance(side, float) else int(area)
