#!/usr/bin/env python3
"""Generate PDF: full scene-by-scene script + VO chunks (max 40s, scene-complete only)."""

from fpdf import FPDF
from pathlib import Path

OUTPUT = Path("/opt/cursor/artifacts/POV-Sister-OnlyFans-Brother-Script-Complet.pdf")
WORKSPACE_OUTPUT = Path("/workspace/POV-Sister-OnlyFans-Brother-Script-Complet.pdf")

TITLE = "POV: Your Life As The Sister Of An OnlyFans Brother - The Party Wasn't TikTok"

# Mesure reelle utilisateur : 321 sec VO pour 160 lignes (13 blocs deja generes)
VO_REF_SECONDS = 321
VO_REF_LINES = 160
SEC_PER_LINE = VO_REF_SECONDS / VO_REF_LINES  # ~2.01 sec/ligne
MAX_LINES_40S = int(40 / SEC_PER_LINE)  # 19 lignes max par bloc VO (~38 sec)
EXISTING_VO_PARTS = 13  # VO 1-13 deja generes par l'utilisateur

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

    {
        "name": "ACTE 6 - La semaine d'apres",
        "pacing": "~3-4 sec/image",
        "images": "i161-i180",
        "duration": "~40 sec VO",
        "lines": [
            ("i161", "The week after was worse than the party."),
            ("i162", "Not louder."),
            ("i163", "Quieter."),
            ("i164", "The kind of quiet where everyone waits for someone else to speak first."),
            ("i165", "Mom stopped asking about your day."),
            ("i166", "Dad stopped making jokes at dinner."),
            ("i167", "Your brother acted like nothing happened."),
            ("i168", "He still edited videos at the kitchen table."),
            ("i169", "With headphones on."),
            ("i170", "Like the house belonged to his subscribers."),
            ("i171", "At school the jokes never fully stopped."),
            ("i172", "They just changed shape."),
            ("i173", "People didn't say OnlyFans in the hallway anymore."),
            ("i174", "They just said your brother."),
            ("i175", "Like that was enough."),
            ("i176", "Like everyone had already googled the rest."),
            ("i177", "Maya stayed your friend."),
            ("i178", "But she stopped sitting with you at lunch."),
            ("i179", "Not because she hated you."),
            ("i180", "Because being near you had become a risk."),
        ],
    },
    {
        "name": "ACTE 7 - La faveur",
        "pacing": "~3-4 sec/image",
        "images": "i181-i198",
        "duration": "~36 sec VO",
        "lines": [
            ("i181", "Social risk."),
            ("i182", "The kind teenagers understand better than adults."),
            ("i183", "That Friday your brother knocked on your door."),
            ("i184", "First time in months he knocked."),
            ("i185", "He said he needed a favor."),
            ("i186", "Don't say it like that, you told him."),
            ("i187", "He smiled anyway."),
            ("i188", "The smile that works on camera."),
            ("i189", "Not the one he used when you were kids."),
            ("i190", "He needed a ride to a studio across town."),
            ('i191', '"Management booked it," he said.'),
            ('i192', '"It\'s professional now."'),
            ("i193", "You drove because you were tired of feeling powerless."),
            ("i194", "Or because you still loved him."),
            ("i195", "Probably both."),
            ("i196", "Ring lights in the lobby."),
            ("i197", "Your brother walked in like he owned the place."),
            ("i198", "You stayed in the car."),
        ],
    },
    {
        "name": "ACTE 8 - Menaces",
        "pacing": "~3-4 sec/image",
        "images": "i199-i216",
        "duration": "~36 sec VO",
        "lines": [
            ("i199", "Forty minutes later he came out counting money on his phone."),
            ('i200', '"This is one afternoon," he said.'),
            ("i201", "It was more than Mom made in two weeks at the hospital."),
            ('i202', 'He said, "You could help me. Just drive. Just keep quiet."'),
            ('i203', 'You said, "You turned our kitchen into a set."'),
            ('i204', 'He said, "I turned our kitchen into rent."'),
            ("i205", "That night Dad found an envelope in the mailbox."),
            ("i206", "No stamp. No name."),
            ("i207", "Inside was a printed screenshot of your house."),
            ("i208", "Your brother's face circled in red marker."),
            ('i209', 'Written underneath: "We know where the scenes are filmed."'),
            ("i210", "Dad didn't scream this time."),
            ("i211", "He just sat at the table holding that paper."),
            ("i212", "Mom called the police."),
            ("i213", "Your brother said fans get obsessed."),
            ('i214', '"It\'s normal," he said.'),
            ("i215", "Nothing about this felt normal."),
            ("i216", "A boy from your school DM'd you the next week."),
        ],
    },
    {
        "name": "ACTE 9 - Il demenage",
        "pacing": "~3-4 sec/image",
        "images": "i217-i231",
        "duration": "~30 sec VO",
        "lines": [
            ("i217", "He recognized the staircase in a preview."),
            ("i218", "He said he lived two blocks away."),
            ("i219", "You blocked him and sent the screenshot to Mom."),
            ("i220", "Your brother posted a family boundary video."),
            ("i221", "Not your name. Not your face."),
            ("i222", "But everyone knew who he meant."),
            ("i223", "Comments called you controlling."),
            ("i224", "Comments asked if you had an account too."),
            ("i225", "On a Tuesday Mom made an announcement at dinner."),
            ("i226", "Your brother had to move out by the first of next month."),
            ("i227", "He laughed. Then saw her face. Then stopped laughing."),
            ("i228", "He moved into a one-bedroom near downtown."),
            ("i229", "Box fans instead of ring lights."),
            ("i230", "Smaller audience. Bigger excuses."),
            ("i231", "You left his texts on read."),
        ],
    },
    {
        "name": "ACTE 10 - Nouvelle ecole",
        "pacing": "~3-4 sec/image",
        "images": "i232-i243",
        "duration": "~24 sec VO",
        "lines": [
            ("i232", "Two months later someone tagged you in a fan edit."),
            ("i233", "Your front door in the background."),
            ("i234", "Your last name in the caption."),
            ("i235", "The internet doesn't forget. It archives."),
            ("i236", "You changed schools the following semester."),
            ("i237", "New hallway. New cafeteria."),
            ("i238", "No one knew your brother."),
            ("i239", "For three weeks that felt like peace."),
            ('i240', 'Then a girl in chemistry class said, "Wait, aren\'t you-"'),
            ('i241', 'You said, "No." Too fast. Too loud.'),
            ("i242", "She blinked and changed the subject."),
            ("i243", "You knew she would search later."),
        ],
    },
    {
        "name": "ACTE 11 - Cloture finale",
        "pacing": "~3-4 sec/image",
        "images": "i244-i260",
        "duration": "~34 sec VO",
        "lines": [
            ("i244", "Your brother called on your birthday."),
            ("i245", "He said he missed how things used to be."),
            ("i246", "Before ring lights. Before Apple IDs. Before the house became content."),
            ("i247", "You asked if he was going to apologize."),
            ('i248', 'He said, "I didn\'t think I did anything wrong."'),
            ("i249", "You hung up."),
            ("i250", "Last month you found an old photo on your camera roll."),
            ("i251", "You and him on the porch swing."),
            ("i252", "Before subscribers. Before collabs."),
            ("i253", "You didn't delete it. You didn't post it either."),
            ("i254", "Some things aren't content."),
            ("i255", "He still posts. Different city. Same smile."),
            ("i256", "You still don't follow him. But sometimes you check."),
            ("i257", "Not to watch. To know if your hallway is still out there."),
            ("i258", "It isn't. Not anymore."),
            ("i259", "You keep your curtains closed after six."),
            ("i260", "The party wasn't TikTok. And you are still learning what it actually was."),
        ],
    },

]

