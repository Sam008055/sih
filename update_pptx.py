"""
Update the generated Odisha Heritage PPTX to cover ALL points from the reference PPT.
Ensures bold formatting on important keywords throughout.
"""
from pptx import Presentation
from pptx.util import Pt

INPUT_PATH = r"C:\Users\shree\Desktop\sih\OdishaHeritage-SIH2026-Idea-Presentation.pptx"
OUTPUT_PATH = r"C:\Users\shree\Desktop\sih\OdishaHeritage-SIH2026-Idea-Presentation.pptx"

prs = Presentation(INPUT_PATH)


def write_textbox(shape, lines, default_size=Pt(16)):
    tf = shape.text_frame
    tf.word_wrap = True
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


# ============================================================
# SLIDE 2: IDEA / APPROACH DETAILS — FULL COVERAGE
# ============================================================
slide2 = prs.slides[1]

for shape in slide2.shapes:

    # ---- LEFT TOP: Problem Statement ----
    if shape.name == "TextBox 15361":
        write_textbox(shape, [
            {"text": "PROBLEM STATEMENT:", "size": Pt(18), "bold": True},
            {"parts": [
                ("Problem: ", True),
                ("Odisha is home to one of India's richest cultural heritages — from the UNESCO World Heritage Site ", False),
                ("Konark Sun Temple", True),
                (" to ", False),
                ("Jagannath Puri", True),
                (", ", False),
                ("Lingaraja Temple", True),
                (", and ", False),
                ("Udayagiri-Khandagiri caves", True),
                (". These monuments face deterioration from ", False),
                ("pollution, climate change", True),
                (", and ", False),
                ("human interference", True),
                (". Tourists lack ", False),
                ("immersive multilingual cultural context", True),
                (".", False),
            ], "size": Pt(14)},
            {"parts": [
                ("Need: ", True),
                ("A ", False),
                ("digitalized platform", True),
                (" for ", False),
                ("cultural preservation and tourism", True),
                (" of Odisha Heritage with ", False),
                ("AR/VR experiences", True),
                (", an ", False),
                ("AI-powered multilingual tour guide", True),
                (" (Sarvam AI), ", False),
                ("crowdsourced 3D scanning", True),
                (" (VGGT-Ω), and ", False),
                ("gamification", True),
                (" to engage visitors.", False),
            ], "size": Pt(14)},
        ])

    # ---- LEFT BOTTOM: Proposed Solution (all 8 points from reference) ----
    if shape.name == "TextBox 15362":
        write_textbox(shape, [
            {"text": "Proposed Solution:", "size": Pt(17), "bold": True},
            {"parts": [
                ("1. The platform provides an immersive experience through ", False),
                ("augmented reality", True),
                (" technologies.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("2. An ", False),
                ("AI-powered AR tour guide", True),
                (" (Sarvam AI) tells the history behind all monuments in the user's ", False),
                ("preferred language", True),
                (".", False),
            ], "size": Pt(13)},
            {"parts": [
                ("3. Users can have ", False),
                ("one-to-one communication", True),
                (" with the AR guide and ", False),
                ("ask questions", True),
                (" — the guide answers in ", False),
                ("22 Indian languages", True),
                (".", False),
            ], "size": Pt(13)},
            {"parts": [
                ("4. ", False),
                ("Virtual Reality", True),
                (" modules with ", False),
                ("animated reconstructions", True),
                (" and ", False),
                ("immersive audio guides", True),
                (" for experiencing heritage in its original form.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("5. Users can step inside monuments virtually and explore a ", False),
                ("360-degree view", True),
                (".", False),
            ], "size": Pt(13)},
            {"parts": [
                ("6. ", False),
                ("AR-based maps", True),
                (" help users find ", False),
                ("travel routes", True),
                (" to monuments and ", False),
                ("nearby attractions", True),
                (".", False),
            ], "size": Pt(13)},
            {"parts": [
                ("7. ", False),
                ("Gamification", True),
                (" — cultural ", False),
                ("treasure hunts", True),
                (", ", False),
                ("quizzes", True),
                (", and ", False),
                ("rewards", True),
                (" for visiting multiple sites, encouraging exploration.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("8. ", False),
                ("Crowdsourced 3D Scanning", True),
                (" — tourists capture smartphone video → ", False),
                ("VGGT-Ω AI", True),
                (" instantly generates ", False),
                ("3D models", True),
                (", turning visitors into ", False),
                ("digital preservationists", True),
                (".", False),
            ], "size": Pt(13)},
        ])

    # ---- RIGHT: How it addresses the problem + Innovation ----
    if shape.name == "TextBox 15363":
        write_textbox(shape, [
            {"text": "How it Addresses the Problem:", "size": Pt(16), "bold": True},
            {"parts": [
                ("1. ", False),
                ("Digitization and Preservation", True),
                (" — Ensures ", False),
                ("long-term preservation", True),
                (" of cultural assets that may otherwise deteriorate due to ", False),
                ("pollution, climate change", True),
                (", or human interference.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("2. ", False),
                ("Inclusivity and Community Involvement", True),
                (" — Accessibility features (", False),
                ("audio guides, subtitles, voice navigation", True),
                (") ensure inclusivity for ", False),
                ("differently-abled users", True),
                (".", False),
            ], "size": Pt(13)},
            {"blank": True},
            {"text": "Innovation and Uniqueness:", "size": Pt(16), "bold": True},
            {"parts": [
                ("1. ", False),
                ("Digital 3D Scanning & AR Models", True),
                (" → Preserve monuments and artifacts virtually via ", False),
                ("VGGT-Ω", True),
                (".", False),
            ], "size": Pt(13)},
            {"parts": [
                ("2. Mobile/Web ", False),
                ("AR App", True),
                (" → Provide immersive tours of heritage sites.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("3. Integration of ", False),
                ("storytelling", True),
                (" and ", False),
                ("history", True),
                (" with immersive AR experiences.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("4. Promotes inclusivity by bridging the ", False),
                ("digital divide", True),
                (" — ", False),
                ("Sarvam AI", True),
                (" supports ", False),
                ("22 Indian languages", True),
                (".", False),
            ], "size": Pt(13)},
            {"parts": [
                ("5. ", False),
                ("Low-bandwidth", True),
                (" optimized — downloadable content for areas with poor connectivity.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("6. ", False),
                ("Gamification", True),
                (" makes exploration ", False),
                ("fun and engaging", True),
                (".", False),
            ], "size": Pt(13)},
            {"parts": [
                ("7. ", False),
                ("AR-based maps", True),
                (" for navigation and discovery.", False),
            ], "size": Pt(13)},
        ])

print("✅ Slide 2: Idea/Approach — ALL POINTS COVERED")


# ============================================================
# SLIDE 3: TECHNICAL APPROACH — Ensure bold on key tech
# ============================================================
slide3 = prs.slides[2]

for shape in slide3.shapes:
    if shape.name == "TextBox 17409":
        write_textbox(shape, [
            {"text": "Core Technologies:", "size": Pt(16), "bold": True},
            {"parts": [
                ("• ", False), ("Unity", True), (" (", False), ("C#", True),
                ("): For developing immersive ", False), ("AR/VR experiences", True),
                (" on mobile and VR headsets.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("• ", False), ("Three.js", True), (" / ", False), ("gsplat.js", True),
                (": Display ", False), ("animated 3D graphics", True),
                (", Gaussian splats, and ", False), ("360-degree views", True),
                (" in browser.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("• ", False), ("React Native", True), (" (Expo): ", False),
                ("Cross-platform", True), (" mobile framework for iOS & Android.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("• ", False), ("NextJS", True), (" + ", False), ("React", True),
                (": ", False), ("Server-side rendering", True),
                (" and static site generation for web frontend.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("• ", False), ("VGGT-Ω", True), (" (Meta AI, CVPR 2026): State-of-the-art ", False),
                ("feed-forward 3D reconstruction", True),
                (". Converts ", False), ("smartphone video → 3D models", True),
                (" — ", False), ("no LiDAR needed", True), (".", False),
            ], "size": Pt(13)},
            {"parts": [
                ("• ", False), ("Sarvam AI Suite", True), (": ", False),
                ("Saaras", True), (" (ASR, ", False), ("22 languages", True),
                ("), ", False), ("Bulbul", True), (" (TTS, ", False),
                ("11 languages", True), ("), ", False), ("Translate", True),
                (" (", False), ("22 languages", True), ("). India's ", False),
                ("sovereign Indic AI", True), (".", False),
            ], "size": Pt(13)},
            {"parts": [
                ("• ", False), ("NodeJS", True), (" backend + ", False),
                ("MongoDB", True), (" (NoSQL) for ", False),
                ("scalable", True), (" data storage.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("• ", False), ("Cloudinary", True),
                (": Media ", False), ("CDN", True),
                (" to optimize and deliver images, videos, and 3D assets globally.", False),
            ], "size": Pt(13)},
        ])

print("✅ Slide 3: Technical Approach — BOLD UPDATED")


# ============================================================
# SLIDE 4: FEASIBILITY & VIABILITY — Bold key terms
# ============================================================
slide4 = prs.slides[3]

for shape in slide4.shapes:
    if shape.name == "TextBox 17416":
        write_textbox(shape, [
            {"text": "Feasibility:", "size": Pt(18), "bold": True},
            {"parts": [
                ("1. ", False), ("Processing Speed", True),
                (" (Fig. 2): Meta ", False), ("VGGT-Ω", True),
                (" is ", False), ("50× faster", True),
                (" than optimization-based methods, processing ", False),
                ("1000+ frames", True), (" on a single GPU.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("2. ", False), ("Sovereign AI", True),
                (" (Fig. 3): ", False), ("Sarvam AI", True),
                (" is optimized for Indian languages with ", False),
                ("code-mixed speech", True),
                (" support — outperforming global models.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("3. ", False), ("Cloud Infrastructure", True),
                (" ensures scalability. ", False),
                ("Cloudinary CDN", True),
                (" + AWS for global delivery of heavy 3D/AR assets.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("4. Collaboration with ", False),
                ("ASI", True), (", ", False),
                ("UNESCO", True), (", and ", False),
                ("Odisha Tourism Board", True),
                (" for content approval and outreach.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("5. ", False), ("Education", True),
                (": Engages students and researchers with ", False),
                ("immersive AR/VR storytelling", True), (".", False),
            ], "size": Pt(13)},
        ])

    if shape.name == "TextBox 17417":
        write_textbox(shape, [
            {"text": "Viability & Solutions:", "size": Pt(18), "bold": True},
            {"parts": [
                ("1. ", False), ("Mobile Optimizations", True),
                (": ", False), ("gsplat.js", True),
                (" compresses 3D models for smooth ", False),
                ("60fps rendering", True), (" on mid-range phones.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("2. Multiple ", False), ("revenue streams", True),
                (": ", False), ("Partnerships, Subscriptions", True),
                (", API licensing for tourism boards.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("3. ", False), ("Large potential user base", True),
                (": Millions of domestic and international tourists.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("4. ", False), ("Scalable", True),
                (": Can expand from Odisha to ", False),
                ("all heritage sites across India", True),
                (" without re-architecture.", False),
            ], "size": Pt(13)},
            {"parts": [
                ("5. Increasing ", False), ("smartphone penetration", True),
                (" and interest in immersive experiences make ", False),
                ("AR adoption practical", True), (".", False),
            ], "size": Pt(13)},
        ])

print("✅ Slide 4: Feasibility & Viability — BOLD UPDATED")


# ============================================================
# SLIDE 5: IMPACT & BENEFITS — Bold key terms
# ============================================================
slide5 = prs.slides[4]

for shape in slide5.shapes:
    if shape.name == "TextBox 17409":
        write_textbox(shape, [
            {"text": "Impact:", "size": Pt(18), "bold": True},
            {"blank": True},
            {"parts": [
                ("• ", False), ("Cultural Awareness", True),
                (" → Increases pride and knowledge about Odisha's ", False),
                ("rich heritage", True), (".", False),
            ], "size": Pt(15)},
            {"parts": [
                ("• ", False), ("Global Reach", True),
                (" → Puts Odisha's heritage on the ", False),
                ("international digital map", True), (".", False),
            ], "size": Pt(15)},
            {"parts": [
                ("• ", False), ("Sustainable Heritage Management", True),
                (" → Ensures ", False), ("long-term preservation", True),
                (" with periodic digital updates.", False),
            ], "size": Pt(15)},
            {"parts": [
                ("• ", False), ("Tourism", True),
                (" → Target ", False), ("10% increase", True),
                (" in tourist engagement.", False),
            ], "size": Pt(15)},
            {"parts": [
                ("• ", False), ("Inclusive Growth", True),
                (" → Benefits not just tourists but also ", False),
                ("schools, rural communities", True),
                (", and ", False), ("researchers", True), (".", False),
            ], "size": Pt(15)},
        ])

    if shape.name == "TextBox 17410":
        write_textbox(shape, [
            {"text": "Benefits:", "size": Pt(18), "bold": True},
            {"blank": True},
            {"parts": [
                ("• ", False), ("Digital Preservation", True),
                (" → Preserve the monuments ", False),
                ("digitally", True), (" for future generations.", False),
            ], "size": Pt(14)},
            {"parts": [
                ("• ", False), ("Enhanced Tourism", True),
                (" → Immersive ", False), ("AR", True),
                (" and ", False), ("VR", True),
                (" attract more visitors and boost revenue.", False),
            ], "size": Pt(14)},
            {"parts": [
                ("• ", False), ("Educational Value", True),
                (" → Interactive learning of history through ", False),
                ("AR and VR", True), (" for students, researchers, and the public.", False),
            ], "size": Pt(14)},
            {"parts": [
                ("• ", False), ("Community Engagement", True),
                (" → Boost Odisha tourism ", False),
                ("across the world", True), (".", False),
            ], "size": Pt(14)},
            {"parts": [
                ("• ", False), ("Economic Growth", True),
                (" → An increase in tourism helps in increasing the ", False),
                ("economic growth of Odisha", True), (".", False),
            ], "size": Pt(14)},
            {"parts": [
                ("• ", False), ("Bridging Digital Divide", True),
                (" → ", False), ("Sarvam AI", True),
                (" enables access in ", False), ("22 Indian languages", True),
                (" for all citizens.", False),
            ], "size": Pt(14)},
        ])

print("✅ Slide 5: Impact & Benefits — BOLD UPDATED")


# ============================================================
# SAVE
# ============================================================
prs.save(OUTPUT_PATH)
print(f"\n🎉 SAVED: {OUTPUT_PATH}")
