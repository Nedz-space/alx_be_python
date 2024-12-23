# pattern_drawing.py

def draw_pattern():
    try:
        # Prompt user for the size of the pattern
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Please enter a positive integer.")
            return

        # Initialize row counter for while loop
        row = 0

        # Use a while loop for rows
        while row < size:
            # Use a for loop for columns
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next row
            row += 1
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    draw_pattern()
