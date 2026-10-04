import platform 
import socket

def show_system_info():
    print("\n--- SYSTEM INFORMATION ---")
    print(f"Computer Name: {socket.gethostname()}")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"OS Release: {platform.release()}")
    print(f"Architecture: {platform.architecture()}")
    print(f"Processor: {platform.processor()}")

while True:
    print("=" * 50)
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

    elif choice == "6":
        print("\nExiting the IT Support Toolkit...")
        break

    else:
        print("\nThat feature is not available yet.")
        