#!/usr/bin/env python

import roslib   #roslib.load_manifest('smach_tutorials')
import rospy
import smach
import smach_ros
import time


# define state Foo
class Foo(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'],
                                    input_keys=['foo_counter_in'],
                                    output_keys=['foo_counter_out'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Executing state FOO')
        if self.counter < 10:
            userdata.foo_counter_out = userdata.foo_counter_in + 1
            self.counter += 1
            time.sleep(5) 
            return 'outcome1'
        else:
            return 'outcome1'


# define state Bar
class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1', 'error'],
                                   input_keys=['bar_counter_in'],
                                   output_keys=['bar_counter_out'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR')
        userdata.bar_counter_out = userdata.bar_counter_in + 1
        time.sleep(1) 
        self.counter += 1
        if self.counter < 10:
            return 'outcome1'
            self.counter = 0
        else: 
            return 'error'

        # define state Bar
class Work(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome3'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Executing state Work')
        if self.counter < 5:
            self.counter += 1
            time.sleep(2) 
            return 'outcome3'
        else:
            return 'outcome3'
     


# main
def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm_top = smach.StateMachine(outcomes=['END1'])  
  
    # Open the container
    with sm_top:
        # Add states to the container
        smach.StateMachine.add('WORK', Work(), 
                               transitions={'outcome3':'CON'})   

        sm_con = smach.Concurrence(outcomes = ['outcome1', 'outcome2','ENDerror'],
                                   default_outcome = 'outcome1',
                                   outcome_map = {'outcome2':{'FOO':'outcome1',
                                                              'BAR':'outcome1'},
                                                   'ENDerror':{'BAR':'error'}})

        sm_con.userdata.sm_sub_counter = 0        
        sm_con.userdata.sm_sub_counter2 = 0                                
                        

        #open sub container
        with sm_con:
            # Add states to the container
            smach.Concurrence.add('FOO', Foo(), 
                                    remapping={'foo_counter_in':'sm_sub_counter',
                                             'foo_counter_out':'sm_sub_counter'})

            smach.Concurrence.add('BAR', Bar(), 
                                remapping={'bar_counter_in':'sm_sub_counter2',
                                           'bar_counter_out':'sm_sub_counter2'})    

        smach.StateMachine.add('CON', sm_con,
                                  transitions={'outcome1':'CON',
                                               'outcome2':'CON',
                                               'ENDerror':'END1'})             

                                   

   # Create and start the introspection server
    sis = smach_ros.IntrospectionServer('server_name', sm_top, '/SM_ROOT')
    sis.start()

    # Execute SMACH plan
    outcome = sm_top.execute()

    # Wait for ctrl-c to stop the application
    #rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

