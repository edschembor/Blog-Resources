#For a full OpenCV image templating tutorial, see: 
#http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html#template-matching

import cv2
import numpy as np
import smtplib

#Set up SMTP connection with Gmail servers
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( '<gmail_address>', '<gmail_password>' )

done = cv2.imread("done.jpg")
not_done = cv2.imread("not_done.jpg")

done_tape = done.crop(500, 350, 150, 150)
#Uncomment below to see the crop
#done.show()

tape_colored = done_tape.colorDistance(color.BROWN)
#Uncomment below to see color greyscale change with tape distinct
#done.show()

only_tape = done_tape - tape_colored
#Uncomment below to effect of color subtraction
#done.show()

is_done_color = only_tape.meanColor()

not_done_tape = not_done.crop(500, 350, 150, 150)
not_done_color_extracted = not_done_tape.colorDistance(color.BROWN)
only_tape = done_tape - tape_colored
is_not_done_color = only_tape.meanColor()

#Empirical check of the color values for each image
#print(is_done_color)
#print(is_not_done_color)

#Checks if the tape is in the done position or not
#Values chosen empirically from above prints
if (R > 10) and (B > 10):
	server.sendmail( 'Laundry Machine', '9084612091@vtext.com', 'Your laundry is finished drying.' )
else:
	print("The laundry is NOT done")