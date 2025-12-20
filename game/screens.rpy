## Ren'Py Default Screens

init offset = -1

## Styles
style default:
    font gui.text_font
    size gui.text_size
    color gui.text_color

style input:
    color gui.accent_color
    adjust_spacing False

style hyperlink_text:
    color gui.accent_color
    hover_underline True

style gui_text:
    font gui.interface_text_font
    color gui.interface_text_color
    size gui.interface_text_size

style button:
    padding gui.button_borders.padding

style button_text is gui_text:
    yalign 0.5

style label_text is gui_text:
    size gui.label_text_size
    color gui.accent_color

style prompt_text is gui_text:
    color gui.text_color

style vbar:
    xsize gui.bar_size
    base_bar Solid(gui.muted_color)
    thumb Solid(gui.accent_color)

style bar:
    ysize gui.bar_size
    base_bar Solid(gui.muted_color)
    thumb Solid(gui.accent_color)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Solid(gui.muted_color)
    thumb Solid(gui.accent_color)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Solid(gui.muted_color)
    thumb Solid(gui.accent_color)

style vslider:
    xsize gui.slider_size
    base_bar Solid(gui.muted_color)
    thumb Solid(gui.accent_color)

style slider:
    ysize gui.slider_size
    base_bar Solid(gui.muted_color)
    thumb Solid(gui.accent_color)

## Say Screen
screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Solid("#1a1a1acc")

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background None
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    text_align gui.dialogue_text_xalign
    layout ("subtitle" if gui.dialogue_text_xalign else "tex")

## Input Screen
screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default
style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

## Choice Screen
screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    xsize gui.choice_button_width
    padding gui.choice_button_borders.padding
    background Solid("#2a2a2a")
    hover_background Solid("#3a3a3a")

style choice_button_text is default:
    xalign gui.choice_button_text_xalign
    color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color
    insensitive_color gui.choice_button_text_insensitive_color

## NVL Screen
screen nvl(dialogue, items=None):
    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        vpgrid:
            cols 1
            yinitial 1.0
            scrollbars "vertical"
            mousewheel True
            draggable True
            side_xalign 0.5

            use nvl_dialogue(dialogue)

        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:
                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

style nvl_window is default:
    xfill True
    yfill True
    background Solid("#1a1a1ab0")  # Semi-transparent to show scene backgrounds
    padding gui.nvl_borders.padding

style nvl_entry is default:
    xfill True
    ysize gui.nvl_height

style nvl_label is say_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue is say_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

## Quick Menu
screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Prefs") action ShowMenu('preferences')

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    background None
    padding (15, 6, 15, 0)

style quick_button_text:
    size 21
    idle_color gui.idle_small_color
    hover_color gui.hover_color
    selected_color gui.accent_color
    insensitive_color gui.insensitive_color

## Navigation
screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"

style navigation_button_text:
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color

## Main Menu
screen main_menu():
    tag menu
    add gui.main_menu_background

    frame:
        style "main_menu_frame"

    use navigation

    text "{size=72}Council of Chalcedon{/size}":
        xalign 0.5
        ypos 100
        color gui.accent_color

    text "The Fourth Ecumenical Council (451 AD)":
        xalign 0.5
        ypos 200
        size 28
        color gui.idle_color

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True
    background Solid("#1a1a1a")

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    xalign 1.0

style main_menu_title:
    size gui.title_text_size

## Game Menu
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_xalign 0.5

                        vbox:
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_xalign 0.5

                        transclude

                else:
                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"
        action Return()

    label title

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text
style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background gui.game_menu_background

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

## Preferences Screen
screen preferences():
    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    padding (6, 6, 6, 6)

style radio_button_text:
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    padding (6, 6, 6, 6)

style check_button_text:
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color

style slider_slider:
    xsize 525

style slider_button:
    yalign 0.5
    left_margin 15

style slider_button_text:
    idle_color gui.idle_color
    hover_color gui.hover_color

style slider_vbox:
    xsize 675

## History Screen
screen history():
    tag menu

    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:
            window:
                has fixed:
                    yfit True

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")

style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

## Save and Load Screens
screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):
        fixed:
            order_reverse True

            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            grid 3 3:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(3 * 3):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()
                key "save_page_prev" action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()
                key "save_page_next" action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    padding (15, 6, 15, 6)

style page_button_text:
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color

style slot_button:
    xsize gui.slot_button_width
    ysize gui.slot_button_height
    padding gui.slot_button_borders.padding
    background Solid("#2a2a2a")
    hover_background Solid("#3a3a3a")

style slot_button_text:
    size gui.slot_button_text_size
    xalign gui.slot_button_text_xalign
    idle_color gui.slot_button_text_idle_color
    hover_color gui.hover_color
    selected_idle_color gui.slot_button_text_selected_idle_color
    selected_hover_color gui.slot_button_text_selected_hover_color

style slot_time_text:
    size 21

style slot_name_text:
    size 21

## Confirm Screen
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add Solid("#000000aa")

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Solid("#1a1a1aee")
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    padding (60, 15, 60, 15)
    background Solid("#2a2a2a")
    hover_background Solid("#3a3a3a")

style confirm_button_text:
    size 30

## Skip Indicator
screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 9
            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Solid("#1a1a1a")
    padding (24, 8, 36, 8)

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    font "DejaVuSans.ttf"

## Notify Screen
screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    background Solid("#1a1a1a")
    padding (24, 8, 60, 8)

style notify_text:
    size gui.notify_text_size

## NVL Screen Bubble
screen nvl_bubble(dialogue):
    for d in dialogue:
        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:
                    text d.who:
                        id d.who_id
                        style "bubble_namebox_label"

                text d.what:
                    id d.what_id
                    style "bubble_say_dialogue"
