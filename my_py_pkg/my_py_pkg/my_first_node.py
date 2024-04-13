#! /usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("py_test") #creates node and give a name
        self.counter_ = 0
        self.get_logger().info("Hello ROS2") #print something
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello " + str(self.counter_))

def main(args=None):
    rclpy.init(args=args) #inicialize ROS2 comunication
    node = MyNode()
    rclpy.spin(node) #allow to callback node by other
    rclpy.shutdown() #shutdown

if __name__ == '__main__':
    main()