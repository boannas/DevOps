#!/usr/bin/python3

from lecture2.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, Point, TransformStamped, PoseStamped
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose
from turtlesim_plus_interfaces.srv import GivePosition
from turtlesim_plus_interfaces.msg._scanner_data_array import ScannerDataArray
from std_srvs.srv import Empty
import numpy as np
from tf_transformations import quaternion_from_euler
from math import sqrt, atan, atan2, cos, sin

class DummyNode(Node):
    def __init__(self):
        super().__init__('dummy_node')
        # Publisher 
        self.odom_publisher = self.create_publisher(Odometry, '/odom', 10)   
        self.tf_broadcaster = TransformBroadcaster(self)               
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Subscribtion
        self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.create_subscription(Point, '/mouse_position', self.mouse_pose_callback, 10)
        self.create_subscription(PoseStamped , '/goal_pose', self.pizza_callback, 10)
        self.create_subscription(ScannerDataArray , '/turtle1/scan', self.scanner, 10)
        
        # Variables
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
        
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = "odom"
        odom_msg.child_frame_id = "robot"
        
        odom_msg.pose.pose.position.x = self.robot_pose[0]
        odom_msg.pose.pose.position.y = self.robot_pose[1]
        
        q = quaternion_from_euler(0,0,self.robot_pose[2])
        odom_msg.pose.pose.orientation.x = q[0]
        odom_msg.pose.pose.orientation.y = q[1]
        odom_msg.pose.pose.orientation.z = q[2]
        odom_msg.pose.pose.orientation.w = q[3]
        
        self.odom_publisher.publish(odom_msg)
        
        
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'robot'
        
        t.transform.translation.x = self.robot_pose[0]
        t.transform.translation.y = self.robot_pose[1]
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        
        self.tf_broadcaster.sendTransform(t)
        # print(odom_msg)
        # print(self.robot_pose)
        
    def mouse_pose_callback(self, msg):
        self.mouse_pose[0] = msg.x
        self.mouse_pose[1] = msg.y
        self.spawn_pizza(self.mouse_pose[0], self.mouse_pose[1])
        # print(self.mouse_pose)
               
    def spawn_pizza(self, x, y):
        if x >= 0 and x < 10 and y >= 0 and y < 10:
            timeStamp = self.get_clock().now().to_msg().sec
            position_request = GivePosition.Request()
            position_request.x = x
            position_request.y = y
            self.spawn_pizza_cli.call_async(position_request)
            print(timeStamp)
        
    def eat_pizza(self):
        eat_request = Empty.Request()
        self.eat_pizza_cli.call_async(eat_request)
        
    def pizza_callback(self, msg):
        pizza_x = msg.pose.position.x
        pizza_y = msg.pose.position.y
        if pizza_x >= 0 and pizza_x <= 10 and pizza_y >= 0 and pizza_y <= 10 :
            self.mouse_pose[0] = msg.pose.position.x
            self.mouse_pose[1] = msg.pose.position.y
            self.spawn_pizza(self.mouse_pose[0], self.mouse_pose[1])

    def scanner(self, msg):
        detect = msg.data[0]
        print(detect.type)              
        # print(msg.data)
        
        
    def timer_callback(self):
        # self.cmdvel(0.5,0.5)
        self.eat_pizza()
        diff_x = self.mouse_pose[0] - self.robot_pose[0]
        diff_y = self.mouse_pose[1] - self.robot_pose[1]
        distance = sqrt(diff_x**2 + diff_y**2)
        omega = atan2(diff_y,diff_x) - self.robot_pose[2]
        angular_velo = atan2(sin(omega),cos(omega))
        # print("robot pose : ", self.robot_pose[2])
        # print("mouse pose : ", self.mouse_pose[1])
        # print("Distance = ",  w )
        self.cmdvel(distance*4, angular_velo*8)


        
def main(args=None):
    rclpy.init(args=args)   
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
