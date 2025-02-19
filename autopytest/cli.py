from .autotest import Autotest
import sys

def cli() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    autotest = Autotest(path)
    autotest.start()

def main() -> None:
    cli()