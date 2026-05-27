# 🎈 RansomerzerIT

A small Python project demonstrating how symmetric file encryption works using the `cryptography` library.

This repository contains:

- `pennywise.py` → Encrypts files in a selected folder
- `Richie.py` → Decrypts files after solving a riddle
- `requirements.txt` → Required Python dependencies

---

# 🚨 DISCLAIMER

> ## ⚠️ WARNING
>
> <span style="color:red"><strong>DO NOT RUN THIS ON IMPORTANT FILES, PERSONAL DATA, OR SYSTEM DIRECTORIES.</strong></span>
>
> <span style="color:orange"><strong>This script intentionally overwrites files with encrypted data.</strong></span>
>
> <span style="color:yellow"><strong>If the encryption key is lost, your files may become permanently inaccessible.</strong></span>
>
> This project is created strictly for:
>
> - Educational purposes
> - Encryption demonstrations
>
> Use only inside:
>
> - Test folders
> - Virtual machines
> - Controlled lab environments

---

# ⚖️ Consent & Responsibility

By using this project, you agree that:

- You will only run these scripts on files and systems you own or have explicit permission to test.
- You understand the risks associated with file encryption.
- You accept full responsibility for any misuse or damage caused by these scripts.

## The author is NOT responsible for:

- Unauthorized usage
- Illegal activities
- Data loss
- Damaged systems
- Misuse without consent

---

# 📂 Repository Structure

```bash
aftabrahamanapprentice1729-oss/
│
├── pennywise.py
├── Richie.py
├── requirements.txt
└── README.md
```

---

# 🔐 How `pennywise.py` Works

`pennywise.py` acts like a simplified local ransomware simulator.

## Features

### 1. File Discovery

The script scans the directory where it is executed and creates a list of files to encrypt.

It intentionally skips files such as:

- `pennywise.py`
- `thefear.key`
- `decrypt.py`
- `Richie.py`

---

### 2. Key Generation

The script uses `cryptography.fernet` to generate a symmetric encryption key.

The generated key is saved locally as:

```bash
thefear.key
```

---

### 3. Encryption Process

For every discovered file:

1. Original data is read
2. Data is encrypted using the Fernet key
3. The original file is overwritten with encrypted data

---

### 4. Notification

After encryption finishes, the script prints a ransom-style message in the terminal.

---

# 🎭 How `Richie.py` Works

`Richie.py` reverses the encryption process.

---

## Features

### 1. File Discovery

The script scans the current directory to locate encrypted files.

---

### 2. Key Retrieval

It loads the encryption key from:

```bash
thefear.key
```

---

### 3. The Riddle Challenge

Before decryption starts, the user must solve this riddle:

> “What word is spelled incorrectly in every single dictionary?”

---

### 4. Validation

- Any answer other than:

```bash
incorrectly
```

will stop the script immediately.

- Correct input unlocks the decryption process.

---

### 5. Decryption Process

For each encrypted file:

1. Encrypted data is read
2. Data is decrypted using the Fernet key
3. Original file contents are restored

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/aftabrahamanapprentice1729-oss/RansomerzerIT.git
cd aftabrahamanapprentice1729-oss
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage Instructions

## IMPORTANT

Place `pennywise.py` inside the folder whose files you want to encrypt.

Example:

```bash
TestFolder/
│
├── photo.png
├── notes.txt
├── project.pdf
└── pennywise.py
```

Then run:

```bash
python pennywise.py
```

---

## To Decrypt Files

Place `Richie.py` inside the same folder and run:

```bash
python Richie.py
```

Then answer the riddle correctly to restore the files.

---

# 📦 Requirements

Example `requirements.txt`:

```txt
cryptography
```

---

# 🛡️ Educational Purpose

This project demonstrates:

- Symmetric encryption
- Python file handling
- Directory traversal
- Cryptographic key management
- Basic ransomware behavior in controlled environments

- Ethical hacking labs
- Malware analysis beginners
- Encryption demonstrations
