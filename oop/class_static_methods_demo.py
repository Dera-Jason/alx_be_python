# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and display the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage:
if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")

    # Using class method
    product_result = Calculator.multiply(10, 5)
    print(f"Product: {product_result}")
