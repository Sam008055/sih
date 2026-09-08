from pptx import Presentation
from pptx.util import Inches, Pt, Emu

pptx_path = r"C:\Users\shree\Desktop\sih\MonasteryAI-SIH2026-Idea-Presentation-FINAL_v15.pptx"
prs = Presentation(pptx_path)

print(f"Slide width: {prs.slide_width}, height: {prs.slide_height}")
print(f"Number of slides: {len(prs.slides)}")
print("=" * 80)

for i, slide in enumerate(prs.slides):
    print(f"\n{'='*80}")
    print(f"SLIDE {i+1}")
    print(f"Layout: {slide.slide_layout.name}")
    print(f"{'='*80}")
    
    for j, shape in enumerate(slide.shapes):
        print(f"\n  Shape {j}: type={shape.shape_type}, name='{shape.name}'")
        print(f"    Position: left={shape.left}, top={shape.top}, w={shape.width}, h={shape.height}")
        
        if shape.has_text_frame:
            for k, para in enumerate(shape.text_frame.paragraphs):
                text = para.text.strip()
                if text:
                    runs_info = []
                    for run in para.runs:
                        try:
                            color_str = str(run.font.color.rgb) if run.font.color and run.font.color.type is not None and hasattr(run.font.color, 'rgb') else None
                        except:
                            color_str = "scheme_color"
                        font_info = f"[text='{run.text}', bold={run.font.bold}, size={run.font.size}]"
                        runs_info.append(font_info)
                    print(f"    Para {k}: '{text}'")
                    if runs_info:
                        for ri in runs_info:
                            print(f"      Run: {ri}")
        
        if shape.has_table:
            table = shape.table
            print(f"    Table: {len(list(table.rows))} rows x {len(table.columns)} cols")
            for row_idx, row in enumerate(table.rows):
                for col_idx, cell in enumerate(row.cells):
                    cell_text = cell.text.strip()
                    if cell_text:
                        print(f"      [{row_idx},{col_idx}]: {cell_text[:100]}")
        
        if shape.shape_type == 13:  # Picture
            print(f"    Image: {shape.image.content_type}, size={len(shape.image.blob)} bytes")

    # Check for notes
    if slide.has_notes_slide:
        notes_text = slide.notes_slide.notes_text_frame.text.strip()
        if notes_text:
            print(f"\n  NOTES: {notes_text[:200]}")
