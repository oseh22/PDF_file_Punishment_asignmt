from reportlab.pdfgen import canvas
import subprocess

# Get user input for text, filename, and path
# Set the background color
title = input("Enter file title: ")
text = input("Enter the text to convert to PDF: ")
filename = input("Enter the filename for the PDF (without extension): ")
path = input("Enter the path to save the PDF file: ")

# If path is not specified, use current directory
if not path:
    path = "."

# Add the .pdf extension to the filename
filename = filename + ".pdf"

# Create a new PDF file
pdf = canvas.Canvas(f"{path}/{filename}")

# Set the font and font size
pdf.setFont("Helvetica", 19)

# Set the title font and background color
pdf.setFillColorRGB(1, 0, 0)  # red background color


# Draw the title
pdf.drawString(50, 800, title)
pdf.setFont("Helvetica", 12)
# Set the default font color and background color
pdf.setFillColorRGB(0, 1, 0),  # green font color


# Split the text into lines and add to PDF
lines = text.split("\n")
y = 750  # Start at top of page
for line in lines:
    pdf.drawString(50, y, line)
    y -= 20  # Move down to next line

# Save the PDF file
pdf.save()

# Open the PDF file with the default PDF viewer
subprocess.Popen([filename], shell=True, cwd=path)

print(f"PDF file saved as {path}/{filename}")
