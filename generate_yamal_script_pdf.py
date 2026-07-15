#!/usr/bin/env python3
"""Generate PDF: Lamine Yamal Little Brother World Cup 2026 - full script + VO + Flow."""

from fpdf import FPDF
from pathlib import Path

OUTPUT = Path("/opt/cursor/artifacts/POV-Lamine-Yamal-Little-Brother-Script-Complet.pdf")
WORKSPACE_OUTPUT = Path("/workspace/POV-Lamine-Yamal-Little-Brother-Script-Complet.pdf")

TITLE = "POV: Your Life As Lamine Yamal's Little Brother - The World Cup Changed Everything"

HOOK_SEC_PER_LINE = 1.5
BODY_SEC_PER_LINE = 3.5
MAX_LINES_40S = 11  # ~38 sec at 3.5 sec/line (corps)

HOOK = [
    ("i1", "July 14th."),
    ("i2", "Bastille Day."),
    ("i3", "French Republic Day."),
    ("i4", "France was playing Spain."),
    ("i5", "In Dallas."),
    ("i6", "AT&T Stadium."),
    ("i7", "Eighty thousand people."),
    ("i8", "So loud I covered my ears."),
    ("i9", "France lost."),
    ("i10", "Zero. Two."),
    ("i11", "Oyarzabal scored a penalty."),
    ("i12", "Porro scored the second."),
    ("i13", "My brother Lamine didn't score."),
    ("i14", "But he won the penalty."),
    ("i15", "The day after his birthday."),
    ("i16", "July 13th."),
    ("i17", "He turned nineteen."),
    ("i18", "I am three."),
    ("i19", "Almost four."),
    ("i20", "When the whistle blew, I ran."),
    ("i21", "He picked me up."),
    ("i22", "The cameras found me again."),
    ("i23", "But this story didn't start in Dallas."),
    ("i24", "It started in Atlanta."),
    ("i25", "June 15th."),
    ("i26", "Our first match."),
    ("i27", "POV: Your Life As Lamine Yamal's Little Brother."),
    ("i28", "The World Cup Changed Everything."),
]

