"""
Rebuild the MonasteryAI PPTX for Odisha Heritage Preservation.
Preserves layout, colors, shapes, images. Replaces all text content.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import copy

INPUT_PATH = r"C:\Users\shree\Desktop\sih\MonasteryAI-SIH2026-Idea-Presentation-FINAL_v15.pptx"
OUTPUT_PATH = r"C:\Users\shree\Desktop\sih\OdishaHeritage-SIH2026-Idea-Presentation.pptx"

prs = Presentation(INPUT_PATH)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def clear_textbox(shape):
    """Remove all paragraphs from a text frame."""
    tf = shape.text_frame
    for para in tf.paragraphs:
        for run in para.runs:
            run.text = ""
        para.text = ""
    # Remove all but first paragraph
    while len(tf.paragraphs) > 1:
        p = tf.paragraphs[-1]._p
        p.getparent().remove(p)
    tf.paragraphs[0].clear()


def set_paragraph_text(para, text, bold=None, size=None, color=None, font_name=None):
    """Set text of a paragraph with formatting."""
    para.clear()
    run = para.add_run()
    run.text = text
    if bold is not None:
        run.font.bold = bold
    if size is not None:
        run.font.size = size
    if color is not None:
        run.font.color.rgb = color
    if font_name is not None:
        run.font.name = font_name


def add_paragraph(tf, text, bold=None, size=None, color=None, font_name=None, alignment=None):
    """Add a new paragraph to a text frame."""
    para = tf.add_paragraph()
    if alignment:
        para.alignment = alignment
    run = para.add_run()
    run.text = text
    if bold is not None:
        run.font.bold = bold
    if size is not None:
        run.font.size = size
    if color is not None:
        run.font.color.rgb = color
    if font_name is not None:
        run.font.name = font_name
    return para


def add_mixed_paragraph(tf, parts, size=None, alignment=None):
    """
    Add a paragraph with mixed bold/normal formatting.
    parts: list of (text, bold) tuples
    """
    para = tf.add_paragraph()
    if alignment:
        para.alignment = alignment
    for text, bold in parts:
        run = para.add_run()
        run.text = text
        run.font.bold = bold
        if size:
            run.font.size = size
    return para


def write_textbox(shape, lines, default_size=Pt(16), title_size=Pt(20)):
    """
    Rewrite a textbox entirely.
    lines: list of dicts with keys:
      - text: str
      - bold: bool (optional)
      - size: Pt (optional)
      - parts: list of (text, bold) tuples for mixed formatting (optional)
      - blank: bool (optional) — insert empty paragraph
    """
    tf = shape.text_frame
    tf.word_wrap = True

    # Clear existing
    while len(tf.paragraphs) > 1:
        p = tf.paragraphs[-1]._p
        p.getparent().remove(p)
    tf.paragraphs[0].clear()

    for idx, line in enumerate(lines):
        if idx == 0:
            para = tf.paragraphs[0]
        else:
            para = tf.add_paragraph()

        if line.get("blank"):
            continue

        if "parts" in line:
            sz = line.get("size", default_size)
            for text, bold in line["parts"]:
                run = para.add_run()
                run.text = text
                run.font.bold = bold
                run.font.size = sz
        else:
            run = para.add_run()
            run.text = line.get("text", "")
            run.font.bold = line.get("bold", None)
            run.font.size = line.get("size", default_size)
            if "color" in line:
                run.font.color.rgb = line["color"]


# ============================================================
# SLIDE 1: TITLE PAGE
# ============================================================
slide1 = prs.slides[0]

for shape in slide1.shapes:
    # Subtitle placeholder — "TITLE PAGE"
    if shape.name == "Subtitle 3":
        tf = shape.text_frame
        while len(tf.paragraphs) > 1:
            p = tf.paragraphs[-1]._p
            p.getparent().remove(p)
        tf.paragraphs[0].clear()
        # Empty first para
        para2 = tf.add_paragraph()
        run = para2.add_run()
        run.text = "TITLE PAGE"
        run.font.bold = True

    # Main title
    if shape.name == "Title 7":
        tf = shape.text_frame
        tf.paragraphs[0].clear()
        run = tf.paragraphs[0].add_run()
        run.text = "SMART INDIA HACKATHON 2026"
        run.font.bold = True
        run.font.size = Pt(40)

    # Team info box
    if shape.name == "TextBox 9":
        write_textbox(shape, [
            {"text": "Problem Statement ID – [Insert PS ID]", "bold": True, "size": Pt(24)},
            {"text": "Problem Statement Title – Digitize and Preserve the Cultural Heritage of Odisha", "bold": True, "size": Pt(24)},
            {"text": "Theme – Heritage & Culture", "bold": True, "size": Pt(24)},
            {"text": "PS Category – Software", "bold": True, "size": Pt(24)},
            {"text": "Team ID – [Insert Team ID]", "bold": True, "size": Pt(24)},
            {"text": "Team Name (Registered on portal) – [FULCRUM]", "bold": True, "size": Pt(24)},
        ], default_size=Pt(24))

    # Team name oval
    if shape.name == "Oval 1" or (hasattr(shape, "text") and "FULCRUM" in shape.text and shape.name != "TextBox 9"):
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    run.text = "FULCRUM"

print("✅ Slide 1: Title Page — DONE")


# ============================================================
# SLIDE 2: IDEA / APPROACH DETAILS
# ============================================================
slide2 = prs.slides[1]

for shape in slide2.shapes:
    # Title
    if shape.name == "Title 1":
        tf = shape.text_frame
        tf.paragraphs[0].clear()
        run = tf.paragraphs[0].add_run()
        run.text = "IDEA / APPROACH DETAILS"
        run.font.bold = True
        run.font.size = Pt(36)

    # Team name oval
    if shape.name == "Oval 1":
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    run.text = "FULCRUM"

    # Left top box: Problem Statement
    if shape.name == "TextBox 15361":
        write_textbox(shape, [
            {"text": "PROBLEM STATEMENT:", "size": Pt(20), "bold": True},
            {"parts": [
                ("Problem: ", True),
                ("Odisha is home to one of India's richest cultural heritages — from the UNESCO World Heritage Site of ", False),
                ("Konark Sun Temple", True),
                (" to the sacred ", False),
                ("Jagannath Puri", True),
                (", ancient ", False),
                ("Udayagiri-Khandagiri caves", True),
                (", and the magnificent ", False),
                ("Lingaraja Temple", True),
                (". These monuments face deterioration from ", False),
                ("pollution, climate change", True),
                (", and ", False),
                ("human interference", True),
                (". Tourists lack ", False),
                ("immersive multilingual cultural context", True),
                (".", False),
            ], "size": Pt(16)},
            {"parts": [
                ("Need: ", True),
                ("A ", False),
                ("digital cultural preservation platform", True),
                (" with ", False),
                ("immersive AR/VR experiences", True),
                (", an ", False),
                ("AI-powered multilingual tour guide", True),
                (" (via Sarvam AI), and ", False),
                ("crowdsourced 3D scanning", True),
                (" (via VGGT-Ω) to digitize and showcase Odisha's heritage to the world.", False),
            ], "size": Pt(16)},
        ])

    # Left bottom box: UVPs
    if shape.name == "TextBox 15362":
        write_textbox(shape, [
            {"text": "Unique Value Propositions (UVP):", "size": Pt(20), "bold": True},
            {"parts": [
                ("Crowdsourced 3D Reconstruction: ", True),
                ("Instead of ", False),
                ("$4,000 LiDAR rigs", True),
                (", tourists reconstruct true ", False),
                ("3D environments", True),
                (" from a simple ", False),
                ("smartphone video", True),
                (" using VGGT-Ω AI.", False),
            ], "size": Pt(16)},
            {"parts": [
                ("Sovereign Indic Language AI: ", True),
                ("Powered by ", False),
                ("Sarvam AI", True),
                (" — India's own language models supporting ", False),
                ("22 Indian languages", True),
                (" with native accent recognition and ", False),
                ("code-mixed speech", True),
                (" (e.g., Odia + English).", False),
            ], "size": Pt(16)},
            {"parts": [
                ("Immersive AR/VR Tours: ", True),
                ("360-degree virtual exploration", True),
                (" of monument interiors with ", False),
                ("animated reconstructions", True),
                (" and interactive storytelling.", False),
            ], "size": Pt(16)},
        ])

    # Right side box: Idea/Solution
    if shape.name == "TextBox 15363":
        write_textbox(shape, [
            {"text": "IDEA / SOLUTION:", "size": Pt(20), "bold": True},
            {"text": "We are building a digitalized platform for cultural preservation and tourism of Odisha Heritage, combining AI, AR/VR, and crowdsourced 3D reconstruction.", "size": Pt(16)},
            {"blank": True},
            {"text": "Key Features:", "size": Pt(18), "bold": True},
            {"text": "1. AR/VR Immersive Experiences: Augmented Reality overlays and Virtual Reality modules with animated reconstructions via Unity & Three.js.", "size": Pt(15)},
            {"text": "2. AI-Powered Multilingual Tour Guide: Conversational AR guide powered by Sarvam AI (Saaras ASR + Bulbul TTS + Translate) for 22 Indian languages.", "size": Pt(15)},
            {"text": "3. Crowdsourced 3D Scanning: Users capture smartphone video → VGGT-Ω AI instantly generates high-fidelity 3D models, turning tourists into digital preservationists.", "size": Pt(15)},
            {"text": "4. 360-Degree Virtual Tours: Step inside monument interiors virtually from anywhere in the world.", "size": Pt(15)},
            {"text": "5. AR-Based Navigation Maps: Interactive maps with travel routes and nearby attraction discovery.", "size": Pt(15)},
            {"text": "6. Phased Rollout: Starting with Konark, Puri, Lingaraja — scaling to 100+ heritage sites across Odisha and India.", "size": Pt(15)},
        ])

print("✅ Slide 2: Idea/Approach — DONE")


# ============================================================
# SLIDE 3: TECHNICAL APPROACH
# ============================================================
slide3 = prs.slides[2]

for shape in slide3.shapes:
    # Title
    if shape.name == "Title 1":
        tf = shape.text_frame
        tf.paragraphs[0].clear()
        run = tf.paragraphs[0].add_run()
        run.text = "TECHNICAL APPROACH"
        run.font.bold = True
        run.font.size = Pt(36)

    # Team oval
    if shape.name == "Oval 10":
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    run.text = "FULCRUM"

    # Main tech stack text box
    if shape.name == "TextBox 17409":
        write_textbox(shape, [
            {"text": "Core Technologies and Why We Chose Them:", "size": Pt(18), "bold": True},
            {"text": "• Unity (C#): Industry-standard engine for building immersive AR/VR experiences on mobile and VR headsets.", "size": Pt(14)},
            {"text": "• Three.js / gsplat.js: Renders animated 3D graphics, Gaussian splats, and 360-degree views directly in the browser.", "size": Pt(14)},
            {"text": "• React Native (Expo): Cross-platform mobile app for iOS and Android with a single codebase.", "size": Pt(14)},
            {"text": "• NextJS + React: Server-side rendered web frontend for SEO, performance, and static site generation.", "size": Pt(14)},
            {"text": "• VGGT-Ω (Meta AI, CVPR 2026): State-of-the-art feed-forward 3D reconstruction. Converts smartphone video into high-fidelity 3D models — no LiDAR needed.", "size": Pt(14)},
            {"text": "• Sarvam AI Suite: Saaras (ASR for 22 languages), Bulbul (natural TTS in 11 languages), Translate (22 languages). India's sovereign Indic AI.", "size": Pt(14)},
            {"text": "• NodeJS + MongoDB: Scalable backend and NoSQL database for tourist and heritage data.", "size": Pt(14)},
            {"text": "• Cloudinary: Media CDN to optimize and deliver heavy 3D assets, images, and videos globally.", "size": Pt(14)},
        ])

    # Caption for VGGT figure
    if shape.name == "TextBox 3":
        write_textbox(shape, [
            {"parts": [
                ("Fig 1: 3D Consistency: ", True),
                ("Older models like ", False),
                ("MegaSaM ", True),
                ("bend walls and smear textures. Meta ", False),
                ("VGGT-Ω ", True),
                ("builds straight, ", False),
                ("consistent 3D environments", True),
                (" from smartphone videos — enabling crowdsourced heritage preservation.", False),
            ], "size": Pt(12)},
        ])

print("✅ Slide 3: Technical Approach — DONE")


# ============================================================
# SLIDE 4: FEASIBILITY AND VIABILITY
# ============================================================
slide4 = prs.slides[3]

for shape in slide4.shapes:
    # Title
    if shape.name == "Title 1":
        tf = shape.text_frame
        tf.paragraphs[0].clear()
        run = tf.paragraphs[0].add_run()
        run.text = "FEASIBILITY AND VIABILITY"
        run.font.bold = True
        run.font.size = Pt(36)

    # Team oval
    if shape.name == "Oval 11":
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    run.text = "FULCRUM"

    # Feasibility text
    if shape.name == "TextBox 17416":
        write_textbox(shape, [
            {"text": "Feasibility:", "size": Pt(20), "bold": True},
            {"text": "1. Processing Speed (See Fig. 2): Meta VGGT-Ω is 50× faster than optimization-based methods, processing 1000+ frames on a single GPU.", "size": Pt(14)},
            {"text": "2. Sovereign AI (See Fig. 3): Sarvam AI is optimized for Indian languages with code-mixed speech support — outperforming global models on Indic benchmarks.", "size": Pt(14)},
            {"text": "3. Scalable Cloud Infrastructure: Cloudinary CDN + AWS ensures global delivery of heavy 3D/AR assets.", "size": Pt(14)},
            {"text": "4. Partnerships: Collaboration with ASI (Archaeological Survey of India), Odisha Tourism Board, and UNESCO for content approval and historical accuracy.", "size": Pt(14)},
            {"text": "5. Education: Engages students and researchers with immersive AR/VR storytelling tools.", "size": Pt(14)},
        ])

    # Solutions / Viability text
    if shape.name == "TextBox 17417":
        write_textbox(shape, [
            {"text": "Viability & Solutions:", "size": Pt(20), "bold": True},
            {"text": "1. Revenue Streams: Partnerships, premium VR subscriptions, API licensing for tourism boards, and institutional collaborations.", "size": Pt(14)},
            {"text": "2. Cost-Effective: VGGT-Ω eliminates expensive LiDAR equipment. Open-source stack (React, Node, Three.js) keeps dev costs low.", "size": Pt(14)},
            {"text": "3. Community Validation: Local historians and ASI experts review AR content before deployment for historical accuracy.", "size": Pt(14)},
            {"text": "4. Market Opportunity: Growing smartphone penetration and AR adoption makes immersive heritage tourism practical for millions of domestic tourists.", "size": Pt(14)},
            {"text": "5. Scalable Architecture: Built to expand from Odisha to all heritage sites across India without re-architecture.", "size": Pt(14)},
        ])

    # VGGT figure caption
    if shape.name == "TextBox 17415":
        write_textbox(shape, [
            {"text": "Fig. 2: 3D Generation Efficiency: Meta VGGT-Ω drastically reduces inference time compared to older models. Processing hundreds of videos into 3D environments is fast and cost-effective. (Source: Meta AI)", "size": Pt(10)},
        ])

    # LFM figure caption → now Sarvam caption
    if shape.name == "TextBox 17414":
        write_textbox(shape, [
            {"text": "Fig. 3: Sovereign Indic AI: Sarvam AI's models natively handle 22 Indian languages with code-mixed speech recognition, outperforming global models on Indian benchmarks. Powers our multilingual AR tour guide. (Source: Sarvam AI)", "size": Pt(10)},
        ])

print("✅ Slide 4: Feasibility & Viability — DONE")


# ============================================================
# SLIDE 5: IMPACT AND BENEFITS
# ============================================================
slide5 = prs.slides[4]

for shape in slide5.shapes:
    # Title
    if shape.name == "Title 1":
        tf = shape.text_frame
        tf.paragraphs[0].clear()
        run = tf.paragraphs[0].add_run()
        run.text = "IMPACT AND BENEFITS"
        run.font.bold = True
        run.font.size = Pt(36)

    # Team oval
    if shape.name == "Oval 11":
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    run.text = "FULCRUM"

    # Left box — Impact
    if shape.name == "TextBox 17409":
        write_textbox(shape, [
            {"text": "Potential Impact on Target Audience:", "size": Pt(20), "bold": True},
            {"blank": True},
            {"parts": [
                ("Cultural Awareness & Global Reach: ", True),
                ("Puts Odisha's heritage on the international digital map. Tourists worldwide experience temples and caves via ", False),
                ("immersive AR/VR", True),
                (" and ", False),
                ("crowdsourced 3D models", True),
                (".", False),
            ], "size": Pt(16)},
            {"parts": [
                ("Democratized Preservation: ", True),
                ("Any tourist with a smartphone becomes a ", False),
                ("digital preservationist", True),
                (" — capturing video that AI converts into permanent 3D heritage records, without expensive LiDAR teams.", False),
            ], "size": Pt(16)},
            {"parts": [
                ("Boosted Local Economy: ", True),
                ("Increased tourist engagement (target ", False),
                ("10% boost", True),
                (") translates to revenue for local communities, artisans, and guides.", False),
            ], "size": Pt(16)},
        ])

    # Right box — Benefits
    if shape.name == "TextBox 17410":
        write_textbox(shape, [
            {"text": "Benefits of the Solution:", "size": Pt(20), "bold": True},
            {"blank": True},
            {"text": "Social:", "size": Pt(18), "bold": True},
            {"text": "• Fosters global appreciation for Odisha's rich cultural heritage.", "size": Pt(14)},
            {"text": "• Bridges the linguistic digital divide — Sarvam AI enables access in 22 Indian languages.", "size": Pt(14)},
            {"text": "• Benefits not just tourists but also schools, rural communities, and researchers.", "size": Pt(14)},
            {"blank": True},
            {"text": "Economic:", "size": Pt(18), "bold": True},
            {"text": "• Low deployment overhead — open-source stack with Cloudinary CDN eliminates expensive infrastructure.", "size": Pt(14)},
            {"text": "• Strategic Partnerships: Collaborating with ASI, Odisha Tourism Board, and UNESCO.", "size": Pt(14)},
            {"text": "• Premium AR/VR subscriptions and API licensing create sustainable revenue streams.", "size": Pt(14)},
        ])

print("✅ Slide 5: Impact & Benefits — DONE")


# ============================================================
# SLIDE 6: RESEARCH AND REFERENCES
# ============================================================
slide6 = prs.slides[5]

for shape in slide6.shapes:
    # Title
    if shape.name == "Title 1":
        tf = shape.text_frame
        tf.paragraphs[0].clear()
        run = tf.paragraphs[0].add_run()
        run.text = "RESEARCH  AND REFERENCES"
        run.font.bold = True
        run.font.size = Pt(36)

    # Team oval
    if shape.name == "Oval 8":
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    run.text = "FULCRUM"

    # References text box
    if shape.name == "TextBox 17409":
        write_textbox(shape, [
            {"text": "❖ References", "size": Pt(20), "bold": True},
            {"blank": True},
            {"text": "➤ VGGT-Ω (CVPR 2026): Feed-forward 3D/4D reconstruction at scale. https://vggt-omega.github.io/", "size": Pt(13)},
            {"text": "➤ Sarvam AI: Sovereign Indic language AI — ASR, TTS, Translation for 22 Indian languages. https://www.sarvam.ai/", "size": Pt(13)},
            {"text": "➤ UNESCO (2021): Digital Heritage Preservation Initiatives. https://en.unesco.org/themes/information-preservation/digital-heritage", "size": Pt(13)},
            {"text": "➤ JOCCH Report (2018): Survey of AR/VR/MR for Cultural Heritage. https://www.researchgate.net/publication/323975580", "size": Pt(13)},
            {"text": "➤ ScienceDirect: AR for Intangible Heritage (dance, rituals, oral traditions). https://www.sciencedirect.com/science/article/pii/S2577444121000113", "size": Pt(13)},
            {"text": "➤ React Native Architecture: https://reactnative.dev/architecture", "size": Pt(13)},
        ])

    # Comparison heading
    if shape.name == "TextBox 17411":
        write_textbox(shape, [
            {"blank": True},
            {"text": "❖ Comparison with Existing Systems", "size": Pt(20), "bold": True},
        ])

    # Comparison table
    if shape.name == "Table 17412":
        table = shape.table
        # Row 0: Headers
        cells = [
            ("Features", "Our Platform", "Matterport", "Google A&C"),
            ("Crowdsourced 3D (VGGT-Ω)", "✅", "No", "No"),
            ("Hardware Cost", "$0 (smartphone)", "~$4,000", "N/A"),
            ("Indic Language AI (Sarvam)", "✅ (22 langs)", "No", "Cloud"),
            ("Cloud Hosting Fees", "Cloudinary CDN", "$100+/mo", "Free"),
            ("AR/VR Immersive Tours", "✅", "Partial", "No"),
            ("Code-Mixed Speech Support", "✅", "No", "No"),
        ]
        for row_idx, row_data in enumerate(cells):
            for col_idx, cell_text in enumerate(row_data):
                cell = table.cell(row_idx, col_idx)
                # Clear existing text
                tf = cell.text_frame
                while len(tf.paragraphs) > 1:
                    p = tf.paragraphs[-1]._p
                    p.getparent().remove(p)
                tf.paragraphs[0].clear()
                run = tf.paragraphs[0].add_run()
                run.text = cell_text
                run.font.size = Pt(11)
                if row_idx == 0:
                    run.font.bold = True

print("✅ Slide 6: Research & References — DONE")


# ============================================================
# SAVE
# ============================================================
prs.save(OUTPUT_PATH)
print(f"\n🎉 SAVED: {OUTPUT_PATH}")
