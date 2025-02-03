import weakref

from .program import ModularProgram

class MultiProgram(object):
    def __init__(self, vcode="", fcode="", gcode=None): ...
    def add_program(self, name=None): ...
    @property
    def vert(self): ...
    @vert.setter
    def vert(self, code): ...
    @property
    def frag(self): ...
    @frag.setter
    def frag(self, code): ...
    @property
    def geom(self): ...
    @geom.setter
    def geom(self, code): ...
    def __contains__(self, key): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __iter__(self): ...
    def bind(self, data): ...

class MultiShader(object):
    def __init__(self, program, shader): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def _new_program(self, p): ...
