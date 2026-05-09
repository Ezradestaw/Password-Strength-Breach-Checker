# Password Strength & Breach Checker

A modular cybersecurity-focused Python CLI tool that evaluates password strength, estimates entropy, checks simulated breach exposure, and generates secure passwords.

## Features

- **Password Strength Checker**
  - Scores passwords from **0–100** based on length and character diversity.
  - Detects weak/common patterns (e.g., `123456`, `password`, `qwerty`) and repeated/sequential characters.
  - Labels results as **Weak**, **Medium**, or **Strong**.

- **Entropy Calculator**
  - Computes estimated entropy in bits.
  - Provides a plain-language explanation of security level.

- **Breach Checker (Simulated Local Dataset)**
  - Checks passwords against a local compromised-password hash set.
  - Returns:
    - `Password found in leaked database`
    - `Password not found in known breaches`

- **Secure Password Generator**
  - Configurable length, numbers, and symbols.
  - Uses Python's `secrets` module for cryptographically strong randomness.
  - Enforces strong defaults and complexity requirements.

- **Cybersecurity CLI Experience**
  - ASCII startup banner.
  - Colored output using `colorama`.
  - Menu-based workflow with input validation.

- **Logging**
  - Saves timestamped checks in `logs.txt` with score and breach status.

## Project Structure

- `main.py` — entry point and CLI menu
- `password_strength.py` — password scoring + label logic
- `breach_checker.py` — simulated breach detection
- `generator.py` — secure password generation
- `utils.py` — entropy and logging helpers

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the tool:
   ```bash
   python main.py
   ```

## Notes

- This project uses a **simulated local breach dataset** and does not require an API key.
- Do not store real sensitive passwords in plaintext logs in production systems.
