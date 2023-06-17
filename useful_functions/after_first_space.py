def after_first_space_function(s):
    parts = s.split(' ', 1)  # Split the string at the first space
    if len(parts) > 1:       # If there was a space in the string...
        return parts[1]      # Return the part after the first space
    else:
        return ''            # If there was no space in the string, return an empty string
