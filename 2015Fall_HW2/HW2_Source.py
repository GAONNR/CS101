##########################################################################
# Title : Photoshop of Minimalism
# Author : Ji Junseop
# The number of hours taken for finishing the homework : 6
##########################################################################
from cs1graphics_HW2 import *
import math

# Global variables
canvas = None # canvas
depth = 599
photo_depth = 600

# test mode flag. When you submit, set this False.
test_mode = False

def gray_scale(img): # DO NOT MODIFY THE DEFINITION LINE
    # Parameters:
    #     img: original image
    #
    # Return value: None
    #
    # Modify 'img' to make it gray scale image.
    # Use colors whose R, G, and B values are same.
    # Use luminance value. Refer to Photo processing lecture notes page 2.
    #
    # Note that you must commit before return.

    ### Implement here ###
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            R, G, B = img.get(x, y)
            avg = int(0.299 * R + 0.587 * G + 0.114 * B)
            #take luminance value of the RGBs to make grayscale
            img.set(x, y, (avg, avg, avg))

    img.commit()

def make_lighter(img, factor_percent): # DO NOT MODIFY THE DEFINITION LINE
    # Parameters:
    #     img: original image
    #     factor_percent: the percentage of how much light intensity will be increased
    #
    # Return value: None
    #
    # Modify 'img' to make it lighter.
    # Careful with 'factor_percent'. If factor_percent = 20, it means 20% of
    # light intensity should be increased. That is, if R value is 150 and
    # factor_percent = 20, R value will be set as 180.
    #
    # Refer to Photo processing lecture notes page 2.
    # Note that you must commit before return.

    ### Implement here ###

    w, h = img.size()
    for y in range(h):
        for x in range(w):
            R, G, B = img.get(x, y)
            R = (1 + factor_percent / 100.0) * R
            G = (1 + factor_percent / 100.0) * G
            B = (1 + factor_percent / 100.0) * B
            #change RGB more brighter
            R = int(R)
            G = int(G)
            B = int(B)
            img.set(x, y, (R, G, B))

    img.commit()

def blur(img, radius): # DO NOT MODIFY THIS FUNCTION
    # Parameters:
    #     img: original image
    #     radius:
    #
    # Return value: new image object which is a blurred version of the original image
    #
    # Reference: Photo processing lecture notes page 3.

    w, h = img.size()
    new_img = Image(w, h)
    new_img.move(w/2, h/2)
    norm = (2 * radius + 1)**2
    for y in range(radius, h - radius):
        for x in range(radius, w - radius):
            r, g, b = 0, 0, 0
            for x0 in range(-radius, radius+1):
                for y0 in range(-radius, radius+1):
                    r0, g0, b0 = img.get(x + x0, y + x0)
                    r, g, b = r+r0, g+g0, b+b0
            r, g, b = r/norm, g/norm, b/norm
            new_img.set(x, y, (r, g, b))
    new_img.commit()

    return new_img

def put_smile_mark(x_pos, y_pos, size): # DO NOT MODIFY THE DEFINITION LINE
    global canvas, depth

    # Parameters:
    #     x_pos: x-axis position of the mark. (center)
    #     y_pos: y-axis position of the mark. (center)
    #     size: size of the mark
    #
    # Return value: None
    #
    # Draw a star mark on the canvas.
    # Careful with size and depth

    # Guide box
    if test_mode:
        guide_box = Rectangle(size, size, Point(x_pos, y_pos))
        guide_box.setBorderColor('black')
        guide_box.setBorderWidth(3)
        guide_box.setDepth(depth)
        depth = depth - 1
        canvas.add(guide_box)

    ### Implement here ###
    smile_mark = Layer()

    face = Circle(size/2, Point(x_pos, y_pos))
    face.setBorderColor('black')
    face.setBorderWidth(3)
    face.setFillColor('yellow')
    face.setDepth(depth)
    smile_mark.add(face) #make face

    left_eye = Circle(size/8, Point(x_pos - size / 4, y_pos - size / 8))
    left_eye.setBorderColor((52, 73, 94))
    left_eye.setFillColor((52, 73, 94))
    left_eye.setDepth(depth - 1)
    smile_mark.add(left_eye) #make left eye

    right_eye = Circle(size/8, Point(x_pos + size / 4, y_pos - size / 8))
    right_eye.setBorderColor((52, 73, 94))
    right_eye.setFillColor((52, 73, 94))
    right_eye.setDepth(depth - 1)
    smile_mark.add(right_eye) #make right eye

    mouth = Spline(Point(x_pos - size / 4, y_pos + size / 8), Point(x_pos, y_pos + size / 4), Point(x_pos + size / 4, y_pos + size / 8))
    mouth.setBorderColor((231, 76, 60))
    mouth.setBorderWidth(3)
    mouth.setDepth(depth - 1)
    smile_mark.add(mouth) #make mouth

    smile_mark.setDepth(depth)
    depth = depth - 1 # decreases depth to make the mark in the future will be placed in front of the current mark
    canvas.add(smile_mark)

