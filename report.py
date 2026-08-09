"""
Security assessment report generator.
"""

import os
from datetime import datetime


def generate_report(target, results):

    # Create reports directory if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    filename = "reports/security_report.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write("       PENETRATION TESTING LAB REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write("Project: Penetration Testing (Metasploit)\n")
        file.write("Author: Ankit Kumar\n")
        file.write("Intern ID: CMQ7VDB7B0\n")
        file.write(f"Target: {target}\n")
        file.write(
            f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        file.write("IMPORTANT:\n")
        file.write(
            "This is an educational simulated assessment. "
            "No real exploitation was performed.\n\n"
        )

        file.write("-" * 60 + "\n")
        file.write("FINDINGS\n")
        file.write("-" * 60 + "\n\n")

        for number, item in enumerate(results, start=1):

            file.write(f"Finding #{number}\n")
            file.write(f"Service: {item['service']}\n")
            file.write(f"Severity: {item['severity']}\n")
            file.write(f"Finding: {item['finding']}\n")
            file.write(
                f"Recommendation: {item['recommendation']}\n\n"
            )

        file.write("-" * 60 + "\n")
        file.write("END OF REPORT\n")
        file.write("-" * 60 + "\n")
