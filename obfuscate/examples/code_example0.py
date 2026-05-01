"""
This is my code module.
"""

class MyDefinedClass:

    # method a
    def method_a(self):
        return "Method A"

def fibonacci(top_n):
    """Return the nth Fibonacci number."""
    left, right = 0, 1
    for _ in range(top_n): # For Loop
        left, right = right, left + right
    return left

if __name__ == '__main__':
    res = fibonacci(10)
    print(res)