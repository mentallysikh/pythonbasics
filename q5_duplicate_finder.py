import os
import hashlib

def calculate_sha256(file_path):
    """Calculates the SHA-256 checksum of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read file in chunks to avoid memory issues with large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except (PermissionError, OSError):
        return None

def find_duplicates(directory, min_size_mb=0):
    """
    Scans directory for duplicate files based on checksums.
    Bonus: Filters files by minimum size[cite: 69].
    """
    files_metadata = {} # Dictionary to store {checksum: [file_paths]}
    min_bytes = min_size_mb * 1024 * 1024
    
    print(f"\nScanning: {directory} (Min Size: {min_size_mb}MB)...")

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            
            # Bonus: Minimum file size filter [cite: 69]
            try:
                if os.path.getsize(file_path) < min_bytes:
                    continue
                
                checksum = calculate_sha256(file_path)
                if checksum:
                    if checksum in files_metadata:
                        files_metadata[checksum].append(file_path)
                    else:
                        files_metadata[checksum] = [file_path]
            except OSError:
                continue

    # Identify duplicates (checksums with more than one file path) [cite: 66]
    duplicates = {cksum: paths for cksum, paths in files_metadata.items() if len(paths) > 1}
    return duplicates

def generate_report(duplicates):
    """Bonus: Creates a report listing duplicate files and their checksums."""
    report_file = "duplicate_report.txt"
    with open(report_file, "w") as f:
        f.write("DUPLICATE FILE REPORT\n")
        f.write("=" * 30 + "\n")
        for cksum, paths in duplicates.items():
            f.write(f"Checksum: {cksum}\n")
            for path in paths:
                f.write(f"  - {path}\n")
            f.write("-" * 30 + "\n")
    print(f"\nReport saved to: {os.path.abspath(report_file)}")

def main():
    target_dir = input("Enter the directory path to scan: ").strip()
    if not os.path.isdir(target_dir):
        print("Error: Invalid directory path.")
        return

    size_input = input("Enter minimum file size to consider (in MB, default 0): ").strip()
    min_size = int(size_input) if size_input.isdigit() else 0

    duplicates = find_duplicates(target_dir, min_size)

    if not duplicates:
        print("No duplicate files found.")
        return

    print(f"\nFound {len(duplicates)} sets of duplicate files:")
    for cksum, paths in duplicates.items():
        print(f"\n[Checksum: {cksum}]")
        for path in paths:
            print(f"  -> {path}")

    # Bonus: Generate the report 
    generate_report(duplicates)

    # Option to delete duplicates 
    action = input("\nWould you like to delete duplicates? (Only the original will remain) [y/N]: ").lower()
    if action == 'y':
        for paths in duplicates.values():
            # Keep the first file as the original, delete the rest
            for path_to_delete in paths[1:]:
                try:
                    os.remove(path_to_delete)
                    print(f"Deleted: {path_to_delete}")
                except Exception as e:
                    print(f"Failed to delete {path_to_delete}: {e}")

if __name__ == "__main__":
    main()