def put_star_mark(x_pos, y_pos, size): # DO NOT MODIFY THE DEFINITION LINE
    global canvas, depth

    # Parameters:
    #     x_pos: x-axis position of the mark. (center)
    #     y_pos: y-axis position of the mark. (center)
    #     size: size of the mark
    #
    # Return value: None
    #
    # Draw a star mark on the canvas.
    # Careful with size and depth

    # Guide box
    if test_mode:
        guide_box = Rectangle(size, size, Point(x_pos, y_pos))
        guide_box.setBorderColor('black')
        guide_box.setBorderWidth(3)
        guide_box.setDepth(depth)
        depth = depth - 1
        canvas.add(guide_box)

    ### Implement here ###
    pi = math.pi
    theta = 2 * pi / 10 #degree 36
    sin = math.sin
    cos = math.cos
    rad = size / 4 # the basic radius of the star

    star_mark = Layer()

    for i in range(5): # star has 5 directions, so we make one direction and copy the rotations five times
        inner_point_one = Point(x_pos + rad * sin((2 * i - 1) * theta), y_pos - rad * cos((2 * i - 1) * theta))
        inner_point_two = Point(x_pos + rad * sin((2 * i + 1) * theta), y_pos - rad * cos((2 * i + 1) * theta))
        outer_point = Point(x_pos + 2 * rad * sin(2 * i * theta), y_pos - 2 * rad * cos(2 * i * theta))
        # divide a star into 10 same small triangles, and take a coordinates of each point

        star_tmp_one = Polygon(Point(x_pos, y_pos), inner_point_one, outer_point)
        star_tmp_two = Polygon(Point(x_pos, y_pos), inner_point_two, outer_point)

        star_tmp_one.setBorderColor((255, 245, 22))
        star_tmp_two.setBorderColor((255, 245, 22))
        star_tmp_one.setFillColor((255, 245, 22))
        star_tmp_two.setFillColor((255, 245, 22))
        #paint these yellow

        star_mark.add(star_tmp_one)
        star_mark.add(star_tmp_two)

    star_mark.setDepth(depth)
    depth = depth - 1
    canvas.add(star_mark)

