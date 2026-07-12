#!/usr/bin/env python3
"""Generate PDF: full scene-by-scene script + VO chunks (max 40s each)."""

from fpdf import FPDF
from pathlib import Path

OUTPUT = Path("/opt/cursor/artifacts/POV-Sister-OnlyFans-Brother-Script-Complet.pdf")

TITLE = "POV: Your Life As The Sister Of An OnlyFans Brother - The Party Wasn't TikTok"

# Words per 40 seconds at ~145 wpm dramatic narration
MAX_WORDS_40S = 95

HOOK = [
    ("i1", "Your brother said he was throwing a party."),
    ("i2", "Not a normal party."),
    ("i3", 'A "brand party."'),
    ("i4", "For TikTok."),
    ("i5", "For Instagram."),
    ("i6", "Ring lights in the garage."),
    ("i7", "You thought dance videos."),
    ("i8", "You were wrong."),
    ("i9", "OnlyFans."),
    ("i10", "Fansly."),
    ("i11", "Collabs with models."),
    ("i12", "Filmed in your house."),
    ("i13", "Your kitchen."),
    ("i14", "Your hallway."),
    ("i15", "Your bathroom mirror."),
    ("i16", "POV: Your Life As The Sister Of An OnlyFans Brother."),
    ("i17", "The party wasn't TikTok."),
    ("i18", "It was a shoot."),
    ("i19", "Mom and Dad were out of town."),
    ("i20", "The house was his."),
    ("i21", '"Just creators," he said.'),
    ("i22", "Three girls arrived with equipment cases."),
    ("i23", "Tripod in the hallway."),
    ("i24", "Softbox in the kitchen."),
    ("i25", '"Stay upstairs. We\'ve got content to film."'),
    ("i26", "You googled his username that night."),
    ("i27", "The first result wasn't social media."),
    ("i28", "It was a subscription page."),
]

