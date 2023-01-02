from PIL import Image  # import the image handling stuff
import math
import random

# Paths to the input and output folder
inputpath = "inputimages/"
outputpath = "outputimages/"

"""Map of the program:
    get info
    convert photo to data
    convert data to ascii points
    convert ascii points to html
"""

# Get input file, text to write, and output file location
inputfilelocation = inputpath + str(
    input("File name to scan: "))
imagetext = str(input("Text to write: "))
outputfilelocation = outputpath + str(
    input("Output file name: "))


# Store image
img = Image.open(inputfilelocation).convert('L')  # Convert the image to black and white
WIDTH, HEIGHT = img.size  # Get the image dimensions
# get requested character dimesions
charwidth = math.floor(WIDTH * float(input("What percent of the photo is 1 character width-wise? ")))
charheight = math.floor(charwidth * 1.89)

# Convert data to a list of ints
data = list(img.getdata())

# Convert that to a 2D array
data = [data[offset:offset + WIDTH] for offset in range(0, WIDTH * HEIGHT, WIDTH)]
newdata = []

average = 0
# Convert that to a smaller set of data by randomly sampling within the area each character covers
for y in range(0, HEIGHT, charheight): # Y
    for x in range(0, WIDTH, charwidth): # X
        for z in range(0, 10): # In the character
            average += data[random.randint(y, min(y + charheight - 1, HEIGHT-1))][random.randint(x, min(x + charwidth - 1, WIDTH-1))]

        average = int(math.floor(average / 10))
        newdata.append(average)
        average = 0

# Convert new data to a 2D array
newdata = [newdata[o:o + int(WIDTH/charwidth) + 1] for o in range(0, int((WIDTH/charwidth) + 1) * int(HEIGHT/charheight), int(WIDTH/charwidth) + 1)]

# Build the HTML file
html = ''
html += '<!DOCTYPE html>\n'
html += '<html lang="en">\n'
html += '<style>* {font-weight: 600;}</style>\n'

currentletter = 0 # keeps track of which part of the word or phrase we are on
pc = 0 # keeps count of the pixels we have scanned

def increaseContrast(number):
    ContrastValue = 1.2
    number -= 128 # Subtract 128
    number *= ContrastValue # Increase range by ContrastValue many times
    number += 128*ContrastValue # Shift the numbers back up a ContrastValue worth of range
    return number

for line in newdata:
    for point in line:
        # Opening tag and opacity set
        html += '<span style="opacity: ' + str(1 - (increaseContrast(point)/255) + .15) + '">'
        # Add the actual letter
        html += str(imagetext[currentletter])
        # Shift the letter selector
        currentletter += 1
        if currentletter == len(imagetext):
            currentletter = 0
        # Closing tag
        html += '</span>'
    # Newline
    html += '<br>'

# Write to the file
print("Writing to the file...")
fhtml = open(outputfilelocation, 'w')
fhtml.write(html)
fhtml.close()
