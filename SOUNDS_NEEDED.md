# Sounds Needed for Council of Chalcedon

This document lists all audio assets needed for the visual novel. All audio should be in OGG format for best Ren'Py compatibility.

---

## Music Tracks

Place in `game/audio/music/`. These should be loopable background tracks, ideally 2-4 minutes each.

### Main Theme

**Filename:** `main_theme.ogg`
**Used in:** Title screen, Prologue opening, Credits
**Mood:** Solemn, reverent, Byzantine
**Description:** The signature sound of the game. Should evoke 5th century Eastern Christianity - think Byzantine chant influence, modal harmonies, perhaps drone notes with melodic lines above.
**Instruments:** Choir (male voices preferred), strings, perhaps organ or reed instruments
**Tempo:** Slow to moderate
**Reference style:** Byzantine liturgical music, Arvo Pärt, Hildegard von Bingen

---

### Tension

**Filename:** `tension.ogg`
**Used in:** Robber Council narration (Prologue), Session III (Dioscorus's judgment)
**Mood:** Ominous, building unease, conflict
**Description:** Underscores moments of ecclesiastical conflict and impending judgment. The Robber Council of 449 where Flavian was beaten to death, and the trial of Dioscorus.
**Instruments:** Low strings (cello, bass), sparse percussion, dissonant harmonies
**Tempo:** Slow, deliberate
**Reference style:** Film score tension music, Ligeti-influenced textures

---

### Triumph

**Filename:** `triumph.ogg`
**Used in:** Session II when bishops acclaim Leo's Tome ("Peter has spoken through Leo!")
**Mood:** Majestic, victorious, exultant
**Description:** The climactic moment when the council recognizes the orthodox faith. Should feel like a moment of spiritual triumph and unity.
**Instruments:** Brass (horns, trumpets), choir, full strings, timpani
**Tempo:** Moderate to fast, building energy
**Reference style:** Handel's coronation anthems, Orthodox liturgical climaxes

---

### Solemn

**Filename:** `solemn.ogg`
**Used in:** Turning point narration (Prologue), after Dioscorus's deposition (Session III), Definition reading (Epilogue)
**Mood:** Reflective, contemplative, bittersweet
**Description:** For moments of quiet gravity - deaths, consequences, theological reflection. Not sad, but weighty.
**Instruments:** Solo cello or viola, sparse piano, perhaps solo voice
**Tempo:** Very slow
**Reference style:** Górecki Symphony No. 3, Tavener

---

### Imperial

**Filename:** `imperial.ogg`
**Used in:** Council begins (Prologue), Session VI (Emperor Marcian arrives)
**Mood:** Regal, authoritative, Byzantine court
**Description:** The presence of imperial power. Marcian and Pulcheria represent the Christian Roman Empire at its height.
**Instruments:** Brass fanfares, percussion (cymbals, drums), strings, possibly Byzantine-style reed instruments
**Tempo:** Moderate, stately
**Reference style:** Byzantine court music reconstructions, Roman triumph music

---

### Aftermath

**Filename:** `aftermath.ogg`
**Used in:** Epilogue opening (legacy and consequences)
**Mood:** Melancholic, reflective, elegiac
**Description:** The council is over, but its consequences ripple through centuries. Egypt rejects Chalcedon. The seeds of schism are planted.
**Instruments:** Solo instruments (cello, oud, or duduk), minimal accompaniment
**Tempo:** Very slow
**Reference style:** Middle Eastern lament music, Armenian duduk pieces

---

## Sound Effects

Place in `game/audio/sfx/`. These should be short, one-shot sounds.

### Crowd Sounds

**Filename:** `crowd_murmur.ogg`
**Used in:** Prologue (bishops assembling), Session II opening
**Duration:** 5-10 seconds (can loop or fade)
**Description:** The low murmur of hundreds of bishops in conversation before proceedings begin. Should sound like a large indoor space with male voices.
**Notes:** Not chaotic - dignified murmuring, perhaps some Greek phrases audible

---

**Filename:** `crowd_acclaim.ogg`
**Used in:** Session II (acclaiming Leo), Session III (affirming judgment), Session VI (greeting Emperor)
**Duration:** 3-5 seconds
**Description:** Bishops shouting acclamations in unison. "Axios!" (Greek for "He is worthy!") was the traditional acclamation. Should sound like organized, ritual shouting rather than a mob.
**Notes:** Male voices, possibly with some Greek words like "Axios!" or "Anathema!"

---

### Procedural Sounds

**Filename:** `gavel_strike.ogg`
**Used in:** Session III (sentence pronounced)
**Duration:** 1-2 seconds
**Description:** A sharp strike to call order or mark a formal pronouncement. Could be wood on wood, or a staff striking the floor.
**Notes:** Clean, authoritative sound with some reverb (large stone church)

---

**Filename:** `bell_toll.ogg`
**Used in:** Optional - session beginnings, solemn moments
**Duration:** 3-5 seconds (including decay)
**Description:** A church bell tolling. Byzantine/Eastern style if possible (different timbre from Western bells).
**Notes:** Single toll with long reverb tail

---

### Religious Sounds

**Filename:** `chant_kyrie.ogg`
**Used in:** Epilogue (final words before Definition quote)
**Duration:** 10-20 seconds
**Description:** A fragment of Byzantine chant - ideally the Kyrie eleison ("Lord, have mercy"). Male voices in the Eastern Orthodox style.
**Notes:** Can be a cappella or with ison (drone). Greek text preferred.

---

### Document/Object Sounds

**Filename:** `scroll_unroll.ogg`
**Used in:** Session II (Leo's Tome being read)
**Duration:** 2-3 seconds
**Description:** The sound of a parchment scroll being unrolled. Subtle crackling of old paper/vellum.
**Notes:** Should sound authentic to the period - no modern paper sounds

---

### Movement Sounds

**Filename:** `footsteps_marble.ogg`
**Used in:** Optional - character entrances
**Duration:** 3-5 seconds (several steps)
**Description:** Footsteps on marble or stone floor. The council met in a Byzantine church with stone floors.
**Notes:** Sandals or soft leather shoes, not modern hard-soled shoes

---

## Audio Sources

### Royalty-Free Music Libraries
- **Epidemic Sound** - High quality, subscription model
- **Artlist** - Film/game quality, subscription
- **Pond5** - Pay per track
- **AudioJungle** - Budget option

### Free/Creative Commons
- **FreeSound.org** - Excellent for sound effects (check individual licenses)
- **Musopen** - Public domain classical recordings
- **IMSLP** - Public domain scores (need performers)
- **Incompetech** - Kevin MacLeod's royalty-free music

### AI-Generated (Check Licensing)
- **Suno** - AI music generation
- **Udio** - AI music generation
- **Note:** Verify commercial use rights before distribution

### Authentic Byzantine Music
- **Cappella Romana** - Recordings of Byzantine chant
- **The Choir of the Greek Cathedral** recordings
- **Note:** Most commercial recordings are copyrighted

---

## File Structure

```
game/audio/
├── music/
│   ├── main_theme.ogg
│   ├── tension.ogg
│   ├── triumph.ogg
│   ├── solemn.ogg
│   ├── imperial.ogg
│   └── aftermath.ogg
└── sfx/
    ├── crowd_murmur.ogg
    ├── crowd_acclaim.ogg
    ├── gavel_strike.ogg
    ├── bell_toll.ogg
    ├── chant_kyrie.ogg
    ├── scroll_unroll.ogg
    └── footsteps_marble.ogg
```

---

## Priority Order

### Must Have (Core Experience)
1. `main_theme.ogg` - Sets the tone for the entire game
2. `tension.ogg` - Key dramatic moments
3. `triumph.ogg` - The climactic "Peter has spoken through Leo" scene
4. `crowd_acclaim.ogg` - Used in multiple key scenes

### Should Have (Enhanced Experience)
5. `solemn.ogg` - Reflective moments
6. `imperial.ogg` - Emperor's arrival
7. `crowd_murmur.ogg` - Ambient atmosphere
8. `scroll_unroll.ogg` - Leo's Tome reading

### Nice to Have (Complete Experience)
9. `aftermath.ogg` - Epilogue mood
10. `chant_kyrie.ogg` - Final spiritual moment
11. `gavel_strike.ogg` - Punctuation for judgment
12. `bell_toll.ogg` - Optional atmosphere
13. `footsteps_marble.ogg` - Optional movement sounds

---

## Technical Specifications

| Property | Requirement |
|----------|-------------|
| Format | OGG Vorbis (preferred) or MP3 |
| Sample Rate | 44.1 kHz |
| Bit Depth | 16-bit |
| Channels | Stereo for music, Mono acceptable for SFX |
| Music Length | 2-4 minutes, loopable |
| SFX Length | 1-10 seconds |

---

## Audio Cues Already Implemented

The following scripts already have audio cues coded in:

| Script | Music | Sound Effects |
|--------|-------|---------------|
| `prologue.rpy` | main_theme, tension, solemn, imperial | crowd_murmur |
| `session_02.rpy` | solemn, triumph | crowd_murmur, scroll_unroll, crowd_acclaim |
| `session_03.rpy` | tension, solemn | gavel_strike, crowd_acclaim |
| `session_06.rpy` | imperial | crowd_acclaim |
| `epilogue.rpy` | aftermath, solemn, main_theme | chant_kyrie |

The game will run without audio files (Ren'Py handles missing audio gracefully), but you'll see warnings in the console.

---

## Recommended Tracks

Based on research, here are specific tracks to download for each audio slot.

### Music Tracks

| Slot | Recommended Track | Source | License | Notes |
|------|-------------------|--------|---------|-------|
| **main_theme** | "Balefire" | [Scott Buckley](https://www.scottbuckley.com.au/library/) | CC BY 4.0 | Dark, brooding, gothic folk - builds with medieval atmosphere. Perfect Byzantine feel. |
| **tension** | "Eyes In The Void" | [Scott Buckley](https://www.scottbuckley.com.au/library/) | CC BY 4.0 | Dark, chaotic orchestral descending into gothic march. Ideal for Robber Council. |
| **triumph** | "Hyperion" | [Scott Buckley](https://www.scottbuckley.com.au/library/) | CC BY 4.0 | Epic, uplifting with brass fanfare and ethereal male vocals. Perfect for "Peter has spoken through Leo!" |
| **solemn** | "The Great Sea" | [Scott Buckley](https://www.scottbuckley.com.au/library/) | CC BY 4.0 | Opens with solo cello, builds emotionally. Grand and sweeping but contemplative. |
| **imperial** | "Song Of The Forge" | [Scott Buckley](https://www.scottbuckley.com.au/library/) | CC BY 4.0 | Epic war march with full orchestra and dramatic choir. Regal and powerful. |
| **aftermath** | "Shoulders Of Giants" | [Scott Buckley](https://www.scottbuckley.com.au/library/) | CC BY 4.0 | Slow-paced, majestic, bittersweet. Perfect for reflecting on legacy. |

**Alternative options from Pixabay (no attribution required):**

| Slot | Recommended Track | Source | Notes |
|------|-------------------|--------|-------|
| **main_theme** | "Solemn Gregorian Chant of a Latin Private Prayer" | [Pixabay](https://pixabay.com/music/search/solemn/) | Authentic chant feel, 1:33 |
| **solemn** | "Lament for a Mentor - Solemn Instrumental" | [Pixabay](https://pixabay.com/music/search/solemn/) | 3:48, melancholic orchestral |
| **aftermath** | "Melancholic Classical Music - Longing Heart" | [Pixabay](https://pixabay.com/music/search/melancholic%20orchestral/) | By Sonican, 2:02 |

### Sound Effects

| Slot | Recommended Track | Source | License | Direct Link |
|------|-------------------|--------|---------|-------------|
| **crowd_murmur** | "Cathedral church background pack 1" | Freesound | CC BY 3.0 | [klankbeeld](https://freesound.org/people/klankbeeld/packs/10638/) |
| **crowd_acclaim** | "Crowd Murmur" pack | Freesound | CC0 | [SpliceSound](https://freesound.org/people/SpliceSound/packs/15946/) - use louder portions |
| **gavel_strike** | "Gavel - 3 Strikes with room reverb" | Freesound | CC BY 3.0 | [odditonic](https://freesound.org/people/odditonic/sounds/187705/) - extract single strike |
| **bell_toll** | "Orthodox Church Bell Ringing" | Freesound | CC BY 4.0 | [newlocknew](https://freesound.org/people/newlocknew/sounds/717963/) - extract single toll |
| **scroll_unroll** | "Unrolling And Rolling Map.wav" | Freesound | CC BY 4.0 | [Benboncan](https://freesound.org/people/Benboncan/sounds/77319/) |
| **chant_kyrie** | "Byzantine Chant.wav" | Freesound | CC BY 3.0 | [RTB45](https://freesound.org/people/RTB45/sounds/157294/) - field recording from cathedral |

### Additional Byzantine Chant Sources

| Source | Description | Link |
|--------|-------------|------|
| **Internet Archive** | "Ecclesiastical Byzantine Hymns" - free download | [Archive.org](https://archive.org/details/Ecclesiastical_Byzantine_Hymns) |
| **Pixabay** | Byzantine chant search - no attribution | [Pixabay](https://pixabay.com/music/search/byzantine%20chant/) |
| **Creazilla** | 6 Byzantine audio tracks, public domain | [Creazilla](https://creazilla.com/search/audio/byzantine%20music) |

---

## Download Instructions

### Scott Buckley (Recommended for Music)

1. Go to [scottbuckley.com.au/library](https://www.scottbuckley.com.au/library/)
2. Use genre filter: "Orchestral"
3. Click track name to preview
4. Download MP3 or WAV
5. Convert to OGG using Audacity or ffmpeg:
   ```bash
   ffmpeg -i input.mp3 -c:a libvorbis -q:a 6 output.ogg
   ```
6. **Credit required:** "Music by Scott Buckley - www.scottbuckley.com.au"

### Freesound (Recommended for SFX)

1. Create free account at [freesound.org](https://freesound.org)
2. Search or use direct links above
3. Download WAV files
4. Trim/edit in Audacity if needed
5. Export as OGG
6. Check individual license for attribution requirements

### Pixabay (No Attribution Alternative)

1. Go to [pixabay.com/music](https://pixabay.com/music/)
2. Search by mood/genre
3. Download MP3 directly
4. Convert to OGG
5. No attribution required under Pixabay License

---

## Quick Start Script

Run this to download and convert all Freesound SFX (requires freesound-client):

```bash
# Create directories
mkdir -p game/audio/music game/audio/sfx

# Manual downloads needed - Freesound requires login
# After downloading WAV files to ~/Downloads, convert:

cd ~/Downloads
for f in *.wav; do
    ffmpeg -i "$f" -c:a libvorbis -q:a 6 "${f%.wav}.ogg"
done

# Move to project
mv *.ogg /path/to/game/audio/sfx/
```

---

## Attribution Template

If using CC BY licensed tracks, add this to your game credits:

```
MUSIC
"Balefire" by Scott Buckley - www.scottbuckley.com.au
"Eyes In The Void" by Scott Buckley - www.scottbuckley.com.au
"Hyperion" by Scott Buckley - www.scottbuckley.com.au
"The Great Sea" by Scott Buckley - www.scottbuckley.com.au
"Song Of The Forge" by Scott Buckley - www.scottbuckley.com.au
"Shoulders Of Giants" by Scott Buckley - www.scottbuckley.com.au

SOUND EFFECTS
Sounds from Freesound.org:
- "Cathedral church background" by klankbeeld
- "Gavel strikes" by odditonic
- "Orthodox Church Bell" by newlocknew
- "Unrolling Map" by Benboncan
- "Byzantine Chant" by RTB45
```
