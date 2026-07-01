import cv2
import json
import math
import time
import os


class SequenceChecker:

    def __init__(self, position_file):

        self.position_file = position_file

        self.positions = self.load_positions()

        self.order = [
            "P1",
            "P2",
            "P3",
            "P4",
            "P5",
            "P6"
        ]

        self.current_step = 0

        from config import BOLT_RADIUS

        self.radius = BOLT_RADIUS

        self.hold_time = 1.0

        self.hold_start = None

        self.status = "Waiting..."

        self.start_time = None

        self.end_time = None

        self.completed = False

    # ----------------------------------------
    # Load Positions
    # ----------------------------------------

    def load_positions(self):

        if not os.path.exists(self.position_file):
            return {}

        try:

            with open(self.position_file, "r") as file:

                data = json.load(file)

            return data

        except:

            return {}

    # ----------------------------------------
    # Distance
    # ----------------------------------------

    def distance(self, p1, p2):

        return math.sqrt(
            (p1[0] - p2[0]) ** 2 +
            (p1[1] - p2[1]) ** 2
        )

    # ----------------------------------------
    # Update Sequence
    # ----------------------------------------

    def update(self, glove_center):

        if self.completed:
            return

        # No calibration yet
        if len(self.positions) < 6:
            self.status = "Please Calibrate First"
            return

        if self.start_time is None:
            self.start_time = time.time()

        expected = self.order[self.current_step]

        if expected not in self.positions:
            self.status = "Missing Calibration"
            return

        target = self.positions[expected]

        target_center = (
            target["x"],
            target["y"]
        )

        dist = self.distance(
            glove_center,
            target_center
        )

        if dist <= self.radius:

            if self.hold_start is None:
                self.hold_start = time.time()

            elapsed = time.time() - self.hold_start

            self.status = f"Hold {max(0,self.hold_time-elapsed):.1f}s"

            if elapsed >= self.hold_time:

                self.current_step += 1

                self.hold_start = None

                if self.current_step >= len(self.order):

                    self.completed = True

                    self.end_time = time.time()

                    self.status = "ASSEMBLY COMPLETED"

                else:

                    self.status = f"{expected} Completed"

        else:

            self.hold_start = None

            self.status = f"Move to {expected}"

    # ----------------------------------------
    # Draw Regions
    # ----------------------------------------

    def draw_regions(self, frame):

        if len(self.positions) < 6:

            cv2.putText(
                frame,
                "Calibration Required",
                (40, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

            return

        for index, name in enumerate(self.order):

            if name not in self.positions:
                continue

            point = self.positions[name]

            x = point["x"]
            y = point["y"]

            color = (180, 180, 180)

            if index < self.current_step:
                color = (0, 255, 0)

            elif index == self.current_step:
                color = (255, 0, 0)

            cv2.circle(
                frame,
                (x, y),
                self.radius,
                color,
                3
            )

            cv2.putText(
                frame,
                name,
                (x - 15, y - 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2
            )

    # ----------------------------------------
    # Draw Status
    # ----------------------------------------

    def draw_status(self, frame):

        cv2.rectangle(
            frame,
            (0, 0),
            (700, 100),
            (30, 30, 30),
            -1
        )

        if len(self.positions) < 6:

            cv2.putText(
                frame,
                "Press C to Calibrate",
                (20, 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )

            return

        next_bolt = "DONE" if self.completed else self.order[self.current_step]

        cv2.putText(
            frame,
            f"Next : {next_bolt}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        cv2.putText(
            frame,
            self.status,
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        if self.completed:

            total = self.end_time - self.start_time

            cv2.putText(
                frame,
                f"Time : {total:.1f}s",
                (420, 75),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

    # ----------------------------------------
    # Reset
    # ----------------------------------------

    def reset(self):

        self.positions = self.load_positions()

        self.current_step = 0

        self.hold_start = None

        self.status = "Waiting..."

        self.start_time = None

        self.end_time = None

        self.completed = False