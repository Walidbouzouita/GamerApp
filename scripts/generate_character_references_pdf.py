#!/usr/bin/env python3
"""Generate Character Reference PDF for OF Wife POV - Bubbello style."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUTPUT = "/workspace/POV-Husband-OF-Wife-Character-References.pdf"

# ??? GLOBAL STYLE ???????????????????????????????????????????????????????????
GLOBAL_STYLE = {
    "name": "BUBBELLO POV STYLE",
    "rules": [
        "2D minimalist storytime animation, thick black outlines, flat cel colors.",
        "Large expressive eyes, stylized proportions (slightly large head, slender limbs).",
        "Clean white or very light neutral background on every character sheet.",
        "16:9 aspect ratio for character sheets and scene images.",
        "No photorealism. No 3D. No anime. No stick-figure-only - use Sister/Brother channel style.",
        "No readable text inside generated images (labels added in post only).",
        "No explicit nudity. Content-creator outfits are suggestive silhouettes only, never graphic.",
        "Same character design must stay identical across all 250 scene images.",
    ],
    "flow_suffix": (
        "2D minimalist storytime animation, thick black outlines, flat colors, "
        "clean white background, expressive cartoon eyes, 16:9, no text in image"
    ),
}

# ??? CHARACTERS ?????????????????????????????????????????????????????????????
CHARACTERS = [
    {
        "id": "HUSBAND",
        "role": "POV protagonist - the husband",
        "age": "32",
        "bullets": [
            "EARLY 30s.",
            "POV PROTAGONIST.",
            "OFFICE WORKER - ALWAYS TIRED.",
            "MISSED THE SIGNS.",
            "LOVES HER BUT PRIDE GETS IN THE WAY.",
        ],
        "design": [
            "Short messy brown hair, light stubble optional.",
            "Medium skin tone, average build (not muscular).",
            "Default outfit A: light blue button-up work shirt, dark trousers.",
            "Default outfit B: grey t-shirt and sweatpants at home.",
            "Wedding band on left hand (small gold circle, no detail text).",
        ],
        "expressions": [
            ("LOVING", "soft smile, relaxed eyebrows, holding coffee mug"),
            ("OBLIVIOUS", "tired half-lidded eyes, loosened tie, office fatigue"),
            ("SHOCKED", "wide white eyes, small pupils, mouth slightly open, pale face"),
            ("DEVASTATED", "dark circles under eyes, hollow stare, slumped shoulders"),
        ],
        "props": ["smartphone", "car keys", "half-packed suitcase", "wedding photo frame"],
        "flow_sheet_prompt": """Character reference sheet titled HUSBAND. 2D minimalist storytime animation character sheet, thick black outlines, flat colors, clean white background, 16:9.

LEFT SIDE - full body: man age 32, short messy brown hair, medium skin, average build, light blue work shirt, dark trousers, white sneakers, wedding band on left hand, holding smartphone, neutral tired expression.

RIGHT SIDE - four expression headshots in a row:
1. LOVING - soft smile, relaxed eyebrows
2. OBLIVIOUS - tired half-lidded eyes, loosened tie
3. SHOCKED - wide eyes, mouth open, pale face
4. DEVASTATED - dark circles, hollow exhausted eyes

BOTTOM - small prop icons: smartphone, car keys, suitcase, wedding photo frame.

