import cv2
from pupil_apriltags import Detector


class AprilTagDetector:

    def __init__(self):

        # Camera parameters (same as your original project)
        self.fx = 600
        self.fy = 600
        self.cx = 320
        self.cy = 240

        # Actual AprilTag size (meters)
        self.tag_size = 0.05

        # Detector
        self.detector = Detector(
            families="tag36h11",
            nthreads=4,
            quad_decimate=1.0,
            quad_sigma=0.0,
            refine_edges=True,
            decode_sharpening=0.25
        )

    # --------------------------------------------------
    # Detect AprilTags
    # --------------------------------------------------

    def detect(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        tags = self.detector.detect(
            gray,
            estimate_tag_pose=True,
            camera_params=[
                self.fx,
                self.fy,
                self.cx,
                self.cy
            ],
            tag_size=self.tag_size
        )

        return tags

    # --------------------------------------------------
    # Draw One Tag
    # --------------------------------------------------

    def draw(self, frame, tag):

        corners = tag.corners.astype(int)

        # Draw box

        for i in range(4):

            cv2.line(
                frame,
                tuple(corners[i]),
                tuple(corners[(i + 1) % 4]),
                (0, 255, 0),
                2
            )

        # Center

        center = (
            int(tag.center[0]),
            int(tag.center[1])
        )

        cv2.circle(
            frame,
            center,
            6,
            (0, 0, 255),
            -1
        )

        # Tag ID

        cv2.putText(
            frame,
            f"ID : {tag.tag_id}",
            (center[0] - 30, center[1] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2
        )

        # Pose (optional)

        try:

            pose = tag.pose_t.flatten()

            x = pose[0]
            y = pose[1]
            z = pose[2]

            cv2.putText(
                frame,
                f"X:{x:.3f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Y:{y:.3f}",
                (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Z:{z:.3f}",
                (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        except:
            pass

    # --------------------------------------------------
    # Draw All
    # --------------------------------------------------

    def draw_all(self, frame, tags):

        for tag in tags:
            self.draw(frame, tag)

    # --------------------------------------------------
    # Get Center
    # --------------------------------------------------

    def get_center(self, tag):

        return (
            int(tag.center[0]),
            int(tag.center[1])
        )

    # --------------------------------------------------
    # Get Tag ID
    # --------------------------------------------------

    def get_id(self, tag):

        return int(tag.tag_id)

    # --------------------------------------------------
    # Get Pose
    # --------------------------------------------------

    def get_pose(self, tag):

        try:

            pose = tag.pose_t.flatten()

            return (
                float(pose[0]),
                float(pose[1]),
                float(pose[2])
            )

        except:

            return None