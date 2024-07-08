'''Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.'''
def unique_in_order(sequence):
    if not sequence:
        return list(sequence)
    else:
        item1 = [sequence[0]]
        for item in sequence[1:]:
            if item1[-1] != item:
                item1.append(item)
    return item1
ls = 'AAAABBBCCDAABBB'
unique_in_order(ls)