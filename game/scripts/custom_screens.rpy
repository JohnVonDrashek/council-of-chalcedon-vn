## Council of Chalcedon - Custom Screens

# ============================================
# CUSTOM STYLES
# ============================================

style parchment_vscrollbar:
    base_bar Solid("#c4a478")
    thumb Solid("#6a4a28")
    hover_thumb Solid("#8a6a48")
    bar_vertical True
    bar_invert True
    unscrollable "hide"

# ============================================
# SESSION CARD SCREEN
# Displays title cards between sessions
# ============================================

screen session_card(session_num, date, subtitle=""):
    modal True

    # Dark background overlay
    add Solid("#000000cc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 300
        padding (60, 40)
        background Frame("images/ui/glossary_bg.png", 20, 20)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "SESSION [session_num]":
                size 48
                color "#3a2a18"
                xalign 0.5

            text date:
                size 32
                color "#5a4a38"
                xalign 0.5

            if subtitle:
                text subtitle:
                    size 24
                    color "#6a5a48"
                    xalign 0.5
                    text_align 0.5

    timer 3.5 action Return()

# ============================================
# DOCUMENT READER SCREEN
# For presenting Leo's Tome, Creeds, etc.
# ============================================

screen document_reader(title, content, source_note=""):
    modal True

    # Dark background overlay
    add Solid("#000000dd")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 850
        padding (110, 100)
        background Frame("images/ui/document_frame.png", 30, 30)

        vbox:
            xalign 0.5
            spacing 20

            null height 5

            text title:
                size 36
                color "#2a1a08"
                xalign 0.5
                text_align 0.5

            viewport:
                scrollbars "vertical"
                mousewheel True
                xsize 800
                ysize 380
                xalign 0.5
                style_prefix "parchment"

                text content:
                    size 22
                    color "#1a1208"
                    line_spacing 8
                    text_align 0.5
                    xalign 0.5

            if source_note:
                text source_note:
                    size 14
                    color "#5a4a38"
                    xalign 0.5
                    text_align 0.5
                    italic True

            null height 20

            textbutton "Continue" action Return():
                xalign 0.5
                text_color "#3a2a18"
                text_hover_color "#6a4a28"

            null height 25

# ============================================
# CANON DISPLAY SCREEN
# For presenting the 30 canons
# ============================================

screen canon_display(canon_number, canon_text, canon_summary=""):
    modal True

    # Dark background overlay
    add Solid("#000000cc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 780
        ysize 820
        padding (120, 90)
        background Frame("images/ui/canon_scroll.png", 20, 20)

        vbox:
            xalign 0.5
            spacing 15

            null height 10

            text "Canon [canon_number]":
                size 36
                color "#3a2a18"
                xalign 0.5

            null height 5

            viewport:
                scrollbars "vertical"
                mousewheel True
                xsize 460
                ysize 420
                xalign 0.5
                style_prefix "parchment"

                vbox:
                    spacing 15

                    text canon_text:
                        size 22
                        color "#4a3a28"

                    if canon_summary:
                        null height 10

                        text "{i}In brief:{/i}":
                            size 18
                            color "#5a4a38"

                        text canon_summary:
                            size 20
                            color "#4a3a28"

            null height 20

            textbutton "Continue" action Return():
                xalign 0.5
                text_color "#3a2a18"
                text_hover_color "#6a4a28"

            null height 30

# ============================================
# THEOLOGICAL EXPLANATION SCREEN
# For explaining complex theological concepts
# ============================================

screen theology_explanation(title, points):
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 750
        ysize 520
        padding (50, 40)
        background Frame("images/ui/glossary_bg.png", 20, 20)

        # Title at top
        text title:
            size 32
            color "#3a2a18"
            xalign 0.5
            ypos 0

        # Scrollable content area in middle
        viewport:
            ypos 55
            xsize 630
            ysize 330
            scrollbars "vertical"
            mousewheel True
            style_prefix "parchment"

            vbox:
                spacing 12
                for point in points:
                    text point:
                        size 22
                        color "#4a3a28"

        # Button at bottom
        textbutton "Continue" action Return():
            xalign 0.5
            ypos 400
            text_color "#3a2a18"
            text_hover_color "#6a4a28"

# ============================================
# PROGRESS DISPLAY
# Shows how much of the council has been viewed
# ============================================

screen progress_display():
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -10
        yoffset 10
        padding (15, 10)
        background "#1a1a1aaa"

        vbox:
            text "Council Progress":
                size 16
                color "#d4c4a8"

            $ sessions_count = len(persistent.sessions_viewed) if persistent.sessions_viewed else 0
            $ canons_count = len(persistent.canons_read) if persistent.canons_read else 0

            text "Sessions: [sessions_count]/15":
                size 14
                color "#a0a0a0"

            text "Canons: [canons_count]/30":
                size 14
                color "#a0a0a0"

# ============================================
# ACCLAMATION SCREEN
# For dramatic collective proclamations
# ============================================

screen acclamation(text_content):
    modal True

    # Dark background overlay
    add Solid("#000000cc")

    # Decorative frame
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 250
        padding (60, 40)
        background Frame("images/ui/document_frame.png", 20, 20)

        text text_content:
            xalign 0.5
            yalign 0.5
            font "fonts/Cinzel-Bold.ttf"
            size 42
            color "#2a1a08"
            text_align 0.5

    timer 3.5 action Return()
