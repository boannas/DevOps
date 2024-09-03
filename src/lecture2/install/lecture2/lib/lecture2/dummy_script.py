#!/usr/bin/python3

from lecture2.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
from turtlesim_plus_interfaces.srv import GivePosition
from std_srvs.srv import Empty
import numpy as np

class DummyNode(Node):
    def __init__(self):
        super().__init__('dummy_node')
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.create_subscription(Point, '/mouse_position', self.mouse_pose_callback, 10)
        self.create_timer(0.01,self.timer_callback)
        self.spawn_pizza_cli = self.create_client(GivePosition, 'spawn_pizza')
        self.eat_pizza_cli = self.create_client(Empty, '/turtle1/eat')
        self.robot_pose = np.array([0.0, 0.0, 0.0])
        self.mouse_pose = np.array([0.0, 0.0])
        
    def cmdvel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = w
        self.cmd_vel_pub.publish(msg)
        
    def pose_callback(self, msg):
        self.robot_pose[0] = msg.x
        self.robot_pose[1] = msg.y
        self.robot_pose[2] = msg.theta
        # print(self.robot_pose)
        
    def mouse_pose_callback(self, msg):
        self.mouse_pose[0] = msg.x
        self.mouse_pose[1] = msg.y
        self.spawn_pizza(self.mouse_pose[0], self.mouse_pose[1])
        print(self.mouse_pose)
        
        
    def spawn_pizza(self, x, y):
        position_request = GivePosition.Request()
        position_request.x = x
        position_request.y = y
        self.spawn_pizza_cli.call_async(position_request)
        
    def eat_pizza(self):
        eat_request = Empty.Request()
        self.eat_pizza_cli.call_async(eat_request)
        
    def timer_callback(self):
        self.cmdvel(0.5,0.5)
        self.eat_pizza()
        
def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