# Scenes = unites narratives completes. JAMAIS coupees entre deux blocs VO.
# Chaque scene se termine sur une phrase / image complete.
SCENES = [
    {
        "name": "HOOK - La fausse party",
        "lines": HOOK[0:8],  # i1-i8
    },
    {
        "name": "HOOK - Revelation plateformes",
        "lines": HOOK[8:15],  # i9-i15
    },
    {
        "name": "HOOK - Carte titre",
        "lines": HOOK[15:17],  # i16-i17
    },
    {
        "name": "HOOK - Ce n'etait pas TikTok",
        "lines": HOOK[17:28],  # i18-i28
    },
    {
        "name": "ACTE 1 - Vendredi soir (parents absents)",
        "lines": [("i29", "It started on a Friday."), ("i30", "Mom and Dad left for a wedding in another state."),
                  ("i31", "You had the house to yourself - or so you thought."),
                  ("i32", "At 5:47 PM your brother texted the family group chat."),
                  ("i33", '"Brand party tonight. Don\'t embarrass me."'),
                  ("i34", 'You replied: "How many people?"'),
                  ("i35", 'He said: "Just creators."'),
                  ("i36", "You still didn't understand what that meant.")],
    },
    {
        "name": "ACTE 1 - Les creatrices arrivent",
        "lines": [("i37", "At 6 PM the doorbell rang."), ("i38", "A girl with a ring light stand."),
                  ("i39", "Another with a rolling equipment case."), ("i40", "A third in a crop top and heels."),
                  ('i41', '"Hey! We\'re here for the shoot!"'), ("i42", "Shoot. Not party."),
                  ("i43", "You looked at your brother."),
                  ("i44", "He was already pushing the couch against the living room wall.")],
    },
    {
        "name": "ACTE 1 - La maison devient un plateau",
        "lines": [("i45", "Tripod in the hallway."), ("i46", "Softbox in the kitchen."),
                  ("i47", "Backdrop taped to the staircase."), ("i48", "Your staircase."),
                  ('i49', '"Can you stay upstairs?" he said.'), ('i50', '"We\'ve got content to film."'),
                  ("i51", "You went to your room."), ("i52", "Door closed. Door locked."),
                  ('i53', 'Downstairs: music, laughter, someone yelling "Action."')],
    },
    {
        "name": "ACTE 1 - Deni (c'est juste de l'influence)",
        "lines": [("i54", "You told yourself it was influencer stuff."),
                  ("i55", "Brand deals. Fitness content. Nothing weird."),
                  ("i56", "But the laughter didn't sound like TikTok."),
                  ("i57", "It sounded like a set.")],
    },
    {
        "name": "ACTE 1 - La cuisine a minuit",
        "lines": [("i58", "At 10 PM you needed water."), ("i59", "You crept downstairs."),
                  ("i60", "The kitchen was empty."),
                  ("i61", "The counter had makeup wipes, baby oil, and a clipboard with shot lists."),
                  ("i62", "Shot lists."), ("i63", "Not recipes. Not homework."), ("i64", "Shot lists."),
                  ("i65", "On the fridge: a whiteboard schedule."),
                  ('i66', '"Scene 3 - Kitchen Counter - Collab with Jade."'),
                  ("i67", "Jade was the girl in the crop top."),
                  ("i68", "You went back upstairs without drinking anything.")],
    },
    {
        "name": "ACTE 2 - Recherche Google",
        "lines": [("i69", "That night you googled his username."),
                  ("i70", "On your laptop. Door locked. Volume off."),
                  ("i71", "The first result wasn't TikTok."), ("i72", "It wasn't Instagram."),
                  ("i73", "It was a subscription page with his face, his chain, his smile."),
                  ('i74', '"Exclusive collabs with models."'),
                  ("i75", "Monthly tiers. Tip menu. Custom requests.")],
    },
    {
        "name": "ACTE 2 - La maison reconnue",
        "lines": [("i76", "You clicked one preview."), ("i77", "The background looked familiar."),
                  ("i78", "Your hallway."), ("i79", "Your bathroom mirror."),
                  ("i80", "The same towel rack Mom bought at Target."), ("i81", "You felt sick."),
                  ("i82", "Not because of what he was doing with women."),
                  ("i83", "Because he was doing it where you ate cereal."),
                  ("i84", "Where Dad grilled on Sundays."),
                  ("i85", "Where you used to do homework on the floor.")],
    },
    {
        "name": "ACTE 2 - C'est un business",
        "lines": [("i86", "You scrolled down."), ("i87", "Fansly link in his bio."),
                  ("i88", "Twitter link."), ("i89", 'A "management" email you had never seen.'),
                  ("i90", "He wasn't a dancer."), ("i91", "He wasn't a fitness guy."),
                  ("i92", "He was a business.")],
    },
    {
        "name": "ACTE 2 - Realisation",
        "lines": [("i93", "Downstairs the music got louder."),
                  ('i94', 'Someone shouted "Cut!" then laughed.'),
                  ("i95", "You put in earbuds."), ("i96", "It didn't help."),
                  ("i97", "You stared at the ceiling and realized your house was a set."),
                  ("i98", "And you were the only one who didn't get a call time.")],
    },
    {
        "name": "ACTE 3 - Sync iCloud minuit",
        "lines": [("i99", "At midnight your phone buzzed."), ("i100", "iCloud Family Sharing."),
                  ("i101", "A photo backup from his phone."), ("i102", "Synced to YOUR camera roll."),
                  ("i103", "Because you share the same Apple ID."), ("i104", "Mom set it up years ago."),
                  ('i105', '"So we can see family photos."'), ("i106", "Family photos."),
                  ("i107", "This wasn't family."), ("i108", "A preview thumbnail appeared on your lock screen."),
                  ("i109", "You were half asleep."), ("i110", "You swiped it away."), ("i111", "Too slow.")],
    },
    {
        "name": "ACTE 3 - Cafeteria lundi",
        "lines": [("i112", "Monday morning. School cafeteria."), ("i113", "Your phone on the table."),
                  ("i114", "Your friend Maya picked it up to show you a meme."),
                  ("i115", "The photo was still in your Recently Deleted."),
                  ("i116", "She saw it anyway."), ('i117', '"Is that your brother?"'),
                  ('i118', '"Is that your HOUSE?"')],
    },
    {
        "name": "ACTE 4 - Rumeurs au lycee",
        "lines": [("i119", "You snatched the phone back."), ("i120", "Your face was burning."),
                  ("i121", "Maya's face was worse - excited, horrified, already texting."),
                  ("i122", "By lunch everyone knew."), ('i123', '"OnlyFans party at her place."'),
                  ('i124', '"Her brother films girls in their kitchen."'),
                  ("i125", "Someone made a joke about your fridge."),
                  ("i126", "You wanted to disappear.")],
    },
    {
        "name": "ACTE 4 - Le mariage (parents voient tout)",
        "lines": [("i127", "Mom called during fifth period."), ("i128", "Dad had seen the sync too."),
                  ("i129", "On his iPad."), ("i130", "At the wedding."),
                  ("i131", "In front of your aunt, your uncle, your grandmother."),
                  ("i132", "Your uncle asked questions."), ("i133", "Your aunt didn't."),
                  ("i134", "She just stared at you like you were part of the production.")],
    },
    {
        "name": "ACTE 4 - Echange de textos",
        "lines": [('i135', 'Your brother texted: "Why is Mom blowing up my phone?"'),
                  ('i136', 'You texted back: "Because your content synced to the FAMILY iCloud."'),
                  ("i137", "Three dots. Then nothing.")],
    },
    {
        "name": "ACTE 4 - Confrontation mardi",
        "lines": [("i138", "He came home Tuesday afternoon."), ("i139", "No apology."),
                  ('i140', '"It\'s just business," he said.'), ('i141', '"Fans pay. I pay rent."'),
                  ('i142', '"You used our house."'), ('i143', '"You used our Apple ID."'),
                  ("i144", "He shrugged like you were the one being dramatic."),
                  ("i145", "Mom changed the family password that night.")],
    },
    {
        "name": "ACTE 5 - Apres la tempete",
        "lines": [("i146", "The ring lights went back in the garage."),
                  ("i147", "The whiteboard came off the fridge."),
                  ("i148", "The house smelled like hairspray for another week."),
                  ("i149", "Your brother still posts."), ("i150", "Smaller now. Different locations."),
                  ('i151', '"Airbnb collabs," he calls them.'), ("i152", "He still wears the chain."),
                  ("i153", "He still smiles like the camera is always on.")],
    },
    {
        "name": "ACTE 5 - Cloture",
        "lines": [("i154", "You still share a last name."), ("i155", "You still walk past his closed door."),
                  ("i156", "You still hear notification sounds at 2 AM."), ("i157", "He never said sorry."),
                  ("i158", "You never asked him to."),
                  ("i159", "Some things don't get fixed with a password change."),
                  ("i160", "The party wasn't TikTok.")],
    },
    {
        "name": "ACTE 6 - Silence a la maison",
        "lines": [
            ("i161", "The week after was worse than the party."), ("i162", "Not louder."),
            ("i163", "Quieter."),
            ("i164", "The kind of quiet where everyone waits for someone else to speak first."),
            ("i165", "Mom stopped asking about your day."), ("i166", "Dad stopped making jokes at dinner."),
            ("i167", "Your brother acted like nothing happened."),
            ("i168", "He still edited videos at the kitchen table."), ("i169", "With headphones on."),
            ("i170", "Like the house belonged to his subscribers."),
        ],
    },
    {
        "name": "ACTE 6 - Ecole et Maya",
        "lines": [
            ("i171", "At school the jokes never fully stopped."), ("i172", "They just changed shape."),
            ("i173", "People didn't say OnlyFans in the hallway anymore."),
            ("i174", "They just said your brother."), ("i175", "Like that was enough."),
            ("i176", "Like everyone had already googled the rest."),
            ("i177", "Maya stayed your friend."), ("i178", "But she stopped sitting with you at lunch."),
            ("i179", "Not because she hated you."),
            ("i180", "Because being near you had become a risk."),
        ],
    },
    {
        "name": "ACTE 7 - La faveur",
        "lines": [
            ("i181", "Social risk."), ("i182", "The kind teenagers understand better than adults."),
            ("i183", "That Friday your brother knocked on your door."),
            ("i184", "First time in months he knocked."), ("i185", "He said he needed a favor."),
            ("i186", "Don't say it like that, you told him."), ("i187", "He smiled anyway."),
            ("i188", "The smile that works on camera."),
            ("i189", "Not the one he used when you were kids."),
            ("i190", "He needed a ride to a studio across town."),
            ('i191', '"Management booked it," he said.'), ('i192', '"It\'s professional now."'),
            ("i193", "You drove because you were tired of feeling powerless."),
            ("i194", "Or because you still loved him."), ("i195", "Probably both."),
            ("i196", "Ring lights in the lobby."),
            ("i197", "Your brother walked in like he owned the place."),
            ("i198", "You stayed in the car."),
        ],
    },
    {
        "name": "ACTE 8 - Menaces",
        "lines": [
            ("i199", "Forty minutes later he came out counting money on his phone."),
            ('i200', '"This is one afternoon," he said.'),
            ("i201", "It was more than Mom made in two weeks at the hospital."),
            ('i202', 'He said, "You could help me. Just drive. Just keep quiet."'),
            ('i203', 'You said, "You turned our kitchen into a set."'),
            ('i204', 'He said, "I turned our kitchen into rent."'),
            ("i205", "That night Dad found an envelope in the mailbox."),
            ("i206", "No stamp. No name."),
            ("i207", "Inside was a printed screenshot of your house."),
            ("i208", "Your brother's face circled in red marker."),
            ('i209', 'Written underneath: "We know where the scenes are filmed."'),
            ("i210", "Dad didn't scream this time."),
            ("i211", "He just sat at the table holding that paper."),
            ("i212", "Mom called the police."), ("i213", "Your brother said fans get obsessed."),
            ('i214', '"It\'s normal," he said.'), ("i215", "Nothing about this felt normal."),
            ("i216", "A boy from your school DM'd you the next week."),
        ],
    },
    {
        "name": "ACTE 9 - Il demenage",
        "lines": [
            ("i217", "He recognized the staircase in a preview."),
            ("i218", "He said he lived two blocks away."),
            ("i219", "You blocked him and sent the screenshot to Mom."),
            ("i220", "Your brother posted a family boundary video."),
            ("i221", "Not your name. Not your face."), ("i222", "But everyone knew who he meant."),
            ("i223", "Comments called you controlling."),
            ("i224", "Comments asked if you had an account too."),
            ("i225", "On a Tuesday Mom made an announcement at dinner."),
            ("i226", "Your brother had to move out by the first of next month."),
            ("i227", "He laughed. Then saw her face. Then stopped laughing."),
            ("i228", "He moved into a one-bedroom near downtown."),
            ("i229", "Box fans instead of ring lights."),
            ("i230", "Smaller audience. Bigger excuses."), ("i231", "You left his texts on read."),
        ],
    },
    {
        "name": "ACTE 10 - Nouvelle ecole",
        "lines": [
            ("i232", "Two months later someone tagged you in a fan edit."),
            ("i233", "Your front door in the background."), ("i234", "Your last name in the caption."),
            ("i235", "The internet doesn't forget. It archives."),
            ("i236", "You changed schools the following semester."),
            ("i237", "New hallway. New cafeteria."), ("i238", "No one knew your brother."),
            ("i239", "For three weeks that felt like peace."),
            ('i240', 'Then a girl in chemistry class said, "Wait, aren\'t you-"'),
            ('i241', 'You said, "No." Too fast. Too loud.'),
            ("i242", "She blinked and changed the subject."),
            ("i243", "You knew she would search later."),
        ],
    },
    {
        "name": "ACTE 11 - Cloture finale",
        "lines": [
            ("i244", "Your brother called on your birthday."),
            ("i245", "He said he missed how things used to be."),
            ("i246", "Before ring lights. Before Apple IDs. Before the house became content."),
            ("i247", "You asked if he was going to apologize."),
            ('i248', 'He said, "I didn\'t think I did anything wrong."'),
            ("i249", "You hung up."),
            ("i250", "Last month you found an old photo on your camera roll."),
            ("i251", "You and him on the porch swing."),
            ("i252", "Before subscribers. Before collabs."),
            ("i253", "You didn't delete it. You didn't post it either."),
            ("i254", "Some things aren't content."),
            ("i255", "He still posts. Different city. Same smile."),
            ("i256", "You still don't follow him. But sometimes you check."),
            ("i257", "Not to watch. To know if your hallway is still out there."),
            ("i258", "It isn't. Not anymore."), ("i259", "You keep your curtains closed after six."),
            ("i260", "The party wasn't TikTok. And you are still learning what it actually was."),
        ],
    },

]


