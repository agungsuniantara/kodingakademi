def find_peak_element(lst: list[int]) -> int:
    if lst[0] >= lst[1]:
        return lst[0]

    for i in range(1, len(lst) - 1):
        if lst[i] >= lst[i - 1] and lst[i] >= lst[i + 1]:
            return lst[i]
    
    if lst[-1] >= lst[-2]:
        return lst[-1]
    
    return lst[0] 