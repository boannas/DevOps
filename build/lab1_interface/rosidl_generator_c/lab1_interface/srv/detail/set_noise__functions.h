// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from lab1_interface:srv/SetNoise.idl
// generated code does not contain a copyright notice

#ifndef LAB1_INTERFACE__SRV__DETAIL__SET_NOISE__FUNCTIONS_H_
#define LAB1_INTERFACE__SRV__DETAIL__SET_NOISE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "lab1_interface/msg/rosidl_generator_c__visibility_control.h"

#include "lab1_interface/srv/detail/set_noise__struct.h"

/// Initialize srv/SetNoise message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * lab1_interface__srv__SetNoise_Request
 * )) before or use
 * lab1_interface__srv__SetNoise_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Request__init(lab1_interface__srv__SetNoise_Request * msg);

/// Finalize srv/SetNoise message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
void
lab1_interface__srv__SetNoise_Request__fini(lab1_interface__srv__SetNoise_Request * msg);

/// Create srv/SetNoise message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * lab1_interface__srv__SetNoise_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
lab1_interface__srv__SetNoise_Request *
lab1_interface__srv__SetNoise_Request__create();

/// Destroy srv/SetNoise message.
/**
 * It calls
 * lab1_interface__srv__SetNoise_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
void
lab1_interface__srv__SetNoise_Request__destroy(lab1_interface__srv__SetNoise_Request * msg);

/// Check for srv/SetNoise message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Request__are_equal(const lab1_interface__srv__SetNoise_Request * lhs, const lab1_interface__srv__SetNoise_Request * rhs);

/// Copy a srv/SetNoise message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Request__copy(
  const lab1_interface__srv__SetNoise_Request * input,
  lab1_interface__srv__SetNoise_Request * output);

/// Initialize array of srv/SetNoise messages.
/**
 * It allocates the memory for the number of elements and calls
 * lab1_interface__srv__SetNoise_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Request__Sequence__init(lab1_interface__srv__SetNoise_Request__Sequence * array, size_t size);

/// Finalize array of srv/SetNoise messages.
/**
 * It calls
 * lab1_interface__srv__SetNoise_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
void
lab1_interface__srv__SetNoise_Request__Sequence__fini(lab1_interface__srv__SetNoise_Request__Sequence * array);

/// Create array of srv/SetNoise messages.
/**
 * It allocates the memory for the array and calls
 * lab1_interface__srv__SetNoise_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
lab1_interface__srv__SetNoise_Request__Sequence *
lab1_interface__srv__SetNoise_Request__Sequence__create(size_t size);

/// Destroy array of srv/SetNoise messages.
/**
 * It calls
 * lab1_interface__srv__SetNoise_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
void
lab1_interface__srv__SetNoise_Request__Sequence__destroy(lab1_interface__srv__SetNoise_Request__Sequence * array);

/// Check for srv/SetNoise message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Request__Sequence__are_equal(const lab1_interface__srv__SetNoise_Request__Sequence * lhs, const lab1_interface__srv__SetNoise_Request__Sequence * rhs);

/// Copy an array of srv/SetNoise messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Request__Sequence__copy(
  const lab1_interface__srv__SetNoise_Request__Sequence * input,
  lab1_interface__srv__SetNoise_Request__Sequence * output);

/// Initialize srv/SetNoise message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * lab1_interface__srv__SetNoise_Response
 * )) before or use
 * lab1_interface__srv__SetNoise_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Response__init(lab1_interface__srv__SetNoise_Response * msg);

/// Finalize srv/SetNoise message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
void
lab1_interface__srv__SetNoise_Response__fini(lab1_interface__srv__SetNoise_Response * msg);

/// Create srv/SetNoise message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * lab1_interface__srv__SetNoise_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
lab1_interface__srv__SetNoise_Response *
lab1_interface__srv__SetNoise_Response__create();

/// Destroy srv/SetNoise message.
/**
 * It calls
 * lab1_interface__srv__SetNoise_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
void
lab1_interface__srv__SetNoise_Response__destroy(lab1_interface__srv__SetNoise_Response * msg);

/// Check for srv/SetNoise message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Response__are_equal(const lab1_interface__srv__SetNoise_Response * lhs, const lab1_interface__srv__SetNoise_Response * rhs);

/// Copy a srv/SetNoise message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Response__copy(
  const lab1_interface__srv__SetNoise_Response * input,
  lab1_interface__srv__SetNoise_Response * output);

/// Initialize array of srv/SetNoise messages.
/**
 * It allocates the memory for the number of elements and calls
 * lab1_interface__srv__SetNoise_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Response__Sequence__init(lab1_interface__srv__SetNoise_Response__Sequence * array, size_t size);

/// Finalize array of srv/SetNoise messages.
/**
 * It calls
 * lab1_interface__srv__SetNoise_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
void
lab1_interface__srv__SetNoise_Response__Sequence__fini(lab1_interface__srv__SetNoise_Response__Sequence * array);

/// Create array of srv/SetNoise messages.
/**
 * It allocates the memory for the array and calls
 * lab1_interface__srv__SetNoise_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
lab1_interface__srv__SetNoise_Response__Sequence *
lab1_interface__srv__SetNoise_Response__Sequence__create(size_t size);

/// Destroy array of srv/SetNoise messages.
/**
 * It calls
 * lab1_interface__srv__SetNoise_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
void
lab1_interface__srv__SetNoise_Response__Sequence__destroy(lab1_interface__srv__SetNoise_Response__Sequence * array);

/// Check for srv/SetNoise message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Response__Sequence__are_equal(const lab1_interface__srv__SetNoise_Response__Sequence * lhs, const lab1_interface__srv__SetNoise_Response__Sequence * rhs);

/// Copy an array of srv/SetNoise messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_lab1_interface
bool
lab1_interface__srv__SetNoise_Response__Sequence__copy(
  const lab1_interface__srv__SetNoise_Response__Sequence * input,
  lab1_interface__srv__SetNoise_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // LAB1_INTERFACE__SRV__DETAIL__SET_NOISE__FUNCTIONS_H_
