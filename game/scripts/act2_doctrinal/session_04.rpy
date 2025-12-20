## Council of Chalcedon - Session IV
## October 17, 451 AD
## The Question of Definition

label session_04:

    # Track progress
    call after_session(4)

    # Session card
    call screen session_card("IV", "October 17, 451 AD", "The Question of Definition")

    scene bg council_hall with fade

    narrator_doc "With Dioscorus deposed, the council turned to its central task:"
    narrator_doc "To define the orthodox faith concerning Christ's nature."

    nvl clear

    narrator_doc "But a question arose immediately."
    narrator_doc "Was a new definition even necessary?"
    narrator_doc "The creeds of Nicaea and Constantinople already defined the faith."
    narrator_doc "Leo's Tome had explained the doctrine clearly."
    narrator_doc "Why add more?"

    nvl clear

    window hide dissolve

    # Paschasinus states the position of the Roman legates
    show paschasinus at center
    with dissolve

    pasch "As the holy and blessed and Ecumenical Synod holds fast and follows the rule of faith which was set forth by the fathers at Nicaea, it also confirms the faith set forth by the Synod of 150 fathers gathered at Constantinople."

    pasch "Moreover the exposition of their faith, of the illustrious Cyril of blessed memory set forth at the Council of Ephesus, in which Nestorius was condemned, is received."

    pasch "And in the third place the writings of that blessed man, Leo, Archbishop of all the churches, who condemned the heresy of Nestorius and Eutyches, show what the true faith is."

    pasch "Likewise the holy Synod holds this faith, this it follows - nothing further can it add nor can it take anything away."

    hide paschasinus with dissolve

    bishops "So we all believe! So we were baptized! So we baptize! So we have believed! So we now believe!"

    # Imperial pressure
    scene bg throne_room with dissolve

    narrator_doc "But the imperial commissioners had their orders."
    narrator_doc "Emperor Marcian wanted clarity."
    narrator_doc "After decades of controversy, ambiguity was no longer acceptable."

    nvl clear

    window hide dissolve

    show florentius at center
    with dissolve

    commissioners "Since we see that the Holy Gospels have been placed alongside of your holiness, let each one of the bishops here assembled declare whether the epistle of most blessed Archbishop Leo is in accordance with the exposition of the 318 fathers assembled at Nicaea and with the decrees of the 150 fathers afterwards assembled in the royal city."

    hide florentius with dissolve

    scene bg council_hall with dissolve

    narrator_doc "One by one, the bishops affirmed Leo's Tome."
    narrator_doc "It agreed with Nicaea. It agreed with Constantinople. It agreed with Cyril."
    narrator_doc "The doctrine was orthodox."

    nvl clear

    narrator_doc "But still the commissioners pressed."
    narrator_doc "If all agreed, let them put it in writing."
    narrator_doc "Let them add to the definition:"

    nvl clear

    window hide dissolve

    show florentius at center
    with dissolve

    commissioners "Add then to the definition, according to the judgment of our most holy father Leo, that there are two natures in Christ united unchangeably, inseparably, unconfusedly."

    hide florentius with dissolve

    # Resistance
    bishops "We cannot write a new creed!"

    bishops "The fathers forbade new creeds!"

    bishops "Either let the existing faith stand, or we go!"

    window hide dissolve

    narrator_doc "The tension in the hall was palpable."
    narrator_doc "The bishops feared that any new formulation would open the door to future innovations."
    narrator_doc "The emperors feared that without clear language, the controversy would never end."

    nvl clear

    # Resolution
    narrator_doc "Finally, a compromise was reached."
    narrator_doc "A committee would be appointed."
    narrator_doc "They would draft not a new creed, but a definition - an explanation of what the creeds had always meant."
    narrator_doc "The committee would meet in the oratory of Saint Euphemia."

    nvl clear

    pause 1.0

    jump session_05
