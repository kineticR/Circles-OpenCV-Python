# import packages
import numpy as np
import cv2


# initialize canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")


# Loop to draw the circles. This will draw 25 circles.
for x in xrange(0, 25):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size = (3,))
    pt = np.random.randint(0, high = 300, size = (2,))
    thickness = np.random.randint(2, high = 10)
    cv2.circle(canvas, tuple(pt), radius, list(color), -1)
    print("The (x, y) coordinate is: " + str(tuple(pt)) + "\n" +
          "The color is            : " + str(list(color)) + "\n" +
          "The radius is           : " + str(radius) + "\n" +
          "- - - - - - - - - - - - - - - - - - - - - -"
          )
    
    # Show each circle once a random key is pressed
    cv2.imshow("soul", canvas)
    cv2.waitKey(0)