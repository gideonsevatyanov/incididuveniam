def find_largest_font_size(text, space):
    low, high = 1, 100
    while low <= high:
        mid = (low + high) // 2
        if font_fits(text, mid, space):
            low = mid + 1
        else:
            high = mid - 1
    return high

def font_fits(text, size, space):
    # Function to check if the given font size fits within the given space
    # Implement your logic here
    pass

# Example usage
text = "Sample text"
space = 100
largest_font_size = find_largest_font_size(text, space)
print("Largest font size that fits:", largest_font_size)