ACTS = [
    {
        "name": "ACTE 1 - Atlanta, 15 juin (0-0 Cap-Vert)",
        "pacing": "~3-4 sec/image",
        "images": "i29-i50",
        "duration": "~1 min 20",
        "stadium": "Mercedes-Benz Stadium, Atlanta, USA",
        "match": "Spain 0-0 Cape Verde (Group H)",
        "lines": [
            ("i29", "June 15th. Our first World Cup match."),
            ("i30", "Atlanta, Georgia. United States."),
            ("i31", "Mercedes-Benz Stadium."),
            ("i32", "Spain versus Cape Verde."),
            ("i33", "My mom Sheila held my hand."),
            ("i34", "The stadium was louder than Barca."),
            ("i35", "I covered my ears."),
            ("i36", "Everyone stood up. I couldn't see."),
            ("i37", "On the big screen - a player in red."),
            ("i38", 'I pointed and said: "Lamine!"'),
            ("i39", "Mom said: That's not Lamine."),
            ("i40", "I didn't believe her."),
            ("i41", "The match ended zero-zero."),
            ("i42", "No goals."),
            ("i43", "Spain should have won. Everyone said that."),
            ("i44", "I fell asleep on Mom's shoulder at minute seventy."),
            ("i45", "Lamine came to the family zone after."),
            ("i46", "He knelt down to my height."),
            ("i47", 'He said: "You came."'),
            ("i48", 'I said: "I slept."'),
            ("i49", "He laughed."),
            ("i50", "That was our first night in America."),
        ],
    },
    {
        "name": "ACTE 2 - Atlanta, 21 juin (4-0 Arabie saoudite)",
        "pacing": "~3-4 sec/image",
        "images": "i51-i72",
        "duration": "~1 min 20",
        "stadium": "Mercedes-Benz Stadium, Atlanta, USA",
        "match": "Spain 4-0 Saudi Arabia (Group H)",
        "lines": [
            ("i51", "Six days later. June 21st."),
            ("i52", "Same stadium. Same heat."),
            ("i53", "Spain versus Saudi Arabia."),
            ("i54", "This time I brought my Spain shirt."),
            ("i55", "It was too big. It covered my knees."),
            ("i56", "First goal. The stadium exploded."),
            ("i57", "I threw my arms up."),
            ("i58", "Second goal. I did it again."),
            ("i59", "Third goal. I was screaming."),
            ("i60", "Fourth goal. I had no voice left."),
            ("i61", "Final score: four-zero."),
            ("i62", "Mom was crying. Not sad. Happy."),
            ("i63", 'I asked: "Did Lamine score?"'),
            ("i64", 'She said: "Watch the screen."'),
            ("i65", "He was running. Arms open."),
            ("i66", "I thought: that's my brother."),
            ("i67", "The whole section chanted his name."),
            ("i68", 'I chanted too. I only knew "La-mi-ne."'),
            ("i69", "After the match, the families sat together."),
            ("i70", "I saw other players' moms. I waved at everyone."),
            ("i71", "One lady waved back. I thought she was famous."),
            ("i72", "Her son would score a lot this World Cup."),
        ],
    },
    {
        "name": "ACTE 3 - Guadalajara, 26 juin (0-1 Uruguay)",
        "pacing": "~3-4 sec/image",
        "images": "i73-i92",
        "duration": "~1 min 10",
        "stadium": "Estadio Akron, Guadalajara, Mexico",
        "match": "Uruguay 0-1 Spain - Baena 42' (Group H)",
        "lines": [
            ("i73", "June 26th. We left the United States."),
            ("i74", "Mexico. Guadalajara."),
            ("i75", "Estadio Akron."),
            ("i76", "Uruguay versus Spain."),
            ("i77", "New country. New flags. I pointed at everything."),
            ("i78", 'Mom said: "We\'re not home yet."'),
            ("i79", 'I said: "When is home?"'),
            ("i80", "She didn't answer."),
            ("i81", "The goal came in the first half."),
            ("i82", "Baena scored."),
            ("i83", "The goalkeeper dropped it."),
            ("i84", "Adults groaned. Kids cheered. I cheered."),
            ("i85", "Final score: one-zero."),
            ("i86", "Spain won the group."),
            ("i87", "I tried a taco after the match."),
            ("i88", "Too much sauce."),
            ("i89", "I stuck my tongue out."),
            ("i90", "Mom filmed it."),
            ("i91", "She didn't know that face would end up on TV later."),
            ("i92", "We drove back to the United States that night."),
        ],
    },
    {
        "name": "ACTE 4 - Los Angeles, 2 juillet (3-0 Autriche)",
        "pacing": "~3-4 sec/image",
        "images": "i93-i118",
        "duration": "~1 min 30",
        "stadium": "SoFi Stadium, Los Angeles, USA",
        "match": "Spain 3-0 Austria - Oyarzabal 36', 89'; Porro 66' (R32)",
        "lines": [
            ("i93", "July 2nd. Los Angeles."),
            ("i94", "SoFi Stadium."),
            ("i95", "Round of thirty-two. Spain versus Austria."),
            ("i96", 'Mom said: "No sleeping tonight."'),
            ("i97", "First half. Oyarzabal scored."),
            ("i98", "I jumped. I didn't know why. Everyone jumped."),
            ("i99", 'I screamed one word: "Vamos!"'),
            ("i100", "Second goal. Porro. Header."),
            ("i101", 'I screamed "Vamos!" again.'),
            ("i102", "Third goal. Oyarzabal again."),
            ("i103", "I screamed until my throat hurt."),
            ("i104", "Final score: three-zero."),
            ("i105", "The camera found me."),
            ("i106", "I was on the big screen."),
            ("i107", "Eighty thousand people laughed. Not at me. With me."),
            ("i108", "After the match, Lamine spoke to reporters."),
            ("i109", "He didn't talk about goals."),
            ("i110", 'He said: "My little brother means everything to me."'),
            ("i111", "I was in the car when Mom played it on her phone."),
            ("i112", 'I said: "That\'s me."'),
            ("i113", 'She said: "Yes. That\'s you."'),
            ("i114", "Lamine shot early in that match."),
            ("i115", "Straight at the goalkeeper."),
            ("i116", "I still stood up like he scored."),
            ("i117", "Because he's my brother."),
            ("i118", "And I always stand up."),
        ],
    },
    {
        "name": "ACTE 5 - Dallas, 6 juillet (0-1 Portugal) + CR7",
        "pacing": "~3-4 sec/image",
        "images": "i119-i148",
        "duration": "~1 min 45",
        "stadium": "AT&T Stadium, Arlington/Dallas, USA",
        "match": "Portugal 0-1 Spain - Merino 90+1' (R16)",
        "lines": [
            ("i119", "July 6th. Dallas. Texas."),
            ("i120", "AT&T Stadium."),
            ("i121", "Spain versus Portugal."),
            ("i122", 'Mom said: "This one is different."'),
            ("i123", 'I said: "Why?"'),
            ("i124", 'She said: "Because everyone knows everyone."'),
            ("i125", "I saw a man with perfect hair."),
            ("i126", "Sunglasses. Even indoors."),
            ("i127", 'Mom whispered: "That\'s Cristiano Ronaldo."'),
            ("i128", 'I said: "Is he Lamine\'s friend?"'),
            ("i129", 'She said: "Not today."'),
            ("i130", "Zero-zero for a long time."),
            ("i131", "I ate popcorn. Ronaldo ate nothing."),
            ("i132", "Lamine shot twice. The goalkeeper saved both."),
            ("i133", "Ronaldo leaned forward. He didn't blink."),
            ("i134", "I leaned forward. I had popcorn on my face."),
            ("i135", "Minute ninety-one. Spain scored."),
            ("i136", "Merino. Not Lamine."),
            ("i137", "Spain section exploded. Portugal went silent."),
            ("i138", "I looked at Ronaldo. He didn't move."),
            ("i139", "So I waved. Small wave. Like at school."),
            ("i140", "After the match, families walked to the tunnel zone."),
            ("i141", "Ronaldo walked past. Slow steps."),
            ("i142", "He looked at me. I was still holding popcorn."),
            ("i143", 'He said: "Good game, little man."'),
            ("i144", 'I said: "You too."'),
            ("i145", "Mom grabbed my hand."),
            ("i146", "Lamine arrived. He looked at Ronaldo. They nodded."),
            ("i147", "No words. Just nod."),
            ("i148", 'I said: "I talked to Ronaldo."'),
        ],
    },
    {
        "name": "ACTE 6 - Los Angeles, 10 juillet (2-1 Belgique)",
        "pacing": "~3-4 sec/image",
        "images": "i149-i170",
        "duration": "~1 min 20",
        "stadium": "SoFi Stadium, Los Angeles, USA",
        "match": "Spain 2-1 Belgium - Ruiz 30', Merino 88' / De Ketelaere 41' (QF)",
        "lines": [
            ("i149", "July 10th. Back to Los Angeles."),
            ("i150", "Quarter-final. Spain versus Belgium."),
            ("i151", "Belgium scored first. Mom gripped my hand."),
            ("i152", "I didn't like that."),
            ("i153", "Spain scored. Ruiz. I breathed again."),
            ("i154", "Belgium scored again. One-one."),
            ("i155", "I hid my face in Mom's shirt."),
            ("i156", "Then Merino scored. Minute eighty-eight."),
            ("i157", "I came out. Tongue out. Arms up."),
            ("i158", "The stadium camera found me."),
            ("i159", "Big screen. My face. Tongue."),
            ("i160", "Lamine saw it on the pitch."),
            ("i161", "He laughed. On live TV."),
            ("i162", "Spain won two-one."),
            ("i163", 'Mom said: "One more round."'),
            ("i164", 'I said: "I want ice cream."'),
            ("i165", 'She said: "After Dallas."'),
            ("i166", "Lamine cut inside and almost scored that night."),
            ("i167", "I saw it on the screen behind us."),
            ("i168", "I yelled before the replay."),
            ("i169", "Everyone in our row laughed."),
            ("i170", "I didn't know why. I laughed too."),
        ],
    },
    {
        "name": "ACTE 7 - 13 juillet, anniversaire Lamine",
        "pacing": "~3-4 sec/image",
        "images": "i171-i186",
        "duration": "~55 sec",
        "stadium": "Hors match - hotel Dallas",
        "match": "Pas de match - anniversaire Lamine (19 ans)",
        "lines": [
            ("i171", "July 13th."),
            ("i172", "Not a match day."),
            ("i173", "Lamine's birthday."),
            ("i174", "He turned nineteen."),
            ("i175", "We had cake in the hotel."),
            ("i176", "I put nineteen candles on. Mom fixed it to one."),
            ("i177", "Lamine blew it out in one breath."),
            ("i178", "I clapped too long."),
            ("i179", "He gave me a piece. Before anyone else."),
            ("i180", 'He said: "Tomorrow is big."'),
            ("i181", 'I said: "I know. France."'),
            ("i182", 'He said: "Stay with Mom. No running."'),
            ("i183", 'I said: "I always run."'),
            ("i184", "He smiled. The kind that means he can't stop me."),
            ("i185", "That night I slept with my Spain shirt on."),
            ("i186", "July 14th was coming."),
        ],
    },
    {
        "name": "ACTE 8 - Dallas, 14 juillet (0-2 France)",
        "pacing": "~3-4 sec/image",
        "images": "i187-i218",
        "duration": "~1 min 50",
        "stadium": "AT&T Stadium, Arlington/Dallas, USA",
        "match": "France 0-2 Spain - Oyarzabal pen 22', Porro 58' (SF)",
        "lines": [
            ("i187", "July 14th."),
            ("i188", "Bastille Day. French Republic Day."),
            ("i189", "France versus Spain. Semi-final."),
            ("i190", "Dallas. AT&T Stadium."),
            ("i191", "France fans. Spain fans. Red and blue everywhere."),
            ("i192", "I wore my Spain shirt. Mom wore red and yellow."),
            ("i193", "Minute twenty-two. Penalty for Spain."),
            ("i194", "Lamine was on the ground."),
            ("i195", "Digne fouled him. That's what Mom said."),
            ("i196", "I stood up on my seat. Mom pulled me down."),
            ("i197", "Oyarzabal scored. One-zero."),
            ("i198", "I screamed."),
            ("i199", "Second half. Porro scored. Two-zero."),
            ("i200", "I didn't understand the goal. It was too fast."),
            ("i201", "I understood the screaming."),
            ("i202", "Final whistle. France zero. Spain two."),
            ("i203", "Lamine didn't score. But he started the penalty."),
            ("i204", "I ran before Mom could stop me."),
            ("i205", "Security. Players. Cameras. Noise."),
            ("i206", "Lamine knelt. Open arms."),
            ("i207", "I jumped. He caught me."),
            ("i208", 'He said: "We go to New York."'),
            ("i209", 'I said: "I want ice cream first."'),
            ("i210", "The world filmed us again."),
            ("i211", "I didn't wave this time. I held on."),
            ("i212", "France played the third-place match on Saturday."),
            ("i213", "We didn't stay. We packed."),
            ("i214", "Mom said Spain plays the final on July 19th."),
            ("i215", "MetLife Stadium. New Jersey."),
            ("i216", "I asked if Ronaldo would be there."),
            ("i217", "She said Portugal is out."),
            ("i218", "I said: I know. I still asked."),
        ],
    },
    {
        "name": "ACTE 9 - 18 juillet, veille de finale",
        "pacing": "~3-4 sec/image",
        "images": "i219-i232",
        "duration": "~50 sec",
        "stadium": "Hors match - East Rutherford / NYC area",
        "match": "Veille finale - trajet vers MetLife",
        "lines": [
            ("i219", "July 18th. New York area."),
            ("i220", "East Rutherford. MetLife Stadium. Tomorrow."),
            ("i221", "Spain in the final."),
            ("i222", "England or Argentina. We waited to find out."),
            ("i223", "I didn't care who. I cared about the tunnel."),
            ("i224", 'Lamine said I could walk with him. Mom said no.'),
            ("i225", "We took the train. I pressed my face to the window."),
            ("i226", 'Lamine sent a voice note: "Sleep early."'),
            ("i227", 'I sent one back: "You sleep early."'),
            ("i228", "He sent a laughing emoji."),
            ("i229", "I can't read yet. Mom told me."),
            ("i230", "She almost sold my ticket. Dad said a sponsor wanted it."),
            ("i231", "Mom said no. The ticket stayed in her bag."),
            ("i232", "I slept holding it."),
        ],
    },
    {
        "name": "ACTE 10 - 19 juillet, finale",
        "pacing": "~3-4 sec/image",
        "images": "i233-i258",
        "duration": "~1 min 30",
        "stadium": "MetLife Stadium (New York New Jersey Stadium), East Rutherford, USA",
        "match": "FINALE - Spain vs England or Argentina (score a valider apres match)",
        "lines": [
            ("i233", "July 19th. Final day."),
            ("i234", "MetLife Stadium. Eighty-two thousand seats."),
            ("i235", "I had a ticket. Mom said it was the last one."),
            ("i236", "National anthems. I stood. I hummed."),
            ("i237", "First half. I watched Lamine's legs, not the ball."),
            ("i238", "He runs different when he's nervous."),
            ("i239", "Halftime. The screen showed the score behind us."),
            ("i240", "Second half. The stadium shook."),
            ("i241", "I held Mom's hand. She held mine too hard."),
            ("i242", "I don't remember the last minute."),
            ("i243", "I remember the whistle."),
            ("i244", "Lamine looked up at our section."),
            ("i245", "He didn't smile yet. Then he smiled."),
            ("i246", "I knew before the screen showed it."),
            ("i247", "Spain won."),
            ("i248", "NOTE PRODUCTION: remplacer i247 si resultat different."),
            ("i249", "Lamine didn't lift the trophy first."),
            ("i250", "He looked for me."),
            ("i251", "I was there."),
            ("i252", "Three years old. Almost four."),
            ("i253", "The World Cup changed everything."),
            ("i254", "Not for Spain."),
            ("i255", "For me."),
            ("i256", "Because now when they show the big screen..."),
            ("i257", "They know my name."),
            ("i258", "Keyne."),
        ],
    },
]

