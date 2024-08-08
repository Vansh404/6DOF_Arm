import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration
from std_msgs.msg import Header

#list of joints controlled by topic at /arm_controller/joint_trajectory
arm_joints = [ 'link1_to_link2', 
               'link2_to_link3', 
               'link3_to_link4', 
               'link4_to_link5', 
               'link5_to_link6', 
               'link6_to_link6flange']


gripper_joints=['gripper_controller']

class ExampleJointTrajectoryPublisherPy(Node):
    #execute basic traj for the arm
    def __init__(self):

        super.__init__('example_traj_pubpy')

        #publish to topic /arm_controller/joint_trajectory
        self.arm_pose_publisher = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 1)
        self.gripper_pose_publisher = self.create_publisher(JointTrajectory, '/grip_controller/joint_trajectory', 1)


        self.timer_period = 5.0  
        #callback function
        self.timer = self.create_timer(self.timer_period, self.timer_callback)


        self.frame_id = "base_link"