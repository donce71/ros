#!/usr/bin/env python

# Direct robot to move forward via geometry_msgs/Twist messages for some time duration

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class NavTimed():
  def __init__(self):
    rospy.init_node('pirmas_node')
    self.cmdvel_sub = rospy.Subscriber('/mybot/laser/scan', LaserScan, self.LaserCallback)
    self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    self.time_start = rospy.Time.now()
    self.time_to_run = rospy.get_param('~time_to_run',10)
    self.v_target = rospy.get_param('~v_target',0)
    self.w_target = rospy.get_param('~w_target',0)
    self.distance = [None] * 20
    self.state = rospy.get_param('~state','tiesiai')
 
  def LaserCallback(self,msg):
    self.distance = msg.ranges
   # rospy.loginfo('Distance:{}'.format(self.distance[10]))
    rospy.loginfo('state:{}'.format(self.state))


  def update(self):
    #time_duration = (rospy.Time.now() - self.time_start).to_sec()
    #if time_duration > self.time_to_run:
    #  rospy.signal_shutdown('Done nav_forward')
    move_cmd = Twist()
    move_cmd.linear.x = self.v_target
    move_cmd.angular.z = self.w_target
    self.cmd_vel_pub.publish(move_cmd)

  def control(self):
    if (self.distance[10]<1.5) and (self.state=='tiesiai'):
      self.state='posukis'
    elif (self.state=='posukis') and (self.distance[6]>1.8) and (self.distance[10]>1.8):
      self.state='tiesiai'
    elif self.state=='posukis':
      self.v_target=0
      self.w_target=0.1
    elif self.state=='tiesiai':
      self.v_target=0.1
      self.w_target=0

  def spin(self):
    rospy.loginfo("Start nav_forward")
    rate = rospy.Rate(10)
    rospy.on_shutdown(self.shutdown)
    while not rospy.is_shutdown():
      self.control()
      self.update()
      rate.sleep()
    rospy.spin()

  def shutdown(self):
    rospy.loginfo("Stop nav_forward")
    # Stop message
    self.cmd_vel_pub.publish(Twist())
    rospy.sleep(1)

def main():
  nav_timed = NavTimed();
  nav_timed.spin()

if __name__ == '__main__':
  main()