ACTS = [
    {
        "name": "ACTE 1 - La soiree",
        "pacing": "~3-4 sec/image",
        "images": "i29-i68",
        "duration": "~2 min 30",
        "lines": [
            ("i29", "It started on a Friday."),
            ("i30", "Mom and Dad left for a wedding in another state."),
            ("i31", "You had the house to yourself - or so you thought."),
            ("i32", "At 5:47 PM your brother texted the family group chat."),
            ("i33", '"Brand party tonight. Don\'t embarrass me."'),
            ("i34", 'You replied: "How many people?"'),
            ("i35", 'He said: "Just creators."'),
            ("i36", "You still didn't understand what that meant."),
            ("i37", "At 6 PM the doorbell rang."),
            ("i38", "A girl with a ring light stand."),
            ("i39", "Another with a rolling equipment case."),
            ("i40", "A third in a crop top and heels."),
            ('i41', '"Hey! We\'re here for the shoot!"'),
            ("i42", "Shoot. Not party."),
            ("i43", "You looked at your brother."),
            ("i44", "He was already pushing the couch against the living room wall."),
            ("i45", "Tripod in the hallway."),
            ("i46", "Softbox in the kitchen."),
            ("i47", "Backdrop taped to the staircase."),
            ("i48", "Your staircase."),
            ('i49', '"Can you stay upstairs?" he said.'),
            ('i50', '"We\'ve got content to film."'),
            ("i51", "You went to your room."),
            ("i52", "Door closed. Door locked."),
            ('i53', 'Downstairs: music, laughter, someone yelling "Action."'),
            ("i54", "You told yourself it was influencer stuff."),
            ("i55", "Brand deals. Fitness content. Nothing weird."),
            ("i56", "But the laughter didn't sound like TikTok."),
            ("i57", "It sounded like a set."),
            ("i58", "At 10 PM you needed water."),
            ("i59", "You crept downstairs."),
            ("i60", "The kitchen was empty."),
            ("i61", "The counter had makeup wipes, baby oil, and a clipboard with shot lists."),
            ("i62", "Shot lists."),
            ("i63", "Not recipes. Not homework."),
            ("i64", "Shot lists."),
            ("i65", "On the fridge: a whiteboard schedule."),
            ('i66', '"Scene 3 - Kitchen Counter - Collab with Jade."'),
            ("i67", "Jade was the girl in the crop top."),
            ("i68", "You went back upstairs without drinking anything."),
        ],
    },
    {
        "name": "ACTE 2 - La decouverte",
        "pacing": "~3-4 sec/image",
        "images": "i69-i98",
        "duration": "~1 min 45",
        "lines": [
            ("i69", "That night you googled his username."),
            ("i70", "On your laptop. Door locked. Volume off."),
            ("i71", "The first result wasn't TikTok."),
            ("i72", "It wasn't Instagram."),
            ("i73", "It was a subscription page with his face, his chain, his smile."),
            ('i74', '"Exclusive collabs with models."'),
            ("i75", "Monthly tiers. Tip menu. Custom requests."),
            ("i76", "You clicked one preview."),
            ("i77", "The background looked familiar."),
            ("i78", "Your hallway."),
            ("i79", "Your bathroom mirror."),
            ("i80", "The same towel rack Mom bought at Target."),
            ("i81", "You felt sick."),
            ("i82", "Not because of what he was doing with women."),
            ("i83", "Because he was doing it where you ate cereal."),
            ("i84", "Where Dad grilled on Sundays."),
            ("i85", "Where you used to do homework on the floor."),
            ("i86", "You scrolled down."),
            ("i87", "Fansly link in his bio."),
            ("i88", "Twitter link."),
            ("i89", 'A "management" email you had never seen.'),
            ("i90", "He wasn't a dancer."),
            ("i91", "He wasn't a fitness guy."),
            ("i92", "He was a business."),
            ("i93", "Downstairs the music got louder."),
            ('i94', 'Someone shouted "Cut!" then laughed.'),
            ("i95", "You put in earbuds."),
            ("i96", "It didn't help."),
            ("i97", "You stared at the ceiling and realized your house was a set."),
            ("i98", "And you were the only one who didn't get a call time."),
        ],
    },
    {
        "name": "ACTE 3 - Le leak iCloud",
        "pacing": "~3-4 sec/image",
        "images": "i99-i118",
        "duration": "~1 min 10",
        "lines": [
            ("i99", "At midnight your phone buzzed."),
            ("i100", "iCloud Family Sharing."),
            ("i101", "A photo backup from his phone."),
            ("i102", "Synced to YOUR camera roll."),
            ("i103", "Because you share the same Apple ID."),
            ("i104", "Mom set it up years ago."),
            ('i105', '"So we can see family photos."'),
            ("i106", "Family photos."),
            ("i107", "This wasn't family."),
            ("i108", "A preview thumbnail appeared on your lock screen."),
            ("i109", "You were half asleep."),
            ("i110", "You swiped it away."),
            ("i111", "Too slow."),
            ("i112", "Monday morning. School cafeteria."),
            ("i113", "Your phone on the table."),
            ("i114", "Your friend Maya picked it up to show you a meme."),
            ("i115", "The photo was still in your Recently Deleted."),
            ("i116", "She saw it anyway."),
            ('i117', '"Is that your brother?"'),
            ('i118', '"Is that your HOUSE?"'),
        ],
    },
    {
        "name": "ACTE 4 - La chute",
        "pacing": "~3-4 sec/image",
        "images": "i119-i145",
        "duration": "~1 min 35",
        "lines": [
            ("i119", "You snatched the phone back."),
            ("i120", "Your face was burning."),
            ("i121", "Maya's face was worse - excited, horrified, already texting."),
            ("i122", "By lunch everyone knew."),
            ('i123', '"OnlyFans party at her place."'),
            ('i124', '"Her brother films girls in their kitchen."'),
            ("i125", "Someone made a joke about your fridge."),
            ("i126", "You wanted to disappear."),
            ("i127", "Mom called during fifth period."),
            ("i128", "Dad had seen the sync too."),
            ("i129", "On his iPad."),
            ("i130", "At the wedding."),
            ("i131", "In front of your aunt, your uncle, your grandmother."),
            ("i132", "Your uncle asked questions."),
            ("i133", "Your aunt didn't."),
            ("i134", "She just stared at you like you were part of the production."),
            ('i135', 'Your brother texted: "Why is Mom blowing up my phone?"'),
            ('i136', 'You texted back: "Because your content synced to the FAMILY iCloud."'),
            ("i137", "Three dots. Then nothing."),
            ("i138", "He came home Tuesday afternoon."),
            ("i139", "No apology."),
            ('i140', '"It\'s just business," he said.'),
            ('i141', '"Fans pay. I pay rent."'),
            ('i142', '"You used our house."'),
            ('i143', '"You used our Apple ID."'),
            ("i144", "He shrugged like you were the one being dramatic."),
            ("i145", "Mom changed the family password that night."),
        ],
    },
    {
        "name": "ACTE 5 - Epilogue",
        "pacing": "~3-4 sec/image",
        "images": "i146-i160",
        "duration": "~50 sec",
        "lines": [
            ("i146", "The ring lights went back in the garage."),
            ("i147", "The whiteboard came off the fridge."),
            ("i148", "The house smelled like hairspray for another week."),
            ("i149", "Your brother still posts."),
            ("i150", "Smaller now. Different locations."),
            ('i151', '"Airbnb collabs," he calls them.'),
            ("i152", "He still wears the chain."),
            ("i153", "He still smiles like the camera is always on."),
            ("i154", "You still share a last name."),
            ("i155", "You still walk past his closed door."),
            ("i156", "You still hear notification sounds at 2 AM."),
            ("i157", "He never said sorry."),
            ("i158", "You never asked him to."),
            ("i159", "Some things don't get fixed with a password change."),
            ("i160", "The party wasn't TikTok."),
        ],
    },
]


