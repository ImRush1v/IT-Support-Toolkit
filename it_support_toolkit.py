import platform 
import socket
import subprocess
import shutil

def show_system_info():
    print("\n--- SYSTEM INFORMATION ---")
    print(f"Computer Name: {socket.gethostname()}")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"OS Release: {platform.release()}")
    print(f"Architecture: {platform.architecture()}")
    print(f"Processor: {platform.processor()}")

def show_network_info():
    print("\n--- NETWORK INFORMATION ---")

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print(f"Hostname: {hostname}")
    print(f"Local IP Address: {ip_address}")

def check_internet():
    print("\n--- INTERNET CONNECTION TEST ---")
    print("Testing connection...")

    result = subprocess.run(
        ["ping", "-n", "1", "8.8.8.8"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("Internet connection: ONLINE")
    else:
        print("Internet connection: OFFLINE")

def check_disk_usage():
    print("\n--- DISK USAGE ---")

    total, used, free = shutil.disk_usage("C:\\")

    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)
    used_percent = (used / total) * 100

    print(f"Total Space: {total_gb:.2f} GB")
    print(f"Used Space:  {used_gb:.2f} GB")
    print(f"Free Space:  {free_gb:.2f} GB")
    print(f"Disk Usage:  {used_percent:.1f}%")

while True:
    print("\n" +"=" * 50)
    print("      IT Support Toolkit")
    print("=" * 50)

    print("\n1. System Information")
    print("2. Network Information")
    print("3. Check Internet Connection")
    print("4. Check Disk Usage")
    print("5. DNS Test")
    print("6. Exit")

    choice = input("\nSelect an option (1-6): ")

    if choice == "1":
        show_system_info()

    elif choice == "2":
        show_network_info()

    elif choice == "3":
        check_internet()

    elif choice == "4":
        check_disk_usage()

    elif choice == "6":
        print("\nExiting the IT Support Toolkit...")
        break

    else:
        print("\nThat feature is not available yet.")
