## Council of Chalcedon - Session I
## October 8, 451 AD
## The Judgment of Dioscorus

label session_01:

    # Track progress
    call after_session(1)

    # Session card
    call screen session_card("I", "October 8, 451 AD", "The Judgment of Dioscorus")

    scene bg council_hall crowded with fade

    # Documentary narration
    narrator_doc "The Church of Saint Euphemia was filled to capacity."
    narrator_doc "Imperial commissioners sat at the center, representing Emperor Marcian."
    narrator_doc "The Roman legates - Paschasinus, Lucentius, and Boniface - bore Pope Leo's instructions."
    narrator_doc "And there, among the Eastern bishops, sat Dioscorus of Alexandria."

    nvl clear

    # Transition to dramatized scene
    window hide dissolve

    show paschasinus at left
    with dissolve

    narrator "Paschasinus rose to speak."

    pasch "We received directions at the hands of the most blessed and apostolic bishop of the Roman city, which is the head of all the churches."

    pause 0.5

    pasch "Dioscorus is not to be allowed a seat in this assembly, but that if he should attempt to take his seat he is to be cast out."

    show dioscorus at right
    with dissolve

    pasch "This instruction we must carry out."

    pasch "If now your holiness so commands, let him be expelled - or else we leave."

    hide paschasinus with dissolve

    # The judges respond
    show florentius at left
    with dissolve

    commissioners "What special charge do you prefer against the most reverend bishop Dioscorus?"

    hide florentius with dissolve

    show paschasinus at left
    with dissolve

    pasch "Since he has come, it is necessary that objection be made to him."

    hide paschasinus with dissolve

    show florentius at left
    with dissolve

    commissioners "In accordance with what has been said, let the charge under which he lies be specifically made."

    hide florentius with dissolve

    show lucentius at left
    with dissolve

    lucentius "Let him give a reason for his judgment."

    lucentius "For he undertook to give sentence against one over whom he had no jurisdiction."

    pause 0.5

    lucentius "He dared to hold a synod without the authority of the Apostolic See, a thing which had never taken place nor can take place."

    hide lucentius with dissolve

    show paschasinus at left
    with dissolve

    pasch "We cannot go counter to the decrees of the most blessed and apostolic bishop, who governs the Apostolic See, nor against the ecclesiastical canons nor the patristic traditions."

    hide paschasinus with dissolve

    show florentius at left
    with dissolve

    commissioners "It is proper that you should set forth specifically in what he has gone astray."

    hide florentius with dissolve

    show lucentius at left
    with dissolve

    lucentius "We will not suffer so great a wrong to be done us and you, as that he who has come to be judged should sit down as one to give judgment."

    hide lucentius
    hide dioscorus
    with dissolve

    # Documentary explanation
    narrator_doc "The charges against Dioscorus were grave:"
    narrator_doc "At the Council of Ephesus in 449 - the 'Robber Council' - he had condemned Flavian of Constantinople without proper trial."
    narrator_doc "He had refused to read Pope Leo's Tome."
    narrator_doc "He had rehabilitated the heretic Eutyches."
    narrator_doc "And Flavian had died from the violence inflicted upon him."

    nvl clear

    scene bg council_hall with dissolve

    narrator_doc "The imperial judges ordered that Dioscorus be seated among the accused, not among the bishops."
    narrator_doc "The council would now examine the acts of the 'Robber Council' to determine what had truly happened."

    nvl clear

    # Reading of the acts
    narrator_doc "The records were brought forth and read aloud."
    narrator_doc "Bishop by bishop, the council heard testimony of what had occurred at Ephesus."

    nvl clear

    show eusebius at center
    with dissolve

    eusebius "I presented a petition against Eutyches to the holy synod at Constantinople."

    eusebius "Eutyches taught that our Lord Jesus Christ has only one nature after the incarnation."

    eusebius "This I opposed, for I confess that Christ is of two natures, divine and human, united in one person."

    hide eusebius with dissolve

    # The vindication of Flavian
    narrator_doc "The council examined how Flavian had judged Eutyches."
    narrator_doc "They found his judgment orthodox and just."
    narrator_doc "The imperial commissioners asked the bishops to declare themselves."

    nvl clear

    window hide dissolve

    show florentius at center
    with dissolve

    commissioners "What do the most reverend bishops of the present holy synod say? When Flavian thus expounded the faith, did he preserve the orthodox and catholic religion, or did he in any respect err concerning it?"

    hide florentius with dissolve

    scene bg council_hall crowded with dissolve

    show paschasinus at left
    with dissolve

    pasch "Flavian of blessed memory has most holily and perfectly expounded the faith. His faith and exposition agrees with the epistle of the most blessed and apostolic man, the bishop of Rome."

    hide paschasinus with dissolve

    show anatolius at center
    with dissolve

    anatolius "The blessed Flavian has beautifully and orthodoxly set forth the faith of our fathers."

    hide anatolius with dissolve

    show lucentius at left
    with dissolve

    lucentius "Since the faith of Flavian of blessed memory agrees with the Apostolic See and the tradition of the fathers, it is just that the sentence by which he was condemned by the heretics should be turned back upon them by this most holy synod."

    hide lucentius with dissolve

    bishops "Flavian was orthodox! Dioscorus judged unjustly!"

    # Dioscorus speaks
    show dioscorus defiant at center
    with dissolve

    diosc "I receive the 'of two.'"

    pause 0.5

    diosc "The 'two' I do not receive."

    hide dioscorus with dissolve

    # Documentary explanation of this cryptic statement
    call screen theology_explanation(
        "Understanding Dioscorus's Statement",
        [
            "Dioscorus accepted that Christ came 'of two' natures - that both divine and human elements were involved in the Incarnation.",
            "But he rejected that Christ exists 'in two' natures after the union - claiming the natures merged into one.",
            "This subtle distinction was at the heart of the theological controversy.",
            "The council would ultimately affirm both: Christ is 'of two' AND 'in two' natures."
        ]
    )

    scene bg council_hall with fade

    narrator_doc "As the session drew to a close, the bishops made their judgment clear."
    narrator_doc "Flavian had been right. Dioscorus had been wrong."
    narrator_doc "The 'Robber Council' was overturned."

    nvl clear

    narrator_doc "But the council's work was only beginning."
    narrator_doc "Tomorrow they would examine the faith itself."
    narrator_doc "Tomorrow they would hear the Tome of Pope Leo."

    nvl clear

    pause 1.0

    jump session_02
