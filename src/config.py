import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

INVENTORY_FILE = os.path.abspath(
    os.path.join(BASE_DIR, "..", "inventory", "ios-devices.yml")
)

OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")

