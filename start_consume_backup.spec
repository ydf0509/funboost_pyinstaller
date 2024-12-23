# -*- mode: python ; coding: utf-8 -*-
# 导入必要的模块
import os
import site
from pathlib import Path

# 递归获取当前文件夹下所有 .py 文件的路径
def get_py_files__dir(folder):
    py_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".py") :
                py_files.append((os.path.join(root, file), root))
                # py_files.append(os.path.join(root, file))
    return py_files

# 获取当前文件夹下所有 .py 文件的路径
py_files__dir = get_py_files__dir(".")

print(0,py_files__dir)

a = Analysis(
    ['start_consume.py'],
    pathex=[],
    binaries=[],
    datas= py_files__dir ,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='start_consume',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
