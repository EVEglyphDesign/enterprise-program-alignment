#!/usr/bin/env python3
"""Build the phone-readable review brief PDF for the Enterprise Program Alignment surface.

Canon: cream ground, one orange accent, Fraunces display + Inter body, EgD watermark,
SHA-256 content hash, Key ID, ISO-8601 UTC timestamp, closing mark. Built twice so the
stamped page count matches the pages rendered.
"""
import hashlib, datetime, pathlib, sys
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

ROOT = pathlib.Path(__file__).resolve().parents[1]
FONTS = pathlib.Path("/home/user/workspace/fonts")
MARK = ROOT / "docs" / "assets" / "egd-mark.jpg"
OUT = ROOT / "docs" / "EVEglyphDesign_Enterprise_Program_Alignment_Review_Brief.pdf"

CREAM, CREAM2 = HexColor("#fdfaf4"), HexColor("#f7f2e7")
INK, MUTE, LINE = HexColor("#1a1a1a"), HexColor("#6b665c"), HexColor("#e7e1d3")
ACCENT = HexColor("#e87722")

pdfmetrics.registerFont(TTFont("Fraunces", str(FONTS / "Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf.ttf")))
pdfmetrics.registerFont(TTFont("Inter", str(FONTS / "Inter%5Bopsz,wght%5D.ttf.ttf")))

SURFACE = "https://eveglyphdesign.github.io/enterprise-program-alignment/"
REVIEW = "https://eveglyphdesign.github.io/enterprise-program-alignment/review.html"
MAILTO = ("mailto:dany@steelcloudsolutions.com?subject=Enterprise%20Program%20Alignment"
          "%20%E2%80%94%20review%20comments")
KEY_ID = "EgD-KEY-2026-07"

S = {
 "eyebrow": ParagraphStyle("eyebrow", fontName="Inter", fontSize=7.5, leading=10,
                           textColor=ACCENT, spaceAfter=5, alignment=TA_LEFT),
 "h1": ParagraphStyle("h1", fontName="Fraunces", fontSize=21, leading=24,
                      textColor=INK, spaceAfter=8),
 "lead": ParagraphStyle("lead", fontName="Inter", fontSize=10, leading=15,
                        textColor=MUTE, spaceAfter=12),
 "h2": ParagraphStyle("h2", fontName="Fraunces", fontSize=14, leading=17,
                      textColor=INK, spaceBefore=12, spaceAfter=7),
 "item": ParagraphStyle("item", fontName="Inter", fontSize=10, leading=14,
                        textColor=INK, spaceAfter=1),
 "body": ParagraphStyle("body", fontName="Inter", fontSize=9.5, leading=14,
                        textColor=MUTE, spaceAfter=9),
 "link": ParagraphStyle("link", fontName="Inter", fontSize=10, leading=15,
                        textColor=ACCENT, spaceAfter=6),
}

CHANGES = [
 ("It opens in plain language",
  "The technical argument is still there, but it no longer leads. A business reader gets the "
  "whole story without meeting a single acronym."),
 ("Everything has a second level",
  "The page used to be one long plane of text. Each point is now a single line that opens when "
  "you tap it — read the headlines only, or open the ones you care about."),
 ("What the client keeps sits near the top",
  "Seven plain commitments: the client owns the record, a person approves before anything counts, "
  "nothing is deleted to tidy the record, and so on. Each opens to the detail and the standard "
  "behind it."),
 ("The technical layer is behind one click",
  "Client tools, zero egress, a model that runs inside the client's own boundary, fixed output, "
  "analytics that continue after the program ends. Collapsed by default, for security and IT."),
 ("Delivery described the way it is run",
  "Six phases, each carrying the access work and the recorded-session work underneath. "
  "Connections proven before the team is mobilised."),
]

ASKS = [
 ("Does the opening sound like us?",
  "The first screen and the two lanes underneath it — right tone, or still too much?"),
 ("Are the seven commitments the right seven?",
  "Anything missing that a client would ask about, or anything we should not be promising."),
 ("Is the technical detail in the right place?",
  "Behind one click: enough for a security reviewer, invisible to everyone else."),
 ("Anything you would not say to a client?",
  "Flag the sentence and it comes out."),
 ("Your name and role on the page",
  "The stewardship section describes the role but names no one. Say the word and it carries your "
  "name, or it stays as it is."),
]


