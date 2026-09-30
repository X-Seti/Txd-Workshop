# TXD Workshop

Standalone TXD (texture dictionary) editor for GTA III, VC, SA and other RenderWare games, synced from IMG Factory 1.6.

## Windows
Download `Txd_Workshop_Windows.zip` from the `windows-build` release, unzip, run `Txd_Workshop/Txd_Workshop.exe`.
Settings save in `settings/` beside the exe. Custom ribbon icons go in `icons/`.

## Run from source
```
pip install PyQt6 numpy Pillow
python3 launch_txd_workshop.py
```

## Features
- Open TXD (PC, Xbox, PS2, mobile), XTX, CHK and mobile texture databases.
- View normal, alpha, split and overlay; checkerboard and tiled preview.
- Import / export PNG and other formats, rename, duplicate, copy / paste textures.
- Convert format, compress / uncompress (DXT1/3/5), bit depth, resize, AI upscale.
- Mipmap and bumpmap managers; flip, rotate, filters, paint editor (DP5).
- Save as TXD with version selector; build TXD from DFF materials.
- Ribbon Manager: move buttons, presets, custom icons from icons/.
- Drag and drop .txd, .img or image files onto the window.

## Code layout
| File | Job |
|------|-----|
| apps/components/Txd_Editor/txd_workshop.py | Init, settings, docking, help, theme, tabs |
| depends/txd_win_func.py | Frameless window drag, resize, window menus |
| depends/txd_ui_func.py | Panels, ribbons, fonts, icons, view modes, hotkeys |
| depends/txd_logic_func.py | Load/save, texture edits, import/export, mipmaps, bumpmaps |
| apps/methods/txd_dialogs.py | Bumpmap, mipmap, properties, preview windows |
| apps/methods/txd_dxt_encode.py | DXT1/DXT5 encoders |
| apps/methods/ribbon_dialog.py | Ribbon Manager and custom icons |
| apps/methods/grip_splitter.py | Grip splitter, saved pane sizes |

X-Seti - IMG Factory 1.6
