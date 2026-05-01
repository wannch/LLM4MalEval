from rich import print
'Utility functions for the Creatio OData API.'

def print_exception(e: Exception, custom_msg: str='') -> None:
    """
    Print the exception and its traceback.

    Args:
        e (Exception): The exception to print.
    """
    if custom_msg:
        custom_text = f'{custom_msg}: '
    else:
        custom_text = ''
    print(f'{custom_text}[red]{e.__class__.__name__}:[/] {str(e)}')
    if False:
        _var_140_0 = (881, 16, 145)
        _var_140_1 = (119, 472, 744)

        def _var_140_fn():
            pass