def word_count(text: str) -> int:
    return len(text.split())


def estimate_seconds(text: str, wpm: float = 145) -> float:
    return (word_count(text) / wpm) * 60


def build_vo_chunks():
    """Split all narration into VO parts <= 40 seconds (~97 words)."""
    all_lines = list(HOOK)
    for act in ACTS:
        all_lines.extend(act["lines"])

    chunks = []
    current_lines = []
    current_words = 0
    part_num = 1
    start_id = None

    for img_id, line in all_lines:
        w = word_count(line)
        if current_lines and current_words + w > MAX_WORDS_40S:
            chunks.append(
                {
                    "part": part_num,
                    "start": start_id,
                    "end": current_lines[-1][0],
                    "lines": current_lines,
                    "text": " ".join(t for _, t in current_lines),
                    "words": current_words,
                    "seconds": round(estimate_seconds(" ".join(t for _, t in current_lines)), 1),
                }
            )
            part_num += 1
            current_lines = []
            current_words = 0
            start_id = None

        if start_id is None:
            start_id = img_id
        current_lines.append((img_id, line))
        current_words += w

    if current_lines:
        chunks.append(
            {
                "part": part_num,
                "start": start_id,
                "end": current_lines[-1][0],
                "lines": current_lines,
                "text": " ".join(t for _, t in current_lines),
                "words": current_words,
                "seconds": round(estimate_seconds(" ".join(t for _, t in current_lines)), 1),
            }
        )

    return chunks


class ScriptPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, TITLE[:70] + "...", align="C", new_x="LMARGIN", new_y="NEXT")
            self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def section_title(self, title: str, size: int = 14):
        self.ln(4)
        self.set_font("Helvetica", "B", size)
        self.set_text_color(20, 20, 20)
        self.set_x(self.l_margin)
        self.multi_cell(self.epw, 8, title)
        self.ln(2)

    def sub_title(self, title: str):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(40, 40, 40)
        self.set_x(self.l_margin)
        self.multi_cell(self.epw, 6, title)
        self.ln(1)

    def body_text(self, text: str, size: int = 10):
        self.set_font("Helvetica", "", size)
        self.set_text_color(30, 30, 30)
        self.set_x(self.l_margin)
        self.multi_cell(self.epw, 5, text)

    def meta_line(self, text: str):
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(80, 80, 80)
        self.set_x(self.l_margin)
        self.multi_cell(self.epw, 5, text)
        self.ln(1)

    def scene_line(self, img_id: str, line: str):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(0, 80, 160)
        self.cell(18, 5, img_id)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(self.epw - 18, 5, line)
        self.ln(0.5)


