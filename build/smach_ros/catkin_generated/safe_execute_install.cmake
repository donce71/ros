execute_process(COMMAND "/home/zaibs/mybot_ws2/build/smach_ros/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/zaibs/mybot_ws2/build/smach_ros/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
