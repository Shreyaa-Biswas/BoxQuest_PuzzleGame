'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_EXT_device_query'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.EGL,'EGL_EXT_device_query',error_checker=_errors._error_checker)
EGL_BAD_DEVICE_EXT=_C('EGL_BAD_DEVICE_EXT',0x322B)
EGL_DEVICE_EXT=_C('EGL_DEVICE_EXT',0x322C)
# EGL_NO_DEVICE_EXT=_C('EGL_NO_DEVICE_EXT',((EGLDeviceEXT)(0)))
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDeviceEXT,_cs.EGLint,arrays.EGLAttribArray)
def eglQueryDeviceAttribEXT(device,attribute,value):pass
@_f
@_p.types(ctypes.c_char_p,_cs.EGLDeviceEXT,_cs.EGLint)
def eglQueryDeviceStringEXT(device,name):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLint,arrays.EGLAttribArray)
def eglQueryDisplayAttribEXT(dpy,attribute,value):pass
