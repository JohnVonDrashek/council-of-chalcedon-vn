## Council of Chalcedon - Session VI
## October 25, 451 AD
## The Emperor Arrives

label session_06:

    # Track progress
    call after_session(6)

    # Session card
    call screen session_card("VI", "October 25, 451 AD", "The Emperor Arrives")

    # Imperial fanfare as the Emperor arrives
    play music imperial fadein 1.0

    scene bg throne_room with fade

    narrator_doc "For the first time, Emperor Marcian himself attended the council."
    narrator_doc "Beside him sat the Empress Pulcheria, whose piety had guided the empire back to orthodoxy."

    nvl clear

    narrator_doc "The bishops rose as the imperial couple entered."
    narrator_doc "Here was the power that had made this council possible."
    narrator_doc "Here was the authority that would enforce its decrees."

    nvl clear

    window hide dissolve

    show marcian at center
    with dissolve

    # The bishops acclaim the Emperor - from the Acts
    play sound crowd_acclaim

    bishops "Many years to our Emperor and Empress, the pious, the Christian!"

    bishops "May Christ whom you serve keep you!"

    bishops "These things are worthy of the faith! To the Priest, the Emperor!"

    bishops "You have straightened out the churches, victor of your enemies, teacher of the faith!"

    bishops "Many years to the pious Empress, the lover of Christ! Many years to her that is orthodox!"

    bishops "You have put down the heretics, you have kept the faith!"

    bishops "May hatred be far removed from your empire, and may your kingdom endure for ever!"

    pause 0.5

    hide marcian with dissolve

    narrator_doc "Marcian's presence was both ceremonial and political."
    narrator_doc "By attending in person, he gave the council the highest possible endorsement."
    narrator_doc "By invoking Constantine - who had presided at Nicaea - he claimed continuity with the first ecumenical council."

    nvl clear

    # The Definition is ratified
    scene bg council_hall crowded with dissolve

    narrator_doc "The Definition of Faith, drafted in Session V, was formally presented to the Emperor."
    narrator_doc "Marcian signed it, giving it the force of imperial law."

    nvl clear

    window hide dissolve

    show marcian at center
    with dissolve

    marcian "To the honour of the holy martyr Euphemia, and of your holiness, we decree that the city of Chalcedon, in which the synod of the holy faith has been held, shall have the honours of a metropolis."

    marcian "In name only giving it this honour, the proper dignity of the city of Nicomedia being preserved."

    hide marcian with dissolve

    play sound crowd_acclaim

    bishops "This is a just decree! Many years to the Emperor! Many years to the Empress!"

    window hide dissolve

    narrator_doc "With the Emperor's endorsement, the council turned to institutional matters."
    narrator_doc "Disputes between rival sees must be settled."
    narrator_doc "The canons governing Church discipline must be established."

    nvl clear

    pause 1.0

    jump session_07
