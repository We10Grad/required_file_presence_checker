def check_required_files():
    required_files = ["README.md", ".gitignore"]  
    missing_files = []
    
    for required_file in required_files:
        if not os.path.isfile(required_file):  
            missing_files.append(required_file)
    
    if missing_files:
        print("Missing Files:", ", ".join(missing_files))
        exit(1)
    else:
        exit(0)

if __name__ == "__main__":
    check_required_files()