def story(total_pages_label):
    f = []
    f.append(Paragraph("REVIEW BRIEF · FOR LILLIAN", S["eyebrow"]))
    f.append(Paragraph("The surface is ready for your read.", S["h1"]))
    f.append(Paragraph(
        "Nothing here is final. This is the short version of what changed and what would be most "
        "useful to hear back on. The surface itself takes about four minutes if you only open the "
        "parts you care about.", S["lead"]))
    f.append(Paragraph(f'<link href="{SURFACE}"><b>Open the surface</b></link>', S["link"]))
    f.append(Paragraph(f'<link href="{REVIEW}"><b>Open the review page</b></link>', S["link"]))
    f.append(Paragraph(f'<link href="{MAILTO}"><b>Send your comments</b></link>', S["link"]))

    f.append(Paragraph("What changed in this pass", S["h2"]))
    for i, (t, d) in enumerate(CHANGES, 1):
        f.append(KeepTogether([Paragraph(f"{i:02d} &nbsp;{t}", S["item"]),
                               Paragraph(d, S["body"])]))

    f.append(Paragraph("What would help most to hear", S["h2"]))
    for i, (t, d) in enumerate(ASKS, 1):
        f.append(KeepTogether([Paragraph(f"{i:02d} &nbsp;{t}", S["item"]),
                               Paragraph(d, S["body"])]))

    f.append(Paragraph("How to send comments", S["h2"]))
    f.append(Paragraph(
        "Quote the section heading and, where it helps, the row number — for example "
        '"What the client keeps, row 04". No need to be tidy about it. Every comment lands as a '
        "dated entry in the repository, so the next version shows what changed and why. Nothing is "
        "deleted; earlier versions stay alongside the current one.", S["body"]))
    f.append(Paragraph(f'<link href="{MAILTO}"><b>dany@steelcloudsolutions.com</b></link>', S["link"]))
    return f


def make(path, page_total, content_hash, stamp):
    doc = BaseDocTemplate(str(path), pagesize=A5,
                          leftMargin=14 * mm, rightMargin=14 * mm,
                          topMargin=18 * mm, bottomMargin=17 * mm,
                          title="Enterprise Program Alignment — Review Brief",
                          author="EVEglyphDesign", subject="Review brief")

    def decorate(canvas, docu):
        canvas.saveState()
        canvas.setFillColor(CREAM)
        canvas.rect(0, 0, A5[0], A5[1], stroke=0, fill=1)
        # the supplied EgD mark, small, top of each page
        if MARK.exists():
            side = 9 * mm
            canvas.drawImage(str(MARK), 14 * mm, A5[1] - 9.6 * mm - side * 0.05,
                             width=side, height=side, mask='auto')
        # rules
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.6)
        canvas.line(14 * mm, A5[1] - 12 * mm, A5[0] - 14 * mm, A5[1] - 12 * mm)
        canvas.line(14 * mm, 13 * mm, A5[0] - 14 * mm, 13 * mm)
        canvas.setFont("Inter", 6.5)
        canvas.setFillColor(MUTE)
        canvas.drawString(26 * mm, A5[1] - 6.5 * mm, "EVEglyphDesign · Enterprise Program Alignment")
        canvas.drawRightString(A5[0] - 14 * mm, A5[1] - 6.5 * mm, stamp)
        canvas.drawString(14 * mm, 9.5 * mm,
                          f"© 2026 EVEglyphDesign. Controlled copy · Key {KEY_ID}")
        canvas.drawRightString(A5[0] - 14 * mm, 9.5 * mm,
                               f"Page {docu.page} of {page_total}")
        canvas.setFont("Inter", 6)
        canvas.drawString(14 * mm, 6.5 * mm, f"SHA-256 {content_hash}")
        canvas.setFillColor(ACCENT)
        canvas.drawRightString(A5[0] - 14 * mm, 6.5 * mm, "Pour le bien-être du peuple")
        canvas.restoreState()

    frame = Frame(doc.leftMargin, doc.bottomMargin,
                  A5[0] - doc.leftMargin - doc.rightMargin,
                  A5[1] - doc.topMargin - doc.bottomMargin, id="body")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=decorate)])
    doc.build(story(page_total))
    return doc.page


if __name__ == "__main__":
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = "".join(t + d for t, d in CHANGES + ASKS).encode()
    chash = hashlib.sha256(payload).hexdigest()
    tmp = OUT.with_suffix(".tmp.pdf")
    n = make(tmp, 1, chash, stamp)          # pass one: discover the page count
    make(OUT, n, chash, stamp)              # pass two: stamp it
    tmp.unlink(missing_ok=True)
    print(f"built {OUT} · {n} page(s) · sha256 {chash[:16]}… · {stamp}")
