# backend/engine/device_sim.py

def simulate_device_read(filename):
    """
    Simulate reading content from a device (file).
    """
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return "File not found."

def simulate_device_overwrite(filename):
    """
    Simulate overwriting device/file (wiping).
    """
    with open(filename, "w") as f:
        f.write("0" * 1024)  # Overwrite with zeros
    return True