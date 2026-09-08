from pptx import Presentation

pptx_path = r"C:\Users\shree\Desktop\sih\OdishaHeritage-SIH2026-Idea-Presentation.pptx"
prs = Presentation(pptx_path)

print(f"Number of slides: {len(prs.slides)}")

for i, slide in enumerate(prs.slides):
    print(f"\n{'='*60}")
    print(f"SLIDE {i+1}")
    print(f"{'='*60}")
    
    for shape in slide.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text.strip()
            if text and len(text) > 5:
                # Truncate long text
                display = text[:200] + "..." if len(text) > 200 else text
                print(f"  [{shape.name}]: {display}")
        
        if shape.has_table:
            table = shape.table
            print(f"  [TABLE - {shape.name}]:")
            for row_idx, row in enumerate(table.rows):
                row_text = " | ".join(cell.text.strip() for cell in row.cells)
                print(f"    Row {row_idx}: {row_text}")
