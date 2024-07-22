import platform
import OLD_enc

def show_device_info():
    system = platform.system()
    node = platform.node()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()

    print(f"System: {system}")
    print(f"Node Name: {node}")
    print(f"Release: {release}")
    print(f"Version: {version}")
    print(f"Machine: {machine}")
    print(f"Processor: {processor}")

def main():
    architecture = platform.architecture()[0]
    if architecture == '32bit':
        print("Your device is 32-bit.")
        show_device_info()
    elif architecture == '64bit':
        print("Your device is 64-bit.")
        show_device_info()
    else:
        print("Unknown architecture.")
        show_device_info()

    # Run the OLD_enc module
    OLD_enc.main()

if __name__ == "__main__":
    main()
