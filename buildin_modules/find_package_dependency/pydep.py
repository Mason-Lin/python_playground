# not ready yet


import logging
import site
import sys
import click
from importlib.util import find_spec
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)


class ImportWatcher(object):
    ps = {}
    sites = site.getsitepackages()
    sites.append(site.getusersitepackages())
    sites = tuple(sites)
    logging.debug(sites)

    @classmethod
    def find_spec(cls, name, path, target=None):
        if path:
            for p in path:
                # if str(p).startswith(cls.sites):
                #     continue
                if p in cls.ps:
                    cls.ps[p].add(name)
                else:
                    cls.ps[p] = {name}


sys.meta_path.insert(0, ImportWatcher)


@click.command()
@click.argument('f')
def get_dependencies(f):
    pf = Path(f)
    logging.debug(f'pf, {type(pf)}')
    pass

if __name__ == "__main__":
    get_dependencies()
