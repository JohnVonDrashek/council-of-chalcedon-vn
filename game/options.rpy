## Council of Chalcedon - Ren'Py Configuration

define config.name = _("Council of Chalcedon")
define config.version = "1.0.32"

define gui.show_name = True
define gui.about = _p("""
An educational kinetic novel re-enacting the Fourth Ecumenical Council (451 AD).

Based on the historical records from New Advent:
https://www.newadvent.org/fathers/3811.htm

This is not a game with choices - it is a documentary-style presentation
of one of the most important councils in Christian history.
""")

define build.name = "CouncilOfChalcedon"

## Sounds and music

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.main_menu_music = None

## Transitions

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

## Window behavior

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## NVL mode configuration (documentary narration)

define config.nvl_paged_rollback = True

## Save/Load configuration

define config.save_directory = "CouncilOfChalcedon-1704067200"
define config.window_icon = "gui/window_icon.png"

## Build configuration

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')

    # Application icons
    build.icon = "icon.png"
    build.windows_icon = "icon.ico"
    build.mac_icon = "icon.icns"
