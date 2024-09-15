import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

class DemoSubscriber(Node):

    def __init__(self):
        super().__init__("demo_subscriber")
        self.point_listener = self.create_subscription(
            Point,
            "/mediapipe_face_tracker/location",
            self.point_listener_callback,
            1)

    def point_listener_callback(self, point: Point):
        # We want to try and keep the face in the center
        face_x = point.x
        face_y = point.y
        face_z = point.z  # Width of face as percentage
        self.get_logger().info(f"Tracked face: x:{face_x}, y:{face_y}, z:{face_z}")
        

def main():
    rclpy.init()
    node = DemoSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()


if __name__ == "__main__":
    main()
