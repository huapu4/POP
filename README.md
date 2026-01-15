# Pocket Ophthalmologist (POP) Image Detection API Tool

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com)
<img width="1795" height="406" alt="中山眼科中心" src="https://github.com/user-attachments/assets/c93d1b5a-805e-4399-b52c-41ac44005be8" />

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


https://github.com/user-attachments/assets/378fd48f-a712-4008-ba3d-144f7476dc01


### 1.2 About This Project

This project is a lightweight Python library for calling the Pocket Ophthalmologist (POP) detection API. Through simple API calls, you can upload images and obtain detailed detection results, including target labels, confidence scores, bounding box coordinates, and more.

This project is particularly suitable for:

- 🏥 **Medical Image Analysis**: Detection of eye diseases (cataracts, pterygium, etc.)
- 🎯 **Target Recognition**: Identify specific targets in images

---

## 2. Features

| Feature                        | Description                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------ |
| 📸**Image Upload**       | Support uploading image files for detection                                          |
| 🔍**Detailed Results**   | Returns complete information including bounding boxes, labels, and confidence scores |
| 🖼️**Image Annotation** | Automatically annotates detected targets on images with bounding boxes and labels    |
| 🛡️**Error Handling**   | Comprehensive exception handling and error prompts                                   |
| 🔄**Interactive Use**    | Support cyclic input of multiple images for detection                                |

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

### 4.1 Interactive Usage

After running the program, enter the image path as prompted:

```bash
python run.py
```

**Usage Example:**

```
============================================================
Pocket Ophthalmologist (POP) Tool
============================================================

Please enter image path to detect (enter 'q' or 'quit' to exit): test.jpg

Detecting image: test.jpg
------------------------------------------------------------

==================================================
Detection Results
==================================================

Detected 3 target(s):

Target 1:
  Label: Eye
  Confidence: 0.9468135
  Position: left=12, top=11, right=1277, bottom=729

Target 2:
  Label: Cataract
  Confidence: 0.82525355
  Position: left=719, top=296, right=829, bottom=413

Target 3:
  Label: Pterygium
  Confidence: 0.79924196
  Position: left=167, top=284, right=642, bottom=639

==================================================

✓ Annotated image saved to: output/test_annotated_20260114_123456.jpg

Please enter image path to detect (enter 'q' or 'quit' to exit): q

Thank you for using, goodbye!

```
![test_annotated](https://github.com/user-attachments/assets/d4dd6b26-4c76-4391-abfe-db688e4fe7f7)

### 4.2 Feature Description

- ✅ **Interactive Detection**: After running the program, you can cyclically input multiple image paths for detection
- ✅ **Formatted Output**: Detection results are displayed in English with clear format on the console
- ✅ **Image Annotation**: Automatically annotates detected targets on images with bounding boxes and labels, saves to `output/` folder
- ✅ **Label Translation**: Chinese labels are automatically translated to English in console output
- ✅ **Error Handling**: Automatically checks if files exist and if formats are supported

---

## 5. Project Structure

```
.
├── run.py                    # Entry point (run this file to start the application)
├── src/                      # Source code directory
│   └── main.py              # Main program file 
├── config/                   # Configuration directory
│   └── config.py            # API configuration file 
├── utils/                    # Utility modules directory
│   ├── api_client.py        # API client module
│   ├── label_mapping.py     # Chinese-English label mapping
│   ├── image_annotator.py   # Image annotation module
│   ├── font_manager.py      # Font management module
│   └── fonts/               # Font files directory
│       └── simhei.ttf       # SimHei font file for Chinese text rendering
├── output/                   # Output directory (annotated images are saved here)
├── requirements.txt          # Dependency package list
└── README.md                # Project documentation 
```

### File Description

| File/Directory               | Description                                                       |
| ---------------------------- | ----------------------------------------------------------------- |
| `run.py`                   | Entry point file, run this to start the application               |
| `src/main.py`              | Core code file, contains main function and image processing logic |
| `config/config.py`         | API configuration file                                           |
| `utils/api_client.py`      | API client module for making detection requests                   |
| `utils/label_mapping.py`   | Chinese-English label mapping dictionary                          |
| `utils/image_annotator.py` | Image annotation module for drawing bounding boxes and labels     |
| `utils/font_manager.py`    | Font management module for loading Chinese fonts                  |
| `utils/fonts/simhei.ttf`   | SimHei font file for rendering Chinese text on images             |
| `output/`                  | Directory where annotated images are saved                        |
| `requirements.txt`         | Python dependency package list                                    |
| `README.md`                | Project documentation                                             |

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

### 7.1 Dependencies

| Package Name | Version  | Purpose                             |
| ------------ | -------- | ----------------------------------- |
| `requests` | >=2.31.0 | For sending HTTP requests           |
| `Pillow`   | >=10.0.0 | For image processing and annotation |

### 7.2 Important Notes

> ⚠️ **Important Notes**:
>
> 1. Ensure the image file path is valid
> 2. Network connection is normal

---

## 8. Contact

If you have any questions, please contact us through the following methods:

- 🐛 **Issues**: [GitHub Issues](https://github.com/huapu4/POP/issues)
- 💬 **Discussion**: Welcome to submit Issues and Pull Requests!

---

## Acknowledgments

Thanks to all developers who have contributed to this project!

---

**⭐ If this project is helpful to you, please give it a Star!**
