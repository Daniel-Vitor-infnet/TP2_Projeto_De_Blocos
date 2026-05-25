from setuptools import setup, Extension
from Cython.Build import cythonize

from setuptools import setup, Extension
ext_modules = [ 
    Extension(
        "exercicio1",
        ["exercicio1.pyx"],
        extra_compile_args=["-fopenmp"],
        extra_link_args=["-fopenmp"],
    )
    
]
setup(name="exercicio1", ext_modules=ext_modules)