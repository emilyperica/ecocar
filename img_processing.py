import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

# known pump geometry
#  - units are pixels (of half-size image)
PUMP_DIAMETER = 360
PISTON_DIAMETER = 90
PISTON_COUNT = 7

def showImage(img):
    cv2.imshow('image', img)
    cv2.waitKey(1)

def process_image(msg):
    try:
        # convert sensor_msgs/Image to OpenCV Image
        bridge = CvBridge()
        orig = bridge.imgmsg_to_cv2(msg, "bgr8")
    except Excepttion as err:
        print err

def start_node():
    rospy.init_node('detect_pump')
    rospy.loginfo('detect_pump node started')
    
    rospy.Subscriber("image", Image, process_image)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
