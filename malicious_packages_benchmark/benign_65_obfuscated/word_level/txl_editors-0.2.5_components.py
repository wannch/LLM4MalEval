from pathlib import Path
xO=type
xT=str
xz=super
xf=None
xc=RuntimeError
xd=True
from typing import Callable, Dict, List

from asphalt.core import Component, Context
from textual.containers import Container

from txl.base import Editor, Editors, FileOpenEvent, Footer, Header, MainArea


class xo(xO(Editors), xO(Container)):
    pass


class xL(Editors, Container, metaclass=xo):
    xM: Dict[xT, List[Callable[[], Editor]]]

    def __init__(
        xr,
        xS: Header,
        xB: Footer,
        xI: MainArea,
    ):
        xz().__init__(id=("".join([chr(101),chr(100),chr(105),chr(116),chr(111),chr(114),chr(115)]))                                  )
        xr.header = xS
        xr.footer = xB
        xr.main_area = xI
        xr.ext_editor_factories = {}
        xr.editor_factories = []

    def xh(
        xr, editor_factory: Callable[[], Editor], extensions: List[xT] = [xf]
    ):
        xr.editor_factories.append(editor_factory)
        for xe in extensions:
            if xe not in xr.ext_editor_factories:
                xr.ext_editor_factories[xe] = []
            xr.ext_editor_factories[xe].append(editor_factory)

    async def xF(xr, event: FileOpenEvent) -> xf:
        xg = Path(event.path)
        xE = xg.suffix
        for xe, editor_factories in xr.ext_editor_factories.items():
            if xe == xE:
                xt = editor_factories[int("".join([chr(48)]))                                       ]
                break
        else:
            if xf not in xr.ext_editor_factories:
                raise xc(f"Could not find an editor for file extension {extension}")
            xt = xr.ext_editor_factories[xf][int("".join([chr(48)]))                                              ]
        xC = xt()
        xr.main_area.show(xC, xg.name)
        xa = xC.get_bindings()
        if xa:
            xr.footer.update_bindings(xa)
        await xC.open(xT(xg))
        xC.refresh(layout=xd)


class xW(Component):
    async def xk(
        xr,
        ctx: Context,
    ) -> xf:
        xS = await ctx.request_resource(Header)
        xB = await ctx.request_resource(Footer)
        xI = await ctx.request_resource(MainArea)
        xY = xL(xS, xB, xI)
        ctx.add_resource(xY, types=Editors)
