from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim_plus',
            namespace='',
            executable='turtlesim_plus_node.py',
            name='turtle_sim'
        ),
        Node(
            package='turtle_bringup',
            namespace='',
            executable='controller.py',
            name='controller_turtle'
        ),
        Node(
            package='turtle_bringup',
            namespace='',
            executable='crazy_pizza.py',
            name='crazypizza'
        ),
        Node(
            package='turtle_bringup',
            namespace='',
            executable='crazy_turtle.py',
            name='',

        ),
        # Node(
        #     package='turtlesim',
        #     executable='mimic',
        #     name='mimic',
        #     remappings=[
        #         ('/input/pose', '/turtlesim1/turtle1/pose'),
        #         ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
        #     ]
        # )
    ])