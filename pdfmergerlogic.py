from PyPDF2 import PdfMerger
from pathlib import Path

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    desktop_path = Path.home() / "Desktop"
    base_filename = "Merged_PDF"
    counter = 1
    output_pdf_path = desktop_path / f"{base_filename}.pdf"

    # Ensure a unique filename
    while output_pdf_path.exists():
        output_pdf_path = desktop_path / f"{base_filename}_{counter}.pdf"
        counter += 1

    merger.write(output_pdf_path)
    merger.close()
    print(f"Merged PDF saved as {output_pdf_path}")
