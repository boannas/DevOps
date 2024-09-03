# generated from rosidl_generator_py/resource/_idl.py.em
# with input from controller_interfaces:srv/SetParam.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SetParam_Request(type):
    """Metaclass of message 'SetParam_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('controller_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'controller_interfaces.srv.SetParam_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_param__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_param__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_param__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_param__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_param__request

            from std_msgs.msg import Float64
            if Float64.__class__._TYPE_SUPPORT is None:
                Float64.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetParam_Request(metaclass=Metaclass_SetParam_Request):
    """Message class 'SetParam_Request'."""

    __slots__ = [
        '_kp_linear',
        '_kp_angular',
    ]

    _fields_and_field_types = {
        'kp_linear': 'std_msgs/Float64',
        'kp_angular': 'std_msgs/Float64',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float64'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float64'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Float64
        self.kp_linear = kwargs.get('kp_linear', Float64())
        from std_msgs.msg import Float64
        self.kp_angular = kwargs.get('kp_angular', Float64())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.kp_linear != other.kp_linear:
            return False
        if self.kp_angular != other.kp_angular:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def kp_linear(self):
        """Message field 'kp_linear'."""
        return self._kp_linear

    @kp_linear.setter
    def kp_linear(self, value):
        if __debug__:
            from std_msgs.msg import Float64
            assert \
                isinstance(value, Float64), \
                "The 'kp_linear' field must be a sub message of type 'Float64'"
        self._kp_linear = value

    @builtins.property
    def kp_angular(self):
        """Message field 'kp_angular'."""
        return self._kp_angular

    @kp_angular.setter
    def kp_angular(self, value):
        if __debug__:
            from std_msgs.msg import Float64
            assert \
                isinstance(value, Float64), \
                "The 'kp_angular' field must be a sub message of type 'Float64'"
        self._kp_angular = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_SetParam_Response(type):
    """Metaclass of message 'SetParam_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('controller_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'controller_interfaces.srv.SetParam_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_param__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_param__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_param__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_param__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_param__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetParam_Response(metaclass=Metaclass_SetParam_Response):
    """Message class 'SetParam_Response'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


class Metaclass_SetParam(type):
    """Metaclass of service 'SetParam'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('controller_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'controller_interfaces.srv.SetParam')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__set_param

            from controller_interfaces.srv import _set_param
            if _set_param.Metaclass_SetParam_Request._TYPE_SUPPORT is None:
                _set_param.Metaclass_SetParam_Request.__import_type_support__()
            if _set_param.Metaclass_SetParam_Response._TYPE_SUPPORT is None:
                _set_param.Metaclass_SetParam_Response.__import_type_support__()


class SetParam(metaclass=Metaclass_SetParam):
    from controller_interfaces.srv._set_param import SetParam_Request as Request
    from controller_interfaces.srv._set_param import SetParam_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
