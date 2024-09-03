#!/usr/bin/python3

from lecture2.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, Point, TransformStamped, PoseStamped
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
from turtlesim_plus_interfaces.srv import GivePosition
from turtlesim_plus_interfaces.msg._scanner_data_array import ScannerDataArray
from std_srvs.srv import Empty
import numpy as np
from tf_transformations import quaternion_from_euler
from math import sqrt, atan, atan2, cos, sin

class Crazy_turtle(Node):
    def __init__(self):
        super().__init__('crazy_turtle_node') 
        # Publisher 
        # self.odom_publisher = self.create_publisher(Odometry, '/odom', 10)   
        # self.tf_broadcaster = TransformBroadcaster(self)               
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        
        # Subscribtion
        self.create_subscription(Pose, '/turtle2/pose', self.pose_callback, 10)
        self.create_subscription(ScannerDataArray , '/turtle2/scan', self.scanner, 10)
        self.create_subscription(Pose , '/crazy_pizza', self.crazy_pizza, 10)
        
        # Variables
        self.create_timer(0.01,self.timer_callback)
        self.spawn_pizza_cli = self.create_client(GivePosition, 'spawn_pizza')
        self.eat_pizza_cli = self.create_client(Empty, '/turtle2/eat')
        self.robot_pose = np.array([0.0, 0.0, 0.0])
        self.pizza_pose = np.array([0.0,0.0])

        self.spawn_turtle2_cli = self.create_client(Spawn, 'spawn_turtle')
        self.spawn_turtle()

    def crazy_pizza(self, msg):
        self.pizza_pose = [msg.x, msg.y]
        self.spawn_pizza(msg.x,msg.y)
        
    def spawn_turtle(self):
        spawn_request = Spawn.Request()
        spawn_request.x = 5.0
        spawn_request.y = 5.0
        spawn_request.theta = 0.0
        spawn_request.name = 'turtle2'
        print(spawn_request)
        self.spawn_turtle2_cli.call_async(spawn_request)
    
    def cmdvel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = w
        self.cmd_vel_pub.publish(msg)
        
    def spawn_pizza(self, x, y):
        if x >= 0 and x < 10 and y >= 0 and y < 10:
            timeStamp = self.get_clock().now().to_msg().sec
            position_request = GivePosition.Request()
            position_request.x = x
            position_request.y = y
            self.spawn_pizza_cli.call_async(position_request)
        
    def eat_pizza(self):
        eat_request = Empty.Request()
        self.eat_pizza_cli.call_async(eat_request)

    def scanner(self, msg):
        detect = msg.data[0]
        
    def pose_callback(self, msg):
        self.robot_pose[0] = msg.x
        self.robot_pose[1] = msg.y
        self.robot_pose[2] = msg.theta
        
        # odom_msg = Odometry()
        # odom_msg.header.stamp = self.get_clock().now().to_msg()
        # odom_msg.header.frame_id = "odom"
        # odom_msg.child_frame_id = "robot2"
        
        # odom_msg.pose.pose.position.x = self.robot_pose[0]
        # odom_msg.pose.pose.position.y = self.robot_pose[1]
        
        # q = quaternion_from_euler(0,0,self.robot_pose[2])
        # odom_msg.pose.pose.orientation.x = q[0]
        # odom_msg.pose.pose.orientation.y = q[1]
        # odom_msg.pose.pose.orientation.z = q[2]
        # odom_msg.pose.pose.orientation.w = q[3]
        
        # self.odom_publisher.publish(odom_msg)
        
        
        # t = TransformStamped()
        # t.header.stamp = self.get_clock().now().to_msg()
        # t.header.frame_id = 'odom'
        # t.child_frame_id = 'robot2'
        
        # t.transform.translation.x = self.robot_pose[0]
        # t.transform.translation.y = self.robot_pose[1]
        # t.transform.rotation.x = q[0]
        # t.transform.rotation.y = q[1]
        # t.transform.rotation.z = q[2]
        # t.transform.rotation.w = q[3]
        
        # self.tf_broadcaster.sendTransform(t)

    def timer_callback(self):
        self.eat_pizza()
        diff_x = self.pizza_pose[0] - self.robot_pose[0]
        diff_y = self.pizza_pose[1] - self.robot_pose[1]
        distance = sqrt(diff_x**2 + diff_y**2)
        omega = atan2(diff_y,diff_x) - self.robot_pose[2]
        angular_velo = atan2(sin(omega),cos(omega))
        self.cmdvel(distance*5, angular_velo*8)
        # print(self.robot_pose)
        
def main(args=None):
    rclpy.init(args=args)
    node = Crazy_turtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
