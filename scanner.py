"""
Simulated vulnerability scanner.

This module contains predefined lab scenarios.
It does not perform network scanning or exploitation.
"""


def scan_target(target):
    """
    Return simulated security findings for a selected lab target.
    """

    lab_data = {
        "Web Server": [
            {
                "service": "HTTP",
                "severity": "MEDIUM",
                "finding": "Missing security headers",
                "recommendation": "Configure appropriate HTTP security headers."
            },
            {
                "service": "Web Application",
                "severity": "HIGH",
                "finding": "Outdated application component",
                "recommendation": "Update the application and its dependencies."
            }
        ],

        "FTP Server": [
            {
                "service": "FTP",
                "severity": "HIGH",
                "finding": "Unencrypted FTP service",
                "recommendation": "Use SFTP or FTPS instead of plain FTP."
            },
            {
                "service": "FTP Authentication",
                "severity": "MEDIUM",
                "finding": "Weak authentication policy",
                "recommendation": "Use strong passwords and account lockout policies."
            }
        ],

        "SSH Server": [
            {
                "service": "SSH",
                "severity": "MEDIUM",
                "finding": "Password-based authentication enabled",
                "recommendation": "Consider using SSH key-based authentication."
            },
            {
                "service": "SSH Configuration",
                "severity": "LOW",
                "finding": "Security configuration can be hardened",
                "recommendation": "Disable unnecessary authentication methods."
            }
        ],

        "Database Server": [
            {
                "service": "Database",
                "severity": "HIGH",
                "finding": "Database service requires security hardening",
                "recommendation": "Restrict database access to trusted hosts."
            },
            {
                "service": "Database Authentication",
                "severity": "MEDIUM",
                "finding": "Weak access-control configuration",
                "recommendation": "Apply least-privilege permissions."
            }
        ]
    }

    return lab_data.get(target, [])
