from PIL import Image
import cv2
import pytesseract
from pathlib import Path


class Engine:
    @staticmethod
    def start_engine(path, choice):
        root_path = str(Path(__file__).parent.parent)
        pytesseract.pytesseract.tesseract_cmd = 'E:\\Tmp\\Studia_Materialy\\semestr_10\\Przemysl_4.0\\tesseract\\tesseract.exe'
        img = cv2.imread(root_path + '/media/' + str(path))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        out_fun = Engine.format_output(choice)
        print(out_fun(img))
        cv2.imshow('Result', img)
        cv2.waitKey(0)

    @staticmethod
    def format_output(choice):
        if choice not in {'p', 't'}:
            raise ValueError(f"Zly format wyjsciowy pliku {choice}")
        else:
            if choice == 'p':
                return pytesseract.image_to_pdf_or_hocr
            if choice == 't':
                return pytesseract.image_to_string

