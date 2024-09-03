from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    
    launch_description = LaunchDescription()
    
    interface_type = "lab1_interface/srv/SetNoise"
    noise_properties = [
        ('linear', 1.0, 0.1),
        ('angular', 0.0, 3.0)
    ]
    
    for ns, mean, var in noise_properties:
        set_noise = ExecuteProcess(
            cmd=[
                'ros2', 'service', 'call', 
                f'/{ns}/set_noise', interface_type, 
                f'"{{mean: {{data: {mean}}}, variance: {{data: {var}}}}}"'
            ],
            shell=True
        )
        launch_description.add_action(set_noise)
    
    return launch_description
