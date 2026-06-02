import yaml
import logging
from src.config import INVENTORY_FILE

def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as f:
            data = yaml.safe_load(f)
        return data.get("devices", [])
    except FileNotFoundError:
        logging.error("Inventory file not found")
        raise
    except yaml.YAMLError as e:
        logging.error(f"YAML parsing error: {e}")
        raise

