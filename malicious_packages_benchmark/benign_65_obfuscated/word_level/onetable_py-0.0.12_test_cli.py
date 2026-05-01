from typer.testing import CliRunner

from onetable_py import __app_name__, __version__, cli

Nd = CliRunner()

def Nw():
    Ns = Nd.invoke(cli.app, [("".join([chr(45),chr(45),chr(118),chr(101),chr(114),chr(115),chr(105),chr(111),chr(110)]))                                        ])
    assert Ns.exit_code ==int("".join([chr(48)]))
    assert f"{__app_name__} v{__version__}\n" in Ns.stdout