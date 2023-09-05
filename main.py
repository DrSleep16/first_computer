import pdfplumber

from gtts import gTTS


def get_no_line_break_text(text):
    return text.replace('\n', '')


def get_audio_from_text(text, language):
    audio = gTTS(text=text, lang=language)
    file_name = "pdf_text.mp3"
    audio.save(file_name)


def get_pdf_text(pdf):
    pdf_text = ''.join(page.extract_text() for page in pdf)
    return pdf_text


def main():
    file_path = "text.pdf"
    with pdfplumber.PDF(open(file_path, mode='rb')) as pdf_file:
        pdf_text = get_pdf_text(pdf_file.pages)
    print(pdf_text)
    get_audio_from_text(pdf_text, 'ru')


if __name__ == '__main__':
    main()
