# multiplication_table.py

def generate_multiplication_table():
    try:
        # Prompt user for a number
        number = int(input("Enter a number to see its multiplication table: "))

        # Generate and print the multiplication table
        for i in range(1, 11):
            product = number * i
            print(f"{number} * {i} = {product}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    generate_multiplication_table()

