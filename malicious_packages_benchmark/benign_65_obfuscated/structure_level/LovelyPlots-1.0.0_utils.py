import matplotlib as mpl

def set_font(font_path):
    """Set fonts for matplotlib plots

    Args:
        font_path (str): path to .tiff font
    """
    font = mpl.font_manager.FontEntry(fname=font_path, name='my_font')
    if False:
        _var_85_0 = (657, 719, 555)

        def _var_85_fn():
            pass
    mpl.font_manager.fontManager.ttflist.append(font)
    mpl.rcParams.update({'font.family': font.name})
    if False:
        _var_86_0 = (115, 526, 93)
        _var_86_1 = (366, 217, 802)
        _var_86_2 = (692, 856, 423)

        def _var_86_fn():
            pass

def set_retina():
    from IPython import get_ipython
    'set retina display support in IPython notebooks\n    '
    get_ipython().run_line_magic('matplotlib', 'inline')
    from IPython.display import set_matplotlib_formats
    set_matplotlib_formats('retina')
if False:
    _var_89_0 = (741, 37, 819)
    _var_89_1 = (562, 491, 205)

    def _var_89_fn():
        pass

def set_size(subplots=(1, 1)):
    """Set size for subplots

    Args:
        subplots (tuple, optional): number of (row,col) subplots. Defaults to (1, 1).

    Returns:
        tuple: size of subplots
    """
    fig_width_in = mpl.rcParams['figure.figsize'][0]
    if False:
        _var_87_0 = (791, 825, 732)
        _var_87_1 = (192, 38, 104)

        def _var_87_fn():
            pass
    fig_height_in = mpl.rcParams['figure.figsize'][1] * (subplots[0] / subplots[1])
    return (fig_width_in, fig_height_in)
    if False:
        _var_88_0 = (247, 576, 336)
        _var_88_1 = (941, 337, 407)
        _var_88_2 = (894, 725, 127)

        def _var_88_fn():
            pass