def word_count(text: str) -> int:
    return len(text.split())


def estimate_seconds_from_lines(n_lines: int) -> float:
    return n_lines * SEC_PER_LINE


def estimate_seconds_text(text: str) -> float:
    return estimate_seconds_from_lines(len(text.split()))


def scene_lines_count(scene: dict) -> int:
    return len(scene["lines"])


def scene_words(scene: dict) -> int:
    return sum(word_count(line) for _, line in scene["lines"])


def make_chunk(part_num: int, scenes: list, lines: list, is_new: bool = False) -> dict:
    text = " ".join(t for _, t in lines)
    n = len(lines)
    return {
        "part": part_num,
        "start": lines[0][0],
        "end": lines[-1][0],
        "scenes": [s["name"] for s in scenes],
        "lines": lines,
        "text": text,
        "words": word_count(text),
        "lines_count": n,
        "seconds": round(estimate_seconds_from_lines(n), 1),
        "is_new": is_new,
    }


# Regroupement FIXE des 13 premiers VO (deja generes par l'utilisateur)
EXISTING_VO_SCENE_GROUPS = [
    [0, 1, 2],       # VO 1  i1-i17
    [3],             # VO 2  i18-i28
    [4],             # VO 3  i29-i36
    [5, 6],          # VO 4  i37-i53
    [7, 8],          # VO 5  i54-i68
    [9],             # VO 6  i69-i75
    [10, 11],        # VO 7  i76-i92
    [12],            # VO 8  i93-i98
    [13],            # VO 9  i99-i111
    [14, 15],        # VO 10 i112-i126
    [16, 17],        # VO 11 i127-i137
    [18, 19],        # VO 12 i138-i153
    [20],            # VO 13 i154-i160
]
EXTENSION_SCENE_START = 21  # index premiere scene extension dans SCENES


