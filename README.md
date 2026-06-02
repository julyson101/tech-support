# Cisco IOS Show Tech-Support Collector

## Overview
This project connects to Cisco IOS devices and collects `show tech-support` output, saving it locally.

## Features
- YAML inventory support
- Netmiko SSH connections
- Per-device output files
- Logging
- Error handling
- Unit tests

## Project Structure
(see repo layout)

## Setup

```bash
python3 -m venv tesu-venv
source tesu-venv/bin/activate  # Linux/Mac
tesu-venv\Scripts\activate     # Windows

pip install -r requirements.txt

