def after_first_space_function(s):
    parts = s.split(' ', 1)  # Split the string at the first space
    if len(parts) > 1:       # If there was a space in the string...
        first_part = parts[0]
        second_part = parts[1]
        return second_part, first_part      # Return the part after the first space
    else:
        return ''            # If there was no space in the string, return an empty string
