# This is a comment

def  foo(bar,  baz=  2):   # inline comment
    """
    docstring should remain because it's a string literal
    """
    s = "Hello , World!"  # another comment
    if (bar > 0):
        x = bar  +  baz
        return x  # return value
    return None