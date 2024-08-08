cmake_minimum_required(VERSION 3.8)
project(robotic_arm)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(controller_manager REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(gazebo_ros2_control REQUIRED)
find_package(gazebo_ros_pkgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(ros_gz REQUIRED)
find_package(ros_gz_bridge REQUIRED)
find_package(ros_gz_sim REQUIRED)
find_package(ros_gz_image REQUIRED)
find_package(ros2_control REQUIRED)
find_package(ros2_controllers REQUIRED)
find_package(trajectory_msgs REQUIRED)
find_package(xacro REQUIRED)


set(dependencies
  rclcpp
  std_msgs
  trajectory_msgs
  ros2_control
  ros2_controllers
  gazebo_ros2_control
  gazebo_ros_pkgs
)

include_directories(include)

#add_executable(example_joint_trajectory_publisher_cpp src/example_joint_trajectory_publisher.cpp)

#ament_target_dependencies(example_joint_trajectory_publisher_cpp ${dependencies})


install (
  DIRECTORY config 
  launch models scripts src urdf worlds
  DESTINATION share/${PROJECT_NAME}
)

install(
  DIRECTORY include/
  DESTINATION include
)

# Install cpp executables
#install(
 # TARGETS
  #example_joint_trajectory_publisher_cpp
  #DESTINATION lib/${PROJECT_NAME}
#)

# Install Python modules for import
ament_python_install_package(${PROJECT_NAME})

# Install Python executables
#install(PROGRAMS
  #scripts/example_joint_trajectory_publisher.py
  #scripts/test_set_joint_position_publisher.py
  #scripts/test_set_joint_trajectory_publisher.py
  #DESTINATION lib/${PROJECT_NAME}
#)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
