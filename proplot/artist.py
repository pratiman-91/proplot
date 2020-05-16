#!/usr/bin/env python3
"""
Create a metaclass
"""
import matplotlib.artist as martist
import matplotlib.lines as mlines

__all__ = []

PROPS_PROTECTED = [
    'figure', 'axes', 'pickradius',
]


def _gen_subclasses(cls):
    """
    Generate all of a class's sublcasses with recursion.
    """
    try:
        for subclass in cls.__subclasses__():
            yield subclass
            for subclass in _gen_subclasses(subclass):
                yield subclass
    except TypeError:
        return


def _gen_properties(cls):
    """
    Generate property definitions for every
    Get proper
    """
    for attr in dir(cls):
        obj = getattr(cls, attr)
        if callable(obj) and attr[:4] == 'get_':
            getter = obj
            name = attr[4:]
            if hasattr(cls, name):
                continue
            elif name in PROPS_PROTECTED:
                continue
            args = [getter]  # property args
            setter = getattr(cls, 'set_' + name, None)
            if callable(setter):
                args.append(setter)
            yield name, property(*args, doc=getter.__doc__)


# Approach #1: Apply properties to all artists
for cls in _gen_subclasses(martist.Artist):
    for name, prop in _gen_properties(cls):
        setattr(cls, name, prop)
    print(f'Added properties to {cls.__name__}.')


# Approach #2: Requires importing proplot before matplotlib.
# This will not work for ProPlot but may be in matplotlib's future.
class Propertifier(type):  # create new class definitions
    """
    Artist metaclass.
    """
    def __init__(cls, *args, **kwargs):
        """
        Add property getters and setters to all matplotlib artist subclasses.
        """
        super().__init__(*args, **kwargs)
        for name, property in _gen_properties(cls):
            setattr(cls, name, property)
        print(f'Added properties to {cls.__name__}.')


class Artist(martist.Artist, metaclass=Propertifier):
    """
    New base class for all matplotlib artists that
    uses `Propertifier` as the metaclass.
    """


# Apply monkey patch
import matplotlib.artist as martist
martist.Artist = Artist


# Testing metaclasses
class MetaClass(type):
    def __init__(cls, *args, **kwargs):
        print('Brand new class!', cls)
        super().__init__(*args, **kwargs)


A = MetaClass('A', (object,), {})
B = MetaClass('B', (A,), {})


# Testing Artist
class Test(Artist):
    def set_foo(self, foo):
        print('set foo!', foo)

    def get_foo(self):
        print('get foo!')

    def get_bar(self):
        print('get bar!')


class Line2D(Artist, mlines.Line2D):
    pass


test = Test()
line = Line2D([0], [0])
