import platform
import OLD_enc

def main():
    architecture = platform.architecture()[0]
    if architecture == '32bit':
        print("Your device is 32-bit.")
    elif architecture == '64bit':
        print("Your device is 64-bit.")
    else:
        print("Unknown architecture.")

    # Run the OLD_enc module
    OLD_enc.main()

if __name__ == "__main__":
    main()
