## Council of Chalcedon - Sessions VIII-XI
## October 27-29, 451 AD
## Matters of Order

label sessions_08_11:

    # Track progress
    call after_session(8)
    call after_session(9)
    call after_session(10)
    call after_session(11)

    # Session card
    call screen session_card("VIII-XI", "October 27-29, 451 AD", "Matters of Order")

    scene bg council_hall with fade

    narrator_doc "The council continued its work of restoring order to the Church."
    narrator_doc "Bishops who had been wrongly condemned at the 'Robber Council' were rehabilitated."
    narrator_doc "Those who had signed under duress were granted forgiveness upon repentance."

    nvl clear

    narrator_doc "Session VIII"
    narrator_doc "The council restored bishops who had been unjustly deposed at Ephesus in 449."
    narrator_doc "Some had been condemned merely for opposing Dioscorus."
    narrator_doc "Others had been forced to sign documents against their conscience."

    nvl clear

    narrator_doc "Session IX"
    narrator_doc "The case of Ibas of Edessa was examined."
    narrator_doc "He had been accused of Nestorianism."
    narrator_doc "The council found his letter to Maris orthodox and restored him to his see."

    nvl clear

    narrator_doc "Session X"
    narrator_doc "The case of Theodoretus of Cyrrhus was heard."
    narrator_doc "He had been a friend of Nestorius and an opponent of Cyril."
    narrator_doc "His orthodoxy was questioned by many."

    nvl clear

    window hide dissolve

    scene bg council_hall crowded with dissolve

    show theodoretus at center
    with dissolve

    bishops "Let him anathematize Nestorius!"

    theodoretus "Anathema to Nestorius and to everyone who does not call the holy Virgin Mary Theotokos."

    theodoretus "Anathema to Nestorius and to everyone who divides the one Son into two."

    hide theodoretus with dissolve

    bishops "Theodoretus is worthy! Let him take his see!"

    window hide dissolve

    narrator_doc "Upon his anathema of Nestorius, Theodoretus was restored."
    narrator_doc "This restoration would later be contested."
    narrator_doc "The Second Council of Constantinople in 553 would condemn his writings against Cyril - though not Theodoretus himself."

    nvl clear

    narrator_doc "Session XI"
    narrator_doc "Further restorations and minor disputes were resolved."
    narrator_doc "The work of reconciliation continued."

    nvl clear

    pause 1.0

    jump session_12
