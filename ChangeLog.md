#this belongs in root /ChangeLog.md - Txd-Workshop

## March 2026 — Sync from Img-Factory-1.6 Build 161

### SVG Icon system
- `imgfactory_svg_icons.py` updated with full icon set including
  sphere, box, mesh, col_workshop, txd_workshop icons
- Theme-aware colour support throughout

### Platform detection fixes
- D3D9/PSP device_id collision resolved
- PS2 platform detection no longer always shows "PC"
- Mobile files no longer misidentified as IMG archives

### TXD Parser updates
- Per-platform TXD parser modules (PC, Xbox, PS2, PSP, mobile)
- LC Android TXD parser (RW version 0x1005FFFF)
- GTA III PC D3D8 vs D3D9 header layout improvements
- PVRTC/ETC1 pixel decode stubs (native library required)

### UI improvements
- Panel collapse threshold system (settings slider)
- Button layout fixes — icon-only collapses correctly
- Centred text on buttons
- SVG icon methods updated throughout

### Bug fixes
- Bogus alpha validation dialogs removed
- LCS iOS load failure investigated
- IMG rebuild file size growth (ongoing)
- Missing method stubs added across codebase

### Shared infrastructure
- `img_core_classes.py` updated
- `img_factory_settings.py` — panel collapse threshold default 550
- `imgfactory_ui_settings.py` — settings dialog with QSlider
- `imgcol_exists.py` updated
