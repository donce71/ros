#!/usr/bin/env python

import rospy
import smach
import smach_ros
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from smach import CBState

@smach.cb_interface(input_keys=[], output_keys=[], outcomes=['finished', 'failed'])
def takeoff_cb(user_data):
    rospy.loginfo('Taking Off')
    takeoff_topic = rospy.Publisher('/cmd_vel',  Twist, queue_size=10)
    rospy.sleep(1)
    msg = Twist()
    msg.linear.x = 0.1
    msg.angular.z = 0
    result = takeoff_topic.publish(msg)
    if result == None:
        return 'finished'
    else:
        return 'failed'


@smach.cb_interface(input_keys=[], output_keys=[], outcomes=['finished', 'failed'])
def land_cb(user_data):
    rospy.loginfo('Landing')
    takeoff_topic = rospy.Publisher('/cmd_vel',  Twist, queue_size=10)
    rospy.sleep(5)
    msg = Twist()
    msg.linear.x = 0
    msg.angular.z = 0
    result = takeoff_topic.publish(msg)
    if result == None:
        return 'finished'
    else:
        return 'failed'


def main():
    rospy.init_node('drone_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['outcome'])
    sm.userdata.lspeed = 0.5
    sm.userdata.rspeed = 1.2

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('TAKEOFF', CBState(takeoff_cb),
                               {'finished': 'LAND', 'failed': 'LAND'})
        smach.StateMachine.add('LAND', CBState(land_cb),
                               {'finished': 'outcome', 'failed': 'outcome'})


    # Create and start the introspection server
    sis = smach_ros.IntrospectionServer('drone_server', sm, '/SM_DRONE')
    sis.start()

    # Execute SMACH plan
    outcome = sm.execute()

    sis.stop()

if __name__ == '__main__':
    main()