MATCH_FACTS = [
    ("15 Jun", "Spain 0-0 Cape Verde", "Mercedes-Benz Stadium", "Atlanta, USA", "Group H"),
    ("21 Jun", "Spain 4-0 Saudi Arabia", "Mercedes-Benz Stadium", "Atlanta, USA", "Group H"),
    ("26 Jun", "Uruguay 0-1 Spain", "Estadio Akron", "Guadalajara, Mexico", "Group H - Baena 42'"),
    ("2 Jul", "Spain 3-0 Austria", "SoFi Stadium", "Los Angeles, USA", "R32 - Oyarzabal x2, Porro"),
    ("6 Jul", "Portugal 0-1 Spain", "AT&T Stadium", "Dallas, USA", "R16 - Merino 90+1'"),
    ("10 Jul", "Spain 2-1 Belgium", "SoFi Stadium", "Los Angeles, USA", "QF - Ruiz, Merino / De Ketelaere"),
    ("14 Jul", "France 0-2 Spain", "AT&T Stadium", "Dallas, USA", "SF - Oyarzabal pen 22', Porro 58'"),
    ("19 Jul", "Spain vs TBD", "MetLife Stadium", "East Rutherford, USA", "FINAL - valider score"),
]

SCENES = [
    {"name": "HOOK - 14 juillet demi-finale", "lines": HOOK[0:16]},
    {"name": "HOOK - Keyne et retour Atlanta", "lines": HOOK[16:26]},
    {"name": "HOOK - Carte titre", "lines": HOOK[26:28]},
    {"name": "ACTE 1 - Premier match Atlanta", "lines": ACTS[0]["lines"]},
    {"name": "ACTE 2 - Quatre-zero Arabie", "lines": ACTS[1]["lines"]},
    {"name": "ACTE 3 - Mexique Guadalajara", "lines": ACTS[2]["lines"]},
    {"name": "ACTE 4 - Vamos viral Autriche", "lines": ACTS[3]["lines"]},
    {"name": "ACTE 5 - CR7 tribune et tunnel", "lines": ACTS[4]["lines"][:16]},
    {"name": "ACTE 5 - CR7 apres-match", "lines": ACTS[4]["lines"][16:]},
    {"name": "ACTE 6 - Ecran geant Belgique", "lines": ACTS[5]["lines"]},
    {"name": "ACTE 7 - Anniversaire 13 juillet", "lines": ACTS[6]["lines"]},
    {"name": "ACTE 8 - Demi France 14 juillet", "lines": ACTS[7]["lines"][:16]},
    {"name": "ACTE 8 - Calin et depart NYC", "lines": ACTS[7]["lines"][16:]},
    {"name": "ACTE 9 - Veille finale", "lines": ACTS[8]["lines"]},
    {"name": "ACTE 10 - Finale 19 juillet", "lines": ACTS[9]["lines"]},
]

