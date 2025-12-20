## Council of Chalcedon - Audio Definitions
## Music tracks and sound effects

# ============================================
# MUSIC TRACKS
# ============================================

# Main theme - solemn Byzantine chant feel
define audio.main_theme = "audio/music/main_theme.ogg"

# Tension - low strings, building unease for conflicts
define audio.tension = "audio/music/tension.ogg"

# Triumph - majestic brass/choir for acclamations
define audio.triumph = "audio/music/triumph.ogg"

# Solemn - reflective, sparse for contemplative moments
define audio.solemn = "audio/music/solemn.ogg"

# Imperial - regal Byzantine court music
define audio.imperial = "audio/music/imperial.ogg"

# Aftermath - melancholic for epilogue
define audio.aftermath = "audio/music/aftermath.ogg"

# ============================================
# SOUND EFFECTS
# ============================================

# Crowd sounds
define audio.crowd_murmur = "audio/sfx/crowd_murmur.ogg"
define audio.crowd_acclaim = "audio/sfx/crowd_acclaim.ogg"

# Council procedural sounds
define audio.gavel_strike = "audio/sfx/gavel_strike.ogg"
define audio.bell_toll = "audio/sfx/bell_toll.ogg"

# Religious sounds
define audio.chant_kyrie = "audio/sfx/chant_kyrie.ogg"

# Document/object sounds
define audio.scroll_unroll = "audio/sfx/scroll_unroll.ogg"

# Movement sounds
define audio.footsteps_marble = "audio/sfx/footsteps_marble.ogg"

# ============================================
# AUDIO CONFIGURATION
# ============================================

# Music channel configuration
init python:
    # Set default music fade time
    config.fade_music = 1.0

    # Allow music to continue across screens
    config.main_menu_music = "audio/music/main_theme.ogg"

# ============================================
# AUDIO HELPER LABELS
# ============================================

# Fade to silence
label audio_fade_out:
    stop music fadeout 2.0
    return

# Transition between tracks smoothly
label audio_crossfade(new_track):
    $ renpy.music.play(new_track, fadeout=1.5, fadein=1.5)
    return
