import rclpy
from rclpy.node import Node
import time
from trajectory_msgs.msg import JointTrajectory , JointTrajectoryPoint

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.trajectory_publihser = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory'
        , 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        dual_armRjoints = ['joint_1,joint_2,joint_3,joint_4,joint_5,joint_8']
        goal_positions = [0.5,0.5,0.5,0.5,0.5,0.5]
                ## creating a message to send Joint Trajectory type
        dual_armR_traj_msgs = JointTrajectory()
        dual_armR_traj_msgs.joint_names = dual_armRjoints
        dual_armR_traj_msgs.points.append(JointTrajectoryPoint())
        dual_armR_traj_msgs.points[0].positions = goal_positions
        dual_armR_traj_msgs.points[0].velocities = [0.0 for i in dual_armRjoints]
        dual_armR_traj_msgs.points[0].accelerations = [0.0 for i in dual_armRjoints]
        dual_armR_traj_msgs.points[0].time_from_start = time.sleep(2)
        time.sleep(1)
        self.trajectory_publihser.publish(dual_armR_traj_msgs)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()