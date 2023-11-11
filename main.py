from docx import Document
from datetime import date
from pandas import read_csv

def fill_doc(template_path, output_path, data):
    doc = Document(template_path)
    for paragraph in doc.paragraphs:
        for key, value in data.items():
            if key in paragraph.text:
                # paragraph.text = paragraph.text.replace(key, value)
                for run in  paragraph.runs:
                    run.text = run.text.replace(key, str(value))

    doc.save(output_path)

def generate_docs(csv_path, template_path):
    df = read_csv(csv_path)
    for idx, row in df.iterrows():
        data = {
            "<sMrMs>": "Mr." if row['gender'].lower()=="male" else "Ms.",
            "<Full Name>": row['full_name'],
            "<s/d of>" : "S/o" if row['gender'].lower()=="male" else "D/o",
            "<pMr./Ms.>": "Mr." if row['parent_gender'].lower()=="male" else "Ms.",
            "<Parent Name>": row['parent_name'],
            "<sHe/She>": "He" if row['gender'].lower()=="male" else "She",
            "<Course Name>": row['course_name'],
            "<Joining Date>": row['joining_date'],
            "<Admission Number>": row['admission_number'],
            "<Academic Year>": row['academic_year'],
            "<Completion Date>": row['completion_year'],
            "<Current Date>": date.today().strftime("%B %d, %Y")
        }
        print(data)
        output_path = f"./Output/{''.join(data['<Full Name>'].split())}_{date.today().strftime('%d%m%y')}.docx"
        fill_doc(template_path, output_path, data)
        print(f"---Document created for {data['<Full Name>']}---")

if __name__ == "__main__":
    csv_path = "./Data/Bonafide_111123.csv"
    template_path = "./Templates/Bonafide.docx"
    generate_docs(csv_path, template_path)