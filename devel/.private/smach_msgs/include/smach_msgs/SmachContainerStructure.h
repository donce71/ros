// Generated by gencpp from file smach_msgs/SmachContainerStructure.msg
// DO NOT EDIT!


#ifndef SMACH_MSGS_MESSAGE_SMACHCONTAINERSTRUCTURE_H
#define SMACH_MSGS_MESSAGE_SMACHCONTAINERSTRUCTURE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace smach_msgs
{
template <class ContainerAllocator>
struct SmachContainerStructure_
{
  typedef SmachContainerStructure_<ContainerAllocator> Type;

  SmachContainerStructure_()
    : header()
    , path()
    , children()
    , internal_outcomes()
    , outcomes_from()
    , outcomes_to()
    , container_outcomes()  {
    }
  SmachContainerStructure_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , path(_alloc)
    , children(_alloc)
    , internal_outcomes(_alloc)
    , outcomes_from(_alloc)
    , outcomes_to(_alloc)
    , container_outcomes(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _path_type;
  _path_type path;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _children_type;
  _children_type children;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _internal_outcomes_type;
  _internal_outcomes_type internal_outcomes;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _outcomes_from_type;
  _outcomes_from_type outcomes_from;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _outcomes_to_type;
  _outcomes_to_type outcomes_to;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _container_outcomes_type;
  _container_outcomes_type container_outcomes;





  typedef boost::shared_ptr< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> const> ConstPtr;

}; // struct SmachContainerStructure_

typedef ::smach_msgs::SmachContainerStructure_<std::allocator<void> > SmachContainerStructure;

typedef boost::shared_ptr< ::smach_msgs::SmachContainerStructure > SmachContainerStructurePtr;
typedef boost::shared_ptr< ::smach_msgs::SmachContainerStructure const> SmachContainerStructureConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::smach_msgs::SmachContainerStructure_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace smach_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'smach_msgs': ['/home/zaibs/mybot_ws2/src/executive_smach/smach_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3d3d1e0d0f99779ee9e58101a5dcf7ea";
  }

  static const char* value(const ::smach_msgs::SmachContainerStructure_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3d3d1e0d0f99779eULL;
  static const uint64_t static_value2 = 0xe9e58101a5dcf7eaULL;
};

template<class ContainerAllocator>
struct DataType< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> >
{
  static const char* value()
  {
    return "smach_msgs/SmachContainerStructure";
  }

  static const char* value(const ::smach_msgs::SmachContainerStructure_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
\n\
# The path to this node in the server\n\
string path\n\
\n\
# The children of this node\n\
string[] children\n\
\n\
# The outcome edges\n\
# Each index across these arrays denote one edge\n\
string[] internal_outcomes\n\
string[] outcomes_from\n\
string[] outcomes_to\n\
\n\
# The potential outcomes from this container\n\
string[] container_outcomes\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::smach_msgs::SmachContainerStructure_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.path);
      stream.next(m.children);
      stream.next(m.internal_outcomes);
      stream.next(m.outcomes_from);
      stream.next(m.outcomes_to);
      stream.next(m.container_outcomes);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SmachContainerStructure_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::smach_msgs::SmachContainerStructure_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::smach_msgs::SmachContainerStructure_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "path: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.path);
    s << indent << "children[]" << std::endl;
    for (size_t i = 0; i < v.children.size(); ++i)
    {
      s << indent << "  children[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.children[i]);
    }
    s << indent << "internal_outcomes[]" << std::endl;
    for (size_t i = 0; i < v.internal_outcomes.size(); ++i)
    {
      s << indent << "  internal_outcomes[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.internal_outcomes[i]);
    }
    s << indent << "outcomes_from[]" << std::endl;
    for (size_t i = 0; i < v.outcomes_from.size(); ++i)
    {
      s << indent << "  outcomes_from[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.outcomes_from[i]);
    }
    s << indent << "outcomes_to[]" << std::endl;
    for (size_t i = 0; i < v.outcomes_to.size(); ++i)
    {
      s << indent << "  outcomes_to[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.outcomes_to[i]);
    }
    s << indent << "container_outcomes[]" << std::endl;
    for (size_t i = 0; i < v.container_outcomes.size(); ++i)
    {
      s << indent << "  container_outcomes[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.container_outcomes[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // SMACH_MSGS_MESSAGE_SMACHCONTAINERSTRUCTURE_H