Style: same as YouTube POV storytime animation, Sister character sheet style, thick outlines, no text, no photorealism.""",
        "flow_tag": (
            "HUSBAND: man 32, short messy brown hair, medium skin, average build, "
            "blue work shirt or grey home t-shirt, wedding band, tired expressive eyes"
        ),
    },
    {
        "id": "THE WIFE",
        "role": "Wife - content creator (glamorous 2000s-inspired design)",
        "age": "29",
        "bullets": [
            "LATE 20s.",
            "GLAMOROUS 2000s-INSPIRED LOOK.",
            "CONTENT CREATOR.",
            "HIDING A MORTGAGE SECRET.",
            "HUSBAND DOES NOT KNOW UNTIL ACT 3.",
        ],
        "design": [
            "Named THE WIFE on all reference sheets - do not use real-person names in prompts.",
            "Voluminous honey-blonde wavy hair, long layers, side-swept bangs.",
            "Warm tan skin, full lips, defined cheekbones, glamorous but cartoon proportions.",
            "Athletic toned silhouette (stylized, not photorealistic).",
            "Outfit A (home): cream oversized sweater, black leggings, barefoot or white socks.",
            "Outfit B (creator): black crop top, high-waist jeans, ring light nearby - suggestive never explicit.",
            "Small gold hoop earrings optional.",
        ],
        "expressions": [
            ("LOVING", "warm bright smile, morning energy, holding laptop"),
            ("HIDING", "eyes glancing away, phone turned toward chest, nervous half-smile"),
            ("DEFENSIVE", "calm firm stare, arms crossed, chin raised"),
            ("BROKEN", "tears on cheeks, reaching hands forward, red rimmed eyes"),
        ],
        "props": ["ring light on tripod", "laptop", "shipping box labeled EQUIPMENT", "mortgage letter envelope"],
        "flow_sheet_prompt": """Character reference sheet titled THE WIFE. 2D minimalist storytime animation character sheet, thick black outlines, flat colors, clean white background, 16:9.

LEFT SIDE - full body: woman age 29 named THE WIFE, voluminous honey-blonde wavy hair with long layers, warm tan skin, full lips, defined cheekbones, athletic toned stylized figure, cream oversized sweater, black leggings, white socks, warm smile, holding laptop.

RIGHT SIDE - four expression headshots in a row:
1. LOVING - warm bright smile, relaxed eyes
2. HIDING - nervous eyes, phone held close to chest
3. DEFENSIVE - firm stare, arms crossed
4. BROKEN - tears, reaching hands, red rimmed eyes

BOTTOM - small prop icons: ring light on tripod, laptop, cardboard box, sealed envelope.

Glamorous early-2000s inspired cartoon woman. Not photorealistic. Not a real person. No nudity. No text in image. Same style as POV Sister character sheet.""",
        "flow_tag": (
            "THE WIFE: woman 29, voluminous honey-blonde wavy hair, warm tan skin, "
            "full lips, defined cheekbones, cream sweater or black crop top with jeans, "
            "glamorous cartoon proportions, gold hoop earrings"
        ),
        "variants": [
            {
                "id": "THE_WIFE_HOME",
                "file": "character-ref-the-wife.png",
                "scenes": "04-06, 19-20, 22-24",
                "outfit": "cream oversized sweater, black leggings",
                "flow_tag": "THE WIFE HOME: cream sweater, black leggings, warm smile",
            },
            {
                "id": "THE_WIFE_CREATOR",
                "file": "character-ref-the-wife-creator.png",
                "scenes": "07-09, 16",
                "outfit": "black cropped halter top, high-waist jeans, ring light",
                "flow_tag": "THE WIFE CREATOR: black crop halter, high-waist jeans, ring light, confident smirk",
            },
            {
                "id": "THE_WIFE_PERFORMING",
                "file": "character-ref-the-wife-performing.png",
                "scenes": "10-12, 21",
                "outfit": "black crop top, fitted shorts, ring light, phone selfie",
                "flow_tag": "THE WIFE PERFORMING: black crop top, ring light glow, performing for camera, flirty",
            },
            {
                "id": "THE_WIFE_NIGHT",
                "file": "character-ref-the-wife-night.png",
                "scenes": "08, 10-11, 20-21",
                "outfit": "black fitted tank top, yoga pants, barefoot, office at night",
                "flow_tag": "THE WIFE NIGHT: black tank top, yoga pants, ring light, secretive shush gesture",
            },
            {
                "id": "THE_WIFE_GLAMOUR",
                "file": "character-ref-the-wife-glamour.png",
                "scenes": "13, 15, 17-18, 23",
                "outfit": "black cowl halter crop, low-rise flared jeans, heels",
                "flow_tag": "THE WIFE GLAMOUR: black halter crop top, low-rise jeans, heels, glamorous 2000s look",
            },
        ],
    },
    {
        "id": "NEIGHBOR",
        "role": "Suburban neighbor - social embarrassment trigger",
        "age": "45",
        "bullets": [
            "MID 40s.",
            "SUBURBAN DAD ENERGY.",
            "JUDGMENTAL BUT FRIENDLY ON THE SURFACE.",
            "SAW THE WIFE ONLINE.",
        ],
        "design": [
            "Short receding brown hair, slight dad-bod, friendly-but-smug face.",
            "Polo shirt (light green or blue), khaki shorts, lawn care vibe.",
            "Holding garden hose or phone casually.",
        ],
        "expressions": [
            ("FRIENDLY", "casual wave, watering lawn"),
            ("CURIOUS", "raised eyebrow, showing phone screen"),
            ("SMUG", "knowing grin, arms crossed"),
        ],
        "props": ["garden hose", "smartphone", "lawn"],
        "flow_sheet_prompt": """Character reference sheet titled NEIGHBOR. 2D minimalist storytime animation, thick black outlines, flat colors, white background, 16:9.

