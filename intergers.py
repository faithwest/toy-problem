# Function to check if at least two out of three numbers are positive
def positives(a, b, c):
    # Check if either the first or second number is positive, or if both the second and third numbers are positive
    if (a > 0 or b > 0) or (b > 0 and c > 0):
        return True
    else:
        return False

# test output
print(positives(4, -6, 9))  # Output: True