def put_my_mark(x_pos, y_pos, size): # DO NOT MODIFY THE DEFINITION LINE
    global canvas, depth
    # Parameters:
    #     x_pos: x-axis position of the mark. (center)
    #     y_pos: y-axis position of the mark. (center)
    #     size: size of the mark
    #
    # Return value: None
    #
    # Draw a mark on the canvas.
    # Careful with size and depth

    # Guide box
    if test_mode:
        guide_box = Rectangle(size, size, Point(x_pos, y_pos))
        guide_box.setBorderColor('black')
        guide_box.setBorderWidth(3)
        guide_box.setDepth(depth)
        depth = depth - 1
        canvas.add(guide_box)

    ### Implement here ###

    my_mark = Layer()
    #my mark will be the shape of the bear face

    gom_face = Circle(size / 2, Point(x_pos, y_pos))
    gom_face.setBorderColor((115, 74, 65))
    gom_face.setFillColor((115, 74, 65))
    gom_face.setDepth(depth - 2)
    my_mark.add(gom_face)
    #make face

    gom_ear_out_left = Circle(size / 6, Point(x_pos - size / 3, y_pos - size / 3))
    gom_ear_out_left.setBorderColor((115, 74, 65))
    gom_ear_out_left.setFillColor((115, 74, 65))
    gom_ear_out_left.setDepth(depth)
    my_mark.add(gom_ear_out_left)
    #make outer ears

    gom_ear_out_right = Circle(size / 6, Point(x_pos + size / 3, y_pos - size / 3))
    gom_ear_out_right.setBorderColor((115, 74, 65))
    gom_ear_out_right.setFillColor((115, 74, 65))
    gom_ear_out_right.setDepth(depth)
    my_mark.add(gom_ear_out_right)

    gom_ear_in_left = Circle(size / 8, Point(x_pos - size / 3, y_pos - size / 3))
    gom_ear_in_left.setBorderColor((82, 51, 43))
    gom_ear_in_left.setFillColor((82, 51, 43))
    gom_ear_in_left.setDepth(depth - 1)
    my_mark.add(gom_ear_in_left)
    #make inner ears

    gom_ear_in_right = Circle(size / 8, Point(x_pos + size / 3, y_pos - size / 3))
    gom_ear_in_right.setBorderColor((82, 51, 43))
    gom_ear_in_right.setFillColor((82, 51, 43))
    gom_ear_in_right.setDepth(depth - 1)
    my_mark.add(gom_ear_in_right)

    gom_eye_left = Circle(size / 24, Point(x_pos - size / 9, y_pos - size / 12))
    gom_eye_left.setBorderColor((0, 0, 0))
    gom_eye_left.setFillColor((0, 0, 0))
    gom_eye_left.setDepth(depth - 3)
    my_mark.add(gom_eye_left)
    #make eyes

    gom_eye_right = Circle(size / 24, Point(x_pos + size / 9, y_pos - size / 12))
    gom_eye_right.setBorderColor((0, 0, 0))
    gom_eye_right.setFillColor((0, 0, 0))
    gom_eye_right.setDepth(depth - 3)
    my_mark.add(gom_eye_right)

    gom_nose_around = Circle(size / 6, Point(x_pos, y_pos + size / 6))
    gom_nose_around.setBorderColor((238, 206, 197))
    gom_nose_around.setFillColor((238, 206, 197))
    gom_nose_around.setDepth(depth - 3)
    my_mark.add(gom_nose_around)
    #make the thing around the nose and mouth

    gom_nose = Polygon(Point(x_pos, y_pos + size / 12), Point(x_pos - size / 18, y_pos + size / 48), Point(x_pos + size / 18, y_pos + size / 48))
    gom_nose.setBorderColor((0, 0, 0))
    gom_nose.setFillColor((0, 0, 0))
    gom_nose.setDepth(depth - 4)
    my_mark.add(gom_nose)
    #make nose

    gom_mouth = Path(Point(x_pos, y_pos + size / 12), Point(x_pos, y_pos + size / 8), Point(x_pos - size / 18, y_pos + size / 6), Point(x_pos, y_pos + size / 8), Point(x_pos + size / 18, y_pos + size / 6))
    gom_mouth.setBorderColor((0, 0, 0))
    gom_mouth.setBorderWidth(size / 50)
    gom_mouth.setDepth(depth - 4)
    my_mark.add(gom_mouth)
    #make mouth

    my_mark.setDepth(depth)
    depth = depth - 1
    canvas.add(my_mark)

def put_text(text, x_pos, y_pos, size, color): # DO NOT MODIFY THIS FUNCTION
    global canvas, depth
    # Parameters:
    #     text: a text message to draw in the canvas
    #     x_pos: x-axis position of the text. (center)
    #     y_pos: y-axis position of the text. (center)
    #     size: font size of the text
    #     color: font color of the text
    #
    # Return value: None
    #
    # Draw text on the canvas.

    if color == '':
        color = 'white'
    text = Text(text, size, Point(x_pos, y_pos))
    text.setFontColor(color)
    text.setDepth(depth)
    depth = depth - 1
    canvas.add(text)

