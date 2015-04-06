import platform
import shutil
import os
import re

OS_VERSION = platform.system()
OS_BITS = platform.architecture()[0]
LIB_NLPIR = 'libNLPIR.so' if OS_VERSION == 'Linux' else 'NLPIR.dll'
SCRIPT_SUFFIX = '.sh' if OS_VERSION == 'Linux' else '.bat'


def is_swig_installed():
    for cmdpath in os.environ['PATH'].split(':'):
        if os.path.isdir(cmdpath) and 'swig' in os.listdir(cmdpath):
            return True


def check_installers():
    swig_pattern = re.compile(r'^swig-(?P<swig_version>[\d\.]+)')
    pcre_pattern = re.compile(r'^pcre-(?P<pcre_version>[\d\.]+)')

    for f in os.listdir('dependences'):
        if swig_pattern.match(f):
            swig_version = swig_pattern.match(f).groups('swig_version')[0][0:-1]
        elif pcre_pattern.match(f):
            pcre_version = pcre_pattern.match(f).groups('pcre_version')[0][0:-1]

    if swig_version is None:
        raise 'swig tarball not found!'
    elif pcre_version is None:
        raise 'pcre tarball not found!'


def install_swig():
    if OS_VERSION == 'Windows':
        # TODO Add swig installation scripts in Windows.
        print 'SWIG should be installed manually in Windows'
        return
    os.system(os.path.join('scripts', 'install_swig' + SCRIPT_SUFFIX))


def install_nlpir():
    print 'Generate NLPIR wrapper.'
    os.system('swig -c++ -python NLPIR.interface')

    lib_dir = os.path.join(os.curdir, 'lib', ('linux' if OS_VERSION == 'Linux' else 'win') + OS_BITS.replace('bit', ''))
    if OS_VERSION == 'Linux':
        lib_target = os.path.join('/usr', 'lib')
    elif OS_VERSION == 'Windows':
        lib_target = os.path.join(os.environ['SYSTEMROOT'], 'system32')
        pass
    print 'Copy %s to %s' % (LIB_NLPIR, lib_target)
    shutil.copy(os.path.join(lib_dir, LIB_NLPIR), os.path.join(lib_target, LIB_NLPIR))

    print 'Install PyNLPIR.'
    os.system('python setup.py build_ext --inplace')
    os.system('python setup.py install')

if __name__ == '__main__':

    if not is_swig_installed():
        check_installers()
        install_swig()

    if is_swig_installed():
        install_nlpir()
    else:
        print 'Make sure that SWIG have been installed already.'