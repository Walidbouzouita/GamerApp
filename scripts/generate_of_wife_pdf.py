#!/usr/bin/env python3
"""Generate Bubbello-style production PDF for OF Wife POV video."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUTPUT = "/workspace/POV-Husband-OF-Wife-Production-Script.pdf"

# ─── SCENE DATA ───────────────────────────────────────────────────────────
# Each scene: (num, act, name, images_range, rhythm, phrases[])
SCENES = [
    {
        "num": 1, "act": "HOOK RAPIDE", "name": "Cold Open I",
        "range": "i1-i10", "count": 10, "rhythm": "1-2 sec/image",
        "phrases": [
            "Your phone won't stop buzzing.",
            "A ring light glows behind a closed door.",
            "Stacks of cash cover the kitchen table.",
            "Your neighbor stares at you differently now.",
            "An open package sits on the counter.",
            "She turns her screen away from you.",
            "The office door locks from the inside.",
            "You knock. She doesn't answer.",
            "A familiar logo appears on her laptop.",
            "Voices rise through the hallway.",
        ],
    },
    {
        "num": 2, "act": "HOOK RAPIDE", "name": "Cold Open II",
        "range": "i11-i20", "count": 10, "rhythm": "1-2 sec/image",
        "phrases": [
            "She steps back like she's afraid of you.",
            "Your hands won't stop shaking.",
            "A bank deposit you never expected.",
            "The wedding photo still hangs on the wall.",
            "Tears run down her face.",
            "You stand completely still.",
            "A door slams somewhere in the house.",
            "The house goes quiet.",
            "She reaches toward you.",
            "Everything you trusted is breaking apart.",
        ],
    },
    {
        "num": 3, "act": "HOOK RAPIDE", "name": "The Line",
        "range": "i21-i30", "count": 10, "rhythm": "1-2 sec/image",
        "phrases": [
            "She finally looks you in the eyes.",
            "She opens her mouth to speak.",
            "You can't look at her anymore.",
            "She whispers one sentence.",
            "I never wanted you to find out like this.",
            "You step back like she struck you.",
            "Black screen.",
            "Twenty-four hours earlier.",
            "The house was still peaceful.",
            "POV: Your Life As The Husband Of An OnlyFans Wife.",
        ],
    },
    {
        "num": 4, "act": "ACTE 1 - NORMAL LIFE", "name": "A Perfect Morning",
        "range": "i31-i41", "count": 11, "rhythm": "3-4 sec/image",
        "phrases": [
            "Morning light fills the kitchen.",
            "She pours coffee into your favorite mug.",
            "You kiss her before leaving for another long day.",
            "Three years of marriage still feels new.",
            "Deadlines pile up at the office every week.",
            "You miss dinner more than you ever admit.",
            "But coming home to her still makes it worth it.",
            "That night she smiles over her laptop at the table.",
            "Honey, I found a side hustle online, she says.",
            "You tell her that sounds awesome and mean it.",
            "She deserves something of her own beyond this routine.",
        ],
    },
    {
        "num": 5, "act": "ACTE 1 - NORMAL LIFE", "name": "Side Hustle",
        "range": "i42-i52", "count": 11, "rhythm": "3-4 sec/image",
        "phrases": [
            "You ask what kind of hustle makes her eyes light up.",
            "Just content creation, she says, like it means nothing.",
            "The next weeks pass in a blur of late nights.",
            "You work late while she works behind a closed door.",
            "A package arrives while you are still at your desk.",
            "She brings it inside before you read the label.",
            "Busy night, she says over another reheated dinner.",
            "Good numbers today, she adds without explaining.",
            "You are too tired to ask questions that night.",
            "That tiredness will haunt you later.",
            "The side hustle becomes part of your normal life.",
        ],
    },
    {
        "num": 6, "act": "ACTE 1 - NORMAL LIFE", "name": "First Clue",
        "range": "i53-i63", "count": 11, "rhythm": "3-4 sec/image",
        "phrases": [
            "Saturday morning. You sort the mail at the counter.",
            "A crumpled receipt falls from the middle of the stack.",
            "Ring light. Professional studio kit. An unfamiliar price.",
            "You show it to her at breakfast with a half-smile.",
            "It is for the side hustle, she says too quickly.",
            "She changes the subject to weekend plans.",
            "You want to believe her because doubting feels worse.",
            "She seems happy. That is what matters, you tell yourself.",
            "You fold the receipt and let it disappear.",
            "She squeezes your hand like nothing happened.",
            "The first clue vanishes into a normal day.",
        ],
    },
    {
        "num": 7, "act": "ACTE 2 - SOMETHING IS WRONG", "name": "Packages Arrive",
        "range": "i64-i74", "count": 11, "rhythm": "3-4 sec/image",
        "phrases": [
            "Packages start arriving every other day.",
            "Outfits, makeup kits, and softbox lights fill the hallway.",
            "The delivery driver smiles like they share a private joke.",
            "Have a great shoot, he says before driving away.",
            "You freeze on the porch with keys in your hand.",
            "She laughs it off as standard influencer mail.",
            "Inside, she stacks boxes in the office quickly.",
            "The door closes faster every time you walk past.",
            "You notice but say nothing because saying it makes it real.",
            "Something feels wrong. You still cannot name it.",
            "The packages keep coming like warnings you ignore.",
        ],
    },
    {
        "num": 8, "act": "ACTE 2 - SOMETHING IS WRONG", "name": "She Hides Her Phone",
        "range": "i75-i85", "count": 11, "rhythm": "3-4 sec/image",
        "phrases": [
            "Dinner. Her phone vibrates against the table.",
            "She flips it face down without glancing at the screen.",
            "You ask who keeps texting during every meal.",
            "Just spam, she says. Her smile does not reach her eyes.",
            "At two in the morning you wake up alone.",
            "Light bleeds under the office door down the hall.",
            "You hear her voice. A tone you do not recognize.",
            "You walk to the door. The lock clicks inside.",
            "You stand there. Then return to bed without knocking.",
            "She slips in at dawn smelling like new perfume.",
            "You pretend to sleep because you fear the truth.",
        ],
    },
    {
        "num": 9, "act": "ACTE 2 - SOMETHING IS WRONG", "name": "Money Appears",
        "range": "i86-i96", "count": 11, "rhythm": "3-4 sec/image",
        "phrases": [
            "Your banking app sends a notification.",
            "Deposit. Four thousand two hundred dollars.",
            "You stare at the number like it might vanish.",
            "She grins over your shoulder with unfamiliar pride.",
            "Told you the hustle was working, she says.",
            "You want to celebrate. She already feels distant.",
            "Where did this come from, you ask calmly.",
            "Brand deals and subscriptions, she answers smoothly.",
            "A notification vanishes from her screen too fast.",
            "You catch the color of the app icon.",
            "Your stomach drops. She does not notice.",
        ],
    },
    {
        "num": 10, "act": "ACTE 3 - THE DISCOVERY", "name": "The Locked Door",
        "range": "i97-i107", "count": 11, "rhythm": "3-4 sec/image",
        "phrases": [
            "This is the day everything changes.",
            "The office door is locked with her voice behind it.",
            "Her voice is softer than you have ever heard.",
            "Nothing like how she talks at breakfast.",
            "You search the drawer for the spare key.",
            "The brass is cold against your palm.",
            "You hear a camera shutter from inside.",
            "You should knock. You should wait. You should trust her.",
            "Instead you slide the key in and turn slowly.",
            "The door opens onto a life you no longer know.",
            "Your hand trembles on the handle.",
        ],
    },
    {
        "num": 11, "act": "ACTE 3 - THE DISCOVERY", "name": "The Screen",
        "range": "i108-i118", "count": 11, "rhythm": "3-4 sec/image",
        "phrases": [
            "A ring light blinds you when the door swings wide.",
            "Her laptop sits open like evidence at a trial.",
            "A profile page fills the screen with her name.",
            "Photos you were never meant to see.",
            "Subscriber counts climbing into the thousands.",
            "She spins around. Color drains from her face.",
            "Your heart stops between two beats.",
            "Neither of you speaks. Words would make this permanent.",
            "The cursor blinks waiting for your reaction.",
            "You understand the packages, money, and locked door.",
            "Every clue from the past weeks crashes into focus.",
        ],
    },
    {
        "num": 12, "act": "ACTE 3 - THE DISCOVERY", "name": "I Started An OnlyFans",
        "range": "i119-i129", "count": 11, "rhythm": "3-4 sec/image",
        "phrases": [
            "She says the words because the screen already did.",
            "I started an OnlyFans.",
            "You do not yell. Silence is worse.",
            "How long, you whisper.",
            "Three months, she answers.",
            "Three months of smiles and secrets at dinner.",
            "Why did you not tell me.",
            "I was going to, she says, tears in her eyes.",
            "I just needed the right moment.",
            "The right moment never came because you worked late.",
            "This discovery is not the end. It is the beginning.",
        ],
    },
    {
        "num": 13, "act": "ACTE 4 - CONSEQUENCES", "name": "The Neighbor Knows",
        "range": "i130-i140", "count": 11, "rhythm": "3-4 sec/image",
        "phrases": [
            "You walk outside because the walls cannot hold this.",
            "Your neighbor waters his lawn like any other day.",
            "Hey, he says. Saw your wife online last night.",
            "Congrats on the success, he adds with a grin.",
            "He laughs. You do not.",
            "Word travels faster than you imagined.",
            "Someone whispers behind you at the grocery store.",
            "A group chat screenshot reaches your cousin.",
            "You delete it. It is already too late.",
            "Inside, she edits content like nothing happened.",
            "She acts like the world did not just shift.",
        ],
    },
    {
        "num": 14, "act": "ACTE 4 - CONSEQUENCES", "name": "Work Finds Out",
        "range": "i141-i150", "count": 10, "rhythm": "3-4 sec/image",
        "phrases": [
            "Monday at the office feels like a spotlight.",
            "A coworker shows his phone with a smirk.",
            "Is this your wife, he asks loudly.",
            "Laughter spreads across the break room.",
            "Human resources calls you before lunch.",
            "We need to discuss your situation, they say.",
            "Your promotion is frozen indefinitely.",
            "You drive home gripping the steering wheel.",
            "Anger replaces shock for the first time.",
            "This is destroying everything outside these walls.",
        ],
    },
    {
        "num": 15, "act": "ACTE 4 - CONSEQUENCES", "name": "Family Dinner",
        "range": "i151-i160", "count": 10, "rhythm": "3-4 sec/image",
        "phrases": [
            "Sunday dinner at her parents feels like a trial.",
            "Her mother smiles too wide across the table.",
            "So, online business, she says slowly.",
            "Everyone at the table understands.",
            "Her father will not meet your eyes.",
            "She squeezes your hand under the tablecloth.",
            "You eat without tasting anything.",
            "In the car you finally speak.",
            "This is destroying us, you say.",
            "Then let me explain everything, she answers.",
        ],
    },
    {
        "num": 16, "act": "ACTE 5 - THE REAL SECRET", "name": "She Won't Stop",
        "range": "i161-i170", "count": 10, "rhythm": "3-4 sec/image",
        "phrases": [
            "That night you demand she stop immediately.",
            "Delete everything. Walk away from all of it.",
            "She shakes her head with terrifying certainty.",
            "I cannot. Not yet. Not until this is finished.",
            "So money matters more than us, you say.",
            "She goes quiet. That silence hurts more than shouting.",
            "You pull the honeymoon suitcase from the closet.",
            "She watches from the doorway with held-back tears.",
            "Where are you going, she asks.",
            "I do not know, you say. Anywhere but here.",
        ],
    },
    {
        "num": 17, "act": "ACTE 5 - THE REAL SECRET", "name": "The Bank Statement",
        "range": "i171-i180", "count": 10, "rhythm": "3-4 sec/image",
        "phrases": [
            "You search the dresser for your passport.",
            "Beneath folded shirts: a bank statement she hid.",
            "Past due notices highlighted in red.",
            "Mortgage payments missed. Four months.",
            "Late fees stacking like a second debt.",
            "You never knew. She handled every bill.",
            "Your hands go cold reading the numbers.",
            "We were about to lose everything, you whisper.",
            "She appears behind you silently.",
            "Please let me explain, she says softly.",
        ],
    },
    {
        "num": 18, "act": "ACTE 5 - THE REAL SECRET", "name": "The Mortgage",
        "range": "i181-i190", "count": 10, "rhythm": "3-4 sec/image",
        "phrases": [
            "She sits on the bed because her legs will not hold.",
            "I lost my job eight weeks before I started.",
            "I found foreclosure letters when you were traveling.",
            "Three months until they take our house.",
            "I panicked and searched for anything fast.",
            "OnlyFans was the only door that opened quickly.",
            "Every dollar went straight to the mortgage.",
            "I was going to tell you after one more month.",
            "Would you have let me, she asks.",
            "You have no answer.",
        ],
    },
    {
        "num": 19, "act": "ACTE 6 - RETURN TO THE HOOK", "name": "He Considers Leaving",
        "range": "i191-i200", "count": 10, "rhythm": "3-4 sec/image",
        "phrases": [
            "The suitcase stays half packed by the door.",
            "You stare at the wedding photo on the wall.",
            "Messages flood your phone from every direction.",
            "Coworkers. Neighbors. Family. All wanting answers.",
            "Your career, reputation, and home hang in balance.",
            "Two paths split before you. Neither looks clean.",
            "The open door promises escape.",
            "The bedroom light promises a harder fight.",
            "Yesterday you trusted everything without asking.",
            "That version of you is gone now.",
        ],
    },
    {
        "num": 20, "act": "ACTE 6 - RETURN TO THE HOOK", "name": "She Explains Everything",
        "range": "i201-i210", "count": 10, "rhythm": "3-4 sec/image",
        "phrases": [
            "She spreads papers across the kitchen table.",
            "Seventy percent of the debt is already paid.",
            "Six more weeks to save the house.",
            "I never cheated on you, she says firmly.",
            "Not once. Not with anyone.",
            "You should have told me, you say.",
            "Would you have listened, she asks.",
            "Or told me to stop before I saved anything.",
            "Silence fills the room.",
            "You are both right. You are both wrong.",
        ],
    },
    {
        "num": 21, "act": "ACTE 6 - RETURN TO THE HOOK", "name": "Return to the Hook",
        "range": "i211-i220", "count": 10, "rhythm": "3-4 sec/image",
        "phrases": [
            "Hours later the argument returns to the hallway.",
            "The same locked door. The same tension.",
            "Your phone buzzes with another notification.",
            "Cash still sits on the kitchen table.",
            "The neighbor's porch light clicks on.",
            "You understand the cold open now.",
            "Every image from the start makes sense.",
            "She reaches toward you with tears on her cheeks.",
            "Your hands shake. Rage or grief, you cannot tell.",
            "I never wanted you to find out like this.",
        ],
    },
    {
        "num": 22, "act": "ACTE 7 - THE CHOICE", "name": "The Ultimatum",
        "range": "i221-i230", "count": 10, "rhythm": "3-4 sec/image",
        "phrases": [
            "Morning after a night on the couch.",
            "She sets coffee in front of you.",
            "I will stop today, she says, if you need that.",
            "We lose the house in six weeks.",
            "Or I finish six weeks. Then I am done forever.",
            "Two options. Neither one is clean.",
            "You look at the wedding photo.",
            "Then at the door where your suitcase waits.",
            "Your career is already damaged.",
            "Your marriage might still be salvageable. Maybe.",
        ],
    },
    {
        "num": 23, "act": "ACTE 7 - THE CHOICE", "name": "Her Final Words",
        "range": "i231-i240", "count": 10, "rhythm": "3-4 sec/image",
        "phrases": [
            "She stands calmly. No more crying.",
            "Without this money, she says quietly.",
            "We lose the house.",
            "You look up. Everything collides at once.",
            "Trust. Pride. Fear. Love. Shame.",
            "You open your mouth.",
            "Maybe not physically, you say.",
            "She steps back like you hit her.",
            "Neither of you explains what that means.",
            "The question hangs. The video refuses to answer.",
        ],
    },
    {
        "num": 24, "act": "ACTE 7 - THE CHOICE", "name": "Black Screen",
        "range": "i241-i250", "count": 10, "rhythm": "3-5 sec/image",
        "phrases": [
            "The kitchen goes silent.",
            "Coffee steam rises between you.",
            "She does not move.",
            "You do not move.",
            "No music swells.",
            "No narrator explains.",
            "No easy answer appears.",
            "Black screen.",
            "Hold.",
            "What would you have done.",
        ],
    },
]

FLOW_STYLE = (
    "16:9, stick-figure-plus cartoon, clean white background, "
    "consistent character references, black outlines, no text in image"
)

CHAR_BIBLE = [
    "Husband (POV): 32 years old, short brown hair, blue work shirt or grey home t-shirt, tired eyes, consistent stick-figure design.",
    "Wife: 29 years old, mid-length blonde hair, casual home dress or content-creator outfit (suggestive never explicit), smile that fades across acts.",
    "Neighbor: 45 years old, polo shirt, judgmental expression.",
    "Mother-in-law: 55 years old, blouse, forced polite smile.",
    "HR Manager: 40 years old, office attire, neutral stern face.",
    "Recurring objects: ring light, shipping boxes, laptop, mortgage letters, wedding photo, half-packed suitcase, kitchen table cash.",
    "Avoid generated text inside images; add titles, dates, amounts, and app names in post-production only.",
]

DISCLAIMER = (
    "Fiction POV inspired by real social dynamics. Names, characters, specific events, "
    "financial details, and workplace responses are narrative devices. This video does not "
    "depict real people. OnlyFans is referenced as a plot element only; no explicit content "
    "is shown or described."
)


def word_count(text: str) -> int:
    return len(text.split())


def vo_duration(words: int, wps: float = 2.5) -> float:
    return words / wps


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="CoverTitle", parent=styles["Title"], fontSize=16, leading=20, spaceAfter=12,
    ))
    styles.add(ParagraphStyle(
        name="SectionHead", parent=styles["Heading1"], fontSize=13, leading=16,
        textColor=colors.HexColor("#1a1a1a"), spaceBefore=14, spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="SceneHead", parent=styles["Heading2"], fontSize=11, leading=14,
        textColor=colors.HexColor("#333333"), spaceBefore=10, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="BodySmall", parent=styles["Normal"], fontSize=9, leading=12,
    ))
    styles.add(ParagraphStyle(
        name="Meta", parent=styles["Normal"], fontSize=8, leading=10,
        textColor=colors.HexColor("#555555"),
    ))
    styles.add(ParagraphStyle(
        name="ProdBullet", parent=styles["Normal"], fontSize=8.5, leading=11,
        leftIndent=12, bulletIndent=0,
    ))
    return styles


def scene_meta(scene: dict) -> str:
    words = sum(word_count(p) for p in scene["phrases"])
    dur = vo_duration(words)
    return (
        f"{scene['act']} | {scene['range']} | {scene['count']} images | "
        f"{words} words | VO ~{dur:.1f}s | {scene['rhythm']}"
    )


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.grey)
    canvas.drawString(0.75 * inch, 0.5 * inch, "Bubbello - Production Script")
    canvas.drawRightString(7.75 * inch, 0.5 * inch, f"Page {doc.page}")
    canvas.restoreState()


def main():
    total_words = sum(word_count(p) for s in SCENES for p in s["phrases"])
    total_images = sum(s["count"] for s in SCENES)
    total_vo = vo_duration(total_words)

    doc = SimpleDocTemplate(
        OUTPUT, pagesize=letter,
        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
        topMargin=0.75 * inch, bottomMargin=0.75 * inch,
    )
    styles = build_styles()
    story = []

    # ── COVER ──
    story.append(Paragraph("BUBBELLO", styles["CoverTitle"]))
    story.append(Paragraph(
        "POV: Your Life As The Husband Of An OnlyFans Wife",
        styles["CoverTitle"],
    ))
    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph(
        "Script complet scene par scene + Voice-Over + organisation Google Flow",
        styles["BodySmall"],
    ))
    story.append(Paragraph(
        f"{total_images} images | {len(SCENES)} complete scenes | {len(SCENES)} VO blocks | "
        f"~{total_vo / 60:.1f} min VO | ~13-14 min visual target",
        styles["BodySmall"],
    ))
    story.append(PageBreak())

    # ── SPECS ──
    story.append(Paragraph("SPECIFICATIONS TECHNIQUES", styles["SectionHead"]))
    specs = [
        ["Titre YouTube", "POV: Your Life As The Husband Of An OnlyFans Wife"],
        ["Format", "POV storytime animation - stick-figure-plus / cartoon minimaliste"],
        ["Total images", f"{total_images} images (i1 a i{total_images})"],
        ["Scenes", f"{len(SCENES)} scenes completes"],
        ["Voice-over", f"{len(SCENES)} blocs | {total_words} mots | ~{total_vo / 60:.1f} min a 2.5 mots/sec"],
        ["Duree visuelle cible", "~13-14 min"],
        ["Hook", "i1-i30 | 30 images | 1 a 2 sec/image"],
        ["Corps", f"i31-i{total_images} | {total_images - 30} images | moyenne ~3.4 sec/image"],
    ]
    t = Table(specs, colWidths=[1.6 * inch, 5.2 * inch])
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.15 * inch))

    story.append(Paragraph("REGLES DE PRODUCTION", styles["SectionHead"]))
    rules = [
        "1 phrase = 1 image, sans exception.",
        "Chaque bloc VO contient une scene complete seulement.",
        "Ne jamais couper une scene au milieu pour changer de voix.",
        "Chaque bloc VO reste sous 40 secondes.",
        "1 scene = 1 bloc VO = 1 lot Flow.",
        "Chaque lot Flow contient 10 ou 11 images, donc jamais plus de 16.",
        "Le hook utilise des images tres rapides, puis le reste est reparti de facon reguliere.",
        "Aucun contenu explicite dans les images ou la narration.",
    ]
    for r in rules:
        story.append(Paragraph(f"• {r}", styles["ProdBullet"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph("DISCLAIMER NARRATIF", styles["SectionHead"]))
    story.append(Paragraph(DISCLAIMER, styles["BodySmall"]))
    story.append(PageBreak())

    # ── INDEX ──
    story.append(Paragraph("INDEX GENERAL DES SCENES", styles["SectionHead"]))
    idx_data = [["Scene", "Acte", "Nom", "Images", "Mots", "VO", "Rythme"]]
    for s in SCENES:
        w = sum(word_count(p) for p in s["phrases"])
        idx_data.append([
            f"{s['num']:02d}", s["act"], s["name"], s["range"],
            str(w), f"~{vo_duration(w):.1f}s", s["rhythm"],
        ])
    idx_table = Table(idx_data, colWidths=[0.45 * inch, 1.35 * inch, 1.2 * inch, 0.75 * inch, 0.45 * inch, 0.55 * inch, 0.85 * inch])
    idx_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f9f9f9")]),
    ]))
    story.append(idx_table)
    story.append(PageBreak())

    # ── PARTIE A ──
    story.append(Paragraph("PARTIE A - SCRIPT COMPLET IMAGE PAR IMAGE", styles["SectionHead"]))
    story.append(Paragraph("Regle: chaque ligne ci-dessous correspond exactement a une image.", styles["Meta"]))
    story.append(Spacer(1, 0.1 * inch))

    img_counter = 0
    for s in SCENES:
        story.append(Paragraph(
            f"SCENE {s['num']:02d} - {s['name']}",
            styles["SceneHead"],
        ))
        story.append(Paragraph(scene_meta(s), styles["Meta"]))
        rows = [["Image", "Phrase / image prompt"]]
        for phrase in s["phrases"]:
            img_counter += 1
            rows.append([f"i{img_counter}", phrase])
        tbl = Table(rows, colWidths=[0.55 * inch, 6.25 * inch])
        tbl.setStyle(TableStyle([
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("GRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
        ]))
        story.append(tbl)
        story.append(Spacer(1, 0.08 * inch))
    story.append(PageBreak())

    # ── PARTIE B ──
    story.append(Paragraph("PARTIE B - SCRIPTS VOICE-OVER (ELEVENLABS)", styles["SectionHead"]))
    story.append(Paragraph(
        "REGLE: chaque bloc = une scene complete. Aucun bloc ne depasse 40 secondes.",
        styles["Meta"],
    ))
    story.append(Spacer(1, 0.1 * inch))

    for s in SCENES:
        words = sum(word_count(p) for p in s["phrases"])
        story.append(Paragraph(f"SCENE {s['num']:02d} - {s['name']}", styles["SceneHead"]))
        story.append(Paragraph(scene_meta(s), styles["Meta"]))
        vo_text = " ".join(s["phrases"])
        story.append(Paragraph(vo_text, styles["BodySmall"]))
        story.append(Spacer(1, 0.1 * inch))
    story.append(PageBreak())

    # ── PARTIE C ──
    story.append(Paragraph("PARTIE C - ORGANISATION GOOGLE FLOW", styles["SectionHead"]))
    story.append(Paragraph(
        "1 lot Flow = 1 scene complete = 1 bloc VO. Maximum autorise: 16 images.",
        styles["Meta"],
    ))
    story.append(Spacer(1, 0.1 * inch))

    img_counter = 0
    for s in SCENES:
        story.append(Paragraph(f"SCENE {s['num']:02d} - {s['name']}", styles["SceneHead"]))
        story.append(Paragraph(scene_meta(s), styles["Meta"]))
        story.append(Paragraph(
            f"Prompt Flow: Generate {s['count']} separate images ({FLOW_STYLE}).",
            styles["BodySmall"],
        ))
        for phrase in s["phrases"]:
            img_counter += 1
            story.append(Paragraph(f"• i{img_counter} {phrase}", styles["ProdBullet"]))
        story.append(Spacer(1, 0.08 * inch))
    story.append(PageBreak())

    # ── INDEX FLOW ──
    story.append(Paragraph("INDEX FLOW - VUE RAPIDE", styles["SectionHead"]))
    flow_data = [["Lot", "Scene", "Acte", "Images", "Nb", "VO lie", "Rythme"]]
    for s in SCENES:
        flow_data.append([
            f"Flow {s['num']:02d}", s["name"], s["act"], s["range"],
            str(s["count"]), f"VO {s['num']:02d}", s["rhythm"],
        ])
    ft = Table(flow_data, colWidths=[0.55 * inch, 1.1 * inch, 1.35 * inch, 0.75 * inch, 0.35 * inch, 0.55 * inch, 0.85 * inch])
    ft.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(ft)
    story.append(PageBreak())

    # ── PARTIE D ──
    story.append(Paragraph("PARTIE D - BIBLE VISUELLE ET ELEMENTS FICTIONNELS", styles["SectionHead"]))
    story.append(Paragraph("Elements volontairement fictionnels", styles["SceneHead"]))
    fiction = [
        "Tous les personnages, noms, entreprises et evenements specifiques.",
        "Les montants financiers, delais de foreclosure et reponses RH.",
        "Les dialogues prives et pensees du mari (POV).",
        "La chronologie exacte des discoveries et notifications.",
    ]
    for f in fiction:
        story.append(Paragraph(f"• {f}", styles["ProdBullet"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph("BIBLE VISUELLE FLOW", styles["SceneHead"]))
    for c in CHAR_BIBLE:
        story.append(Paragraph(f"• {c}", styles["ProdBullet"]))
    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph("STRUCTURE NARRATIVE - OPEN LOOPS", styles["SceneHead"]))
    loops = [
        "LOOP 1 - Qu'est-ce qu'elle cache ? → Ferme Scene 12",
        "LOOP 2 - Le mariage va-t-il survivre ? → Ouvert jusqu'a Scene 24",
        "LOOP 3 - Qui va le decouvrir ? → Ferme Scene 14",
        "LOOP 4 - Pourquoi refuse-t-elle d'arreter ? → Ferme Scene 18",
        "LOOP 5 - A sa place, que ferais-tu ? → Jamais ferme (fin debatable)",
    ]
    for lo in loops:
        story.append(Paragraph(f"• {lo}", styles["ProdBullet"]))
    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph("FIN DE LA PRODUCTION", styles["SceneHead"]))
    story.append(Paragraph(
        "La video se termine sur un ecran noir sans resolution. "
        "Objectif commentaires: debat 50/50 Team Husband vs Team Wife.",
        styles["BodySmall"],
    ))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"PDF generated: {OUTPUT}")
    print(f"Total images: {total_images}, Total words: {total_words}, VO: {total_vo:.1f}s")


if __name__ == "__main__":
    main()
