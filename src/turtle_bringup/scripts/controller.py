#!/usr/bin/python3

from lecture2.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, Point, TransformStamped, PoseStamped
from nav_msgs.msg import Odometry
# from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose
from turtlesim_plus_interfaces.srv import GivePosition
from turtlesim_plus_interfaces.msg._scanner_data_array import ScannerDataArray
from std_srvs.srv import Empty
import numpy as np
# from tf_transformations import quaternion_from_euler
from math import sqrt, atan, atan2, cos, sin
from controller_interfaces.srv import  SetParam, SetTarget

class DummyNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        
        # Param
        self.declare_parameter('frequency', 10.0)
        self.frequency = (self.get_parameter('frequency').get_parameter_value().double_value)

        # Create Server 
        self.target_server = self.create_service(SetTarget, 'cli', self.set_target_callback)
        self.param_server = self.create_service(SetParam, 'set_param_controller', self.set_param_callback)
        
        # Publisher             
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Subscribtion
        self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.create_subscription(Point, '/mouse_position', self.mouse_pose_callback, 10)
        self.create_subscription(PoseStamped , '/goal_pose', self.pizza_callback, 10)
        self.create_subscription(ScannerDataArray , '/turtle1/scan', self.scanner, 10)
        
        # Variables
        self.timer = self.create_timer(1/self.frequency, self.timer_callback)
        self.spawn_pizza_cli = self.create_client(GivePosition, 'spawn_pizza')
        self.eat_pizza_cli = self.create_client(Empty, '/turtle1/eat')
        self.robot_pose = np.array([0.0, 0.0, 0.0])
        self.mouse_pose = np.array([0.0, 0.0])
        self.k_p = [5.0, 8.0]       # linear , angular
        # "{kp_linear: {data: 5.0}, kp_angular: {data: 8.0}}"


        
    def set_target_callback(self, request:SetTarget.Request, response:SetTarget.Response):
        self.mouse_pose[0] = float(request.target.x)
        self.mouse_pose[1] = float(request.target.y)
        self.spawn_pizza(self.mouse_pose[0],self.mouse_pose[1])
        return response
    
    def set_param_callback(self, request:SetParam.Request, response:SetParam.Response):
        self.k_p[0] = float(request.kp_linear.data)
        self.k_p[1] = float(request.kp_angular.data)
        return response
    
    def cmdvel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = w
        self.cmd_vel_pub.publish(msg)
        
    def pose_callback(self, msg):
        self.robot_pose[0] = msg.x
        self.robot_pose[1] = msg.y
        self.robot_pose[2] = msg.theta
        
    def mouse_pose_callback(self, msg):
        self.mouse_pose[0] = msg.x
        self.mouse_pose[1] = msg.y
        self.spawn_pizza(self.mouse_pose[0], self.mouse_pose[1])
               
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
        
    def pizza_callback(self, msg):
        pizza_x = msg.pose.position.x + 5.0
        pizza_y = msg.pose.position.y + 5.0
        if pizza_x >= 0 and pizza_x <= 10 and pizza_y >= 0 and pizza_y <= 10 :
            self.mouse_pose[0] = msg.pose.position.x
            self.mouse_pose[1] = msg.pose.position.y
            self.spawn_pizza(self.mouse_pose[0], self.mouse_pose[1])

    def scanner(self, msg):
        detect = msg.data[0]
        
        
    def timer_callback(self):
        
        diff_x = self.mouse_pose[0] - self.robot_pose[0]
        diff_y = self.mouse_pose[1] - self.robot_pose[1]
        distance = float(sqrt(diff_x**2 + diff_y**2))
        omega = atan2(diff_y,diff_x) - self.robot_pose[2]
        angular_velo = atan2(sin(omega),cos(omega))
        self.cmdvel(distance*self.k_p[0], angular_velo*self.k_p[1])
        if distance < 0.2 :
            self.eat_pizza()
        # self.get_logger().info(f'{(distance*self.k_p[0])}, {self.k_p[1]}')
        
def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
