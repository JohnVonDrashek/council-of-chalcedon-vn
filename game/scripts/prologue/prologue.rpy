## Council of Chalcedon - Prologue
## Historical Context: 428-451 AD

label prologue:

    # Start with main theme
    play music main_theme fadein 2.0

    scene bg black with fade

    # Title card
    show text "{color=#d4c4a8}{size=48}THE COUNCIL OF CHALCEDON{/size}\n\n{size=28}The Fourth Ecumenical Council{/size}\n\n{size=22}October 8 - November 1, 451 AD{/size}{/color}" at truecenter

    pause 4.0

    hide text with dissolve

    # Historical context in NVL mode
    narrator_doc "In the fifth century, the Catholic Church faced a profound question:"
    narrator_doc "How can Jesus Christ be both fully God and fully human?"

    nvl clear

    narrator_doc "This was not mere philosophical speculation."
    narrator_doc "The answer would determine how the faithful understood salvation itself."
    narrator_doc "If Christ was not truly God, could He save humanity?"
    narrator_doc "If Christ was not truly human, was His suffering real?"

    nvl clear

    scene bg constantinople with fade

    narrator_doc "428 AD - The Nestorian Controversy"
    narrator_doc "Nestorius, Patriarch of Constantinople, taught that Christ's divine and human natures were so distinct that Mary should not be called 'Theotokos' - the God-bearer."
    narrator_doc "This teaching was condemned at the Council of Ephesus in 431 AD."

    nvl clear

    scene bg alexandria with fade

    narrator_doc "448 AD - Eutyches"
    narrator_doc "An elderly monk named Eutyches taught the opposite extreme:"
    narrator_doc "After the Incarnation, Christ had only ONE nature - His humanity absorbed into His divinity like a drop of honey dissolved in the sea."
    narrator_doc "Flavian, Patriarch of Constantinople, condemned Eutyches for heresy."

    nvl clear

    # Shift to tension for the Robber Council
    play music tension fadeout 1.0 fadein 1.0

    narrator_doc "449 AD - The 'Robber Council'"
    narrator_doc "Emperor Theodosius II called a council at Ephesus."
    narrator_doc "Dioscorus, Patriarch of Alexandria, presided with an iron fist."
    narrator_doc "He rehabilitated Eutyches and deposed Flavian."
    narrator_doc "Pope Leo I's letter explaining the orthodox faith was not even read."
    narrator_doc "Flavian was beaten so severely that he died days later."

    nvl clear

    scene bg rome with fade

    narrator_doc "Leo called it 'Latrocinium' - the Robber Council."
    narrator_doc "He demanded it be overturned."

    nvl clear

    scene bg constantinople with fade

    # Solemn music for the turning point
    play music solemn fadeout 1.0 fadein 1.0

    narrator_doc "450 AD - The Turning Point"
    narrator_doc "Emperor Theodosius II died in a riding accident."
    narrator_doc "His sister Pulcheria, a devout virgin, took the throne."
    narrator_doc "She married the general Marcian, who shared her orthodox faith."
    narrator_doc "Together they called a new council to settle the matter once and for all."

    nvl clear

    narrator_doc "451 AD - Chalcedon"
    narrator_doc "The council would meet at the Church of Saint Euphemia in Chalcedon,"
    narrator_doc "across the Bosphorus from Constantinople."
    narrator_doc "Over five hundred bishops gathered - the largest council in Church history to that date."
    narrator_doc "The fate of Christendom hung in the balance."

    nvl clear

    scene bg council_hall with fade

    # Imperial music as the council begins, crowd murmur
    play music imperial fadeout 1.0 fadein 1.0
    play sound crowd_murmur

    narrator_doc "And so, on October 8, 451 AD, the bishops assembled."
    narrator_doc "The imperial commissioners took their seats."
    narrator_doc "The Roman legates bore Pope Leo's instructions."
    narrator_doc "And Dioscorus of Alexandria sat among those he had condemned."

    nvl clear

    narrator_doc "The Council of Chalcedon was about to begin."

    nvl clear

    pause 1.0

    jump session_01
