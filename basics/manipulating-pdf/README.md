# Manipulating PDF

> **Note**  
> This material was created based on the content from the course:  
> [Python Automático: Aprenda a Programar e Automatizar do Zero](https://www.udemy.com/course/python-automatico-aprenda-a-programar-e-automatizar-do-zero/)  
> Specifically from **Section 21**.

This script is focuses on studying **PDF reading and text extraction using Python**.

It covers the fundamental concepts of working with PDF files:

- Open → Load a PDF file using a reader
- Read → Access individual pages from the document
- Extract → Pull plain text content from a page

The goal is to understand how to interact with PDF files programmatically using Python, enabling tasks like text analysis, data extraction, and document processing.

---

## Overview

The script loads a PDF file called `relatorio_de_vendas.pdf` and extracts text from its pages.

It demonstrates how to:

* Initialize a PDF reader
* Access a specific page by index
* Extract text content from a page
* Properly close the reader after use

---

## Technologies Used

* Python
* `pypdf` (PDF reading library)

---

## Structure

* [Reading the PDF](#reading-the-pdf)
* [Page Access](#page-access)
* [Text Extraction](#text-extraction)

---

## Reading the PDF

The script initializes a `PdfReader` instance pointing to the target file:

```python
from pypdf import PdfReader

report = PdfReader("src/pdfs/relatorio_de_vendas.pdf")
```

### Concepts covered:

* Importing and using third-party libraries
* File path handling
* Object instantiation

---

## Page Access

A specific page is accessed by index:

```python
page_1 = report.pages[0]
```

### Concepts covered:

* Indexed access to document pages
* Zero-based indexing

---

## Text Extraction

The text content of the page is extracted and printed:

```python
text = page_1.extract_text()
print(text)
```

### Concepts covered:

* Calling methods on page objects
* Printing extracted string data

---

## Notes

* This script is intended for **learning purposes only**
* The `close()` call is important to avoid file conflicts
* A commented-out loop shows how to iterate over all pages for full document extraction

---

## Purpose

This project is part of my learning journey to:

* Understand how to read and process PDF files with Python
* Learn text extraction techniques for document analysis
* Build a foundation for automation and data extraction workflows

It is not intended for production use, but it follows **practices used in real document processing pipelines**.
