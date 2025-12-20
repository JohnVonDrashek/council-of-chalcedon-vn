## Council of Chalcedon - Session XIII
## October 31, 451 AD
## Nicomedia and Nicaea

label session_13:

    # Track progress
    call after_session(13)

    # Session card
    call screen session_card("XIII", "October 31, 451 AD", "Nicomedia and Nicaea")

    scene bg council_hall with fade

    narrator_doc "Another jurisdictional dispute came before the council."
    narrator_doc "This one concerned two ancient cities: Nicomedia and Nicaea."

    nvl clear

    narrator_doc "Nicomedia had been the eastern capital under Diocletian."
    narrator_doc "Nicaea was famous as the site of the first ecumenical council in 325."
    narrator_doc "Both claimed metropolitan status."
    narrator_doc "Both wanted jurisdiction over the surrounding churches."

    nvl clear

    narrator_doc "The council examined the historical precedents."
    narrator_doc "Which city had held metropolitan rights?"
    narrator_doc "When had these rights been established?"
    narrator_doc "What did ancient custom prescribe?"

    nvl clear

    window hide dissolve

    scene bg council_hall crowded with dissolve

    show florentius at center
    with dissolve

    commissioners "The rights of Nicomedia as metropolitan shall be preserved."

    commissioners "Nicaea shall have the honor of its name but the jurisdiction belongs to Nicomedia."

    hide florentius with dissolve

    window hide dissolve

    narrator_doc "It was a characteristic Chalcedonian solution."
    narrator_doc "Honor was preserved for both parties."
    narrator_doc "But clear lines of authority were established."
    narrator_doc "Ambiguity was the enemy of good order."

    nvl clear

    pause 1.0

    jump sessions_14_15
