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
            time.sleep(2) 
            return 'outcome1'
        else:
            return 'outcome2'


# define state Bar
class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'],
                                   input_keys=['bar_counter_in'],
                                   output_keys=['bar_counter_out'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR')
        userdata.bar_counter_out = userdata.bar_counter_in + 1
        time.sleep(1) 
        self.counter += 1
        if self.counter == 2:
            return 'outcome1'
            self.counter = 0
        else: 
            return 'outcome1'

        # define state Bar
class Work(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome3','outcomeERROR'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Executing state Work')
        if self.counter < 5:
            self.counter += 1
            time.sleep(2) 
            return 'outcome3'
        else:
            return 'outcomeERROR'

 # State Bas
class SoneSUB(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome3'])
      
    def execute(self, userdata):
        time.sleep(4) 
        return 'outcome3'
        


# main
def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm_top = smach.StateMachine(outcomes=['outcome5'])
    sm_top.userdata.sm_counter = 0

    # Open the container
    with sm_top:
        # Add states to the container
        smach.StateMachine.add('WORK', Work(), 
                               transitions={'outcome3':'SUB',
                                        'outcomeERROR':'SONE_SUB'})   

        smach.StateMachine.add('SONE_SUB', SoneSUB(), 
                               transitions={'outcome3':'outcome5'})   


        sm_sub=smach.StateMachine(outcomes=['outcome4','outcome7'])
        sm_sub.userdata.sm_sub_counter = 0

        #open sub container
        with sm_sub:
            # Add states to the container
            smach.StateMachine.add('FOO', Foo(), 
                               transitions={'outcome1':'BAR', 
                                            'outcome2':'outcome4'},
                               remapping={'foo_counter_in':'sm_sub_counter',
                                          'foo_counter_out':'sm_sub_counter'})

            smach.StateMachine.add('BAR', Bar(), 
                               transitions={'outcome1':'FOO'},
                                remapping={'bar_counter_in':'sm_sub_counter',
                                           'bar_counter_out':'sm_sub_counter'})    

        smach.StateMachine.add('SUB',sm_sub,
                                transitions={'outcome4':'outcome5',
                                             'outcome7':'WORK'})                
                               

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

