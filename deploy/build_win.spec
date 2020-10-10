# -*- mode: python -*-

# dynamically find site-packages dir
# see http://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory
from distutils.sysconfig import get_python_lib

a = Analysis([os.path.join('@goxgui.dir@', 'application.py')],
             pathex=['@goxtool.dir@', os.path.join(get_python_lib(), 'Crypto')])

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scrip