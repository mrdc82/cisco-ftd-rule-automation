# Cisco FTD Rule Automation

## Overview
This project was developed to streamline and automate the time-consuming task of manually implementing FTD firewall rules. Our department processes between 30 to 50 firewall rule changes daily, making automation essential for efficiency. By leveraging Python automation and the FMC API, this project significantly reduces manual input, improving accuracy and speed.

Our team uses **ServiceNow (SNOW)** as a ticketing system, where:
1. A business unit logs a ticket with source, destination, and port information.
2. ServiceNow compiles the request into a table.
3. The Data Centre Automation team determines the relevant firewall.
4. The security team receives a file (e.g., `CHG0001.txt`) for rule implementation on FMC.

This project provides a flexible automation framework adaptable to different ticketing systems and rule request processes. Feel free to collaborate on custom integrations!

---

## Process Workflow
This automation follows a three-stage workflow:

### **Stage 1: Generating Policy-Specific Rule Files** (`build_policyid_files.py`)
- The engineer selects the file containing FTD rules.
- The script processes the file and generates individual rule files based on FTD Policy Names.
- The output filenames follow the format: `FTDname_CHGxxx.txt` (used for both policy name and rule name in FMC).

### **Stage 2: Payload Generation** (`payload_generator.py`)
- The engineer selects a generated policy file.
- The script extracts source, destination, and port information.
- Duplicate ports are removed to prevent API duplication errors.
- The payload is created but lacks a **rule ID**, which is assigned in the next step.

### **Stage 3: Rule Implementation on FMC** (`PUT_acp_new_rules.py`)
- The script first creates a **blank rule** (containing only the name and log settings).
- Once created, the rule ID is retrieved and assigned to the payload.
- The script then **updates the rule** with the extracted values.
- Policies are referenced using **policy ID mappings** (since FMC APIs require IDs instead of names).

> ⚠ **Important:** If a rule with the same name already exists, an **invalid key error** occurs. Exception handling will be included in future updates.

---

## Key Features
- **Automates Firewall Rule Implementation**: Eliminates the need for manual rule creation.
- **ServiceNow Integration**: Works with SNOW or other ticketing systems.
- **Efficient Rule Processing**: Reduces implementation time from **45 minutes (3 engineers)** to **less than 10 minutes (1 engineer)**.
- **Port Deduplication**: Prevents duplicate port object creation in FMC.
- **Safe & Reversible Changes**: Each rule is created as a new entity instead of modifying existing rules.

---

## Setup & Configuration
Before running the scripts, ensure the following variables are properly configured:

1. **FTD Policy ID Dictionary**: Populate the dictionary in `PUT_acp_new_rules.py` with policy names and corresponding IDs.
2. **FMC API Credentials**:
   - Add your **FMC IP**, **API key**, and **domain ID** in `generate_token.py`.
3. **Port Protocol Mapping**:
   - The `payload_generator.py` script contains a dictionary for protocol-to-port mappings.
4. **ServiceNow File Format**:
   - Ensure incoming request files follow the standard format (`CHG00001.txt`).

---

## Future Enhancements
🔹 Automate iteration through multiple rule files.
🔹 Enhance exception handling for duplicate rule names.
🔹 Implement rule merging instead of always creating new rules.

---

## Conclusion
This project aims to **streamline FTD rule implementations**, saving valuable time and effort. By replacing manual rule entry with an automated workflow, teams can focus on higher-priority security tasks while reducing errors and implementation delays.

If you have any questions or ideas for improvement, feel free to collaborate! 🚀