Full body: man age 45, short receding brown hair, dad-bod, light green polo shirt, khaki shorts, white sneakers, holding garden hose, suburban lawn background minimal.

Three expression headshots: FRIENDLY wave, CURIOUS raised eyebrow with phone, SMUG knowing grin.

No text in image. POV storytime style.""",
        "flow_tag": (
            "NEIGHBOR: man 45, receding brown hair, dad-bod, green polo shirt, "
            "khaki shorts, smug or friendly expression"
        ),
    },
    {
        "id": "MOTHER_IN_LAW",
        "role": "Wife's mother - passive-aggressive family pressure",
        "age": "55",
        "bullets": [
            "MID 50s.",
            "POLITE ON THE OUTSIDE.",
            "EVERYONE KNOWS WHAT ONLINE BUSINESS MEANS.",
            "FAMILY DINNER SCENE ONLY.",
        ],
        "design": [
            "Short styled grey-blonde hair, pearl earrings.",
            "Floral blouse, cardigan, dining table setting.",
            "Smile too wide - eyes tell a different story.",
        ],
        "expressions": [
            ("POLITE", "wide forced smile, hands folded"),
            ("PASSIVE-AGGRESSIVE", "tight smile, one raised eyebrow"),
            ("DISAPPOINTED", "looking down, lips pressed thin"),
        ],
        "props": ["dining table", "wine glass", "family dinner plates"],
        "flow_sheet_prompt": """Character reference sheet titled MOTHER IN LAW. 2D minimalist storytime animation, thick black outlines, flat colors, white background, 16:9.

Full body: woman age 55, short grey-blonde hair, pearl earrings, floral blouse, beige cardigan, black slacks, forced polite smile, standing beside dining table.

Three expression headshots: POLITE wide smile, PASSIVE-AGGRESSIVE tight smile with raised eyebrow, DISAPPOINTED looking down.

No text in image. POV storytime style.""",
        "flow_tag": (
            "MOTHER IN LAW: woman 55, grey-blonde hair, pearl earrings, "
            "floral blouse, cardigan, forced polite smile"
        ),
    },
    {
        "id": "FATHER_IN_LAW",
        "role": "Wife's father - silent shame",
        "age": "58",
        "bullets": [
            "LATE 50s.",
            "QUIET AT FAMILY DINNER.",
            "WILL NOT MEET HUSBAND'S EYES.",
            "BACKGROUND FAMILY SCENE ONLY.",
        ],
        "design": [
            "Grey hair, glasses, plain button-up shirt.",
            "Sitting at dinner table, looking down at plate.",
            "Minimal presence - shame through body language.",
        ],
        "expressions": [
            ("NEUTRAL", "reading glasses, calm face"),
            ("AVOIDANT", "eyes looking down, uncomfortable"),
        ],
        "props": ["dinner plate", "water glass"],
        "flow_sheet_prompt": """Character reference sheet titled FATHER IN LAW. 2D minimalist storytime animation, thick black outlines, flat colors, white background, 16:9.

