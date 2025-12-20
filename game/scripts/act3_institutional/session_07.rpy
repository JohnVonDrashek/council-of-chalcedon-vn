## Council of Chalcedon - Session VII
## October 26, 451 AD
## Antioch and Jerusalem

label session_07:

    # Track progress
    call after_session(7)

    # Session card
    call screen session_card("VII", "October 26, 451 AD", "Antioch and Jerusalem")

    scene bg council_hall with fade

    narrator_doc "With the doctrinal crisis resolved, the council addressed jurisdictional disputes."
    narrator_doc "The most pressing: the rivalry between Antioch and Jerusalem."

    nvl clear

    narrator_doc "Antioch was one of the ancient patriarchates."
    narrator_doc "Saint Peter himself had been bishop there before going to Rome."
    narrator_doc "Its jurisdiction extended over much of the East."

    nvl clear

    narrator_doc "But Jerusalem was the Holy City."
    narrator_doc "Christ had died and risen there."
    narrator_doc "Its bishop, Juvenal, sought independence from Antioch."
    narrator_doc "He wanted his own patriarchate."

    nvl clear

    window hide dissolve

    show florentius at center
    with dissolve

    commissioners "Let Maximus the most holy bishop of the city of Antioch and Juvenal the most holy bishop of Jerusalem come to the midst and make known to us what points of jurisdiction they have contended about."

    hide florentius with dissolve

    window hide dissolve

    narrator_doc "Both bishops came forward."
    narrator_doc "They had been negotiating privately."
    narrator_doc "Now they presented their agreement to the council."

    nvl clear

    window hide dissolve

    show maximus at left
    show juvenal at right
    with dissolve

    maximus "We have reached an agreement between ourselves concerning the boundaries of our jurisdictions."

    juvenal "We have divided the provinces according to what seems just and ancient custom."

    hide maximus
    hide juvenal
    with dissolve

    # The settlement
    narrator_doc "The council confirmed their agreement."

    nvl clear

    show florentius at center
    with dissolve

    commissioners "The arrangement arrived at through the agreement of the most holy Maximus, the bishop of the city of Antioch, and of the most holy Juvenal, the bishop of Jerusalem, shall remain firm for ever."

    commissioners "The most holy bishop Maximus, or rather the most holy church of Antioch, shall have under its own jurisdiction the two Phoenicias and Arabia."

    commissioners "The most holy Juvenal, bishop of Jerusalem, or rather the most holy Church which is under him, shall have under his own power the three Palestines."

    hide florentius with dissolve

    window hide dissolve

    narrator_doc "Jerusalem thus became an independent patriarchate."
    narrator_doc "It was a momentous decision."
    narrator_doc "The ancient structure of the Church was being reshaped."

    nvl clear

    bishops "This is just! This is fitting!"

    bishops "Let peace reign between the sees!"

    window hide dissolve

    narrator_doc "Similar disputes would occupy the remaining sessions."
    narrator_doc "The council would adjudicate between rival bishops, restore those wrongly condemned, and establish the framework of Church governance for centuries to come."

    nvl clear

    pause 1.0

    jump sessions_08_11
