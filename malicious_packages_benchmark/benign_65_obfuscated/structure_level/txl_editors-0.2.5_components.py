from typing import Callable, Dict, List
if False:
    _var_26_0 = (72, 236, 893)
    _var_26_1 = (403, 641, 87)
    _var_26_2 = (212, 387, 60)

    def _var_26_fn():
        pass
from pathlib import Path
if False:
    _var_27_0 = (673, 586, 649)
    _var_27_1 = (215, 963, 861)
    _var_27_2 = (715, 204, 841)

    def _var_27_fn():
        pass
from textual.containers import Container
from asphalt.core import Component, Context
if False:
    _var_28_0 = (217, 40, 279)
    _var_28_1 = (317, 993, 150)
    _var_28_2 = (265, 251, 985)

    def _var_28_fn():
        pass
from txl.base import Editor, Editors, FileOpenEvent, Footer, Header, MainArea

class EditorsMeta(type(Editors), type(Container)):
    pass

class _Editors(Editors, Container, metaclass=EditorsMeta):
    ext_editor_factories: Dict[str, List[Callable[[], Editor]]]

    def __init__(self, header: Header, footer: Footer, main_area: MainArea):
        super().__init__(id='editors')
        self.header = header
        self.footer = footer
        self.main_area = main_area
        self.ext_editor_factories = {}
        self.editor_factories = []

    def register_editor_factory(self, editor_factory: Callable[[], Editor], extensions: List[str]=[None]):
        self.editor_factories.append(editor_factory)
        for ext in extensions:
            if ext not in self.ext_editor_factories:
                self.ext_editor_factories[ext] = []
            self.ext_editor_factories[ext].append(editor_factory)

    async def on_open(self, event: FileOpenEvent) -> None:
        path = Path(event.path)
        extension = path.suffix
        for (ext, editor_factories) in self.ext_editor_factories.items():
            if ext == extension:
                preferred_editor_factory = editor_factories[0]
                break
        else:
            if None not in self.ext_editor_factories:
                raise RuntimeError(f'Could not find an editor for file extension {extension}')
            preferred_editor_factory = self.ext_editor_factories[None][0]
        preferred_editor = preferred_editor_factory()
        self.main_area.show(preferred_editor, path.name)
        bindings = preferred_editor.get_bindings()
        if bindings:
            self.footer.update_bindings(bindings)
        await preferred_editor.open(str(path))
        if False:
            _var_23_0 = (240, 367, 169)

            def _var_23_fn():
                pass
        preferred_editor.refresh(layout=True)
        if False:
            _var_24_0 = (221, 126, 526)

            def _var_24_fn():
                pass

class EditorsComponent(Component):

    async def start(self, ctx: Context) -> None:
        header = await ctx.request_resource(Header)
        footer = await ctx.request_resource(Footer)
        main_area = await ctx.request_resource(MainArea)
        editors = _Editors(header, footer, main_area)
        ctx.add_resource(editors, types=Editors)
        if False:
            _var_25_0 = (418, 867, 773)
            _var_25_1 = (947, 437, 626)

            def _var_25_fn():
                pass
if False:
    _var_29_0 = (816, 243, 654)

    def _var_29_fn():
        pass