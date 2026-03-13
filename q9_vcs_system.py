import os
import shutil
import hashlib
import time
import difflib

class SimpleVCS:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.version_dir = os.path.join(target_dir, ".versions")
        
        # Ensure version directory exists [cite: 156]
        if not os.path.exists(self.version_dir):
            os.makedirs(self.version_dir)

    def get_file_hash(self, filepath):
        """Calculate hash to detect changes."""
        hasher = hashlib.md5()
        with open(filepath, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def commit(self, filename):
        """Saves a new version if the file has changed[cite: 156, 157]."""
        original_path = os.path.join(self.target_dir, filename)
        if not os.path.exists(original_path):
            print(f"File {filename} not found.")
            return

        # Create timestamped version name [cite: 157]
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        version_filename = f"{timestamp}_{filename}"
        version_path = os.path.join(self.version_dir, version_filename)

        shutil.copy2(original_path, version_path)
        print(f"Version saved: {version_filename}")

    def list_versions(self, filename):
        """Lists all stored versions for a specific file."""
        versions = [v for v in os.listdir(self.version_dir) if v.endswith(filename)]
        versions.sort()
        print(f"\nVersions for {filename}:")
        for i, v in enumerate(versions):
            print(f"[{i}] {v}")
        return versions

    def restore(self, filename, version_index):
        """Restores a file to a previous version[cite: 158, 159]."""
        versions = [v for v in os.listdir(self.version_dir) if v.endswith(filename)]
        versions.sort()
        
        if 0 <= version_index < len(versions):
            source = os.path.join(self.version_dir, versions[version_index])
            destination = os.path.join(self.target_dir, filename)
            shutil.copy2(source, destination)
            print(f"Restored {filename} to version {versions[version_index]}")
        else:
            print("Invalid version index.")

    def show_diff(self, filename, v_idx1, v_idx2):
        """Bonus: Compare two versions (diff)[cite: 161]."""
        versions = [v for v in os.listdir(self.version_dir) if v.endswith(filename)]
        versions.sort()
        
        path1 = os.path.join(self.version_dir, versions[v_idx1])
        path2 = os.path.join(self.version_dir, versions[v_idx2])

        with open(path1, 'r') as f1, open(path2, 'r') as f2:
            diff = difflib.unified_diff(
                f1.readlines(), f2.readlines(),
                fromfile=versions[v_idx1], tofile=versions[v_idx2]
            )
            print(''.join(diff))

    def cleanup(self, filename, keep_last_n=3):
        """Bonus: Keep only the last n versions[cite: 162]."""
        versions = [v for v in os.listdir(self.version_dir) if v.endswith(filename)]
        versions.sort()
        
        if len(versions) > keep_last_n:
            to_delete = versions[:-keep_last_n]
            for v in to_delete:
                os.remove(os.path.join(self.version_dir, v))
            print(f"Cleaned up {len(to_delete)} old versions.")

# --- Demo Setup ---
if __name__ == "__main__":
    # 1. Initialize
    vcs = SimpleVCS("./my_project")
    test_file = "note.txt"
    
    # Create file for demo
    with open("./my_project/note.txt", "w") as f:
        f.write("Version 1 content")
    
    # 2. Save versions
    vcs.commit(test_file)
    time.sleep(1) # Ensure different timestamps
    
    with open("./my_project/note.txt", "w") as f:
        f.write("Version 2 content updated")
    vcs.commit(test_file)
    
    # 3. List and Restore
    avail_versions = vcs.list_versions(test_file)
    vcs.restore(test_file, 0)
    
    # 4. Show Diff (Bonus)
    print("\n--- Showing Differences ---")
    vcs.show_diff(test_file, 0, 1)
    
    # 5. Cleanup (Bonus)
    vcs.cleanup(test_file, keep_last_n=1)