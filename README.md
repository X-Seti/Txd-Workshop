# TXD Workshop

Standalone TXD (texture dictionary) editor for GTA III, VC, SA and other RenderWare games, synced from IMG Factory 1.6.

## Run
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

X-Seti - IMG Factory 1.6
