#!/usr/bin/env python

import roslib  # roslib.load_manifest('smach_tutorials')
import rospy
import smach
import smach_ros
import time

# define state Foo
class Foo(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'],
                                    input_keys=['foo_in'],
                                    output_keys=['foo_out'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Executing state FOO')
        time.sleep(2) 
        if self.counter < 5:
            self.counter += 1
            userdata.foo_out=userdata.foo_in+1
            return 'outcome2'
        else:
            return 'outcome1'


# define state Bar
class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'],
                                     input_keys=['bar_in'],
                                    output_keys=['bar_out'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR')
        userdata.bar_out=userdata.bar_in+1
        time.sleep(2) 
        return 'outcome1'
        


# define state Bas
class Bas(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome3'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAS')
        time.sleep(2) 
        return 'outcome3'




def main():
    rospy.init_node('smach_example_state_machine')

    # Create the top level SMACH state machine
    sm_top = smach.StateMachine(outcomes=['outcome6'])
    
    # Open the container
    with sm_top:

        smach.StateMachine.add('BAS', Bas(),
                               transitions={'outcome3':'CON'})

        # Create the sub SMACH state machine
        sm_con = smach.Concurrence(outcomes=['outcome4','outcome5','END_error'],
                                   default_outcome='outcome4',
                                   outcome_map={'outcome5':{ 'FOO':'outcome2',
                                                             'BAR':'outcome1'},
                                               'END_error':{'FOO':'outcome1'}})

        sm_con.userdata.sm_con_counter=0;   
        sm_con.userdata.bar_counter=0;                 
              
        # Open the container
        with sm_con:
            # Add states to the container
            smach.Concurrence.add('FOO', Foo(),
                                 remapping={'foo_in':'sm_con_counter',
                                          'foo_out':'sm_con_counter'})   

            smach.Concurrence.add('BAR', Bar(),
                            remapping={'bar_in':'bar_counter',
                                      'bar_out':'bar_counter'})

        smach.StateMachine.add('CON', sm_con,
                               transitions={'outcome4':'CON',
                                            'outcome5':'CON',
                                            'END_error':'outcome6'})

    # Create and start the introspection server
    sis = smach_ros.IntrospectionServer('server_name', sm_top, '/SM_ROOT')
    sis.start()

    # Execute SMACH plan
    outcome = sm_top.execute()

    sis.stop()

if __name__ == '__main__':
    main()