# PDF Merger App

## Description

This application allows merging multiple PDF files into a single document.
It uses the tkinter library for the graphical interface and PyPDF2 for PDF file manipulation.

## Features

* Add multiple PDF files to a list.
* Remove files from the list.
* Reorder files in the list (move up/down).
* Merge selected files into a single PDF.

## Requirements

Before running the application, make sure you have installed the following dependencies:

`pip install pillow pypdf2`

Usage

Run the main script:

`python main.py`

## Controls

* Add: Select PDF files to add to the list.
* Remove: Remove the selected file from the list.
* Move Up/Down: Reorder the position of the files in the list.
* Merge PDFs: Merge the selected files into a single PDF.

## Project Structure

PDF_Merger_App/
│-- images/
│   │-- app_icon.ico
│   │-- add.png
│   │-- delete.png
│   │-- up.png
│   │-- down.png
│   │-- pdf_download.png
│-- pdf_merger.py
│-- README.md

## Author

Developed by Agustín Reyes