def generate_pdf():
    pdf = ScriptPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(20, 20, 20)

    # --- COVER ---
    pdf.add_page()
    pdf.ln(30)
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(20, 20, 20)
    pdf.multi_cell(0, 10, TITLE, align="C")
    pdf.ln(8)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(
        0,
        7,
        "Script complet scene par scene + scripts Voice-Over (ElevenLabs)\n"
        "160 images | ~8 min 20 | Hook rapide (30 sec) + corps lent (3-4 sec/image)",
        align="C",
    )
    pdf.ln(15)
    pdf.set_font("Helvetica", "I", 10)
    pdf.multi_cell(
        0,
        6,
        "PARTIE A : Script image par image (i1-i160)\n"
        "PARTIE B : Scripts VO decoupes (max 40 secondes chacun)",
        align="C",
    )

    # --- TECH SPECS ---
    pdf.add_page()
    pdf.section_title("SPECIFICATIONS TECHNIQUES", 13)
    specs = [
        "Titre YouTube : " + TITLE,
        "Format : POV storytime animation (stick figure minimaliste)",
        "Total images : 160 (i1 a i160)",
        "Duree estimee : ~8 min 20",
        "",
        "RYTHME MONTAGE :",
        "  Hook (i1-i28) : 1 a 1,2 sec par image (~30 sec)",
        "  Corps (i29-i160) : 3 a 4 sec par image",
        "",
        "PERSONNAGES :",
        "  SISTER (POV) | BROTHER (gattouz0 inspired) | MOTHER | FATHER",
        "  MODEL 1 (Jade) | MODEL 2 | MAYA (classmate)",
        "",
        "PLATEFORMES MENTIONNEES : OnlyFans, Fansly, TikTok, Instagram, Twitter",
    ]
    for s in specs:
        if not s.strip():
            pdf.ln(2)
        else:
            pdf.body_text(s)

    # --- PARTIE A ---
    pdf.add_page()
    pdf.section_title("PARTIE A - SCRIPT COMPLET SCENE PAR SCENE", 14)
    pdf.meta_line("1 phrase = 1 image. Copier chaque ligne pour les prompts Flow.")

    # Hook section
    pdf.sub_title("HOOK RAPIDE - i1 a i28 (~30 sec | 1-1,2 sec/image)")
    for img_id, line in HOOK:
        pdf.scene_line(img_id, line)

    for act in ACTS:
        pdf.ln(3)
        pdf.sub_title(f"{act['name']} | {act['images']} | {act['duration']} | {act['pacing']}")
        for img_id, line in act["lines"]:
            pdf.scene_line(img_id, line)

    # --- PARTIE B ---
    vo_chunks = build_vo_chunks()
    pdf.add_page()
    pdf.section_title("PARTIE B - SCRIPTS VOICE-OVER (ELEVENLABS)", 14)
    pdf.meta_line(
        f"Chaque bloc fait maximum 40 secondes (~{MAX_WORDS_40S} mots a 145 mots/min).\n"
        "Generer un fichier audio par bloc. Coller le texte tel quel dans ElevenLabs."
    )
    pdf.ln(2)
    pdf.body_text(f"Nombre total de blocs VO : {len(vo_chunks)}")
    pdf.ln(3)

    for chunk in vo_chunks:
        pdf.sub_title(
            f"VO PART {chunk['part']} - {chunk['start']} a {chunk['end']} "
            f"| ~{chunk['seconds']} sec | {chunk['words']} mots"
        )
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(30, 30, 30)
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(pdf.epw, 5, chunk["text"])
        pdf.ln(4)
        if pdf.get_y() > 250:
            pdf.add_page()

    # --- VO INDEX TABLE ---
    pdf.add_page()
    pdf.section_title("INDEX DES BLOCS VO", 13)
    pdf.set_font("Helvetica", "B", 9)
    pdf.cell(25, 7, "Bloc", border=1)
    pdf.cell(30, 7, "Images", border=1)
    pdf.cell(25, 7, "Mots", border=1)
    pdf.cell(25, 7, "Duree", border=1)
    pdf.cell(0, 7, "Contenu (debut)", border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 8)
    for chunk in vo_chunks:
        preview = chunk["text"][:55] + "..." if len(chunk["text"]) > 55 else chunk["text"]
        pdf.cell(25, 6, f"VO Part {chunk['part']}", border=1)
        pdf.cell(30, 6, f"{chunk['start']}-{chunk['end']}", border=1)
        pdf.cell(25, 6, str(chunk["words"]), border=1)
        pdf.cell(25, 6, f"~{chunk['seconds']}s", border=1)
        pdf.cell(0, 6, preview, border=1, new_x="LMARGIN", new_y="NEXT")

    pdf.output(str(OUTPUT))
    return OUTPUT, vo_chunks


if __name__ == "__main__":
    path, chunks = generate_pdf()
    print(f"PDF genere : {path}")
    print(f"Blocs VO : {len(chunks)}")
    for c in chunks:
        print(f"  Part {c['part']}: {c['start']}-{c['end']} | {c['words']} mots | ~{c['seconds']}s")
