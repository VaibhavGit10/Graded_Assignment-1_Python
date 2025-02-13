"""
# Q3: Configuration File to JSON Converter

"""

# Simple Config Parser
# Made by: Vaibhav Pawar               

import json
import os

def parse_config(filename):
    """Parses a config file and returns data as a dictionary."""
    config = {}
    section = None

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Handle section headers like [Database]
                if line.startswith('[') and line.endswith(']'):
                    section = line[1:-1]
                    config[section] = {}
                
                # Handle key=value pairs within a section
                elif '=' in line and section:
                    key, value = line.split('=', 1)
                    config[section][key.strip()] = value.strip()

        return config

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

    return None

def save_to_json(config, output_file):
    """Saves the config dictionary as a JSON file."""
    try:
        with open(output_file, 'w') as f:
            json.dump(config, f, indent=4)
        print(f"Config saved as '{output_file}'")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def print_config(config):
    """Prints the configuration in a readable format."""
    print("\nParsed Configuration:")
    for section, settings in config.items():
        print(f"\n[{section}]")
        for key, value in settings.items():
            print(f"{key} = {value}")

def main():
    # Create a sample config file if it doesn't exist
    if not os.path.exists('config.txt'):
        with open('config.txt', 'w') as f:
            f.write("""[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080""")
        print("Created sample 'config.txt'")

    # Parse the config file
    config = parse_config('config.txt')

    # If parsing was successful, print and save the config
    if config:
        print_config(config)
        save_to_json(config, 'config.json')

if __name__ == "__main__":
    main()

