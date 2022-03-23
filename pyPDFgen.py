from random import randint
from random import seed
from click import echo
from fpdf import FPDF
import lorem
import os

import string
 # Python program to create
# a pdf file


seed(1)
# save FPDF() class into a
# variable pdf

#print(output_file_count)
name = input("Enter file name: ")

numberOfFiles = int(input("Enter number of files: "))
file_count=0
output_file_count = sum(len(files) for _, _, files in os.walk(r'output/'))
isEmpty = True if (output_file_count == 0) else False

#if(isEmpty == False):
   # os.remove("output/*.pdf")

for x in range(numberOfFiles):
    try:
        tempname=name
        tempname += str(randint(1, 999999))
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size=15)

        # create a cell
        pdf.cell(200, 10, txt = "Sample Text",
                ln = 1, align = 'C')

        # add another cell
        pdf.cell(200, 10, txt = lorem.paragraph(),
                ln = 2, align = 'C')

        # save the pdf with name .pdf
        pdf.output("output/"+tempname+".pdf")
    except BaseException as e:
        print(str(e))
        print("Error in pdf generation")
    else:
        file_count+=1
        print(str(file_count)+" of "+str(numberOfFiles)+" created")
