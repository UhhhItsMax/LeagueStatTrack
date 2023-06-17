def after_last_space_function(s):
    # Find last space
    last_space_index = s.rfind(' ')

    # If no space is found, return entire String
    if last_space_index == -1:
        return s, ''

    # Split String in 2 Parts, first_part everything before the last space, and everything else in second_part
    first_part = s[:last_space_index]
    second_part = s[last_space_index+1:]

    return first_part, second_part