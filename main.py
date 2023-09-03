import pdfplumber

from io import BytesIO
from gtts import gTTS


def get_no_line_break_text(text):
    return text.replace('\n', '')


def get_audio_from_text(text, language):
    audio = gTTS(text=text, lang=language)
    file_name = "pdf_text.mp3"
    audio.save(file_name)


def main():
    file_path = "text.pdf"
    with open(file_path, mode='rb') as file:
        pdf = BytesIO(file.read())

    with pdfplumber.PDF(pdf) as pdf_file:
        pages_pdf_text = [page.extract_text() for page in pdf_file.pages]
        pdf_text = ' '.join(pages_pdf_text)
        print(pdf_text)

    get_audio_from_text(pdf_text, 'ru')


if __name__ =='__main__':
    main()