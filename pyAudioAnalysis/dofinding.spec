# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['G:\\SimilaritySearchingTool\\pyAudioAnalysis\\pyAudioAnalysis\\dofinding.py'],
             pathex=['G:\\SimilaritySearchingTool\\pyAudioAnalysis\\pyAudioAnalysis\\neededpkg'],
             binaries=[],
             datas=[],
             hiddenimports=['sklearn.neighbors._partition_nodes', 'sklearn.utils._vector_sentinel', 'sklearn.utils._sorting', 'sklearn.utils._typedefs', 'sklearn.utils._heap', 'ipykernel', 'tornado', 'wx', 'pkg_resources.py2_warn', 'pkg_resources.markers'],
             hookspath=[],
             hooksconfig={},
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
          [],
          exclude_binaries=True,
          name='dofinding',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='yamadaryo.ico',
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='dofinding')