def build_vo_chunks():
    """
    VO 1-13 : regroupement FIXE (deja generes, ne pas modifier).
    VO 14+  : scenes extension uniquement, pack par scenes completes, max 19 lignes.
    """
    chunks = []

    for part_idx, scene_indices in enumerate(EXISTING_VO_SCENE_GROUPS, start=1):
        scenes = [SCENES[i] for i in scene_indices]
        lines = []
        for s in scenes:
            lines.extend(s["lines"])
        chunks.append(make_chunk(part_idx, scenes, lines, is_new=False))

    ext_scenes = SCENES[EXTENSION_SCENE_START:]
    current_scenes = []
    current_lines = []
    current_line_count = 0
    part_num = EXISTING_VO_PARTS + 1

    def flush_ext():
        nonlocal part_num, current_scenes, current_lines, current_line_count
        if not current_lines:
            return
        chunks.append(make_chunk(part_num, current_scenes, current_lines, is_new=True))
        part_num += 1
        current_scenes = []
        current_lines = []
        current_line_count = 0

    for scene in ext_scenes:
        sl = scene_lines_count(scene)
        if sl > MAX_LINES_40S:
            raise ValueError(f"Scene extension trop longue ({sl} lignes): {scene['name']}")
        if current_lines and current_line_count + sl > MAX_LINES_40S:
            flush_ext()
        current_scenes.append(scene)
        current_lines.extend(scene["lines"])
        current_line_count += sl

    flush_ext()
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
        "260 images | ~8 min 40 VO (mesure reelle) | Hook rapide + corps lent",
        align="C",
    )
    pdf.ln(15)
    pdf.set_font("Helvetica", "I", 10)
    pdf.multi_cell(
        0,
        6,
        "PARTIE A : Script image par image (i1-i160)\n"
        "PARTIE B : Scripts VO (max 40 sec, scenes completes uniquement)",
        align="C",
    )

    pdf.add_page()
    pdf.section_title("SPECIFICATIONS TECHNIQUES", 13)
    specs = [
        "Titre YouTube : " + TITLE,
        "Format : POV storytime animation (stick figure minimaliste)",
        "Total images : 260 (i1 a i260)",
        "Duree VO estimee : ~522 sec (~8.7 min)",
        "",
        "RYTHME MONTAGE :",
        "  Hook (i1-i28) : 1 a 1,2 sec par image (~30 sec)",
        "  Corps (i29-i260) : 3 a 4 sec par image",
        "",
        "TIMING VO REEL (mesure utilisateur) : 321 sec / 160 lignes = ~2.01 sec/ligne.",
        "  260 lignes = ~522 sec (~8 min 42). Extension i161-i260 = ~201 sec (~3 min 21).",
        "",
        "REGLE VO ELEVENLABS (IMPORTANT) :",
        "  Chaque bloc VO se termine a la FIN d'une scene narrative complete.",
        "  Ne jamais couper au milieu d'une phrase ou d'une sequence.",
        "  Raison : la voix peut legerement changer entre deux generations.",
        "  Si on coupe au milieu d'une phrase, la difference devient visible.",
        "",
        "PERSONNAGES :",
        "  SISTER (POV) | BROTHER (gattouz0 inspired) | MOTHER | FATHER",
        "  MODEL 1 (Jade) | MODEL 2 | MAYA (classmate)",
        "",
        "PLATEFORMES : OnlyFans, Fansly, TikTok, Instagram, Twitter",
    ]
    for s in specs:
        if not s.strip():
            pdf.ln(2)
        else:
            pdf.body_text(s)

    pdf.add_page()
    pdf.section_title("PARTIE A - SCRIPT COMPLET SCENE PAR SCENE", 14)
    pdf.meta_line("1 phrase = 1 image. Copier chaque ligne pour les prompts Flow.")

    pdf.sub_title("HOOK RAPIDE - i1 a i28 (~30 sec | 1-1,2 sec/image)")
    for img_id, line in HOOK:
        pdf.scene_line(img_id, line)

    for act in ACTS:
        pdf.ln(3)
        pdf.sub_title(f"{act['name']} | {act['images']} | {act['duration']} | {act['pacing']}")
        for img_id, line in act["lines"]:
            pdf.scene_line(img_id, line)

    vo_chunks = build_vo_chunks()

    pdf.add_page()
    pdf.section_title("PARTIE B - SCRIPTS VOICE-OVER (ELEVENLABS)", 14)
    pdf.meta_line(
        "REGLE : chaque bloc = scenes completes seulement (jamais de coupure mid-scene).\n"
        f"Maximum ~{MAX_LINES_40S} lignes par bloc (~{round(MAX_LINES_40S * SEC_PER_LINE, 0):.0f} sec, mesure reelle).\n"
        "VO 1-13 deja generes. Generer seulement VO 14+ (marques NOUVEAU)."
    )
    pdf.ln(2)
    pdf.body_text(f"Nombre total de blocs VO : {len(vo_chunks)}")
    pdf.ln(3)

    for chunk in vo_chunks:
        label = " [NOUVEAU - A GENERER]" if chunk.get("is_new") else " [DEJA GENERE]"
        pdf.sub_title(
            f"VO PART {chunk['part']}{label} - {chunk['start']} a {chunk['end']} "
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
        scenes_short = " + ".join(s.split(" - ", 1)[-1][:25] for s in chunk["scenes"])
        pdf.cell(22, 6, f"Part {chunk['part']}", border=1)
        pdf.cell(28, 6, f"{chunk['start']}-{chunk['end']}", border=1)
        pdf.cell(18, 6, str(chunk["words"]), border=1)
        pdf.cell(18, 6, f"~{chunk['seconds']}s", border=1)
        pdf.cell(0, 6, scenes_short, border=1, new_x="LMARGIN", new_y="NEXT")

    pdf.add_page()
    pdf.section_title("LISTE DES SCENES (unites indivisibles)", 13)
    pdf.meta_line("Ces scenes ne doivent JAMAIS etre reparties entre deux blocs VO differents.")
    pdf.ln(2)
    for i, scene in enumerate(SCENES, 1):
        sw = scene_words(scene)
        sec = round(estimate_seconds_from_lines(len(scene["lines"])), 1)
        start_id = scene["lines"][0][0]
        end_id = scene["lines"][-1][0]
        pdf.body_text(
            f"Scene {i:02d} | {start_id}-{end_id} | ~{sec}s | {sw} mots | {scene['name']}"
        )

    pdf.output(str(OUTPUT))
    WORKSPACE_OUTPUT.write_bytes(OUTPUT.read_bytes())
    return OUTPUT, vo_chunks


if __name__ == "__main__":
    path, chunks = generate_pdf()
    print(f"PDF genere : {path}")
    print(f"Blocs VO : {len(chunks)}")
    for c in chunks:
        print(f"  Part {c['part']}: {c['start']}-{c['end']} | {c['words']} mots | ~{c['seconds']}s")
        for s in c["scenes"]:
            print(f"    - {s}")
