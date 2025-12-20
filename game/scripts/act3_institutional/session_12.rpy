## Council of Chalcedon - Session XII
## October 30, 451 AD
## The Dispute Over Ephesus

label session_12:

    # Track progress
    call after_session(12)

    # Session card
    call screen session_card("XII", "October 30, 451 AD", "The Dispute Over Ephesus")

    scene bg council_hall with fade

    narrator_doc "A dispute arose concerning the see of Ephesus."
    narrator_doc "Ephesus was a prestigious city - the place where the Council of 431 had condemned Nestorius."
    narrator_doc "It was also where the 'Robber Council' of 449 had taken place."

    nvl clear

    narrator_doc "Two bishops claimed the see."
    narrator_doc "Bassianus had been installed years ago but later expelled."
    narrator_doc "Stephen now held the position."
    narrator_doc "Who was the rightful bishop?"

    nvl clear

    window hide dissolve

    scene bg council_hall crowded with dissolve

    narrator "The council examined the evidence."
    narrator "Both men had been consecrated irregularly."
    narrator "The situation was a canonical nightmare."

    window hide dissolve

    narrator_doc "After lengthy deliberation, the council reached a Solomonic judgment:"
    narrator_doc "Neither Bassianus nor Stephen would be bishop of Ephesus."
    narrator_doc "Both would retain the title and honor of bishop."
    narrator_doc "Both would receive a pension from the revenues of Ephesus."
    narrator_doc "But a new bishop would be elected by proper canonical procedure."

    nvl clear

    bishops "This is just!"

    bishops "Let a new election be held!"

    bishops "Let order be restored!"

    window hide dissolve

    narrator_doc "The case illustrated a broader principle."
    narrator_doc "Canonical order mattered."
    narrator_doc "Even sincere men, improperly consecrated, could not simply be ratified."
    narrator_doc "The Church's procedures existed for good reason."

    nvl clear

    pause 1.0

    jump session_13
