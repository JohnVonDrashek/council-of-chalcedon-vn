## Council of Chalcedon - Sessions XIV-XV
## November 1, 451 AD
## The Final Sessions

label sessions_14_15:

    # Track progress
    call after_session(14)
    call after_session(15)

    # Session card
    call screen session_card("XIV-XV", "November 1, 451 AD", "The Final Sessions")

    scene bg council_hall with fade

    narrator_doc "The council approached its conclusion."
    narrator_doc "Final jurisdictional matters were settled."
    narrator_doc "Remaining appeals were heard."

    nvl clear

    narrator_doc "Session XIV"
    narrator_doc "The question of Constantinople's jurisdiction was raised."
    narrator_doc "Canon 28 would grant Constantinople privileges second only to Rome."
    narrator_doc "The Roman legates objected strenuously."
    narrator_doc "This controversy would echo for centuries."

    nvl clear

    window hide dissolve

    show paschasinus at center
    with dissolve

    pasch "The see of Rome has never accepted this innovation."

    pasch "The primacy of Rome comes from blessed Peter, not from the city's political status."

    pasch "Constantinople cannot claim what belongs to the Apostolic See."

    hide paschasinus with dissolve

    narrator_doc "Despite Roman objections, Canon 28 was adopted by the Eastern bishops."
    narrator_doc "It would become a point of contention between East and West for centuries."
    narrator_doc "To this day, Rome does not accept it."

    nvl clear

    # Session XV
    narrator_doc "Session XV"
    narrator_doc "The final session addressed remaining business."
    narrator_doc "Letters were prepared to be sent to the Emperor."
    narrator_doc "The acts of the council were signed."

    nvl clear

    scene bg council_hall crowded with dissolve

    narrator_doc "And then the bishops prepared to promulgate the canons."
    narrator_doc "Thirty rules for the governance of the Church."
    narrator_doc "Discipline for clergy and monastics."
    narrator_doc "Order for the ages to come."

    nvl clear

    pause 1.0

    jump canons
