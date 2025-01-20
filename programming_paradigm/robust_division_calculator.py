# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform division and handle division by zero
        if den == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / den}"
    
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."

