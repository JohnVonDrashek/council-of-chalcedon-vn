## Council of Chalcedon - Session III
## October 13, 451 AD
## The Deposition of Dioscorus

label session_03:

    # Track progress
    call after_session(3)

    # Session card
    call screen session_card("III", "October 13, 451 AD", "The Deposition of Dioscorus")

    # Tension builds as Dioscorus faces judgment
    play music tension fadein 1.0

    scene bg council_hall with fade

    narrator_doc "Five days had passed since Dioscorus was stripped of his seat among the bishops."
    narrator_doc "Now he stood accused not merely of error, but of crimes against the Church."
    narrator_doc "The council summoned him to answer the charges."

    nvl clear

    # First summons
    narrator_doc "The First Summons"
    narrator_doc "Bishops were sent to bring Dioscorus before the council."
    narrator_doc "He refused to come."

    nvl clear

    # Second summons
    narrator_doc "The Second Summons"
    narrator_doc "Again messengers were dispatched."
    narrator_doc "Again Dioscorus refused, claiming he was being held under guard."

    nvl clear

    # Third summons
    narrator_doc "The Third Summons"
    narrator_doc "A final delegation was sent."
    narrator_doc "Dioscorus still would not appear."

    nvl clear

    scene bg council_hall crowded with fade

    narrator_doc "According to the divine canons, a bishop summoned three times who refuses to appear forfeits his case."
    narrator_doc "The council proceeded to judgment."

    nvl clear

    window hide dissolve

    # Paschasinus opens
    show paschasinus at center
    with dissolve

    pasch "It is well known to this beloved-of-God synod that divine letters were sent to the blessed and apostolic Pope Leo, inviting him to deign to be present at the holy synod."

    pasch "But since ancient custom did not sanction this, nor the general necessity of the time seemed to permit it, our littleness was commanded to preside in his place over this holy council."

    pause 0.3

    # The charges
    pasch "The charges against Dioscorus are these:"

    pasch "That he received Eutyches into communion after his lawful condemnation."

    pasch "That he dared to excommunicate the most holy Pope Leo."

    pasch "That at the synod of Ephesus he did not permit the letter of Pope Leo to be read."

    pasch "That he caused violence to be done to Flavian of blessed memory."

    hide paschasinus with dissolve

    # The sentence
    narrator_doc "The bishops deliberated."
    narrator_doc "One by one, they pronounced their judgment."

    nvl clear

    show paschasinus at left
    with dissolve

    pasch "Wherefore the most holy and blessed Leo, Archbishop of the great and elder Rome, through us and through this present most holy synod, together with the thrice blessed and all-glorious Peter the Apostle, who is the rock and foundation of the Catholic Church, and the foundation of the orthodox faith..."

    pause 0.5

    pasch "...has stripped him of the episcopate, and has alienated from him all hieratic worthiness. Therefore let this most holy and great synod sentence the before-mentioned Dioscorus to the canonical penalties."

    # The gavel falls
    play sound gavel_strike

    hide paschasinus with dissolve

    scene bg council_hall crowded with dissolve

    # The bishops acclaim the judgment
    play sound crowd_acclaim

    bishops "This is a just judgment!"

    bishops "Christ has deposed Dioscorus!"

    bishops "A just sentence! A just sentence!"

    window hide dissolve

    # Documentary summary - shift to solemn reflection
    play music solemn fadeout 1.0 fadein 1.0

    narrator_doc "And so Dioscorus of Alexandria was deposed from the episcopate."
    narrator_doc "The formal sentence read:"

    nvl clear

    call screen document_reader(
        "The Condemnation Sent to Dioscorus",
        "The holy and great and ecumenical Synod, which by the grace of God according to the constitution of our most pious and beloved-of-God emperors assembled together at Chalcedon in the martyry of the most holy and victorious Martyr Euphemia, to Dioscorus:\n\nWe do you to wit that on the thirteenth day of the month of October you were deposed from the episcopate and made a stranger to all ecclesiastical order by the holy and ecumenical synod.\n\nThis on account of your disregard of the divine canons, and of your disobedience to this holy and ecumenical synod, and on account of the other crimes of which you have been found guilty.\n\nFor even when called to answer your accusers three times by this holy and great synod according to the divine canons, you did not come.",
        "Acts of the Council of Chalcedon, Session III"
    )

    narrator_doc "Dioscorus would be exiled to Gangra in Paphlagonia."
    narrator_doc "He would die there three years later, never recanting."
    narrator_doc "To this day, the Coptic Church venerates him as a saint and martyr."

    nvl clear

    narrator_doc "But the council's work was far from complete."
    narrator_doc "The procedural matters were settled."
    narrator_doc "Now came the harder task: to define the faith itself."

    nvl clear

    pause 1.0

    jump session_04
