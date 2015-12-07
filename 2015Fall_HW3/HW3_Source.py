##################################################################
# Homework #3 Skeleton Code
# Student ID : 20150739
# Name : Ji Junseop
##################################################################

from cs1media import * #You cannot import anything else!

def show_img(img_fname):
    #------------------------------------------------------
    # function show_img
    # input: image file name (string)
    # output: none
    #
    # task: (1) open the image
    #       (2) display the image
    #------------------------------------------------------

    # task (1),(2) already implemented for you :)
    img = load_picture(img_fname)
    img.show()

def adj_contrast(img_fname, k):
    #------------------------------------------------------
    # function adj_constrast
    # input: image file name (string)
    # output: none
    #
    # task: (1) open the image
    #       (2) calculates the constrast adjusted pixel value
    #       (3) saves file
    #------------------------------------------------------

    #-----------------------------------------
    # do task (1), (2) from here
    #-----------------------------------------

    if k > 99 or k < -99:
        print "Invalid Factor. Factor should be (-99 ~ 99)"
        return
    ## If factor k is out of lange, print error message.

    img = load_picture(img_fname)
    w, h = img.size()
    ## Get size of the image

    final = create_picture(w, h)
    ## Create new picture 'final', has the same size with img

    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)

            if k < 0:
                c = (100.0 + k) / 100.0

            else:
                c = 100.0 / (100.0 - k)
            ## Calculate c, in case of c's sign

            r = int(128 + c * (r - 128))
            g = int(128 + c * (g - 128))
            b = int(128 + c * (b - 128))
            ## Calculate contrast values of each rgb values

            final.set(x, y, (r, g, b))

    # task (3) already implemented for you :) DO NOT CHANGE THIS LINE!
    final.save_as('iu_adj.jpg')

def lomo(img_fname):
    #--------------------------------------------------------------------
    # function lomo
    # input: image file name (string)
    # output: none
    #
    # task: (1) load original image and vignette image(vignette1.jpg)
    #       (2) add vignette by factor 2
    #       (3) add vignette by factor 3
    #       (4) save file
    #
    #--------------------------------------------------------------------

    #-----------------------------------------
    # do task (1), (2), (3) from here
    #-----------------------------------------

    img = load_picture(img_fname)
    vig = load_picture("vignette1.jpg")

    w, h = img.size()

    final = addVignette(img, vig, w, h, 2)
    final = addVignette(final, vig, w, h, 3)
    ## Call addVignette function twice

    # task (4) already implemented for you :) DO NOT CHANGE THIS LINE!
    final.save_as('final_iu.jpg')

def addVignette(inputPic, vignettePic, w, h, factor):
    #---------------------------------------------------------------------------------
    # function addVignette
    # input: original image (Picture), vignette image (Picture),
    #           width (int), height (int), intensity factor (int)
    # output: new image (Picture)
    #
    # task: (1) create an empty picture
    #       (2) read corresponding pixel pairs from the two pictures
    #       (3) get new pixel color by calling getNewColorValues functions
    #       (4) assign the new pixel to the empty picture
    #
    #---------------------------------------------------------------------------------

    #-----------------------------------------
    # do task (1), (2), (3), (4) from here
    #-----------------------------------------
    newimg = create_picture(w, h)

    for y in range(h):
        for x in range(w):
            img_r, img_g, img_b = inputPic.get(x, y)
            vig_r, vig_g, vig_b = vignettePic.get(x, y)

            new_r, new_g, new_b = getNewColorValues((img_r, img_g, img_b), (vig_r, vig_g, vig_b), factor)
            ## Change pixel value into vignette value

            newimg.set(x, y, (new_r, new_g, new_b))

    return newimg

def getNewColorValues(inputPixel, vignettePixel, factor):
    #---------------------------------------------------------------------------------------
    # function addVignette
    # input: pixel from the original image (tuple), pixel from the vignette image (tuple)
    # output: pixel for the new image (tuple)
    #
    # task: (1) from the two tuples, decompose into R,G,B values for each
    #       (2) calculate the new color by applying the rule,
    #           new value = old value - ( 255 % vignette value ) / 2
    #       (3) return the newly constructed RGB value
    #
    #---------------------------------------------------------------------------------------

    #-----------------------------------------
    # do task (1),(2),(3) from here
    #-----------------------------------------
    img_r, img_g, img_b = inputPixel
    vig_r, vig_g, vig_b = vignettePixel

    new_r = int(img_r - (255 % vig_r) / float(factor))
    new_g = int(img_g - (255 % vig_g) / float(factor))
    new_b = int(img_b - (255 % vig_b) / float(factor))
    ## Calculate the rgb value with vignette filter

    return (new_r, new_g, new_b)


def main():
    #----------------------------------------------------------------------------------------------
    # function main
    # input: none
    # output: none
    # task:
    #
    #       (1) If a user's input is 'q', then quit this program.
    #       (2) If a user's input is 's', then ask the name of the file, call show_img() function
    #       (3) If a user's input is 'l', then ask the name of the file, call lomo() function
    #       (4) If a user's input is 'a', then ask the name of the file, call adj_contrast() function
    #       (5) If the command is unknown, notify the user and ask the user for another input
    #
    #----------------------------------------------------------------------------------------------

    #-----------------------------------------
    # do task (1),(2),(3),(4),(5) from here
    #-----------------------------------------

    quit = False
    while not quit:
        user_input = raw_input("Please Select the Menu\nq) Quit\ns) Show Image\nl) Lomo\na) Adjust Contrast\ninput> ")

        if user_input == 'q':
            quit = True
        elif user_input == 's':
            filename = raw_input("Enter the name of the file: ")
            show_img(filename)
        elif user_input == 'l':
            filename = raw_input("Enter the name of the file: ")
            lomo(filename)
        elif user_input == 'a':
            filename = raw_input("Enter the name of the file: ")
            k = int(raw_input("Enter the integer: "))
            adj_contrast(filename, k)
        else:
            print "Unknown Command. Try another input"


main()