def range_input(prompt, low, high): # DO NOT MODIFY THE DEFINITION LINE
    # Parameters:
    #     prompt: a text message to show in the shell
    #     low: the lowest acceptable value
    #     high: the highest acceptable value
    #
    # Return value:
    # an integer value of user's input which is greater than or equal to 'low'
    # and less than or equal to 'high'
    #
    # Behavior:
    # Show 'prompt' and ask user's input.
    # If user's input is within 'low' ~ 'high', then return it.
    # If not, ask to user again.

    ### Implement here ###
    check = True
    while check == True:
        in_put = raw_input(prompt + ' (' + str(low) + ' ~ ' + str(high) + ')')
        int_put = int(in_put)
        #print prompt message and range, and take input

        if int_put >= low and int_put <= high:
            check = False
        else:
            print 'Error! Enter a number between ' + str(low) + ' and ' + str(high)
        #check the range of input

    return int_put

def color_input(prompt): # DO NOT MODIFY THIS FUNCTION
    while True:
        answer = raw_input(prompt)
        if answer == '':
            return 'white'
        if checkColorName(answer):
            return answer


def main(): # DO NOT MODIFY THIS FUNCTION
    global canvas

    if test_mode:
        filename = 'Changdae.jpg'
    else:
        filename = raw_input('Enter a photo filename:')

    photo = Image(filename)
    width, height = photo.size()
    photo.setDepth(photo_depth)
    photo.move(width/2, height/2)

    canvas = Canvas(width, height)
    canvas.add(photo)

    if test_mode:
        make_lighter(photo, 20)
        put_smile_mark(310,280,100)
        put_star_mark(150,430,75)
        put_my_mark(580, 100, 100)
        put_text('I love myself', 320, 35, 50, 'white')

    while True:
        print '(1) gray scale'
        print '(2) make lighter'
        print '(3) blur'
        print '(4) Add smile mark'
        print '(5) Add star mark'
        print '(6) Add my mark'
        print '(7) Add text'
        print '(8) Save the decorated selfie'
        print '(9) Quit'

        menu = range_input('Select a menu', 1, 9)

        if menu == 1: # gray scale
            gray_scale(photo)

        elif menu == 2: # make lighter
            factor_percent = range_input('Enter a light intensity percentage to be increased', 1, 100)
            make_lighter(photo, factor_percent)

        elif menu == 3: # blur
            radius = range_input('Enter the amount of blurring', 2, 10)
            new_photo = blur(photo, radius)
            new_photo.setDepth(photo_depth)
            canvas.remove(photo)
            canvas.add(new_photo)
            photo = new_photo

        elif menu == 4: # smile mark
            x_pos = range_input('Enter an x-coordinate', 0, width-1)
            y_pos = range_input('Enter a y-coordinate', 0, height-1)
            size = range_input('Enter a size of smile', 1, min(width, height))
            put_smile_mark(x_pos, y_pos, size)

        elif menu == 5: # star mark
            x_pos = range_input('Enter an x-coordinate', 0, width-1)
            y_pos = range_input('Enter a y-coordinate', 0, height-1)
            size = range_input('Enter a size of star', 1, min(width, height))
            put_star_mark(x_pos, y_pos, size)

        elif menu == 6: # my mark
            x_pos = range_input('Enter an x-coordinate', 0, width-1)
            y_pos = range_input('Enter a y-coordinate', 0, height-1)
            size = range_input('Enter a size of star', 1, min(width, height))
            put_my_mark(x_pos, y_pos, size)

        elif menu == 7: # text
            x_pos = range_input('Enter an x-coordinate', 0, width-1)
            y_pos = range_input('Enter a y-coordinate', 0, height-1)
            size = range_input('Enter a size of text', 1, min(width, height))
            text = raw_input('Enter a text to put on')
            color = color_input('Enter a text color')
            put_text(text, x_pos, y_pos, size, color)

        elif menu == 8: # save
            save_file_name = raw_input('Enter a file name (*.eps or skip the extent)')
            if save_file_name.split('.')[-1] != 'eps':
                save_file_name += '.eps'
            canvas.saveToFile(save_file_name)
            print 'Save to eps file. Open it with Photoshop or Adobe Acrobat.'

        elif menu == 9: # quit
            canvas.close()
            break

        else:
            break # cannot occurr!

if __name__ == '__main__':
    main()
