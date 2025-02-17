
# Cisco FTD Rule Automation

![GitHub](https://img.shields.io/github/license/mrdc82/cisco_ftd_rule_automation)
![GitHub last commit](https://img.shields.io/github/last-commit/mrdc82/cisco_ftd_rule_automation)
![GitHub issues](https://img.shields.io/github/issues/mrdc82/cisco_ftd_rule_automation)

A Python-based tool for automating the creation, modification, and management of firewall rules on Cisco Firepower Threat Defense (FTD) devices. This project simplifies the process of managing large sets of firewall rules, reducing manual effort and minimizing errors.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Examples](#examples)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)

---

## Overview

Managing firewall rules on Cisco FTD devices can be time-consuming and error-prone, especially in large-scale environments. This project provides a Python-based solution to automate the process of creating, updating, and deleting firewall rules on Cisco FTD devices using the Firepower Management Center (FMC) API.

The tool is designed to:
- Streamline firewall rule management.
- Reduce manual configuration errors.
- Enable bulk operations for large rule sets.
- Provide a flexible and scriptable interface for network administrators.

---

## Features

- **Rule Creation**: Automate the creation of access control rules on Cisco FTD.
- **Rule Modification**: Update existing rules with new parameters (e.g., source/destination IPs, ports, actions).
- **Rule Deletion**: Remove rules from the configuration.
- **Bulk Operations**: Perform actions on multiple rules simultaneously.
- **Logging and Reporting**: Generate logs and reports for audit purposes.
- **API Integration**: Leverage the Cisco FMC REST API for seamless integration.

---

## Prerequisites

Before using this tool, ensure you have the following:

- **Python 3.7 or higher**: The script is written in Python and requires a compatible version.
- **Cisco FMC API Access**: Access to a Cisco Firepower Management Center (FMC) with API enabled.
- **API Credentials**: A valid username, password, and API token for the FMC.
- **Required Python Libraries**:
  - `requests`
  - `json`
  - `logging`
  - `argparse`

Install the required libraries using pip:
```bash
pip install requests
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mrdc82/cisco_ftd_rule_automation.git
   cd cisco_ftd_rule_automation
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your FMC API credentials in the `config.json` file:
   ```json
   {
     "fmc_host": "your-fmc-hostname-or-ip",
     "username": "your-username",
     "password": "your-password"
   }
   ```

---

## Usage

The tool provides a command-line interface (CLI) for managing firewall rules. Below are the available commands:

### Create a Rule
```bash
python cisco_ftd_rule_automation.py --action create --rule-name "Allow_HTTP" --source-ip "192.168.1.0/24" --destination-ip "10.0.0.1" --port 80 --action allow
```

### Modify a Rule
```bash
python cisco_ftd_rule_automation.py --action modify --rule-name "Allow_HTTP" --new-destination-ip "10.0.0.2"
```

### Delete a Rule
```bash
python cisco_ftd_rule_automation.py --action delete --rule-name "Allow_HTTP"
```

### Bulk Operations
Use a JSON file to perform bulk operations:
```bash
python cisco_ftd_rule_automation.py --action bulk --file rules.json
```

---

## Examples

### Example 1: Create a Rule
```bash
python cisco_ftd_rule_automation.py --action create --rule-name "Block_SSH" --source-ip "any" --destination-ip "192.168.1.10" --port 22 --action block
```

### Example 2: Modify a Rule
```bash
python cisco_ftd_rule_automation.py --action modify --rule-name "Block_SSH" --new-action allow
```

### Example 3: Bulk Rule Creation
Create a `rules.json` file:
```json
[
  {
    "action": "create",
    "rule_name": "Allow_DNS",
    "source_ip": "any",
    "destination_ip": "8.8.8.8",
    "port": 53,
    "action": "allow"
  },
  {
    "action": "create",
    "rule_name": "Block_ICMP",
    "source_ip": "any",
    "destination_ip": "any",
    "port": "icmp",
    "action": "block"
  }
]
```
Run the bulk operation:
```bash
python cisco_ftd_rule_automation.py --action bulk --file rules.json
```

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request with a detailed description of your changes.

Please ensure your code adheres to the project's coding standards and includes appropriate documentation.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Cisco Systems for providing the Firepower Management Center API.
- The Python community for their invaluable resources and libraries.

---

For questions or support, please open an issue on the [GitHub repository](https://github.com/mrdc82/cisco_ftd_rule_automation/issues).

---

This README provides a comprehensive guide to your project, making it easy for users and contributors to understand and use your tool. Let me know if you'd like to add or modify anything!
