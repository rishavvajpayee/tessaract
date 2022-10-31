import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract' # install tesseract and add the file path here.

def ocr_core(path):
    text = pytesseract.image_to_string(path)

    with open('test/output.txt', 'w',encoding='utf-8') as file:
        file.write(text)

path = 'test/image.jpeg' # path to where you want to save the jpeg

if __name__ == "__main__":
    ocr_core(path)