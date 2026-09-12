# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Pathway_Game.py'],
    pathex=[],
    binaries=[],
    datas=[('pa_place.png', '.'), ('p.png', '.'), ('comet_stationary.png', '.'), ('rocks.png', '.'), ('cosmic_dust.png', '.'), ('dot.png', '.'), ('city_scrap.png', '.'), ('cracks.png', '.'), ('line.png', '.'), ('dust_label.png', '.'), ('ring_label.png', '.'), ('scrap_label.png', '.')],
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
    name='Pathway_Game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
