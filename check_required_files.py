import os
import sys
from typing import List

def check_required_files() -> None:
    """
    Check if required files exist in the current directory.
    
    Verifies the presence of README.md and .gitignore files.
    Exits with code 1 if any files are missing, otherwise exits with code 0.
    Prints a list of missing files to stdout if validation fails.
    
    Returns:
        None: This function exits the program and does not return.
    
    Exits:
        0: All required files are present
        1: One or more required files are missing
    """
    # Define the list of files that must exist in the repository
    required_files: List[str] = ["README.md", ".gitignore"]
    
    # Initialize an empty list to track any missing files
    missing_files: List[str] = []
    
    # Loop through each required file and check if it exists
    for required_file in required_files:
        # Check if the file exists in the current directory
        if not os.path.isfile(required_file):
            # Add missing file to our tracking list
            missing_files.append(required_file)
    
    # Determine if validation passed or failed
    if missing_files:
        # Print all missing files as a comma-separated list
        print("Missing Files:", ", ".join(missing_files))
        # Exit with failure code to fail the CI check
        sys.exit(1)
    else:
        # All files present - exit silently with success code
        sys.exit(0)

# Entry point: only run if script is executed directly (not imported)
if __name__ == "__main__":
    check_required_files()