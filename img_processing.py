import rospy
from sensor_msgs.msg import Image

# known pump geometry
#  - units are pixels (of half-size image)
PUMP_DIAMETER = 360
PISTON_DIAMETER = 90
PISTON_COUNT = 7

def start_node():
    rospy.init_node('detect_pump')
    rospy.loginfo('detect_pump node started')

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
