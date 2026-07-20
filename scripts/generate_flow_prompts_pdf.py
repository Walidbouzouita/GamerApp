#!/usr/bin/env python3
"""Generate Bubbello-style Google Flow prompts PDF with reference tables per lot."""

import importlib.util
from pathlib import Path

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

from flow_prompt_data import REF_FILES, REF_ROLES, SCENE_LOT_META

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT.parent / "POV-Husband-OF-Wife-Flow-Prompts.pdf"

# Load SCENES from production script
_spec = importlib.util.spec_from_file_location("prod", ROOT / "generate_of_wife_pdf.py")
_prod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_prod)
SCENES = _prod.SCENES

STYLE_BLOCK = """Minimalist 2D storytime animation cartoon. Same project style as OnlyFans BROTHER/SISTER channel: thick black outlines, flat colors, clean white or very pale background, expressive faces, simple readable compositions, cinematic POV storytime framing. NO photorealism. NO image numbers. No readable text, logos, headlines, dates, names, or captions on artwork; add those during editing. Suggestive outfits allowed, never explicit nudity."""

RULE_BOX_TOP = """RULE #1 - NO IMAGE NUMBERS ON THE ARTWORK (CRITICAL)
DO NOT write image IDs anywhere on the image.
DO NOT write corner numbers, watermarks, filenames, or labels on canvas.
Any narration, dates, names, messages, headlines, or amounts must be added later in editing."""

RULE_BOX_BOTTOM = """REMINDER: Zero image IDs or filenames on artwork. No watermark.
Keep every character consistent with the attached reference sheets.
Rename exported files to match i-numbers after generation."""


def wife_label_from_refs(refs: list[str]) -> str:
  wife_keys = [r for r in refs if r.startswith("WIFE_")]
  if not wife_keys:
    return "-"
  return ", ".join(k.replace("WIFE_", "") for k in wife_keys)


def collect_lot_refs(images_meta: list) -> list[str]:
  seen = []
  for refs, _ in images_meta:
    for r in refs:
      if r != "NONE" and r not in seen:
        seen.append(r)
  return seen


def format_ref_attach(refs: list[str]) -> str:
  if not refs or refs == ["NONE"]:
    return "NONE.\nNO CHARACTER REFERENCE REQUIRED."
  names = ", ".join(refs)
  uses = "\n".join(f"USE {r} REFERENCE." for r in refs)
  files = "\n".join(f"  - {r} -> {REF_FILES[r]}" for r in refs)
  return f"{names}.\n{uses}\nAttach files:\n{files}"


def build_batch_intro(scene: dict, lot_meta: dict, lot_refs: list[str], img_start: int) -> str:
  img_end = img_start + scene["count"] - 1
  wife_ver = lot_meta["wife_version"]
  ref_lines = "\n".join(
    f"- {r}: {REF_ROLES.get(r, '')} -> {REF_FILES.get(r, '')}" for r in lot_refs
  ) or "- NONE for this lot"
  return f"""Generate {scene['count']} separate images. 16:9. Minimalist 2D storytime animation cartoon.
Same project style as OnlyFans BROTHER/SISTER channel.

THE WIFE VERSION FOR THIS LOT: {wife_ver}

CHARACTER REFERENCE FILES (attach in Flow as needed):
{ref_lines}

HUSBAND: man 32, short messy brown hair, medium skin, blue work shirt or grey t-shirt, wedding band.
THE WIFE: woman 29, honey-blonde wavy hair, warm tan skin, glamorous cartoon - use correct WIFE version sheet.

STORY FACTS (DO NOT CHANGE):
Fiction POV. No explicit content. OnlyFans referenced as plot only. Ending is morally open.

STYLE:
{STYLE_BLOCK}

Scene mood: {lot_meta['mood']}
FILE NAMES (export only): i{img_start} through i{img_end}"""


def build_styles():
  styles = getSampleStyleSheet()
  styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontSize=15, leading=18))
  styles.add(ParagraphStyle(name="SectionHead", parent=styles["Heading1"], fontSize=12, leading=15, spaceBefore=10, spaceAfter=6))
  styles.add(ParagraphStyle(name="LotHead", parent=styles["Heading2"], fontSize=11, leading=14, spaceBefore=8, spaceAfter=4))
  styles.add(ParagraphStyle(name="BodySmall", parent=styles["Normal"], fontSize=8.5, leading=11))
  styles.add(ParagraphStyle(name="PromptBox", parent=styles["Code"], fontSize=7, leading=9, backColor=colors.HexColor("#f7f7f7")))
  styles.add(ParagraphStyle(name="RuleBox", parent=styles["Code"], fontSize=7, leading=9, backColor=colors.HexColor("#fff3cd")))
  return styles


def header_footer(canvas, doc):
  canvas.saveState()
  canvas.setFont("Helvetica", 7)
  canvas.setFillColor(colors.grey)
  canvas.drawString(0.75 * inch, 0.5 * inch, "Bubbello - Google Flow batch prompts")
  canvas.drawRightString(7.75 * inch, 0.5 * inch, f"Page {doc.page}")
  canvas.restoreState()