FLOW_BATCHES = [
    {"id": "Hook-A", "act": "HOOK", "start": "i1", "end": "i16", "count": 16, "rythme": "1-2 sec/image"},
    {"id": "Hook-B", "act": "HOOK", "start": "i17", "end": "i28", "count": 12, "rythme": "1-2 sec/image"},
    {"id": "Acte1-A", "act": "ACTE 1 Atlanta 15 jun", "start": "i29", "end": "i44", "count": 16, "rythme": "3-4 sec/image"},
    {"id": "Acte1-B", "act": "ACTE 1 Atlanta 15 jun", "start": "i45", "end": "i50", "count": 6, "rythme": "3-4 sec/image"},
    {"id": "Acte2-A", "act": "ACTE 2 Atlanta 21 jun", "start": "i51", "end": "i66", "count": 16, "rythme": "3-4 sec/image"},
    {"id": "Acte2-B", "act": "ACTE 2 Atlanta 21 jun", "start": "i67", "end": "i72", "count": 6, "rythme": "3-4 sec/image"},
    {"id": "Acte3", "act": "ACTE 3 Guadalajara 26 jun", "start": "i73", "end": "i92", "count": 20, "rythme": "3-4 sec/image"},
    {"id": "Acte4-A", "act": "ACTE 4 LA 2 jul", "start": "i93", "end": "i108", "count": 16, "rythme": "3-4 sec/image"},
    {"id": "Acte4-B", "act": "ACTE 4 LA 2 jul", "start": "i109", "end": "i118", "count": 10, "rythme": "3-4 sec/image"},
    {"id": "Acte5-A", "act": "ACTE 5 CR7 Dallas 6 jul", "start": "i119", "end": "i134", "count": 16, "rythme": "3-4 sec/image"},
    {"id": "Acte5-B", "act": "ACTE 5 CR7 Dallas 6 jul", "start": "i135", "end": "i148", "count": 14, "rythme": "3-4 sec/image"},
    {"id": "Acte6-A", "act": "ACTE 6 LA 10 jul", "start": "i149", "end": "i164", "count": 16, "rythme": "3-4 sec/image"},
    {"id": "Acte6-B", "act": "ACTE 6 LA 10 jul", "start": "i165", "end": "i170", "count": 6, "rythme": "3-4 sec/image"},
    {"id": "Acte7", "act": "ACTE 7 Anniversaire 13 jul", "start": "i171", "end": "i186", "count": 16, "rythme": "3-4 sec/image"},
    {"id": "Acte8-A", "act": "ACTE 8 Demi 14 jul", "start": "i187", "end": "i202", "count": 16, "rythme": "3-4 sec/image"},
    {"id": "Acte8-B", "act": "ACTE 8 Demi 14 jul", "start": "i203", "end": "i218", "count": 16, "rythme": "3-4 sec/image"},
    {"id": "Acte9", "act": "ACTE 9 Veille finale", "start": "i219", "end": "i232", "count": 14, "rythme": "3-4 sec/image"},
    {"id": "Acte10-A", "act": "ACTE 10 Finale 19 jul", "start": "i233", "end": "i248", "count": 16, "rythme": "3-4 sec/image"},
    {"id": "Acte10-B", "act": "ACTE 10 Finale 19 jul", "start": "i249", "end": "i258", "count": 10, "rythme": "3-4 sec/image"},
]


