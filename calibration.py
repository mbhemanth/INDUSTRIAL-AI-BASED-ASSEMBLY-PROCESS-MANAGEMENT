import cv2
import json
import os


class Calibration:

    def __init__(self):

        self.positions = {}

        self.current_step = 1

        self.file_name = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "positions.json"
        )

        self.radius = 35

    # ---------------------------------------
    # Save One Bolt Position
    # ---------------------------------------
    def add_point(self, bolt_number, center):

        x, y = center

        self.positions[f"P{bolt_number}"] = {
            "x": int(x),
            "y": int(y)
        }

        print(f"P{bolt_number} saved at ({x}, {y})")

        self.current_step = min(bolt_number + 1, 6)

    # ---------------------------------------
    # Save JSON File
    # ---------------------------------------
    def save(self):

        print("Saving positions.json...")

        with open(self.file_name, "w") as file:
            json.dump(self.positions, file, indent=4)

        print("positions.json saved successfully!")

    # ---------------------------------------
    # Load Existing Positions
    # ---------------------------------------

    def load(self):

        if not os.path.exists(self.file_name):

            return {}

        with open(self.file_name, "r") as file:

            self.positions = json.load(file)

        return self.positions

    # ---------------------------------------
    # Draw Saved Bolt Positions
    # ---------------------------------------

    def draw_points(self, frame):

        for key, point in self.positions.items():

            x = point["x"]
            y = point["y"]

            cv2.circle(
                frame,
                (x, y),
                self.radius,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                key,
                (x - 15, y - 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

    # ---------------------------------------
    # Show Calibration Instructions
    # ---------------------------------------

    def show_current(self, frame):

        text = f"Move Tag to Bolt {self.current_step} and Press {self.current_step}"

        cv2.rectangle(
            frame,
            (10, 10),
            (700, 55),
            (0, 0, 0),
            -1
        )

        cv2.putText(
            frame,
            text,
            (20, 42),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

    # ---------------------------------------
    # Reset Calibration
    # ---------------------------------------

    def reset(self):

        self.positions = {}

        self.current_step = 1

        print("Calibration Reset")

    # ---------------------------------------
    # Get Positions
    # ---------------------------------------

    def get_positions(self):

        return self.positions