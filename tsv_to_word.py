from docx import Document
import csv

def tsv_to_word(tsv_path, docx_path):
    doc = Document()
    with open(tsv_path, newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        rows = list(reader)
    if not rows:
        return
    table = doc.add_table(rows=1, cols=len(rows[0]))
    hdr_cells = table.rows[0].cells
    # No header in data, so use generic headers
    headers = ["First Name", "Last Name", "ID", "Credit Card", "Date"]
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
    for row in rows:
        row_cells = table.add_row().cells
        for i, val in enumerate(row):
            row_cells[i].text = val
    doc.save(docx_path)

if __name__ == "__main__":
    tsv_to_word("data.tsv", "data.docx")
    print("Word document created: data.docx")
