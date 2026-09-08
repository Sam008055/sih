import comtypes.client
import os

pptx_path = os.path.abspath(r"C:\Users\shree\Desktop\sih\OdishaHeritage-SIH2026-Idea-Presentation.pptx")
pdf_path = os.path.abspath(r"C:\Users\shree\Desktop\sih\OdishaHeritage-SIH2026-Idea-Presentation.pdf")

print(f"Input:  {pptx_path}")
print(f"Output: {pdf_path}")

powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
powerpoint.Visible = 1

presentation = powerpoint.Presentations.Open(pptx_path)
# 32 = ppSaveAsPDF
presentation.SaveAs(pdf_path, 32)
presentation.Close()
powerpoint.Quit()

print(f"✅ PDF saved: {pdf_path}")
