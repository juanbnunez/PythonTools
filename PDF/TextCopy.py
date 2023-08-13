import PyPDF2

def extract_text_from_pdf(pdf_path, start_page, end_page, output_txt):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            if start_page > len(pdf_reader.pages) or end_page > len(pdf_reader.pages):
                print("Error: Páginas fuera del rango del PDF.")
                return
            
            text = ""
            for page_num in range(start_page - 1, end_page):  # Indices de página comienzan en 0
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            
            with open(output_txt, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)
            
            print(f"Texto extraído de las páginas {start_page} a {end_page} guardado en {output_txt}.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    pdf_path = input("Ingrese la ruta del archivo PDF: ")
    start_page = int(input("Ingrese el número de página inicial: "))
    end_page = int(input("Ingrese el número de página final: "))
    output_txt = input("Ingrese el nombre del archivo de texto de salida: ")

    extract_text_from_pdf(pdf_path, start_page, end_page, output_txt)