Full body: man age 58, grey hair, reading glasses, navy button-up shirt, sitting at dining table, looking down at plate, uncomfortable body language.

Two expression headshots: NEUTRAL calm, AVOIDANT eyes down.

No text in image. POV storytime style.""",
        "flow_tag": (
            "FATHER IN LAW: man 58, grey hair, glasses, navy shirt, "
            "sitting at dinner table, avoidant downward gaze"
        ),
    },
    {
        "id": "COWORKER",
        "role": "Office coworker - public humiliation",
        "age": "30",
        "bullets": [
            "EARLY 30s.",
            "BREAK ROOM SCENE ONLY.",
            "SHOWS PHONE TO EVERYONE.",
            "REPRESENTS WORKPLACE FALLOUT.",
        ],
        "design": [
            "Neat short black hair, office badge on lanyard.",
            "White dress shirt, no tie, holding phone toward camera.",
            "Smirk - not evil, just insensitive.",
        ],
        "expressions": [
            ("SMIRK", "one eyebrow raised, showing phone"),
            ("LAUGHING", "open mouth laugh, pointing at phone"),
        ],
        "props": ["smartphone", "office badge", "break room coffee machine"],
        "flow_sheet_prompt": """Character reference sheet titled COWORKER. 2D minimalist storytime animation, thick black outlines, flat colors, white background, 16:9.

Full body: man age 30, neat short black hair, white office shirt, lanyard badge, holding smartphone toward viewer, smirk expression.

Two expression headshots: SMIRK with raised eyebrow, LAUGHING with open mouth.

No text in image. POV storytime style.""",
        "flow_tag": (
            "COWORKER: man 30, short black hair, white office shirt, "
            "lanyard badge, smirk, holding smartphone"
        ),
    },
    {
        "id": "HR_MANAGER",
        "role": "Human resources - career threat",
        "age": "40",
        "bullets": [
            "40s.",
            "GLASS CONFERENCE ROOM SCENE ONLY.",
            "NEUTRAL CORPORATE TONE.",
            "FREEZES HUSBAND'S PROMOTION.",
        ],
        "design": [
            "Dark hair in low bun, glasses, grey blazer.",
            "Sitting across conference table, clipboard in hand.",
            "Professional, emotionless, stern but not cartoon-villain.",
        ],
        "expressions": [
            ("NEUTRAL", "stern professional face, clipboard"),
            ("SERIOUS", "slight frown, direct eye contact"),
        ],
        "props": ["clipboard", "glass conference room table"],
        "flow_sheet_prompt": """Character reference sheet titled HR MANAGER. 2D minimalist storytime animation, thick black outlines, flat colors, white background, 16:9.

Full body: woman age 40, dark hair in low bun, glasses, grey blazer, white blouse, black skirt, sitting at conference table with clipboard, stern neutral expression.

Two expression headshots: NEUTRAL professional, SERIOUS slight frown.

No text in image. POV storytime style.""",
        "flow_tag": (
            "HR MANAGER: woman 40, dark hair bun, glasses, grey blazer, "
            "clipboard, stern neutral expression"
        ),
    },
]

# Scene prompt template
SCENE_PROMPT_TEMPLATE = """Generate {count} separate images (16:9).
STYLE: {style_suffix}
CHARACTERS IN SCENE: {character_tags}
SCENE CONTEXT: {act} - {scene_name}

