"""
Industrial AI Based Assembly Process Management
Configuration File
"""

# ==========================================
# CAMERA SETTINGS
# ==========================================

CAMERA_ID = 1             # USB Camera ID

WINDOW_NAME = "Industrial AI Assembly Monitoring"

FULLSCREEN = False


# ==========================================
# APRILTAG SETTINGS
# ==========================================

APRILTAG_FAMILY = "tag25h9"

TAG_SIZE = 0.05            # meters (5 cm)


# ==========================================
# ASSEMBLY SETTINGS
# ==========================================

TOTAL_BOLTS = 6

ASSEMBLY_ORDER = [

    "P1",

    "P2",

    "P3",

    "P4",

    "P5",

    "P6"

]


# ==========================================
# DETECTION SETTINGS
# ==========================================

BOLT_RADIUS = 120         # pixels

HOLD_TIME = 1.0            # seconds


# ==========================================
# COLORS
# OpenCV uses BGR
# ==========================================

GRAY = (170,170,170)

GREEN = (0,255,0)

RED = (0,0,255)

BLUE = (255,0,0)

YELLOW = (0,255,255)

WHITE = (255,255,255)

BLACK = (20,20,20)


# ==========================================
# UI SETTINGS
# ==========================================

FONT = 0

FONT_SCALE = 0.7

FONT_THICKNESS = 2


# ==========================================
# PANEL SETTINGS
# ==========================================

HEADER_HEIGHT = 70

RIGHT_PANEL_WIDTH = 320


# ==========================================
# ANIMATION
# ==========================================

FLASH_SPEED = 0.5


# ==========================================
# FILES
# ==========================================

POSITION_FILE = "positions.json"

LOG_FILE = "assembly_log.csv"