// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from controller_interfaces:srv/SetTarget.idl
// generated code does not contain a copyright notice

#ifndef CONTROLLER_INTERFACES__SRV__DETAIL__SET_TARGET__TRAITS_HPP_
#define CONTROLLER_INTERFACES__SRV__DETAIL__SET_TARGET__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "controller_interfaces/srv/detail/set_target__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'target'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace controller_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetTarget_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: target
  {
    out << "target: ";
    to_flow_style_yaml(msg.target, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetTarget_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: target
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target:\n";
    to_block_style_yaml(msg.target, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetTarget_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace controller_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use controller_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const controller_interfaces::srv::SetTarget_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  controller_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use controller_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const controller_interfaces::srv::SetTarget_Request & msg)
{
  return controller_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<controller_interfaces::srv::SetTarget_Request>()
{
  return "controller_interfaces::srv::SetTarget_Request";
}

template<>
inline const char * name<controller_interfaces::srv::SetTarget_Request>()
{
  return "controller_interfaces/srv/SetTarget_Request";
}

template<>
struct has_fixed_size<controller_interfaces::srv::SetTarget_Request>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Point>::value> {};

template<>
struct has_bounded_size<controller_interfaces::srv::SetTarget_Request>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Point>::value> {};

template<>
struct is_message<controller_interfaces::srv::SetTarget_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace controller_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetTarget_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetTarget_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetTarget_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace controller_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use controller_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const controller_interfaces::srv::SetTarget_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  controller_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use controller_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const controller_interfaces::srv::SetTarget_Response & msg)
{
  return controller_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<controller_interfaces::srv::SetTarget_Response>()
{
  return "controller_interfaces::srv::SetTarget_Response";
}

template<>
inline const char * name<controller_interfaces::srv::SetTarget_Response>()
{
  return "controller_interfaces/srv/SetTarget_Response";
}

template<>
struct has_fixed_size<controller_interfaces::srv::SetTarget_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<controller_interfaces::srv::SetTarget_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<controller_interfaces::srv::SetTarget_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<controller_interfaces::srv::SetTarget>()
{
  return "controller_interfaces::srv::SetTarget";
}

template<>
inline const char * name<controller_interfaces::srv::SetTarget>()
{
  return "controller_interfaces/srv/SetTarget";
}

template<>
struct has_fixed_size<controller_interfaces::srv::SetTarget>
  : std::integral_constant<
    bool,
    has_fixed_size<controller_interfaces::srv::SetTarget_Request>::value &&
    has_fixed_size<controller_interfaces::srv::SetTarget_Response>::value
  >
{
};

template<>
struct has_bounded_size<controller_interfaces::srv::SetTarget>
  : std::integral_constant<
    bool,
    has_bounded_size<controller_interfaces::srv::SetTarget_Request>::value &&
    has_bounded_size<controller_interfaces::srv::SetTarget_Response>::value
  >
{
};

template<>
struct is_service<controller_interfaces::srv::SetTarget>
  : std::true_type
{
};

template<>
struct is_service_request<controller_interfaces::srv::SetTarget_Request>
  : std::true_type
{
};

template<>
struct is_service_response<controller_interfaces::srv::SetTarget_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // CONTROLLER_INTERFACES__SRV__DETAIL__SET_TARGET__TRAITS_HPP_