{image_lines}"""


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="CoverTitle", parent=styles["Title"], fontSize=16, leading=20, spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name="SectionHead", parent=styles["Heading1"], fontSize=13, leading=16,
        spaceBefore=12, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="CharHead", parent=styles["Heading2"], fontSize=12, leading=15,
        textColor=colors.HexColor("#1a1a1a"), spaceBefore=10, spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="BodySmall", parent=styles["Normal"], fontSize=9, leading=12,
    ))
    styles.add(ParagraphStyle(
        name="ProdBullet", parent=styles["Normal"], fontSize=8.5, leading=11, leftIndent=12,
    ))
    styles.add(ParagraphStyle(
        name="PromptBox", parent=styles["Code"], fontSize=7.5, leading=10,
        backColor=colors.HexColor("#f5f5f5"), leftIndent=6, rightIndent=6,
    ))
    return styles


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.grey)
    canvas.drawString(0.75 * inch, 0.5 * inch, "Bubbello - Character References")
    canvas.drawRightString(7.75 * inch, 0.5 * inch, f"Page {doc.page}")
    canvas.restoreState()


def main():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=letter,
        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
        topMargin=0.75 * inch, bottomMargin=0.75 * inch,
    )
    styles = build_styles()
    story = []

    # Cover
    story.append(Paragraph("BUBBELLO", styles["CoverTitle"]))
    story.append(Paragraph("CHARACTER REFERENCES", styles["CoverTitle"]))
    story.append(Paragraph(
        "POV: Your Life As The Husband Of An OnlyFans Wife",
        styles["CoverTitle"],
    ))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph(
        f"{len(CHARACTERS)} personnages | Style Sister/Brother | Prompts Flow inclus",
        styles["BodySmall"],
    ))
    story.append(Paragraph(
        "Generer ces fiches AVANT les 24 lots de scenes. Reutiliser les FLOW TAGS dans chaque prompt.",
        styles["BodySmall"],
    ))
    story.append(PageBreak())

    # Global style
    story.append(Paragraph("STYLE GLOBAL - REGLES CHANNEL", styles["SectionHead"]))
    for r in GLOBAL_STYLE["rules"]:
        story.append(Paragraph(f"- {r}", styles["ProdBullet"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph("SUFFIXE FLOW (ajouter a chaque prompt scene)", styles["CharHead"]))
    story.append(Preformatted(GLOBAL_STYLE["flow_suffix"], styles["PromptBox"]))
    story.append(PageBreak())

    # Index
    story.append(Paragraph("INDEX PERSONNAGES", styles["SectionHead"]))
    idx = [["ID", "Role", "Age", "Scenes principales"]]
    scene_map = {
        "HUSBAND": "Toutes (POV)",
        "THE WIFE": "Toutes",
        "NEIGHBOR": "13, 21",
        "MOTHER_IN_LAW": "15",
        "FATHER_IN_LAW": "15",
        "COWORKER": "14",
        "HR_MANAGER": "14",
    }
    for c in CHARACTERS:
        idx.append([c["id"], c["role"], c["age"], scene_map.get(c["id"], "-")])
    t = Table(idx, colWidths=[1.1 * inch, 2.5 * inch, 0.5 * inch, 1.0 * inch])
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
    ]))
    story.append(t)
    story.append(PageBreak())

    # Each character
    story.append(Paragraph("FICHES PERSONNAGES - DETAIL + PROMPTS FLOW", styles["SectionHead"]))
    for c in CHARACTERS:
        story.append(Paragraph(c["id"], styles["CharHead"]))
        story.append(Paragraph(f"{c['role']} | Age {c['age']}", styles["BodySmall"]))
        for b in c["bullets"]:
            story.append(Paragraph(f"- {b}", styles["ProdBullet"]))
        story.append(Spacer(1, 0.05 * inch))
        story.append(Paragraph("Design", styles["BodySmall"]))
        for d in c["design"]:
            story.append(Paragraph(f"- {d}", styles["ProdBullet"]))
        story.append(Spacer(1, 0.05 * inch))
        story.append(Paragraph("Expressions", styles["BodySmall"]))
        for label, desc in c["expressions"]:
            story.append(Paragraph(f"- {label} - {desc}", styles["ProdBullet"]))
        story.append(Spacer(1, 0.05 * inch))
        story.append(Paragraph(f"Props: {', '.join(c['props'])}", styles["BodySmall"]))
        story.append(Spacer(1, 0.08 * inch))
        story.append(Paragraph("FLOW TAG (copier dans chaque prompt scene)", styles["BodySmall"]))
        story.append(Preformatted(c["flow_tag"], styles["PromptBox"]))
        story.append(Spacer(1, 0.05 * inch))
        story.append(Paragraph("FLOW PROMPT - GENERER LA FICHE REFERENCE", styles["BodySmall"]))
        story.append(Preformatted(c["flow_sheet_prompt"], styles["PromptBox"]))
        if c.get("variants"):
            story.append(Spacer(1, 0.08 * inch))
            story.append(Paragraph("VARIANTES THE WIFE (par scene)", styles["BodySmall"]))
            vdata = [["Variante", "Fichier", "Scenes", "FLOW TAG"]]
            for v in c["variants"]:
                vdata.append([v["id"], v["file"], v["scenes"], v["flow_tag"]])
            vt = Table(vdata, colWidths=[1.0 * inch, 1.5 * inch, 0.7 * inch, 2.9 * inch])
            vt.setStyle(TableStyle([
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 7),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]))
            story.append(vt)
        story.append(Spacer(1, 0.15 * inch))

    story.append(PageBreak())

    # Workflow
    story.append(Paragraph("WORKFLOW DE PRODUCTION", styles["SectionHead"]))
    workflow = [
        "ETAPE 1 - Generer les 7 fiches reference (prompts ci-dessus) dans Flow.",
        "ETAPE 2 - Valider que HUSBAND et THE WIFE sont coherents sur toutes les fiches.",
        "ETAPE 3 - Uploader les fiches comme reference images dans Flow pour chaque lot.",
        "ETAPE 4 - Dans chaque prompt scene (Partie C du script), ajouter les FLOW TAGS des personnages presents.",
        "ETAPE 5 - Toujours utiliser THE WIFE (jamais de nom reel) pour eviter les blocages Flow.",
        "ETAPE 6 - Pour THE WIFE en mode creator: outfit B + ring light, jamais explicite.",
    ]
    for w in workflow:
        story.append(Paragraph(f"- {w}", styles["ProdBullet"]))

    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph("EXEMPLE PROMPT SCENE ENRICHI", styles["SectionHead"]))
    example = """Generate 10 separate images (16:9).
