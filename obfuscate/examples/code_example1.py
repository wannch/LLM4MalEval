"""
This is my code module.
"""

class MyDefinedClass:

    def method_a(self):
        return 'Method A'
        if False:
            __dead_var_1_0 = (801, 455, 426)

            def __dead_var_1_fn():
                pass

def fibonacci(top_n):
    (left, right) = (0, 1)
    'Return the nth Fibonacci number.'
    for _ in range(top_n):
        (left, right) = (right, left + right)
    return left
if __name__ == '__main__':
    res = fibonacci(10)
    print(res)