#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/zaibs/mybot_ws2/src/executive_smach_visualization/smach_viewer"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/zaibs/mybot_ws2/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/zaibs/mybot_ws2/install/lib/python2.7/dist-packages:/home/zaibs/mybot_ws2/build/smach_viewer/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/zaibs/mybot_ws2/build/smach_viewer" \
    "/usr/bin/python" \
    "/home/zaibs/mybot_ws2/src/executive_smach_visualization/smach_viewer/setup.py" \
    build --build-base "/home/zaibs/mybot_ws2/build/smach_viewer" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/zaibs/mybot_ws2/install" --install-scripts="/home/zaibs/mybot_ws2/install/bin"
