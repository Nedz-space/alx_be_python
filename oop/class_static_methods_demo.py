class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Returns the sum of two numbers.
        :param a: First number
        :param b: Second number
        :return: Sum of a and b
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Returns the product of two numbers, printing the class attribute first.
        :param a: First number
        :param b: Second number
        :return: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

