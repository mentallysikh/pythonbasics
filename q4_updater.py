import subprocess
import logging
import sys

# Configure logging to project folder automatically [cite: 61]
logging.basicConfig(
    filename="package_update.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_updates():
    """Checks for available updates using apt[cite: 58]."""
    print("\n--- Checking for available updates ---\n")
    try:
        # Update package lists first
        subprocess.run(["sudo", "apt", "update"], check=True, capture_output=True)
        
        result = subprocess.run(
            ["apt", "list", "--upgradable"],
            capture_output=True,
            text=True
        )

        packages = result.stdout.split("\n")[1:]  # Skip 'Listing...' header [cite: 58]
        packages = [p for p in packages if p.strip() != ""]

        if not packages:
            print("Your system is already up to date.")
            return []

        print(f"Found {len(packages)} upgradable packages:\n")
        for i, pkg in enumerate(packages):
            print(f"[{i}] {pkg}")

        return packages

    except Exception as e:
        error_msg = f"Error checking updates: {e}"
        logging.error(error_msg)
        print(f"ALERT: {error_msg}")
        return []

def install_update(target):
    """Installs updates based on user choice[cite: 59, 60]."""
    try:
        if target == "all":
            print("\nUpdating all packages... this may take time.")
            subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
            msg = "Update All: Success"
        else:
            print(f"\nInstalling update for: {target}")
            subprocess.run(["sudo", "apt", "install", "--only-upgrade", "-y", target], check=True)
            msg = f"Update Specific ({target}): Success"

        print(f"\nCOMPLETED: {msg}")
        logging.info(msg)

    except subprocess.CalledProcessError as e:
        # Failure Alert and Logging [cite: 61]
        alert_msg = f"CRITICAL: Failed to install update(s). Command error: {e}"
        print(f"\nALERT: {alert_msg}")
        logging.error(alert_msg)

if __name__ == "__main__":
    # Check if user is on Linux
    if not sys.platform.startswith("linux"):
        print("This script is designed for Linux systems using the 'apt' package manager.")
        sys.exit()

    available_pkgs = check_updates()

    if available_pkgs:
        choice = input("\nEnter 'all' to update everything OR the [index number] for a specific package: ").strip()

        if choice.lower() == "all":
            install_update("all")
        elif choice.isdigit() and int(choice) < len(available_pkgs):
            # Extract only the package name (before the '/')
            package_name = available_pkgs[int(choice)].split("/")[0]
            install_update(package_name)
        else:
            print("Invalid input. No updates performed.")