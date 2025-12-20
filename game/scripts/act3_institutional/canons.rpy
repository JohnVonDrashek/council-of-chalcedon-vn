## Council of Chalcedon - The Thirty Canons
## The Disciplinary Decrees

label canons:

    scene bg black with fade

    # Title card
    show text "{color=#d4c4a8}{size=48}THE THIRTY CANONS{/size}\n\n{size=28}Disciplinary Decrees of the Council{/size}{/color}" at truecenter

    pause 3.0

    hide text with dissolve

    scene bg council_hall with fade

    narrator_doc "Before the bishops departed, they promulgated thirty canons."
    narrator_doc "These rules would govern the Church's discipline for centuries."
    narrator_doc "Many remain in force to this day in both East and West."

    nvl clear

    narrator_doc "The canons addressed:"
    narrator_doc "- The authority of previous councils"
    narrator_doc "- The sin of simony (buying and selling church offices)"
    narrator_doc "- The discipline of monks and clergy"
    narrator_doc "- The jurisdiction of bishops"
    narrator_doc "- The rights of Constantinople"

    nvl clear

    # Present the canons
    # Group 1: Authority and Simony (Canons 1-2)

    call screen canon_display(1,
        "The canons of the Holy Fathers made in every synod even until now shall remain in force.",
        "All previous council decisions remain binding law.")

    $ persistent.canons_read.add(1)

    call screen canon_display(2,
        "If any bishop should ordain for money, and put to sale a grace which cannot be sold, and for money ordain a bishop, or chorepiscopus, or presbyter, or deacon... let him who is convicted of this forfeit his own rank.",
        "Simony - buying or selling church offices - is strictly forbidden.")

    $ persistent.canons_read.add(2)

    # Group 2: Clergy Discipline (Canons 3-7)

    scene bg council_hall with dissolve

    narrator_doc "Canons on Clergy Discipline"

    nvl clear

    call screen canon_display(3,
        "It has come to the knowledge of the holy synod that certain of those who are enrolled among the clergy have, for filthy lucre's sake, become hirers of other men's possessions... If any one shall hereafter attempt to do so, he shall be removed from his order.",
        "Clergy may not engage in secular business for profit.")

    $ persistent.canons_read.add(3)

    call screen canon_display(4,
        "Let those who truly and sincerely lead the monastic life be accorded proper honor. But since certain persons using the pretext of monasticism bring confusion both upon the churches and into political affairs... it is decreed that no one anywhere build or found a monastery without the bishop's consent.",
        "Monks must remain in their monasteries under episcopal oversight.")

    $ persistent.canons_read.add(4)

    call screen canon_display(5,
        "Concerning bishops or clergy who go about from city to city, it is decreed that the canons issued by the holy Fathers shall remain in force.",
        "Existing rules on clergy transfers remain binding.")

    $ persistent.canons_read.add(5)

    call screen canon_display(6,
        "Neither presbyter, nor deacon, nor any of the ecclesiastical order shall be ordained at large... Wherefore the holy synod has decreed that such an ordination shall be invalid.",
        "Every ordination must assign the cleric to a specific church.")

    $ persistent.canons_read.add(6)

    call screen canon_display(7,
        "We have decreed that those who have once been enrolled among the clergy, or have been made monks, shall accept neither a military charge nor any secular dignity.",
        "Clergy and monks may not hold military or secular offices.")

    $ persistent.canons_read.add(7)

    # Group 3: Church Order (Canons 8-13)

    scene bg council_hall with dissolve

    narrator_doc "Canons on Church Order"

    nvl clear

    call screen canon_display(8,
        "Let the clergy of the poor-houses, monasteries, and martyries remain under the authority of the bishops in every city... Let not any one rebel against his own bishop.",
        "Religious institutions remain under episcopal authority.")

    $ persistent.canons_read.add(8)

    call screen canon_display(9,
        "If any clergyman have a matter against another clergyman, he shall not forsake his bishop and run to secular courts... If any one shall transgress these decrees, he shall be subjected to canonical penalties.",
        "Clergy must settle disputes through church courts, not secular ones.")

    $ persistent.canons_read.add(9)

    call screen canon_display(10,
        "It shall not be lawful for a clergyman to be at the same time enrolled in the churches of two cities... But if any one shall have done this, he shall be restored to his former church only.",
        "Clergy may serve only one church at a time.")

    $ persistent.canons_read.add(10)

    call screen canon_display(11,
        "We have decreed that the poor and those needing assistance shall travel with letters of peace only, and not with commendatory letters.",
        "Poor travelers may use simplified letters of recommendation.")

    $ persistent.canons_read.add(11)

    call screen canon_display(12,
        "It has come to our knowledge that certain persons, contrary to the laws of the Church, divide one province into two, so that there are two metropolitans. The holy synod has decreed that no such thing shall be attempted hereafter by any bishop.",
        "Provinces may not be divided to create multiple metropolitans.")

    $ persistent.canons_read.add(12)

    call screen canon_display(13,
        "Strange and unknown clergymen without letters commendatory from their own bishop are absolutely prohibited from officiating in another city.",
        "Unknown clergy may not function without proper credentials.")

    $ persistent.canons_read.add(13)

    # Group 4: Marriage and Vows (Canons 14-16)

    scene bg council_hall with dissolve

    narrator_doc "Canons on Marriage and Religious Vows"

    nvl clear

    call screen canon_display(14,
        "Since in certain provinces it is permitted to the readers and singers to marry, the holy synod has decreed that it shall not be lawful for any of them to take a wife that is heterodox.",
        "Minor clergy may only marry Orthodox Christians.")

    $ persistent.canons_read.add(14)

    call screen canon_display(15,
        "A woman shall not receive the laying on of hands as a deaconess under forty years of age, and then only after searching examination. And if, after she has had hands laid on her, she shall despise the grace of God and give herself in marriage, she shall be anathematized.",
        "Deaconesses must be at least forty and may not marry afterward.")

    $ persistent.canons_read.add(15)

    call screen canon_display(16,
        "It is not lawful for a virgin who has dedicated herself to the Lord God, nor for monks, to marry; and if they are found to have done this, let them be excommunicated.",
        "Consecrated virgins and monks may not marry.")

    $ persistent.canons_read.add(16)

    # Group 5: Parishes and Synods (Canons 17-19)

    scene bg council_hall with dissolve

    narrator_doc "Canons on Parishes and Synods"

    nvl clear

    call screen canon_display(17,
        "Country parishes in every province shall remain under the bishops who now have them, especially if the bishops have held them thirty years without dispute... If any city has been newly built by imperial authority, let the arrangement of ecclesiastical parishes follow civil and public examples.",
        "Parish boundaries follow thirty-year possession; new cities follow civil divisions.")

    $ persistent.canons_read.add(17)

    call screen canon_display(18,
        "The crime of conspiracy or secret union shall be utterly unknown among the clergy. If any of the clergy or monks shall be found conspiring or banding together, or plotting against their bishops, let them be altogether deposed from their own rank.",
        "Clergy may not conspire against their bishops.")

    $ persistent.canons_read.add(18)

    call screen canon_display(19,
        "It has come to our ears that in the provinces the synods of bishops are not held twice a year as the canons enjoin, and that many ecclesiastical matters suffer from this neglect. The holy synod has decreed that according to the rules of the holy Fathers the bishops of every province shall assemble together twice a year.",
        "Provincial synods must meet twice yearly.")

    $ persistent.canons_read.add(19)

    # Group 6: Transfers and Accusations (Canons 20-23)

    scene bg council_hall with dissolve

    narrator_doc "Canons on Transfers and Accusations"

    nvl clear

    call screen canon_display(20,
        "It shall not be lawful for a clergyman to accept a charge in another city... If any bishop after the adoption of this decree receive a clergyman belonging to another bishop, it is decreed that both shall be excommunicated.",
        "Unauthorized clergy transfers result in excommunication for both parties.")

    $ persistent.canons_read.add(20)

    call screen canon_display(21,
        "Clergymen or laymen who bring charges against bishops or clergy shall not be admitted to do so indiscriminately and without examination; but their character shall first be investigated.",
        "Accusers' character must be verified before charges are heard.")

    $ persistent.canons_read.add(21)

    call screen canon_display(22,
        "It is not lawful for clergymen after the death of their bishop to seize the goods belonging to him... Those who do so shall be in danger of degradation from their own rank.",
        "Clergy may not seize deceased bishops' property.")

    $ persistent.canons_read.add(22)

    call screen canon_display(23,
        "It has come to the hearing of the holy synod that certain clergymen and monks, having no authority, come to Constantinople and cause disturbances. If any clergy or monks shall be found causing disturbances, they shall be expelled.",
        "Unauthorized clergy causing trouble in Constantinople shall be expelled.")

    $ persistent.canons_read.add(23)

    # Group 7: Monasteries and Ordinations (Canons 24-27)

    scene bg council_hall with dissolve

    narrator_doc "Canons on Monasteries and Ordinations"

    nvl clear

    call screen canon_display(24,
        "Monasteries, which have once been consecrated by the will of the bishop, shall remain monasteries forever. The goods belonging to them shall be preserved, and they shall never again become secular abodes.",
        "Consecrated monasteries are permanent and may not be secularized.")

    $ persistent.canons_read.add(24)

    call screen canon_display(25,
        "Forasmuch as certain of the metropolitans neglect the flocks committed to them and delay the ordinations of bishops, the holy synod has decided that the ordinations of bishops shall take place within three months.",
        "Vacant sees must be filled within three months.")

    $ persistent.canons_read.add(25)

    call screen canon_display(26,
        "Forasmuch as in certain churches the bishops manage ecclesiastical matters without stewards... it has seemed good that every church having a bishop shall have a steward from among its own clergy, to manage church goods under the bishop's oversight.",
        "Every church must have a steward to manage finances.")

    $ persistent.canons_read.add(26)

    call screen canon_display(27,
        "Those who carry off women under pretense of marriage, and the partakers or abettors of such, the holy synod decrees that if they be clergymen they shall be degraded from their rank, and if laymen they shall be anathematized.",
        "Abducting women for marriage brings degradation or anathema.")

    $ persistent.canons_read.add(27)

    # Group 8: The Controversial Canons (28-30)

    scene bg council_hall with dissolve

    narrator_doc "The Controversial Canons"
    narrator_doc "The final three canons proved contentious."
    narrator_doc "Canon 28 in particular would divide East and West."

    nvl clear

    call screen canon_display(28,
        "The Fathers rightly granted privileges to the throne of Old Rome, because it was the royal city. And the One Hundred and Fifty most religious bishops, moved by the same consideration, gave equal privileges to the most holy throne of New Rome... Constantinople shall have the second place after Rome.",
        "Constantinople receives privileges equal to Rome. The Roman legates refused to accept this canon.")

    $ persistent.canons_read.add(28)

    call screen canon_display(29,
        "It is sacrilege to degrade a bishop to the rank of a presbyter. But if any cause justly removes him from episcopal functions, neither ought he to have the position of a presbyter.",
        "A deposed bishop may not be demoted to priest; he is simply removed.")

    $ persistent.canons_read.add(29)

    call screen canon_display(30,
        "Since the most reverend bishops of Egypt have deferred subscribing to the letter of the most holy Archbishop Leo, not from opposition to the Catholic faith, but because they declare their custom to do nothing without the consent of their archbishop... we have decreed to grant them a prolongation of time until the ordination of a bishop of Alexandria.",
        "Egyptian bishops given time to subscribe pending their new patriarch's ordination.")

    $ persistent.canons_read.add(30)

    # Conclusion of canons
    scene bg council_hall crowded with fade

    narrator_doc "And so the thirty canons were promulgated."
    narrator_doc "Together with the Definition of Faith, they became the lasting legacy of Chalcedon."

    nvl clear

    narrator_doc "Canon 28 would remain a point of contention."
    narrator_doc "Rome never accepted Constantinople's claim to 'equal privileges.'"
    narrator_doc "The East and West would interpret this differently for centuries."
    narrator_doc "It was one of the many seeds of the eventual Great Schism of 1054."

    nvl clear

    pause 1.0

    jump epilogue
