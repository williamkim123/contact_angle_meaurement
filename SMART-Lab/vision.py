import cv2
import imutils


class contact_angle:

    def __init__(self, image: str, angle:float):
        self.image = image
        self.angle = angle

    def angle_drawer(self):
        '''
        Drawing the contact angle on the image imported
        '''
        self.img = cv2.imread(self.image)

        # scaling the image to a constant fixed size
        self.width = 600
        self.height = 600
        dimension = (self.width, self.height)
        self.resized_img = cv2.resize(self.img, dimension, interpolation=cv2.INTER_LINEAR)
