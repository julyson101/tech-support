import os
import logging
from src.utils import load_inventory
from src.collector import collect_show_tech
from src.config import OUTPUT_DIR, LOG_FILE


def setup_logging():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )


def main():
    setup_logging()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    logging.info("Starting collection process")

    devices = load_inventory()
    total = len(devices)

    success_count = 0

    for index, device in enumerate(devices, start=1):
        device_name = device.get("name", "unknown")

        print(f"[{index}/{total}] Processing {device_name}...")

        result = collect_show_tech(device)

        if result:
            success_count += 1
            print(f"[{index}/{total}] SUCCESS: {device_name}")
        else:
            print(f"[{index}/{total}] FAILED: {device_name}")


    logging.info(f"Completed. Success: {success_count}/{total}")
    print(f"\n DONE: {success_count}/{total} devices successful")



if __name__ == "__main__":
    main()

