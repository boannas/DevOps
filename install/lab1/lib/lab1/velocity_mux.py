#!/usr/bin/python3

from lab1.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import sys

class DummyNode(Node):
    def __init__(self):
        super().__init__('velocity_mux')
        # Create subscriber for topic /linear/noise
        self.linear_vel_subscriber = self.create_subscription(Float64, '/linear/noise', self.linear_vel_sub, 10)
        # Create subscriber for topic /angular/noise
        self.angular_vel_subscriber = self.create_subscription(Float64, '/angular/noise', self.angular_vel_sub, 10)
        # Create publisher for topic /cmd_vel\
        self.cmd_publisher = self.create_publisher(Twist, '/cmd_vel',10)
        
        self.declare_parameter('rate',  5.0)
        self.rate = (self.get_parameter('rate').get_parameter_value().double_value)
        
        # if(len(sys.argv)>=1):
        #     self.rate = floast(sys.argv[1])
        # else:
        #     self.rate = 5.0
        
        # additional attribute 
        self.cmd_vel = Twist()
        # Start timer for publishing 
        self.timer = self.create_timer(1/self.rate, self.timer_callback)
        self.get_logger().info(f'Starting {self.get_name()}, hz: {self.rate}')
        
    def timer_callback(self):
        self.cmd_publisher.publish(self.cmd_vel)
    
    # Callback : set the x-component of linear velocity
    def linear_vel_sub(self, msg):
        self.cmd_vel.linear.x = msg.data
    # Callback : set the z-component of angular velocity
    def angular_vel_sub(self, msg):
        self.cmd_vel.angular.z = msg.data

def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