def word_count(text: str) -> int:
    return len(text.split())


def get_all_script_lines():
    lines = list(HOOK)
    for act in ACTS:
        lines.extend(act["lines"])
    return lines


def total_images():
    return len(get_all_script_lines())


def estimate_duration():
    hook_n = len(HOOK)
    body_n = total_images() - hook_n
    return round(hook_n * HOOK_SEC_PER_LINE + body_n * BODY_SEC_PER_LINE, 0)


def lines_for_image_range(start_id: str, end_id: str):
    si = int(start_id[1:])
    ei = int(end_id[1:])
    return [(img_id, text) for img_id, text in get_all_script_lines() if si <= int(img_id[1:]) <= ei]


def scene_lines_count(scene: dict) -> int:
    return len(scene["lines"])


def make_chunk(part_num: int, scenes: list, lines: list) -> dict:
    text = " ".join(t for _, t in lines)
    n = len(lines)
    hook_lines = sum(1 for img_id, _ in lines if int(img_id[1:]) <= len(HOOK))
    body_lines = n - hook_lines
    seconds = round(hook_lines * HOOK_SEC_PER_LINE + body_lines * BODY_SEC_PER_LINE, 1)
    return {
        "part": part_num,
        "start": lines[0][0],
        "end": lines[-1][0],
        "scenes": [s["name"] for s in scenes],
        "lines": lines,
        "text": text,
        "words": word_count(text),
        "lines_count": n,
        "seconds": seconds,
    }


