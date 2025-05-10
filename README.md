# Python Port Scanner

A simple, multithreaded port scanner built in Python.

## Features

- Scans TCP ports on a given host/IP.
- Customizable port range (1–65535).
- Multithreaded scanning using `ThreadPoolExecutor`.
- Graceful error handling for invalid hosts and ports.

## Requirements

- Python 3.x

## Usage

1. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
