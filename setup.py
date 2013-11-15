'''
setup.py file for NLPIR
'''
from distutils.core import setup, Extension
 
NLPIR_module = Extension('_NLPIR',sources=['NLPIR_wrap.cxx'], libraries = ['NLPIR'])

setup(name = 'NLPIR',
    version = '2.0',
    author = 'Killua',
    description = 'Python for NLPIR',
    ext_modules = [NLPIR_module],
    py_modules = ['NLPIR', 'PyNLPIR'],
    )
