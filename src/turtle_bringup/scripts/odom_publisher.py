#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose
from tf_transformations import quaternion_from_euler

class DummyNode(Node):
    def __init__(self):
        super().__init__('odom_node')
        
        # Publishers
        self.odom_publisher_t1 = self.create_publisher(Odometry, '/odom1', 10)
        self.odom_publisher_t2 = self.create_publisher(Odometry, '/odom2', 10)
        self.tf_broadcaster = TransformBroadcaster(self)
        
        # Subscriptions
        self.create_subscription(Pose, '/turtle1/pose', lambda msg: self.pose_callback(msg, "turtle1"), 10)
        self.create_subscription(Pose, '/turtle2/pose', lambda msg: self.pose_callback(msg, "turtle2"), 10)
        
        # Timer (if needed for periodic tasks)
        self.create_timer(0.01, self.timer_callback)

    def pose_callback(self, msg, turtle_name):
        if turtle_name == "turtle1":
            child_frame_id = "turtle1"
            self.example_pub(msg, child_frame_id)
        if turtle_name == "turtle2":
            child_frame_id = "turtle2"
            self.example_pub(msg, child_frame_id)

    def example_pub(self, msg, child_frame_id):
        # Create an Odometry message
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = 'odom'
        odom_msg.child_frame_id = child_frame_id
        
        # Set position and orientation
        odom_msg.pose.pose.position.x = msg.x - 5.0
        odom_msg.pose.pose.position.y = msg.y - 5.0
        odom_msg.pose.pose.position.z = 0.0  # Assuming 2D plane
        
        q = quaternion_from_euler(0, 0, msg.theta)
        odom_msg.pose.pose.orientation.x = q[0]
        odom_msg.pose.pose.orientation.y = q[1]
        odom_msg.pose.pose.orientation.z = q[2]
        odom_msg.pose.pose.orientation.w = q[3]

        # Create a TransformStamped message
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = child_frame_id
        
        t.transform.translation.x = msg.x - 5.0
        t.transform.translation.y = msg.y - 5.0
        t.transform.translation.z = 0.0  # Assuming 2D plane
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        self.odom_publisher_t1.publish(odom_msg)
        self.odom_publisher_t2.publish(odom_msg)
        self.tf_broadcaster.sendTransform(t)

    def timer_callback(self):
        pass  # Implement any periodic tasks if necessary

def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