STYLE: 2D minimalist storytime animation, thick black outlines, flat colors, clean white background, 16:9, no text in image

CHARACTERS:
- HUSBAND: man 32, short messy brown hair, medium skin, blue work shirt, wedding band, shocked expression
- THE WIFE: woman 29, voluminous honey-blonde wavy hair, warm tan skin, black crop top, ring light glow, defensive expression

SCENE: ACTE 3 - The Screen
- i108 A ring light blinds you when the door swings wide.
- i109 Her laptop sits open on the desk like evidence at a trial.
(... etc ...)"""
    story.append(Preformatted(example, styles["PromptBox"]))

    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph("THE WIFE - NOTES IMPORTANTES", styles["SectionHead"]))
    notes = [
        "Inspiration visuelle: glamour early-2000s (cheveux volumineux, teint chaud, levres pleines).",
        "Toujours nommer THE WIFE dans les prompts - pas de nom de personne reelle.",
        "Version maison: cream sweater + black leggings (Actes 1-2).",
        "Version creator: black crop top + jeans + ring light (Actes 2-7, jamais explicite).",
        "Meme visage, meme coiffure, memes proportions sur les 250 images.",
    ]
    for n in notes:
        story.append(Paragraph(f"- {n}", styles["ProdBullet"]))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    main()
