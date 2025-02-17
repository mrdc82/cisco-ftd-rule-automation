# Cisco FTD Rule Automation

## GitHub Repository
- **Issues:** [Report an Issue](https://github.com/mrdc82/cisco_ftd_rule_automation/issues)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview
Managing firewall rules on Cisco Firepower Threat Defense (FTD) devices can be a time-consuming and error-prone task, especially in large-scale environments. This project provides a Python-based solution to automate the process of creating, updating, and deleting firewall rules using the Firepower Management Center (FMC) API.

This tool is designed to:
- Streamline firewall rule management.
- Reduce manual configuration errors.
- Enable bulk operations for large rule sets.
- Provide a flexible and scriptable interface for network administrators.

## Features
- **Rule Creation:** Automates the creation of access control rules.
- **Rule Modification:** Updates existing rules with new parameters (e.g., source/destination IPs, ports, actions).
- **Rule Deletion:** Removes rules from the configuration.
- **Bulk Operations:** Allows actions on multiple rules simultaneously.
- **Logging and Reporting:** Generates logs and reports for audit purposes.
- **API Integration:** Utilizes the Cisco FMC REST API for seamless integration.

## Prerequisites
Ensure you have the following before using this tool:
- **Python 3.7 or higher** (Required for script execution)
- **Cisco FMC API Access** (Ensure API access is enabled)
- **API Credentials** (Username, password, and API token for authentication)
- **Required Python Libraries:**
  - `requests`
  - `json`
  - `logging`
  - `argparse`
  
To install the required libraries, run:
```bash
pip install requests json logging argparse
```

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/mrdc82/cisco_ftd_rule_automation.git
   cd cisco_ftd_rule_automation
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure FMC API credentials:**
   Update the `config.json` file with your FMC details:
   ```json
   {
     "fmc_host": "your-fmc-hostname-or-ip",
     "username": "your-username",
     "password": "your-password"
   }
   ```

## Usage
This project consists of three main stages:

### **Stage 1: Rule File Preparation**
Run `build_policyid_files.py` to format and organize rule files based on the FTD Policy Name. The formatted files will be used for policy deployment.

### **Stage 2: Payload Generation**
Run `payload_generator.py` to extract rule data (source, destination, ports) and create a JSON payload for API consumption. This script ensures duplicate ports are removed before sending requests to FMC.

### **Stage 3: Rule Deployment**
Run `PUT_acp_new_rules.py` to implement the rules on the FMC. This script:
- Creates a blank rule.
- Updates the blank rule with the payload data.
- Deploys the updated rule to the correct policy.

## Examples
**Executing the script:**
```bash
python build_policyid_files.py
python payload_generator.py
python PUT_acp_new_rules.py
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch` or `bugfix-branch`).
3. Commit your changes.
4. Submit a pull request with a detailed description of your changes.

Please ensure your code adheres to the project's coding standards and includes appropriate documentation.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Cisco Systems** for providing the Firepower Management Center API.
- **The Python community** for invaluable resources and libraries.

For questions or support, please [open an issue](https://github.com/mrdc82/cisco_ftd_rule_automation/issues) on GitHub.

---
🚀 **Automate your firewall rule management with ease!**