def main():
  total_images = sum(s["count"] for s in SCENES)
  doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=letter,
    leftMargin=0.65 * inch, rightMargin=0.65 * inch,
    topMargin=0.65 * inch, bottomMargin=0.65 * inch,
  )
  styles = build_styles()
  story = []

  # Cover
  story.append(Paragraph("BUBBELLO", styles["CoverTitle"]))
  story.append(Paragraph("Google Flow Prompts - Lot par lot", styles["CoverTitle"]))
  story.append(Paragraph("POV: Your Life As The Husband Of An OnlyFans Wife", styles["CoverTitle"]))
  story.append(Spacer(1, 0.1 * inch))
  story.append(Paragraph(f"Total {len(SCENES)} lots Flow / {total_images} images", styles["BodySmall"]))
  story.append(Paragraph("Hook 3 lots / 30 images / 1-2 sec par image", styles["BodySmall"]))
  story.append(Paragraph(f"Corps 21 lots / {total_images - 30} images / 3-4 sec par image", styles["BodySmall"]))
  story.append(Paragraph("Limite 10 ou 11 images par lot - jamais plus de 16", styles["BodySmall"]))
  story.append(Spacer(1, 0.08 * inch))
  story.append(Paragraph(
    "References: HUSBAND, WIFE_HOME, WIFE_CREATOR, WIFE_PERFORMING, WIFE_NIGHT, WIFE_GLAMOUR, "
    "NEIGHBOR, MOTHER_IN_LAW, FATHER_IN_LAW, COWORKER, HR_MANAGER",
    styles["BodySmall"],
  ))
  story.append(Paragraph(
    "Avant chaque lot: tableau des references + version THE WIFE a utiliser.",
    styles["BodySmall"],
  ))
  story.append(PageBreak())

  # Master reference file table
  story.append(Paragraph("TABLEAU MASTER - FICHIERS REFERENCE", styles["SectionHead"]))
  ref_data = [["Reference ID", "Fichier PNG", "Role"]]
  for rid, fname in REF_FILES.items():
    ref_data.append([rid, fname, REF_ROLES.get(rid, "")])
  rt = Table(ref_data, colWidths=[1.2 * inch, 2.0 * inch, 3.0 * inch])
  rt.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 7),
    ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
  ]))
  story.append(rt)
  story.append(PageBreak())

  # Index lots
  story.append(Paragraph("INDEX DES LOTS FLOW", styles["SectionHead"]))
  idx = [["Lot", "Scene", "Images", "Nb", "WIFE version", "Rythme"]]
  for s in SCENES:
    lm = SCENE_LOT_META[s["num"]]
    idx.append([
      f"Flow {s['num']:02d}", s["name"], s["range"], str(s["count"]),
      lm["wife_version"], s["rhythm"],
    ])
  it = Table(idx, colWidths=[0.55 * inch, 1.1 * inch, 0.7 * inch, 0.35 * inch, 1.5 * inch, 0.85 * inch])
  it.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 6.5),
    ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
  ]))
  story.append(it)
  story.append(PageBreak())

  # Each lot
  img_counter = 0
  for s in SCENES:
    lot_meta = SCENE_LOT_META[s["num"]]
    images_meta = lot_meta["images"]
    if len(images_meta) != s["count"]:
      raise ValueError(f"Scene {s['num']}: expected {s['count']} images, got {len(images_meta)}")

    lot_refs = collect_lot_refs(images_meta)
    img_start = img_counter + 1

    story.append(Paragraph(f"FLOW {s['num']:02d} - {s['name']}", styles["LotHead"]))
    story.append(Paragraph(
      f"{s['act']} | {s['range']} | {s['count']} images | {s['rhythm']}",
      styles["BodySmall"],
    ))
    story.append(Spacer(1, 0.05 * inch))

    # Reference table for lot
    story.append(Paragraph("Tableau des references a utiliser dans ce lot", styles["BodySmall"]))
    story.append(Paragraph(
      f"THE WIFE version pour ce lot: <b>{lot_meta['wife_version']}</b>",
      styles["BodySmall"],
    ))
    if lot_refs:
      tdata = [["Reference", "Fichier", "Role / reminder"]]
      for r in lot_refs:
        tdata.append([r, REF_FILES.get(r, ""), REF_ROLES.get(r, "")])
      tt = Table(tdata, colWidths=[1.1 * inch, 1.8 * inch, 3.3 * inch])
      tt.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8f4e8")),
      ]))
      story.append(tt)
    else:
      story.append(Paragraph("Aucune reference personnage requise pour ce lot (props/decors seulement).", styles["BodySmall"]))

    story.append(Spacer(1, 0.06 * inch))
    story.append(Preformatted(RULE_BOX_TOP, styles["RuleBox"]))
    story.append(Spacer(1, 0.04 * inch))
    story.append(Preformatted(build_batch_intro(s, lot_meta, lot_refs, img_start), styles["PromptBox"]))
    story.append(Spacer(1, 0.06 * inch))

    for i, (phrase, (refs, visual)) in enumerate(zip(s["phrases"], images_meta)):
      img_counter += 1
      wife_ver = wife_label_from_refs(refs)
      ref_used = "\n".join(f"- {r}" for r in refs) if refs != ["NONE"] else "- NONE (no character reference sheet required)"
      block = f"""FILE: i{img_counter} | NO NUMBER ON ARTWORK
THE WIFE VERSION: {wife_ver if wife_ver != '-' else 'NONE (no wife in frame)'}
REFERENCE IMAGE(S) TO ATTACH IN FLOW: {format_ref_attach(refs)}
VISUAL: {visual}
STORY BEAT: {phrase}
Do not place the story-beat sentence on the artwork. NO image numbers.
CHARACTER REFERENCES USED IN THIS PROMPT:
{ref_used}"""
      story.append(Preformatted(block, styles["PromptBox"]))
      story.append(Spacer(1, 0.03 * inch))

    story.append(Preformatted(RULE_BOX_BOTTOM, styles["RuleBox"]))
    story.append(PageBreak())

  doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
  print(f"PDF generated: {OUTPUT}")
  print(f"Pages for {len(SCENES)} lots, {img_counter} images")


if __name__ == "__main__":
  main()
