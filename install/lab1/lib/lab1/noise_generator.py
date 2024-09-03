#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import sys
from lab1_interface.srv import SetNoise
import numpy as np

class Noise_Generator(Node):
    def __init__(self):
        super().__init__('noise_generator')
        # Create publisher for topic /noise
        self.noise_publisher = self.create_publisher(Float64, 'noise', 10)
    
        self.declare_parameter('rate', 5.0)
        self.rate = (self.get_parameter('rate').get_parameter_value().double_value)

        # Addition attribute
        self.mean = 0.0
        self.variance = 1.0
        
        # Create Service server for /set_noise
        self.set_noise_server = self.create_service(SetNoise, 'set_noise', self.set_noise_callback)
        
        # Start timer for publishing /noise
        self.timer = self.create_timer(1/self.rate, self.timer_callback)
        self.get_logger().info(f'Starting {self.get_namespace()} / {self.get_name()} with the default parameter. hz: {self.rate}, mean: {self.mean}, vairiance: {self.variance}')

    def set_noise_callback(self, request:SetNoise.Request , response:SetNoise.Response):
        self.mean = request.mean.data
        self.variance = request.variance.data
        return response
    
    def timer_callback(self):
        msg = Float64()
        msg.data = np.random.normal(self.mean, np.sqrt(self.variance))
        self.noise_publisher.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)
    node = Noise_Generator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
