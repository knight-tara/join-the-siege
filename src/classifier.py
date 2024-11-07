import os
from werkzeug.datastructures import FileStorage
from pypdf import PdfReader
from PIL import Image
from pytesseract import pytesseract
import openai
from openai import OpenAI

def classify_file(file: FileStorage):

    """
    1. Convert file to text (pyPDF for PDFs and pytesseract for jpeg and png)
    2. Send text response to OpenAI API
    Note: files only being classified when file type confirmed as valid, hence if statement not handling invalid file types
    """

    filename = file.filename.lower()

    document_text = ""

    if filename[-3:] == 'pdf':
        text = ""
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
        document_text = text

    else: 
        pytesseract.tesseract_cmd=os.getenv('TESSERACT_EXE')
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        document_text = text
    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant"
            },
            {
                "role": "user",
                "content": f"I need to classify text files based on words found within the document. The 4 classifications are: 'drivers_license', 'bank_statement', 'invoice' and 'unknown'. These are the words that you would typically find within each of these documents: 'bank_statement' = account number, account holder, deposit, purchase, bank, statement, 'invoice' = invoice, invoice date, invoice to, send payment to and 'drivers_license' = driver, license, DOB, date of birth, expires. You should use this information to determine which classifcation to use. If there are no word matches or you are sent an empty string, classify the text as 'unknown'. If there is more than one possibility in terms of classification, choose the classification type with the largest number of word matches. The classifications must be returned in the exact format prescribed in the quotation marks (excluding quotation marks) - do not return anything other than the classification. This is the text: {document_text}"
            }
        ]
    )

    return completion.choices[0].message.content


