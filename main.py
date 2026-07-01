import cv2

from detector import AprilTagDetector
from sequence import SequenceChecker
from calibration import Calibration

# ---------------------------------------
# Camera
# ---------------------------------------

CAMERA_ID = 1

cap = cv2.VideoCapture(CAMERA_ID)

# Camera Resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Window
cv2.namedWindow(
    "Industrial Assembly Monitoring",
    cv2.WINDOW_NORMAL
)

cv2.setWindowProperty(
    "Industrial Assembly Monitoring",
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)

# ---------------------------------------
# Initialize Classes
# ---------------------------------------

detector = AprilTagDetector()

sequence = SequenceChecker(
    position_file="positions.json"
)

calibration = Calibration()

# ---------------------------------------
# Variables
# ---------------------------------------

calibration_mode = False

print("--------------------------------")
print("Assembly Monitoring Started")
print("Press C : Calibration Mode")
print("Press R : Reset Assembly")
print("Press ESC : Exit")
print("--------------------------------")

# ---------------------------------------
# Main Loop
# ---------------------------------------

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # ----------------------------------
    # Detect AprilTag
    # ----------------------------------

    tags = detector.detect(frame)

    glove_center = None

    if len(tags) > 0:

        tag = tags[0]

        glove_center = (
            int(tag.center[0]),
            int(tag.center[1])
        )

        detector.draw(frame, tag)

    # ----------------------------------
    # Calibration View
    # ----------------------------------

    if calibration_mode:

        calibration.draw_points(frame)

        calibration.show_current(frame)

    # ----------------------------------
    # Assembly View
    # ----------------------------------

    else:

        sequence.draw_regions(frame)

        if glove_center is not None:
            sequence.update(glove_center)

        sequence.draw_status(frame)

    # ----------------------------------
    # Draw Tag Center
    # ----------------------------------

    if glove_center is not None:

        cv2.circle(
            frame,
            glove_center,
            8,
            (0, 0, 255),
            -1
        )

    # ----------------------------------
    # Display
    # ----------------------------------

    cv2.imshow(
        "Industrial Assembly Monitoring",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    # ----------------------------------
    # Exit
    # ----------------------------------

    if key == 27:
        break

    # ----------------------------------
    # Toggle Calibration
    # ----------------------------------

    elif key == ord("c"):

        calibration_mode = not calibration_mode

        if calibration_mode:

            print("--------------------------------")
            print("Calibration Mode Enabled")
            print("Move Tag to Bolt 1 and Press 1")
            print("Move Tag to Bolt 2 and Press 2")
            print("Move Tag to Bolt 3 and Press 3")
            print("Move Tag to Bolt 4 and Press 4")
            print("Move Tag to Bolt 5 and Press 5")
            print("Move Tag to Bolt 6 and Press 6")
            print("--------------------------------")

        else:

            calibration.save()

            # Reload new positions
            sequence.positions = sequence.load_positions()

            print("--------------------------------")
            print("Calibration Saved Successfully")
            print("--------------------------------")

    # ----------------------------------
    # Reset
    # ----------------------------------

    elif key == ord("r"):

        sequence.reset()

        print("Assembly Reset")

    # ----------------------------------
    # Save Calibration Points
    # ----------------------------------

    if calibration_mode and glove_center is not None:

        if key == ord("1"):

            calibration.add_point(1, glove_center)

        elif key == ord("2"):

            calibration.add_point(2, glove_center)

        elif key == ord("3"):

            calibration.add_point(3, glove_center)

        elif key == ord("4"):

            calibration.add_point(4, glove_center)

        elif key == ord("5"):

            calibration.add_point(5, glove_center)

        elif key == ord("6"):

            calibration.add_point(6, glove_center)

cap.release()

cv2.destroyAllWindows()