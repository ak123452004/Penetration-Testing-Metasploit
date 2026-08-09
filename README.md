# 🛡️ Penetration Testing (Metasploit)

A beginner-friendly **Cyber Security & Ethical Hacking** project that demonstrates the basic workflow of penetration testing using a safe, simulated lab environment.

This project is designed for learning concepts such as target selection, vulnerability assessment, security findings, risk severity, and report generation.

> **Note:** This project is an educational simulator. It does not perform real exploitation, brute-force attacks, or unauthorized network scanning.

---

## 📌 Project Information

| Field                    | Details                          |
| ------------------------ | -------------------------------- |
| **Intern ID**            | CMQ7VDB7B0                       |
| **Full Name**            | Ankit Kumar                      |
| **No. of Weeks**         | 8                                |
| **Project Name**         | Penetration Testing (Metasploit) |
| **Project Scope**        | Cyber Security & Ethical Hacking |
| **Programming Language** | Python                           |
| **Level**                | Beginner                         |

---

## 📖 About the Project

Penetration testing is a security process used to identify weaknesses in computer systems, applications, and networks.

Metasploit is a widely used penetration-testing framework that helps security professionals test vulnerabilities in authorized environments.

This beginner project provides a **safe simulation of a penetration-testing workflow**.

The user can select a simulated target such as:

* Web Server
* FTP Server
* SSH Server
* Database Server

The program then displays simulated security findings and recommendations and generates a security assessment report.

---

## 🎯 Objectives

The objectives of this project are:

1. Understand the basic penetration-testing workflow.
2. Learn about vulnerability assessment.
3. Understand security severity levels.
4. Learn how security findings are documented.
5. Generate a basic penetration-testing report.
6. Understand the role of tools such as Metasploit in authorized security testing.
7. Practice Python programming and modular code organization.

---

## 🧰 Technologies Used

* Python 3
* Python Standard Library
* Command Line Interface
* Git
* GitHub
* Metasploit concepts

No external Python packages are required.

---

## 📂 Project Structure

```text
Penetration-Testing-Metasploit/
│
├── .gitignore
├── README.md
├── main.py
├── report.py
├── requirements.txt
├── scanner.py
└── reports/
    └── security_report.txt
```

---

## ⚙️ How the Project Works

The project follows a simplified penetration-testing workflow:

```text
Select Target
      ↓
Simulated Security Assessment
      ↓
Identify Security Findings
      ↓
Assign Severity
      ↓
Provide Recommendations
      ↓
Generate Security Report
```

---

## 🔍 Simulated Targets

### 1. Web Server

Example findings:

* Missing security headers
* Outdated application components

### 2. FTP Server

Example findings:

* Unencrypted FTP
* Weak authentication policy

### 3. SSH Server

Example findings:

* Password-based authentication
* Security configuration weaknesses

### 4. Database Server

Example findings:

* Database access-control issues
* Security hardening requirements

---

## 🚦 Severity Levels

The project uses three basic severity levels:

| Severity  | Meaning                                        |
| --------- | ---------------------------------------------- |
| 🔴 HIGH   | Security issue requiring significant attention |
| 🟠 MEDIUM | Security weakness that should be addressed     |
| 🟢 LOW    | Lower-risk configuration or hardening issue    |

---

## ▶️ Installation

### Step 1: Install Python

Download and install Python 3.

Verify the installation:

```bash
python --version
```

---

### Step 2: Clone the Repository

```bash
git clone https://github.com/ak123452004/Penetration-Testing-Metasploit.git
```

---

### Step 3: Open the Project

```bash
cd Penetration-Testing-Metasploit
```

---

### Step 4: Run the Program

```bash
python main.py
```

---

## 💻 Example

```text
============================================================
       PENETRATION TESTING - METASPLOIT LAB
============================================================
Educational Cyber Security Project
Author: Ankit Kumar
Intern ID: CMQ7VDB7B0
============================================================

Available Lab Targets:
1. Web Server
2. FTP Server
3. SSH Server
4. Database Server

Select a target (1-4): 1

Selected Target: Web Server

--- Scan Results ---
[MEDIUM] HTTP
    Finding: Missing security headers
    Recommendation: Configure appropriate HTTP security headers.

[HIGH] Web Application
    Finding: Outdated application component
    Recommendation: Update the application and its dependencies.

Report generated successfully.
Check the 'reports' folder.
```

---

## 📄 Generated Report

After running the program, a report is generated at:

```text
reports/security_report.txt
```

The report contains:

* Project information
* Target information
* Assessment date
* Security findings
* Severity levels
* Security recommendations

---

## 🧠 Cyber Security Concepts

Through this project, beginners can learn:

### Reconnaissance

Collecting information about an authorized target before security testing.

### Vulnerability Assessment

Identifying potential weaknesses in a system.

### Exploitation

In a real authorized penetration test, security professionals may safely validate whether vulnerabilities are exploitable.

This project **does not perform exploitation**.

### Risk Assessment

Security findings can be categorized according to their potential impact.

### Reporting

A penetration test should produce clear documentation of findings and recommended remediation.

---

## 🔐 Ethical Considerations

Penetration testing must only be performed against systems for which you have explicit permission.

Do not use penetration-testing tools against:

* Websites without authorization
* Other people's computers
* Public servers without permission
* College or company networks without approval
* Random IP addresses

Always use a dedicated cybersecurity lab or an authorized testing environment.

---

## 🚀 Future Improvements

The project can be extended with:

* Graphical User Interface
* CVE database integration
* CVSS-based risk scoring
* JSON report generation
* HTML report generation
* Local vulnerable-lab integration
* Port/service identification in an authorized lab
* Interactive security dashboard
* Metasploit Framework lab integration

---

## 📚 Learning Outcomes

After completing this project, a beginner should understand:

* What penetration testing is
* What vulnerability assessment means
* Basic Metasploit concepts
* Security severity levels
* Security recommendations
* Penetration-testing reporting
* Python functions and modules
* File handling in Python
* GitHub project organization

---

## 👨‍💻 Author

**Ankit Kumar**

**Intern ID:** CMQ7VDB7B0

**Project:** Penetration Testing (Metasploit)

**Project Scope:** Cyber Security & Ethical Hacking

**Duration:** 8 Weeks

---

## ⚠️ Disclaimer

This project is intended **strictly for educational and authorized cybersecurity testing**.

The included scanner is a simulation and does not perform real vulnerability exploitation or unauthorized attacks.

Only perform penetration testing on systems that you own or have explicit permission to test.

---

⭐ **If you find this project useful, consider giving the repository a star!**
