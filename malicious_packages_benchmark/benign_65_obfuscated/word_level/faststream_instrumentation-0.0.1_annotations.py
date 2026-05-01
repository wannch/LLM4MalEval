from faststream.utils.context import Context
DX=True
from opentelemetry import trace
from typing_extensions import Annotated

DN = Annotated[trace.Span, Context(("".join([chr(115),chr(112),chr(97),chr(110)]))                                         , cast=DX)]
