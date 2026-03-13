import re

# ──────────────────────────────────────────────────────────
#  IPv4 Validation
# ──────────────────────────────────────────────────────────

def validate_ipv4_regex(ip: str) -> tuple[bool, str]:
    """Validates IPv4 format using Regular Expressions."""
    # Pattern for 0-255 in each octet, ensuring 4 octets
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    if re.match(pattern, ip):
        return True, "Valid IPv4 format (Regex)."
    return False, "Invalid IPv4 format: Must be four octets (0-255) separated by dots."

def validate_ipv4_manual(ip: str) -> tuple[bool, str]:
    """Validates IPv4 format using standard string methods."""
    parts = ip.split(".")
    if len(parts) != 4:
        return False, f"Invalid format: Expected 4 octets, got {len(parts)}."
    
    for i, part in enumerate(parts, 1):
        if not part.isdigit():
            return False, f"Octet {i} ('{part}') is not a number."
        val = int(part)
        if not 0 <= val <= 255:
            return False, f"Octet {i} ({val}) is out of range (0-255)."
        if len(part) > 1 and part[0] == '0':
            return False, f"Octet {i} ('{part}') has an invalid leading zero."
            
    return True, "Valid IPv4 format (Manual)."

# ──────────────────────────────────────────────────────────
#  Gmail Validation
# ──────────────────────────────────────────────────────────

def validate_gmail_regex(email: str) -> tuple[bool, str]:
    """Validates Gmail address using Regular Expressions."""
    # Username: lowercase, numbers, dots, underscores
    # Domain: exactly @gmail.com
    pattern = r"^[a-z0-9._]+@gmail\.com$"
    if re.match(pattern, email):
        return True, "Valid Gmail address (Regex)."
    return False, "Invalid Gmail: Must use lowercase, numbers, or . _ before @gmail.com."

def validate_gmail_manual(email: str) -> tuple[bool, str]:
    """Validates Gmail address using standard string methods."""
    if "@gmail.com" not in email:
        return False, "Missing '@gmail.com' domain."
    
    parts = email.split("@")
    if len(parts) != 2 or parts[1] != "gmail.com":
        return False, "Invalid Gmail domain or multiple '@' symbols."
    
    username = parts[0]
    if not username:
        return False, "Username cannot be empty."
        
    allowed = "abcdefghijklmnopqrstuvwxyz0123456789._"
    for char in username:
        if char not in allowed:
            return False, f"Character '{char}' is not allowed in Gmail usernames."
            
    return True, "Valid Gmail address (Manual)."

if __name__ == "__main__":
    print(validate_ipv4_manual("192.168.1.1")[1])
    print(validate_gmail_manual("user.name123@gmail.com")[1])