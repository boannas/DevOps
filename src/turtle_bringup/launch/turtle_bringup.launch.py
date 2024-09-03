from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    Launch_description = LaunchDescription()

    turtle_sim_p = Node(
        package='turtlesim_plus',
        namespace='',
        executable='turtlesim_plus_node.py',
        name='turtle_sim'
    )
    Launch_description.add_action(turtle_sim_p)


    controller = Node(
        package='turtle_bringup',
        namespace='',
        executable='controller.py',
        name='controller_turtle',
        parameters=[
            {'frequency':10.0}
        ]
    )
    Launch_description.add_action(controller)

    crazy_piz = Node(
        package='turtle_bringup',
        namespace='',
        executable='crazy_pizza.py',
        name='crazypizza'
    )
    Launch_description.add_action(crazy_piz)

    crazy_tur = Node(
        package='turtle_bringup',
        namespace='',
        executable='crazy_turtle.py',
        name='crazyturtle',
        parameters=[
            {'frequency':10.0}
        ]
    )
    Launch_description.add_action(crazy_tur)

    # Node(
    #     package='turtlesim',
    #     executable='mimic',
    #     name='mimic',
    #     remappings=[
    #         ('/input/pose', '/turtlesim1/turtle1/pose'),
    #         ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
    #     ]
    # )
    return Launch_description