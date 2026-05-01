'''
    logger.py
'''
import logging
from rich.logging import RichHandler
from rich.traceback import install
from minishell import config
def enable_pretty_tracebacks()->None:
  install()
def stdout(name:str,log_level:int)->logging.Logger:
  words_to_highlight=config.log_words_to_highlight
  handler=RichHandler(    show_time=config.log_show_time,    keywords=[w.lower()for w in words_to_highlight]+        [w.upper()for w in words_to_highlight]+        [w.capitalize()for w in words_to_highlight]  )
  logger=CustomLogger(name)
  logger.setLevel(log_level)
  formatter=logging.Formatter(config.log_formatter)
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  return logger
class CustomLogger(logging.Logger):
  def flush(self)->None:
    for handler in self.handlers:
      handler.flush()