# PDF Text Extraction and Cleanup

This repository provides a Python script for extracting text from PDF files using GROBID (GeneRation Of BIbliographic Data). The extracted text is in XML format, which is then cleaned to produce a more readable output.

## Why This Project?

In the digital age, managing large amounts of PDF documents and extracting meaningful text from them is crucial for researchers, students, and anyone dealing with scholarly articles. GROBID is a powerful tool for parsing and extracting information from PDFs, but the resulting XML can be cumbersome. This project aims to streamline the process by providing an easy-to-use interface for extracting and cleaning the text from PDFs.

## Features

- **PDF Text Extraction**: Utilizes GROBID to extract text from PDF files
- **Text Cleanup**: Cleans the extracted text by removing unnecessary references and HTTP links
- **Structured Output**: Returns a clean, readable format of the extracted content

## Requirements

- Python 3.x
- GROBID server running locally

## Setup Instructions

1. **Install GROBID**:
   - Follow the instructions in the [GROBID documentation](https://grobid.readthedocs.io/en/latest/Installation/) to install GROBID on your local machine

2. **Run the GROBID Server**:
   ```bash
   cd /path/to/grobid
   ./gradlew run

- This will start the GROBID server on http://localhost:8070

3. Install Required Python Packages: Make sure you have the required packages installed:
  ```bash
  pip install requests lxml
  ```
## How to Use
- To use the script, simply call the extract_text_from_pdf function with the path to your PDF file

## Example:
  ```python
  from pdf_text_extraction import extract_text_from_pdf

  pdf_path = 'path/to/your/document.pdf'
  cleaned_text = extract_text_from_pdf(pdf_path)
  print(cleaned_text)
  ```
### Function Parameters:
- pdf_path: Path to the PDF file you want to extract text from
### Returns:
- A string containing the cleaned text extracted from the PDF
## Error Handling
- If the specified PDF file does not exist, a FileNotFoundError will be raised
- If GROBID is not running, you will receive an HTTP request error
