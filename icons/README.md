#this belongs in icons/README.md - Version: 1
# X-Seti - September30 2026 - TXD Workshop - Icons

# TXD Workshop Icons

The app draws all icons as SVG (apps/methods/imgfactory_svg_icons.py).
This folder is for community PNG / JPG / SVG replacements.
Apply one: Ribbon Manager, select an action, Set Icon... (Reset Icon restores the SVG).
Choices save in txd_workshop.json and in ribbon presets.

## Wanted
Colourful 3ds Max style icons.

## Format
- PNG with transparency (JPG accepted), 64x64 master, also 32x32 and 20x20 if possible.
- File name = action name below, e.g. `generate_alpha_64.png`.
- Readable on light and dark themes.

## Priority: actions sharing an icon
| File name | Ribbon | Action | Current SVG |
|-----------|--------|--------|-------------|
| flip_vertical | Transform | Flip Vertical | flip_vert_icon |
| create | Transform | Create | add_icon |
| delete | Transform | Delete | delete_icon |
| paint | Transform | Paint | paint_icon |
| build_from_dff | Transform | Build from DFF | build_icon |
| switch | Transform | Switch | flip_vert_icon |
| invert_alpha | Transform | Invert Alpha | build_icon |
| generate_alpha | Transform | Generate Alpha | paint_icon |
| resize_texture | Navigation | Resize Texture | _resize_icon |
| black_background | Effects | Black Background | settings_icon |
| white_background | Effects | White Background | settings_icon |
| resize_texture | Format | Resize Texture | _resize_icon |
| import | Format | Import | import_icon |
| export | Format | Export | export_icon |
| generate_mipmaps | Mipmaps | Generate Mipmaps | add_icon |
| remove_mipmaps | Mipmaps | Remove Mipmaps | delete_icon |
| export_bumpmap | Mipmaps | Export Bumpmap | export_icon |
| import_bumpmap | Mipmaps | Import Bumpmap | import_icon |

## Other ribbon actions
| File name | Ribbon | Action | Current SVG |
|-----------|--------|--------|-------------|
| flip_horizontal | Transform | Flip Horizontal | flip_horz_icon |
| rotate_cw | Transform | Rotate CW | rotate_cw_icon |
| rotate_ccw | Transform | Rotate CCW | rotate_ccw_icon |
| copy | Transform | Copy | copy_icon |
| paste | Transform | Paste | paste_icon |
| duplicate | Transform | Duplicate | duplicate_icon |
| check_dff | Transform | Check DFF | analyze_icon |
| filters | Transform | Filters | filter_icon |
| properties | Transform | Properties | properties_icon |
| zoom_in | Navigation | Zoom In | zoom_in_icon |
| zoom_out | Navigation | Zoom Out | zoom_out_icon |
| reset_view | Navigation | Reset View | reset_icon |
| fit_to_window | Navigation | Fit to Window | fit_icon |
| pan_up | Navigation | Pan Up | arrow_up_icon |
| pan_down | Navigation | Pan Down | arrow_down_icon |
| pan_left | Navigation | Pan Left | arrow_left_icon |
| pan_right | Navigation | Pan Right | arrow_right_icon |
| pick_background | Navigation | Pick Background | color_picker_icon |
| colour_adjustments | Effects | Colour Adjustments... | knob_icon |
| seamless_tool | Effects | Seamless Tool... | seamless_icon |
| snow_effect | Effects | Snow Effect... | snow_icon |
| alpha_coverage | Effects | Alpha Coverage... | alpha_coverage_icon |
| checkerboard | Effects | Checkerboard | checkerboard_icon |
| change_bit_depth | Format | Change Bit Depth | _bitdepth_icon |
| ai_upscale | Format | AI Upscale | _upscale_icon |
| compress | Format | Compress | compress_icon |
| uncompress | Format | Uncompress | uncompress_icon |
| convert_format | Format | Convert Format | convert_icon |
| view_mipmaps | Mipmaps | View Mipmaps | view_icon |
| manage_bumpmaps | Mipmaps | Manage Bumpmaps | manage_icon |
