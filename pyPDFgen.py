from random import randint
from random import seed
from fpdf import FPDF
from lorem_text import lorem
import os

# Python program to create
# a pdf file


seed(1)
# save FPDF() class into a
# variable pdf

# print(output_file_count)
redo = True

while redo != False:
    name = input("Enter file name: ")

    numberOfFiles = int(input("Enter number of files to generate: "))
    file_count = 0
    output_exsists = False if(os.path.isdir("output") == False) else True

    if(output_exsists == False):
        os.mkdir("output")

    output_file_count = sum(len(files) for _, _, files in os.walk(r'output/'))
    isEmpty = True if (output_file_count == 0) else False

    # if(isEmpty == False):
    # os.remove("output/*.pdf")

    for x in range(numberOfFiles):
        try:
            tempname = name
            tempname += str(randint(1, 999999))
            pdf = FPDF()

            # Add a page
            pdf.add_page()

            # set style and size of font
            # that you want in the pdf
            pdf.set_font("Arial", size=15)

            # create a cell
            pdf.cell(200, 10, txt="Sample Text",
                     ln=1, align='C')

            # add another cell
            pdf.multi_cell(200, 10, txt=lorem.paragraphs(11))

            # save the pdf with name .pdf
            pdf.output("output/"+tempname+"_CONF"+".pdf")
        except BaseException as e:
            print(str(e))
            print("Error in pdf generation")
        else:
            file_count += 1
            print(str(file_count)+" of "+str(numberOfFiles)+" created")
    choice = input("Create more files? (y/n): ")
    if(choice == "n" or choice == "N"):
        redo = False
