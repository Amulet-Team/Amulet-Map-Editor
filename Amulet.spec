# -*- mode: python -*-

block_cipher = None

a = Analysis(
	['amulet-tech-demo-ui.py'],
	pathex=['.'],
	binaries=[],
	datas=[
		('./venv/Lib/site-packages/PyMCTranslate', './PyMCTranslate'),
		('./venv/Lib/site-packages/amulet', './amulet'),
	],
	hiddenimports=[],
	hookspath=[],
	runtime_hooks=[],
	excludes=[],
	win_no_prefer_redirects=False,
	win_private_assemblies=False,
	cipher=block_cipher,
	noarchive=False
)

pyz = PYZ(
	a.pure,
	a.zipped_data,
	cipher=block_cipher
)

exe = EXE(
	pyz,
	a.scripts,
	[],
	exclude_binaries=True,
	name='Amulet-tech-demo',
	debug=False,
	bootloader_ignore_signals=False,
	strip=False,
	upx=True,
	console=True,
	icon='icon.ico'
)

coll = COLLECT(
	exe,
	a.binaries,
	a.zipfiles,
	a.datas,
	strip=False,
	upx=True,
	name='Amulet-tech-demo'
)
