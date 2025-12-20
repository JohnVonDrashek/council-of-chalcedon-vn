## Council of Chalcedon - Character Definitions

# ============================================
# NARRATOR CHARACTERS
# ============================================

# Documentary narrator (NVL mode, no name displayed)
define narrator_doc = Character(
    None,
    kind=nvl,
    what_color="#d4c4a8",
    what_size=28
)

# Contextual narrator for shorter ADV comments
define narrator = Character(
    None,
    what_color="#d4c4a8"
)

# ============================================
# ROMAN LEGATES (Gold - #c9a227)
# Representatives of Pope Leo I
# ============================================

define pasch = Character(
    "Paschasinus",
    color="#c9a227"
)

define lucentius = Character(
    "Lucentius",
    color="#c9a227"
)

define boniface = Character(
    "Boniface",
    color="#c9a227"
)

# ============================================
# ALEXANDRIAN FACTION (Dark Red - #8b0000)
# ============================================

define diosc = Character(
    "Dioscorus",
    color="#8b0000"
)

# ============================================
# CONSTANTINOPLE (Royal Blue - #4169e1)
# ============================================

define anatolius = Character(
    "Anatolius",
    color="#4169e1"
)

# ============================================
# IMPERIAL FIGURES (Purple - #9932cc)
# ============================================

define marcian = Character(
    "Emperor Marcian",
    color="#9932cc"
)

define pulcheria = Character(
    "Empress Pulcheria",
    color="#9932cc"
)

# Imperial commissioners - secular judges appointed by the Emperor
define commissioners = Character(
    "The Imperial Commissioners",
    color="#9932cc"
)

# ============================================
# OTHER MAJOR FIGURES
# ============================================

define eusebius = Character(
    "Eusebius of Dorylaeum",
    color="#2e8b57"
)

define maximus = Character(
    "Maximus of Antioch",
    color="#4682b4"
)

define juvenal = Character(
    "Juvenal of Jerusalem",
    color="#4682b4"
)

define theodoretus = Character(
    "Theodoretus",
    color="#6b8e23"
)

define ibas = Character(
    "Ibas of Edessa",
    color="#6b8e23"
)

# ============================================
# IMPERIAL OFFICIALS
# ============================================

define official = Character(
    "Imperial Secretary",
    color="#808080"
)

define judges = Character(
    "The Judges",
    color="#708090"
)

# ============================================
# COLLECTIVE VOICES
# ============================================

define bishops = Character(
    "The Bishops",
    color="#708090",
    what_italic=True
)

define egyptian_bishops = Character(
    "Egyptian Bishops",
    color="#cd853f"
)

define eastern_bishops = Character(
    "Eastern Bishops",
    color="#4682b4"
)

# ============================================
# DOCUMENT READERS
# ============================================

define reader = Character(
    "The Reader",
    color="#a0a0a0",
    what_italic=True
)

# Leo's Tome being read aloud
define leo_text = Character(
    "Leo's Tome",
    color="#ffd700",
    what_italic=True,
    what_size=26
)

# Creed readings
define creed = Character(
    "The Creed",
    color="#d4c4a8",
    what_italic=True
)

# ============================================
# TRANSFORMS
# ============================================

# Character scaling - scale down to fit screen nicely
transform character_scale:
    zoom 0.5
    yalign 1.0

# Position transforms for multiple characters
transform left_pos:
    zoom 0.5
    xalign 0.2
    yalign 1.0

transform center_pos:
    zoom 0.5
    xalign 0.5
    yalign 1.0

transform right_pos:
    zoom 0.5
    xalign 0.8
    yalign 1.0

transform far_left_pos:
    zoom 0.45
    xalign 0.05
    yalign 1.0

transform far_right_pos:
    zoom 0.45
    xalign 0.95
    yalign 1.0

# Background scaling - fill screen
transform bg_fill:
    xysize (1920, 1080)

# ============================================
# CHARACTER IMAGES
# ============================================

# Roman Legates - Gold
image paschasinus = Transform("images/characters/paschasinus.png", zoom=0.5)
image lucentius = Transform("images/characters/lucentius.png", zoom=0.5)
image boniface = Transform("images/characters/boniface.png", zoom=0.5)

# Alexandrian - Dark Red
image dioscorus = Transform("images/characters/dioscorus.png", zoom=0.5)
image dioscorus defiant = Transform("images/characters/dioscorus_defiant.png", zoom=0.5)

# Constantinople - Blue
image anatolius = Transform("images/characters/anatolius.png", zoom=0.5)

# Imperial - Purple
image marcian = Transform("images/characters/marcian.png", zoom=0.5)
image pulcheria = Transform("images/characters/pulcheria.png", zoom=0.5)

# Others
image eusebius = Transform("images/characters/eusebius.png", zoom=0.5)
image theodoretus = Transform("images/characters/theodoretus.png", zoom=0.5)
image maximus = Transform("images/characters/maximus.png", zoom=0.5)
image juvenal = Transform("images/characters/juvenal.png", zoom=0.5)
image ibas = Transform("images/characters/ibas.png", zoom=0.5)

# Imperial Officials
image florentius = Transform("images/characters/florentius.png", zoom=0.5)

# ============================================
# BACKGROUNDS
# Scale to fill 1920x1080 screen
# ============================================

image bg council_hall = Transform("images/backgrounds/bg_council_hall.png", xysize=(1920, 1080))
image bg council_hall crowded = Transform("images/backgrounds/bg_council_hall_crowded.png", xysize=(1920, 1080))
image bg throne_room = Transform("images/backgrounds/bg_throne_room.png", xysize=(1920, 1080))
image bg antechamber = Transform("images/backgrounds/bg_antechamber.png", xysize=(1920, 1080))
image bg alexandria = Transform("images/backgrounds/bg_alexandria.png", xysize=(1920, 1080))
image bg constantinople = Transform("images/backgrounds/bg_constantinople.png", xysize=(1920, 1080))
image bg rome = Transform("images/backgrounds/bg_rome.png", xysize=(1920, 1080))
image bg black = Solid("#000000")

# ============================================
# UI ELEMENTS
# ============================================

image ui glossary_bg = "images/ui/glossary_bg.png"
image ui canon_scroll = "images/ui/canon_scroll.png"
image ui document_frame = "images/ui/document_frame.png"

# ============================================
# DOCUMENTS
# ============================================

image doc leos_tome = "images/documents/leos_tome.png"
