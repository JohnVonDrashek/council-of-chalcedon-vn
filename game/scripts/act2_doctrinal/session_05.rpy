## Council of Chalcedon - Session V
## October 22, 451 AD
## The Definition of Faith

label session_05:

    # Track progress
    call after_session(5)

    # Session card
    call screen session_card("V", "October 22, 451 AD", "The Definition of Faith")

    scene bg antechamber with fade

    narrator_doc "The committee met in the oratory of the most holy martyr Euphemia."
    narrator_doc "Their task: to draft a definition of faith that would satisfy all parties."
    narrator_doc "It must affirm Leo's Tome."
    narrator_doc "It must use the language of Cyril."
    narrator_doc "It must not contradict the creeds of Nicaea and Constantinople."
    narrator_doc "And it must condemn both Nestorius and Eutyches."

    nvl clear

    narrator_doc "The committee labored through the night."
    narrator_doc "When they emerged, they brought a text."

    nvl clear

    scene bg council_hall crowded with fade

    narrator_doc "But the Roman legates were not satisfied."
    narrator_doc "The draft did not follow Leo's Tome closely enough."

    nvl clear

    window hide dissolve

    show paschasinus at center
    with dissolve

    pasch "If they do not agree to the letter of that apostolic and blessed man, Pope Leo, give directions that we be given our letters of dismission."

    pasch "Let a synod be held there in the West."

    hide paschasinus with dissolve

    # The bishops cry out
    bishops "Many years to the Emperor! Either let the definition stand or we go!"

    # The imperial commissioners present the choice
    show florentius at center
    with dissolve

    commissioners "Dioscorus acknowledged that he accepted the expression 'of two natures,' but not that there were two natures."

    commissioners "But the most holy Archbishop Leo says that there are two natures in Christ unchangeably, inseparably, unconfusedly united in the one only-begotten Son our Saviour."

    commissioners "Which would you follow, the most holy Leo or Dioscorus?"

    hide florentius with dissolve

    # The bishops respond
    bishops "We believe as Leo! Those who contradict are Eutychians!"

    bishops "Leo has rightly expounded the faith!"

    window hide dissolve

    # The threat
    narrator_doc "The question was decisive."
    narrator_doc "Would the council follow Leo's clear teaching of two natures?"
    narrator_doc "Or would they leave room for Dioscorus's ambiguity?"

    nvl clear

    window hide dissolve

    # Revision
    show florentius at center
    with dissolve

    commissioners "Add then to the definition, according to the judgment of our most holy father Leo, that there are two natures in Christ united unchangeably, inseparably, unconfusedly."

    hide florentius with dissolve

    window hide dissolve

    narrator_doc "The committee retired again to the oratory of Saint Euphemia."
    narrator_doc "They revised their text, adding the crucial phrase from Leo:"
    narrator_doc "'In two natures.'"

    nvl clear

    scene bg council_hall crowded with dissolve

    narrator_doc "And so, on October 22, 451 AD, the Definition of Chalcedon was proclaimed."

    nvl clear

    # The Definition
    call screen document_reader(
        "The Definition of Chalcedon",
        "Following the holy Fathers, we all with one voice teach that it should be confessed:\n\nThat our Lord Jesus Christ is one and the same Son, the Same perfect in Godhead, the Same perfect in manhood, truly God and truly man.\n\nThe Same consisting of a rational soul and a body, homoousios with the Father as touching His Godhead, and the Same homoousios with us as touching His manhood.\n\nIn all things like unto us, sin only excepted.\n\nBegotten of the Father before the ages as touching the Godhead, and in the last days, the Same, for us and for our salvation born of Mary the Virgin Theotokos as touching the manhood.\n\nOne and the Same Christ, Son, Lord, Only-begotten, made known:\n\nIN TWO NATURES\n\nUNCONFUSEDLY\nIMMUTABLY\nINDIVISIBLY\nINSEPARABLY\n\nThe distinction of natures being in no way abolished by the union, but rather the characteristic property of each nature being preserved, and concurring into one Person and one Subsistence.\n\nNot parted or divided into two persons, but one and the Same Son and Only-begotten, the divine Logos, the Lord Jesus Christ.",
        "The Chalcedonian Definition, October 22, 451 AD"
    )

    # Explanation
    call screen theology_explanation(
        "The Four Adverbs of Chalcedon",
        [
            "Unconfusedly (asynchytos) - The two natures do not mix into something new.",
            "Immutably (atreptos) - Neither nature is changed by the union.",
            "Indivisibly (adiairetos) - The two natures cannot be separated.",
            "Inseparably (achoristos) - Christ is always both God and man.",
            "These four words define the boundaries of orthodox Christology to this day."
        ]
    )

    scene bg council_hall crowded with dissolve

    # Acclamations from the source
    bishops "This is the faith of the fathers!"

    bishops "Let the metropolitans immediately subscribe it!"

    bishops "Let that which has been well defined have no delay!"

    bishops "This is the faith of the Apostles! By this we all stand! Thus we all believe!"

    window hide dissolve

    narrator_doc "The Definition of Chalcedon became the standard of orthodox Christology."
    narrator_doc "To this day, Catholics, Eastern Orthodox, and most Protestants affirm it."
    narrator_doc "The Oriental Orthodox churches - Coptic, Ethiopian, Armenian, Syriac - rejected it, leading to a schism that persists to this day."

    nvl clear

    narrator_doc "But the council was not yet finished."
    narrator_doc "Emperor Marcian himself would attend the next session."
    narrator_doc "And there were still matters of Church order to settle."

    nvl clear

    pause 1.0

    jump session_06
