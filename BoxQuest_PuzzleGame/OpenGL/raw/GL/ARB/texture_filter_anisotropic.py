'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_texture_filter_anisotropic'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_texture_filter_anisotropic',error_checker=_errors._error_checker)
GL_MAX_TEXTURE_MAX_ANISOTROPY=_C('GL_MAX_TEXTURE_MAX_ANISOTROPY',0x84FF)
GL_TEXTURE_MAX_ANISOTROPY=_C('GL_TEXTURE_MAX_ANISOTROPY',0x84FE)

