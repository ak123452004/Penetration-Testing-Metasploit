"""
Penetration Testing (Metasploit) - Beginner Project

Author: Ankit Kumar
Intern ID: CMQ7VDB7B0

Educational penetration-testing lab simulator.
This project does NOT perform real exploitation.
"""

from scanner import scan_target
from report import generate_report


def show_banner():
    print("=" * 60)
    print("       PENETRATION TESTING - METASPLOIT LAB")
    print("=" * 60)
    print("Educational Cyber Security Project")
    print("Author: Ankit Kumar")
    print("Intern ID: CMQ7VDB7B0")
    print("=" * 60)


def main():
    show_banner()

    print("\nAvailable Lab Targets:")
    print("1. Web Server")
    print("2. FTP Server")
    print("3. SSH Server")
    print("4. Database Server")

    choice = input("\nSelect a target (1-4): ")

    targets = {
        "1": "Web Server",
        "2": "FTP Server",
        "3": "SSH Server",
        "4": "Database Server"
    }

    if choice not in targets:
        print("\nInvalid choice.")
        return

    target = targets[choice]

    print(f"\nSelected Target: {target}")

    # Perform a safe simulated scan
    results = scan_target(target)

    print("\n--- Scan Results ---")

    for item in results:
        print(f"[{item['severity']}] {item['service']}")
        print(f"    Finding: {item['finding']}")
        print(f"    Recommendation: {item['recommendation']}")
        print()

    # Generate report
    generate_report(target, results)

    print("Report generated successfully.")
    print("Check the 'reports' folder.")


if __name__ == "__main__":
    main()
