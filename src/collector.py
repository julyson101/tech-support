import os
import logging
from datetime import datetime
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
from src.config import OUTPUT_DIR


def collect_show_tech(device):
    device_name = device.get("name", "unknown")
    
    filename = os.path.join(
        OUTPUT_DIR,
        f"{device_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    try:
        logging.info(f"Connecting to {device_name}")

        netmiko_device = device.copy()
        netmiko_device.pop("name", None)

        connection = ConnectHandler(**netmiko_device)

        logging.info(f"Running show tech-support on {device_name} (this may take a while)...")

        output = connection.send_command_timing(
            "show tech-support",
            delay_factor=2,
            max_loops=1000
        )
        
        connection.disconnect()

        with open(filename, "w") as f:
            f.write(output)

        logging.info(f"Saved output for {device_name} → {filename}")

        return True

    except NetmikoTimeoutException:
        logging.error(f"Timeout connecting to {device_name}")
    except NetmikoAuthenticationException:
        logging.error(f"Authentication failed for {device_name}")
    except Exception as e:
        logging.exception(f"Unexpected error with {device_name}: {e}")

    return False


