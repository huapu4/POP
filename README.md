# Pocket Ophthalmologist (POP) Image Detection API Tool

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com)

**Homepage** | **GitHub** | **Documentation**

---

## 👁️ Table of Contents

1. [Introduction](#1-introduction)
2. [Features](#2-features)
3. [Installation](#3-installation)
4. [Quick Start](#4-quick-start)
5. [Project Structure](#5-project-structure)
6. [Error Handling](#6-error-handling)
7. [Configuration](#7-configuration)
8. [Contact](#8-contact)

---

## 1. Introduction

### 1.1 About Pocket Ophthalmologist (POP)

**Pocket Ophthalmologist (POP)** is an AI-powered anterior segment lesion detection model trained with prior knowledge for slit-lamp images. It enables lesion identification of common eye diseases in anterior segment slit-lamp images, including 16 common eye diseases such as cataracts, corneal lesions, pterygium, subconjunctival hemorrhage, and more.

- 🌐 **Official Website**: https://pop.gzzoc.org.cn/
- 🎥 **Video Demo**:

https://github.com/user-attachments/assets/bf3ab7a0-c3e7-4f7f-ad94-f38645a913c3



### 1.2 About This Project

This project is a lightweight Python library for calling the Pocket Ophthalmologist (POP) detection API. Through simple API calls, you can upload images and obtain detailed detection results, including target labels, confidence scores, bounding box coordinates, and more.

This project is particularly suitable for:

- 🏥 **Medical Image Analysis**: Detection of eye diseases (cataracts, pterygium, etc.)
- 🎯 **Target Recognition**: Identify specific targets in images

---

## 2. Features

| Feature                      | Description                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------ |
| 📸**Image Upload**     | Support uploading image files for detection                                          |
| 🔍**Detailed Results** | Returns complete information including bounding boxes, labels, and confidence scores |
| 🛡️**Error Handling** | Comprehensive exception handling and error prompts                                   |
| 🔄**Interactive Use**  | Support cyclic input of multiple images for detection                                |

## 3. Installation

### 3.1 System Requirements

- Python 3.7 or higher
- pip package manager

### 3.2 Installation Steps

**Step 1: Clone the repository**

```bash
git clone https://github.com/huapu4/POP.git
cd POP
```

**Step 2: Install dependencies**

```bash
pip install -r requirements.txt
```

> 💡 **Note**: If using Python 3, you may need to use the `pip3` command. It is recommended to use a virtual environment to manage dependencies.

---

## 4. Quick Start

### 4.1 Configure Pocket Ophthalmologist (POP) Image Detection API Address

**Step 1: Create configuration file**

```bash
# Copy configuration template
cp config.example.py config.py
```

**Step 2: Edit configuration file**

Open the `config.py` file and replace `API_URL` with the actual Pocket Ophthalmologist (POP) image detection API address:

```python
API_URL = "Pocket Ophthalmologist (POP) Image Detection API Address"
```

### 4.2 Interactive Usage

After running the program, enter the image path as prompted:

```bash
python main.py
```

**Usage Example:**

```
============================================================
POP口袋眼科医生图像检测工具
============================================================

请输入要检测的图片路径（输入 'q' 或 'quit' 退出）: test.jpg

正在检测图片: test.jpg
------------------------------------------------------------

==================================================
检测结果
==================================================

检测到 3 个目标:

目标 1:
  标签: 目标眼
  置信度: 0.9468135
  位置: left=12, top=11, right=1277, bottom=729

目标 2:
  标签: 白内障
  置信度: 0.82525355
  位置: left=719, top=296, right=829, bottom=413

目标 3:
  标签: 翼状胬肉
  置信度: 0.79924196
  位置: left=167, top=284, right=642, bottom=639

==================================================

请输入要检测的图片路径（输入 'q' 或 'quit' 退出）: q

感谢使用，再见！

```

### 4.3 Feature Description

- ✅ **Interactive Detection**: After running the program, you can cyclically input multiple image paths for detection
- ✅ **Formatted Output**: Detection results are displayed in a clear format on the console
- ✅ **Error Handling**: Automatically checks if files exist and if formats are supported

---

## 5. Project Structure

```
.
├── main.py                    # Main program file (includes interactive functionality)
├── config.py                 # API configuration file (needs to be created)
├── config.example.py         # Configuration file template
├── requirements.txt           # Dependency package list
├── README.md                 # Project documentation (this file)
```

### File Description

| File                  | Description                                                                           |
| --------------------- | ------------------------------------------------------------------------------------- |
| `main.py`           | Core code file, contains `ImageDetectionAPI` class and interactive main function    |
| `config.py`         | API configuration file (needs to be copied from `config.example.py` and configured) |
| `config.example.py` | Configuration file template                                                           |
| `requirements.txt`  | Python dependency package list                                                        |
| `README.md`         | Project documentation                                                                 |

---

## 6. Error Handling

The program includes comprehensive error handling mechanisms:

| Error Type            | Handling Method                                                 |
| --------------------- | --------------------------------------------------------------- |
| File Not Found        | Raises `FileNotFoundError` exception, prompts file path       |
| Network Request Error | Catches and prints detailed error information, returns `None` |
| JSON Parse Error      | Catches and prints response content for debugging               |
| Other Exceptions      | Unified exception handling to ensure stable program operation   |

### Error Examples

**File Not Found:**

```
FileNotFoundError: Image file does not exist: wrong_path.jpg
```

**Network Error:**

```
Request failed: Connection timeout
Error details: [Error detail information]
```

**API Error:**

```
Request failed: 400 Bad Request
Error details: [API returned error information]
```

---

## 7. Configuration

### 7.1 Pocket Ophthalmologist (POP) Image Detection API Address Configuration

The Pocket Ophthalmologist (POP) image detection API address is encapsulated in the configuration file.

**Configuration Steps:**

1. Copy the configuration template file:

   ```bash
   cp config.example.py config.py
   ```
2. Edit the `config.py` file and set the Pocket Ophthalmologist (POP) image detection API address:

   ```python
   API_URL = "Pocket Ophthalmologist (POP) Image Detection API Address"
   ```

### 7.2 Dependencies

| Package Name | Version  | Purpose                   |
| ------------ | -------- | ------------------------- |
| `requests` | >=2.31.0 | For sending HTTP requests |

### 7.3 Important Notes

> ⚠️ **Important Notes**:
>
> 1. Please ensure the Pocket Ophthalmologist (POP) image detection API address is correct
> 2. Ensure the image file path is valid
> 3. Network connection is normal

---

## 8. Contact

If you have any questions, please contact us through the following methods:

- 🐛 **Issues**: [GitHub Issues](https://github.com/your-username/repository-name/issues)
- 💬 **Discussion**: Welcome to submit Issues and Pull Requests!

---

## Acknowledgments

Thanks to all developers who have contributed to this project!

---

**⭐ If this project is helpful to you, please give it a Star!**