def build_vo_chunks():
    chunks = []
    current_scenes = []
    current_lines = []
    current_line_count = 0
    part_num = 1

    def flush():
        nonlocal part_num, current_scenes, current_lines, current_line_count
        if not current_lines:
            return
        chunks.append(make_chunk(part_num, current_scenes, current_lines))
        part_num += 1
        current_scenes = []
        current_lines = []
        current_line_count = 0

    for scene in SCENES:
        sl = scene_lines_count(scene)
        if sl > MAX_LINES_40S and scene["name"].startswith("ACTE 5"):
            mid = sl // 2
            sub_scenes = [
                {"name": scene["name"] + " (1)", "lines": scene["lines"][:mid]},
                {"name": scene["name"] + " (2)", "lines": scene["lines"][mid:]},
            ]
            for sub in sub_scenes:
                ssl = len(sub["lines"])
                if current_lines and current_line_count + ssl > MAX_LINES_40S:
                    flush()
                current_scenes.append(sub)
                current_lines.extend(sub["lines"])
                current_line_count += ssl
            continue
        if current_lines and current_line_count + sl > MAX_LINES_40S:
            flush()
        current_scenes.append(scene)
        current_lines.extend(scene["lines"])
        current_line_count += sl

    flush()
    return chunks


def vo_parts_for_range(start_id: str, end_id: str, vo_chunks: list) -> str:
    si = int(start_id[1:])
    ei = int(end_id[1:])
    parts = []
    for c in vo_chunks:
        cs = int(c["start"][1:])
        ce = int(c["end"][1:])
        if cs <= ei and ce >= si:
            parts.append(f"VO {c['part']}")
    return ", ".join(parts) if parts else "-"


class ScriptPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, TITLE[:72] + "...", align="C", new_x="LMARGIN", new_y="NEXT")
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
    n_img = total_images()
    dur = estimate_duration()
    vo_chunks = build_vo_chunks()

    pdf = ScriptPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(20, 20, 20)

    pdf.add_page()
    pdf.ln(28)
    pdf.set_font("Helvetica", "B", 15)
    pdf.set_text_color(20, 20, 20)
    pdf.multi_cell(0, 9, TITLE, align="C")
    pdf.ln(8)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(
        0,
        7,
        f"Script complet scene par scene + scripts Voice-Over (ElevenLabs)\n"
        f"{n_img} images | ~{int(dur // 60)} min {int(dur % 60)} sec VO estimee | Hook rapide + corps lent",
        align="C",
    )
    pdf.ln(12)
    pdf.set_font("Helvetica", "I", 10)
    pdf.multi_cell(
        0,
        6,
        "PARTIE A : Script image par image (i1-i258)\n"
        "PARTIE B : Scripts VO (max ~40 sec, scenes completes uniquement)\n"
        "PARTIE C : Organisation Google Flow\n"
        "PARTIE D : Faits reels matchs (NE PAS MODIFIER LES SCORES)",
        align="C",
    )

    pdf.add_page()
    pdf.section_title("SPECIFICATIONS TECHNIQUES", 13)
    specs = [
        "Titre YouTube : " + TITLE,
        "Format : POV storytime animation (stick figure minimaliste)",
        f"Total images : {n_img} (i1 a i{ n_img })",
        f"Duree VO estimee : ~{dur} sec (~{dur / 60:.1f} min)",
        "",
        "RYTHME MONTAGE :",
        f"  Hook (i1-i{len(HOOK)}) : 1 a 2 sec par image (~{len(HOOK) * HOOK_SEC_PER_LINE:.0f} sec)",
        f"  Corps (i{len(HOOK)+1}-i{n_img}) : 3 a 4 sec par image",
        "",
        "REGLE VO ELEVENLABS (IMPORTANT) :",
        "  Chaque bloc VO se termine a la FIN d'une scene narrative complete.",
        "  Ne jamais couper au milieu d'une phrase ou d'une sequence.",
        "  Raison : la voix peut legerement changer entre deux generations.",
        "",
        "REGLE MATCHS (CRITIQUE) :",
        "  Tous les scores, dates, stades et buteurs = FAITS REELS FIFA 2026.",
        "  Ne jamais inventer un resultat ou un buteur.",
        "  Lamine n'a PAS marque en demi vs France - il a obtenu le penalty.",
        "  Anniversaire Lamine : 13 JUILLET (19 ans). Demi : 14 JUILLET.",
        "  Fiction autorisee UNIQUEMENT : tribunes, hotel, tunnel, scenes Keyne.",
        "",
        "PERSONNAGES :",
        "  KEYNE (POV, 3 ans presque 4) | LAMINE YAMAL (frere, #19 Espagne)",
        "  SHEILA EBANA (mere) | CRISTIANO RONALDO (scene comique Portugal)",
        "  Familles joueurs en tribune | Supporters France / Espagne",
        "",
        "STYLE : meme stick-figure-plus que chaîne OnlyFans BROTHER",
        "DISCLAIMER : Fiction POV inspiree de faits reels. Divertissement.",
    ]
    for s in specs:
        if not s.strip():
            pdf.ln(2)
        else:
            pdf.body_text(s)

    pdf.add_page()
    pdf.section_title("PARTIE A - SCRIPT COMPLET SCENE PAR SCENE", 14)
    pdf.meta_line("1 phrase = 1 image. Copier chaque ligne pour les prompts Flow.")

    pdf.sub_title(f"HOOK RAPIDE - i1 a i{len(HOOK)} (~{len(HOOK)*HOOK_SEC_PER_LINE:.0f} sec | 1-2 sec/image)")
    for img_id, line in HOOK:
        pdf.scene_line(img_id, line)

    for act in ACTS:
        pdf.ln(3)
        pdf.sub_title(
            f"{act['name']} | {act['images']} | {act['duration']} | {act['pacing']}"
        )
        pdf.meta_line(f"MATCH REEL : {act['match']} | {act['stadium']}")
        for img_id, line in act["lines"]:
            pdf.scene_line(img_id, line)

    pdf.add_page()
    pdf.section_title("PARTIE B - SCRIPTS VOICE-OVER (ELEVENLABS)", 14)
    pdf.meta_line(
        "REGLE : chaque bloc = scenes completes seulement (jamais de coupure mid-scene).\n"
        f"Maximum ~{MAX_LINES_40S} lignes corps par bloc (~40 sec).\n"
        "Generer tous les blocs VO dans l'ordre."
    )
    pdf.ln(2)
    pdf.body_text(f"Nombre total de blocs VO : {len(vo_chunks)}")
    pdf.ln(3)

    for chunk in vo_chunks:
        pdf.sub_title(
            f"VO PART {chunk['part']} - {chunk['start']} a {chunk['end']} "
            f"| ~{chunk['seconds']} sec | {chunk['lines_count']} lignes"
        )
        pdf.meta_line("Scenes incluses : " + " | ".join(chunk["scenes"]))
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(30, 30, 30)
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(pdf.epw, 5, chunk["text"])
        pdf.ln(4)
        if pdf.get_y() > 245:
            pdf.add_page()

    pdf.add_page()
    pdf.section_title("INDEX DES BLOCS VO", 13)
    pdf.set_font("Helvetica", "B", 8)
    pdf.cell(22, 7, "Bloc", border=1)
    pdf.cell(28, 7, "Images", border=1)
    pdf.cell(18, 7, "Mots", border=1)
    pdf.cell(18, 7, "Duree", border=1)
    pdf.cell(0, 7, "Scenes (completes)", border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 7)
    for chunk in vo_chunks:
        scenes_short = " + ".join(s[:28] for s in chunk["scenes"])
        pdf.cell(22, 6, f"Part {chunk['part']}", border=1)
        pdf.cell(28, 6, f"{chunk['start']}-{chunk['end']}", border=1)
        pdf.cell(18, 6, str(chunk["words"]), border=1)
        pdf.cell(18, 6, f"~{chunk['seconds']}s", border=1)
        pdf.cell(0, 6, scenes_short, border=1, new_x="LMARGIN", new_y="NEXT")

    pdf.add_page()
    pdf.section_title("PARTIE D - FAITS REELS MATCHS (REFERENCE)", 14)
    pdf.meta_line("NE PAS modifier ces informations dans le script ou les images de score.")
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 8)
    pdf.cell(18, 7, "Date", border=1)
    pdf.cell(42, 7, "Resultat", border=1)
    pdf.cell(38, 7, "Stade", border=1)
    pdf.cell(28, 7, "Ville", border=1)
    pdf.cell(0, 7, "Phase", border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 7)
    for row in MATCH_FACTS:
        pdf.cell(18, 6, row[0], border=1)
        pdf.cell(42, 6, row[1], border=1)
        pdf.cell(38, 6, row[2], border=1)
        pdf.cell(28, 6, row[3], border=1)
        pdf.cell(0, 6, row[4], border=1, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(4)
    pdf.body_text(
        "Demi-finale 14 juillet : Lamine Yamal foule par Lucas Digne -> penalty Oyarzabal 22'.\n"
        "Porro 58' (assistance Olmo). Lamine ne marque PAS.\n"
        "Keyne Yamal : vrai petit frere (ne sept. 2022, 3 ans presque 4 en juillet 2026).\n"
        "Moments viraux reels : Vamos vs Autriche, langue ecran geant vs Belgique, calin demi."
    )

    pdf.add_page()
    pdf.section_title("PARTIE C - ORGANISATION GOOGLE FLOW", 14)
    pdf.meta_line(
        "1 prompt Flow = 1 lot ci-dessous. Max ~16 images par prompt pour garder la qualite.\n"
        "Character refs : KEYNE + LAMINE (stylise). Meme style stick-figure-plus que chaîne."
    )
    pdf.ln(2)
    pdf.body_text(f"Nombre total de prompts Flow : {len(FLOW_BATCHES)}")
    pdf.ln(2)

    for batch in FLOW_BATCHES:
        vo_ref = vo_parts_for_range(batch["start"], batch["end"], vo_chunks)
        pdf.sub_title(
            f"FLOW {batch['id']} | {batch['act']} | {batch['start']} a {batch['end']} "
            f"| {batch['count']} images | {batch['rythme']}"
        )
        pdf.meta_line(f"Voice-Over correspondant : {vo_ref}")
        pdf.meta_line(
            f"Prompt Flow : Generate {batch['count']} separate images (16:9, stick figure plus, white bg)"
        )
        for img_id, line in lines_for_image_range(batch["start"], batch["end"]):
            pdf.scene_line(img_id, line)
        pdf.ln(3)
        if pdf.get_y() > 240:
            pdf.add_page()

    pdf.add_page()
    pdf.section_title("INDEX FLOW - VUE RAPIDE", 13)
    pdf.set_font("Helvetica", "B", 8)
    pdf.cell(22, 7, "Flow", border=1)
    pdf.cell(42, 7, "Acte", border=1)
    pdf.cell(28, 7, "Images", border=1)
    pdf.cell(14, 7, "Nb", border=1)
    pdf.cell(22, 7, "VO lie", border=1)
    pdf.cell(0, 7, "Rythme", border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 7)
    for batch in FLOW_BATCHES:
        vo_ref = vo_parts_for_range(batch["start"], batch["end"], vo_chunks)
        pdf.cell(22, 6, batch["id"], border=1)
        pdf.cell(42, 6, batch["act"][:30], border=1)
        pdf.cell(28, 6, f"{batch['start']}-{batch['end']}", border=1)
        pdf.cell(14, 6, str(batch["count"]), border=1)
        pdf.cell(22, 6, vo_ref[:18], border=1)
        pdf.cell(0, 6, batch["rythme"], border=1, new_x="LMARGIN", new_y="NEXT")

    pdf.add_page()
    pdf.section_title("MINIATURE YOUTUBE", 13)
    thumb = [
        "Layout : meme grille que OnlyFans BROTHER (fond blanc, stick-figure-plus).",
        "GRAND : Lamine maillot Espagne #19, bras leves, score 2-0.",
        "PETIT (bas droite) : Keyne, maillot Espagne enfant, expression choquee/fiere.",
        "TEXTE : LAMINE YAMAL (rouge/jaune) + LITTLE BROTHER (noir).",
        "Option : 2-0 FRANCE en petit sous le score.",
        "Prop : drapeaux France/Espagne ou ecran geant stade Dallas.",
    ]
    for t in thumb:
        pdf.body_text(t)

    pdf.add_page()
    pdf.section_title("DESCRIPTION & TAGS YOUTUBE", 13)
    pdf.body_text(
        "DESCRIPTION (accroche) :\n"
        "July 14th. Bastille Day. France versus Spain. Zero-two.\n"
        "My brother Lamine didn't score. But he won the penalty.\n"
        "I am three. Almost four. This is my World Cup.\n\n"
        "TAGS : pov storytime, lamine yamal, keyne yamal, world cup 2026, spain football, "
        "little brother, family story, stick figure animation, world cup final, bastille day, "
        "spain vs france, animated storytime, football storytime\n\n"
        "DISCLAIMER : Fictional POV storytime inspired by real World Cup 2026 matches and results."
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUTPUT))
    WORKSPACE_OUTPUT.write_bytes(OUTPUT.read_bytes())
    return OUTPUT, vo_chunks


if __name__ == "__main__":
    path, chunks = generate_pdf()
    print(f"PDF genere : {path}")
    print(f"Images : {total_images()}")
    print(f"Duree estimee : {estimate_duration()} sec")
    print(f"Blocs VO : {len(chunks)}")
