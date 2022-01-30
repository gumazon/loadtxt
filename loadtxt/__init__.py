__version__ = '1.0.0'
__all__ = ['new']

from pathlib import Path

from .controller import new

__doc__ = [
    ' '.join(['#', Path.cwd().name.capitalize(), 'v'+__version__+'\n\n']),
    ' '.join(['## Features\n\n']),
    ' '.join(['### `new`: ', new.__doc__+'\n'])
]

