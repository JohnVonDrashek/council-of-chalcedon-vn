## Council of Chalcedon - Session II
## October 10, 451 AD
## The Tome of Leo

label session_02:

    # Track progress
    call after_session(2)

    # Session card
    call screen session_card("II", "October 10, 451 AD", "The Tome of Leo")

    # Set the scene with solemn anticipation
    play music solemn fadein 1.0

    scene bg council_hall crowded with fade
    play sound crowd_murmur

    narrator_doc "Two days had passed since Dioscorus was stripped of his episcopal seat."
    narrator_doc "Now the council faced its true purpose: to define the faith."

    nvl clear

    narrator_doc "The imperial commissioners spoke first."

    nvl clear

    window hide dissolve

    show florentius at center
    with dissolve

    narrator "The most glorious judges and the great senate said:"

    commissioners "What course we should pursue is clear after your deliberations. Now however the question to be enquired into is how the true faith is to be established, which is the chief end for which this Council has been assembled."

    commissioners "Hasten therefore without any fear of pleasing or displeasing, to set forth the pure faith, so that they who do not believe with all the rest may be brought to unity through acknowledging the truth."

    hide florentius with dissolve

    # The bishops resist a new definition
    bishops "Any other setting forth no one makes, neither will we attempt it, neither will we dare to set forth anything new!"

    bishops "For the fathers taught, and in their writings are preserved what things were set forth by them, and further than this we can say nothing."

    window hide dissolve

    narrator_doc "The commissioners insisted. Let each bishop declare what he believes."
    narrator_doc "First, the Creed of the 318 Fathers at Nicaea was read aloud."

    nvl clear

    window hide dissolve

    # After the Nicene Creed
    bishops "This is the orthodox faith! This we all believe!"

    bishops "Into this we were baptized! Into this we baptize!"

    bishops "Blessed Cyril so taught! This is the true faith! This is the holy faith! This is the everlasting faith!"

    bishops "We all so believe! So believes Leo, the Pope! Cyril thus believed! Pope Leo so interpreted it!"

    window hide dissolve

    narrator_doc "Then the letters of Cyril were read - his letter to Nestorius, and his letter to John of Antioch."
    narrator_doc "The bishops acclaimed these as well."

    nvl clear

    window hide dissolve

    bishops "We all so believe! Pope Leo thus believes!"

    bishops "Anathema to him who divides and to him who confounds!"

    bishops "Leo and Anatolius so believe! We all thus believe!"

    bishops "As Cyril so believe we, all of us! Eternal be the memory of Cyril!"

    window hide dissolve

    narrator_doc "Finally, the judges commanded that the letter of Pope Leo be read."

    nvl clear

    # Leo's Tome reading
    scene bg black with dissolve
    play sound scroll_unroll

    narrator_doc "And so the Tome of Pope Leo was read aloud to the assembled bishops."
    narrator_doc "This letter, written to Patriarch Flavian in 449, explained the orthodox understanding of Christ's two natures."

    nvl clear

    # Present Leo's Tome as a formal document
    call screen document_reader(
        "The Tome of Pope Leo",
        "Each nature performs its proper functions in communion with the other.\n\nThe Word does what pertains to the Word; the flesh what pertains to the flesh.\n\nOne of these is resplendent with miracles; the other succumbs to injuries.\n\nAnd as the Word does not lose equality with the Father's glory, so the flesh does not abandon the nature of our race.\n\nFor He who is true God is also true man.\n\nThere is nothing unreal about this union, since both the lowliness of the man and the grandeur of the divinity are in mutual relation.\n\nAs God is not changed by the showing of mercy, so the man is not consumed by the dignity.\n\nEach form, in communion with the other, performs the actions which are proper to it.",
        "Letter of Pope Leo I to Flavian, Patriarch of Constantinople, 449 AD"
    )

    scene bg council_hall crowded with fade

    # Triumph! The bishops acclaim Leo
    play music triumph fadeout 0.5 fadein 0.5

    # The famous acclamation - verbatim from the Acts
    bishops "This is the faith of the fathers! This is the faith of the Apostles!"

    bishops "So we all believe! Thus the orthodox believe!"

    bishops "Anathema to him who does not thus believe!"

    pause 0.5

    # The climactic moment
    play sound crowd_acclaim
    call screen acclamation("Peter has spoken thus through Leo!\nSo taught the Apostles!")

    bishops "Piously and truly did Leo teach! So taught Cyril!"

    bishops "Everlasting be the memory of Cyril!"

    bishops "Leo and Cyril taught the same thing! Anathema to him who does not so believe!"

    bishops "This is the true faith! Those of us who are orthodox thus believe!"

    bishops "This is the faith of the fathers!"

    pause 0.3

    # The accusation against Dioscorus
    bishops "Why were not these things read at Ephesus?"

    bishops "These are the things Dioscorus hid away!"

    window hide dissolve

    narrator_doc "With those words - 'Peter has spoken thus through Leo' - the council affirmed the authority of Rome."
    narrator_doc "The bishops declared that Pope Leo spoke with the voice of Saint Peter himself."

    nvl clear

    narrator_doc "And they accused Dioscorus of suppressing Leo's Tome at the Robber Council."
    narrator_doc "He had not permitted it to be read."
    narrator_doc "Now the truth was made manifest to all."

    nvl clear

    narrator_doc "Leo's Tome would become the foundation of the council's doctrinal definition."
    narrator_doc "But before that definition could be written, one matter remained."
    narrator_doc "Dioscorus must answer for his crimes."

    nvl clear

    pause 1.0

    jump session_03
