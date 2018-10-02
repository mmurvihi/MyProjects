import math
import sys

args = sys.argv

def blur():
#The exception tries to open the file and creates a list of the arguments. It assigns 
#a value to reach if the user enters an additional command line argument.
    try:
        if (len(args) < 2):
            print('Usage: python blur.py <image> <OPTIONAL: reach>')

        if (len(args) == 2):
            reach = 4

        else:
            reach = int(args[2])

        filename = args[1]
        infile = open(filename, 'r')
        outfile = open('blur.ppm', 'w')

    except:
        print('Unable to open ' + filename)

#The list pixellist will store a list of the pixels within a neighboring radius. 
#The list pixelslist will store a list of the blurred pixels within a neighboring radius.
#The list rowlist contains a list of each row. The list header contains the first 3 lines of the file.
#The linenum tells which line in the file the interpreter is at. 
    pixellist = []
    pixelslist = []
    rowlist = []
    header = []
    linenum = 1
    col = 0
    row = 0
    width = 0
    height = 0

#This for loop sends the first 3 lines to the outfile as the header, and iterates through the rest as pixels. 
    for line in infile:
        line = line.strip()
        if linenum <= 3:
            header.append(line)
            if linenum == 2:
               width = int(line.split(" ")[0])
               height = int(line.split(" ")[1])

        if linenum == 3:
            fileformat(header, outfile)

        if linenum > 3:
            pixellist.append(int(line))
            if len(pixellist) == 3:
                rowlist.append(pixellist)
                if col == width - 1:
                    pixelslist.append(rowlist)
                    rowlist = []
                    row += 1
                    col = 0
                else:
                    col += 1
                pixellist = []

        linenum += 1

    updatepixels(pixelslist, outfile, reach)
    outfile.close()
    infile.close()

#The function fileformat passes the header and the outfile and formats it as strings.
def fileformat(header, outfile):
    for value in header:
        outfile.write('{:s}\n'.format(str(value)))

#The function groups_of_3 breaks up the list into groups of 3
def groups_of_3(lst):
    lst = [int(elements) for elements in lst]
    groups_of_3 = []

    for index in range(0, len(lst), 3):
        groups_of_3.append(lst[index:index + 3])

    return groups_of_3


#The function neighbor determins which pixels are in the neighboring radius of the currentpixel.
def neighbor(currentpixel, colx, rowy, pixels, reach):
    neighborpixels = []
    xmin = colx - reach
    xmax = colx + reach
    ymin = rowy - reach
    ymax = rowy + reach
    if xmin < 0:
        xmin = 0
    else:
        xmin = xmin

    if xmax > len(pixels[0]):
        xmax = len(pixels[0])

    else:
        xmax = xmax

    if ymin < 0:
        ymin = 0

    else:
        ymin = ymin


    if ymax > len(pixels):
        ymax = len(pixels)

    else:
        ymax = ymax


    for x in range (xmin, xmax):
        for y in range(ymin, ymax):
            if x == colx and y == rowy:
                pass
            else:
                neighborpixels.append(pixels[y][x])

    return neighborpixels


#The function avgofneighbor determines the average red, blue, and green values for the radius of a given pixel. 
def avgofneighbor(currentpixel, colx, rowy, pixels, reach):
    pixelsofneighbors = neighbor(currentpixel, colx, rowy, pixels, reach)
    totalred = 0
    totalgreen = 0
    totalblue = 0
    totalpixels = len(pixelsofneighbors) + 1

    for i in range(len(pixelsofneighbors)):
        totalred += pixelsofneighbors[i][0]
        totalgreen += pixelsofneighbors[i][1]
        totalblue += pixelsofneighbors[i][2]

    totalred += currentpixel[0]
    totalgreen += currentpixel[1]
    totalblue += currentpixel[2]
    totalred += currentpixel[0]
    totalgreen += currentpixel[1]
    totalblue += currentpixel[2]
    redavg = totalred / totalpixels
    greenavg = totalgreen / totalpixels
    blueavg = totalblue / totalpixels
    pixelofavgs = [int(redavg), int(greenavg), int(blueavg)]
    return pixelofavgs

#The function writenewpixels determines how the blurred pixels are written in the outfile.
def writenewpixels(redcom, greencom, bluecom, outfile):
    outfile.write('{:s}\n'.format(str(redcom)))
    outfile.write('{:s}\n'.format(str(greencom)))
    outfile.write('{:s}\n'.format(str(bluecom)))

#The function updatepixels changes the pixel values to the new blurred pixel values.
def updatepixels(pixels, outfile, reach):
    for y in range(len(pixels)):
        for x in range(len(pixels[0])):
            currentpixel = pixels[y][x]
            colx = x
            rowy = y
            newpixel = avgofneighbor(currentpixel, colx, rowy, pixels, reach)
            redcom = newpixel[0]
            greencom = newpixel[1]
            bluecom = newpixel[2]
            writenewpixels(redcom, greencom, bluecom, outfile)

if __name__ == '__main__':
    blur()
