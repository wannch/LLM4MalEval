import logging
if False:
    _var_101_0 = (21, 478, 325)
    _var_101_1 = (422, 828, 226)
    _var_101_2 = (493, 872, 403)

    def _var_101_fn():
        pass
'\n    logger.py\n'
if False:
    _var_102_0 = (986, 830, 760)

    def _var_102_fn():
        pass
from rich.traceback import install
from rich.logging import RichHandler
from minishell import config

def enable_pretty_tracebacks() -> None:
    """
        Enable Pretty Traceback

        Uses rich to print pretty tracebacks
    """
    install()

def stdout(name: str, log_level: int) -> logging.Logger:
    """
        Sets up a logger that logs to stdout

        Uses RichHandler to pretty print logs
    """
    words_to_highlight = config.log_words_to_highlight
    if False:
        _var_97_0 = (996, 704, 783)
        _var_97_1 = (439, 430, 214)

        def _var_97_fn():
            pass
    handler = RichHandler(show_time=config.log_show_time, keywords=[w.lower() for w in words_to_highlight] + [w.upper() for w in words_to_highlight] + [w.capitalize() for w in words_to_highlight])
    if False:
        _var_98_0 = (55, 738, 288)
        _var_98_1 = (415, 562, 613)
        _var_98_2 = (616, 595, 425)

        def _var_98_fn():
            pass
    logger = CustomLogger(name)
    logger.setLevel(log_level)
    formatter = logging.Formatter(config.log_formatter)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
if False:
    _var_103_0 = (555, 383, 518)

    def _var_103_fn():
        pass

class CustomLogger(logging.Logger):
    """
        Extends the logging.Logger class
        with  custom methods
    """

    def flush(self) -> None:
        """
            Flush

            Flushes the logger
        """
        if False:
            _var_99_0 = (697, 73, 445)
            _var_99_1 = (611, 865, 569)

            def _var_99_fn():
                pass
        for handler in self.handlers:
            handler.flush()
        if False:
            _var_100_0 = (231, 310, 924)
            _var_100_1 = (98, 620, 333)
            _var_100_2 = (769, 21, 673)

            def _var_100_fn():
                pass