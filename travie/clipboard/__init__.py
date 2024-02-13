"""Package for pytravie.clipboard."""
__version__ = "0.0.0"
import clipboard
from travie.funcs import readlines

def SimpleXForm():
    print('Template:')
    temp = '\n'.join(readlines())
    if not temp: temp = clipboard.paste()
    From = input('From: ')
    print('To:')
    Tos = readlines()
    clipboard.copy( ''.join( temp.replace( From, To ) for To in Tos ) )
