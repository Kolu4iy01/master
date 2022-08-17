def reverse_list(l):
    new_l = []
    for char in l:
        new_l = [char] + new_l
    return new_l
