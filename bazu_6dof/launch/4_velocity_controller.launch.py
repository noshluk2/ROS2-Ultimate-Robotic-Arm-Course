from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    urdf_file='/home/luqman/ros2_workspace/src/bazu_6dof/urdf/bazu_gazebo_controller_velocity.urdf'
    return LaunchDescription([
    #   publishes TF for links of the robot without joints
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            arguments=[urdf_file]),
    #  To publish tf for Joints only links
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            ),
#  Gazebo related stuff required to launch the robot in simulation
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='urdf_spawner',
            output='screen',
            arguments=["-topic", "/robot_description", "-entity", "bazu"]),
  
#   Running the controllers in launch file
        ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'start','joint_state_broadcaster'],
        output='screen'
    ),

    ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'start', 'VC'],
        output='screen'
    )
  ])
#   after this simple simulation launcher we need to launch the controllers manually

# - run the commands to load the controller as described in your controller names
#     - ***"ros2 control load_controller forward_position_controller"***
# - Now configure it
#     - ***ros2 control set_controller_state forward_position_controller configure***
# - Start the Controller
#     - ***ros2 control switch_controllers --start forward_position_controller***

# "data:
# - 0.5
# - 0.5
# - 0.5
# - 0.5
# - 0.5
# - 0.5"
