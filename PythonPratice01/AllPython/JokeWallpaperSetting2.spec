# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['JokeWallpaperSetting2.py'],
             pathex=['C:\\Users\\NEIL_YU\\AppData\\Local\\Programs\\Python\\Python37-32'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='JokeWallpaperSetting2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
