# -*- mode: python ; coding: utf-8 -*-
#this belongs in root /txd_workshop.spec - Version: 2
# X-Seti - September30 2026 - Txd Workshop - PyInstaller build spec (Windows)

"""
PyInstaller spec for the standalone TXD Workshop Windows build.
Build: pyinstaller txd_workshop.spec  ->  dist/Txd_Workshop/Txd_Workshop.exe
"""

##Methods list -
# _app_data
# _make_icon

import os

ROOT = os.path.abspath(SPECPATH)


def _app_data(): #vers 1
    """Every non-Python file under apps/, kept at the same relative path."""
    out = []
    for base, dirs, files in os.walk(os.path.join(ROOT, 'apps')):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for name in files:
            if name.endswith(('.py', '.pyc', '.log')):
                continue
            src = os.path.join(base, name)
            out.append((src, os.path.relpath(base, ROOT)))
    return out


def _make_icon(): #vers 1
    """Render the TXD Workshop SVG app icon to build/txd_workshop.ico."""
    import sys
    os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
    sys.path.insert(0, ROOT)
    from PyQt6.QtWidgets import QApplication
    app = QApplication.instance() or QApplication([])
    from apps.methods.imgfactory_svg_icons import SVGIconFactory
    out = os.path.join(ROOT, 'build', 'txd_workshop.ico')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if not SVGIconFactory.txd_workshop_icon(256).pixmap(256, 256).toImage().save(out, 'ICO'):
        raise RuntimeError('ICO write failed')
    return out


a = Analysis(
    ['launch_txd_workshop.py'],
    pathex=[ROOT],
    binaries=[],
    datas=_app_data() + [(os.path.join(ROOT, 'appfactory.settings.json'), '.')],
    hiddenimports=['PyQt6.QtSvg', 'PIL.Image', 'numpy', 'pygame', 'pygame._sdl2.controller'],
    excludes=['tkinter'],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name='Txd_Workshop',
    console=False,
    icon=_make_icon(),
    upx=False,
)
coll = COLLECT(exe, a.binaries, a.datas, upx=False, name='Txd_Workshop')
