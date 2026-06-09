"""
To build:
    python setup.py build
To build and install:
    python setup.py install
"""
import os
import re
import sys
import shutil
import subprocess
from distutils import log

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


def get_extra_cmake_options():
    """read --clean, --no, --set, --compiler-flags, and -G options from the command line
    and add them as cmake switches.
    """
    _cmake_extra_options = []
    _clean_build_folder = False

    opt_key = None

    argv = [arg for arg in sys.argv]  # take a copy
    for arg in argv:
        if opt_key == 'compiler-flags':
            _cmake_extra_options.append('-DCMAKE_CXX_FLAGS={arg}'.format(arg=arg.strip()))
        elif opt_key == 'G':
            _cmake_extra_options += ['-G', arg.strip()]
        elif opt_key == 'no':
            _cmake_extra_options.append('-D{arg}=no'.format(arg=arg.strip()))
        elif opt_key == 'set':
            _cmake_extra_options.append('-D{arg}'.format(arg=arg.strip()))

        if opt_key:
            sys.argv.remove(arg)
            opt_key = None
            continue

        if arg == '--clean':
            _clean_build_folder = True
            sys.argv.remove(arg)
            continue

        if arg in ['--no', '--set', '--compiler-flags']:
            opt_key = arg[2:].lower()
            sys.argv.remove(arg)
            continue
        if arg in ['-G']:
            opt_key = arg[1:]
            sys.argv.remove(arg)
            continue

    return _cmake_extra_options, _clean_build_folder

cmake_extra_options,clean_build_folder = get_extra_cmake_options()


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

def rmtree(name):
    """remove a directory and its subdirectories.
    """
    def remove_read_only(func, path, exc):
        excvalue = exc[1]
        if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
            os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            func(path)
        else:
            raise

    if os.path.exists(name):
        log.info('Removing old directory {}'.format(name))
        shutil.rmtree(name, ignore_errors=False, onerror=remove_read_only)

class CMakeBuild(build_ext):

    def test_cmake(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except:
            sys.stderr.write("\nERROR: CMake must be installed to build\n\n") 
            sys.exit(1)
        return re.search(r'version\s*([\d.]+)', out.decode()).group(1)

    def run(self):
        self.test_cmake()

        log.info('Building backend')
        for ext in self.extensions:
            self.build_extension(ext)

    def make_build_folder(self):
        build_folder = os.path.abspath(self.build_temp)

        if clean_build_folder:
            rmtree(build_folder)
        if not os.path.exists(build_folder):
            os.makedirs(build_folder)

        return build_folder

    def cmake_setup(self, ext, build_folder):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir]
        cmake_args += cmake_extra_options

        setup_cmd = ['cmake', ext.sourcedir] + cmake_args

        print("Building extension for Python {}".format(sys.version.split('\n',1)[0]))
        print("Invoking CMake setup: '{}'".format(' '.join(setup_cmd)))
        sys.stdout.flush()
        subprocess.check_call(setup_cmd, cwd=build_folder)

    def cmake_build(self, build_folder):
        build_cmd = ['cmake', '--build', '.']
        print("Invoking CMake build: '{}'".format(' '.join(build_cmd)))
        sys.stdout.flush()
        subprocess.check_call(build_cmd, cwd=build_folder)

    def build_extension(self, ext):
        build_folder = self.make_build_folder()

        self.cmake_setup(ext, build_folder)

        print("Building cpp library from source")
        self.cmake_build(build_folder)

setup(name='tobi',
      version='1.0.0',
      author='tobi-v',
      author_email='tobias.vetter@live.de',
      ext_modules=[CMakeExtension('_cpp_backend_pybind','src/backend/pybindings')],
      cmdclass=dict(build_ext=CMakeBuild),
      package_dir={'tobi': 'src/frontend'},
      packages=['tobi', 'tobi.functions'],
      entry_points={
        'console_scripts': [
            'tobi=ex.frontend.main:main',
        ],
      },
      install_requires = [
          'numpy >= 2.2.0'],
      )
