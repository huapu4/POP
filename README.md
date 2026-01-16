# Pocket Ophthalmologist (POP) Image Detection API Tool

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com)
<img width="4096" height="686" alt="ZOC_logo_" src="https://github.com/user-attachments/assets/d49d2dd2-5a83-4ba7-8678-7e74a580167a" />


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

Please enter image path to detect (enter 'q' or 'quit' to exit): E:\DATA\WJR\ZOC\POP_Github\pop-github\pop-github\test1.jpg

Detecting image: test1.jpg
------------------------------------------------------------

==================================================
Detection Results
==================================================

Detected 4 target(s):

Target 1:
  Label: Eye
  Confidence: 0.9491528
  Position: left=1, top=52, right=2736, bottom=1800

Target 2:
  Label: Subconjunctival hemorrhage
  Confidence: 0.8100369
  Position: left=794, top=1211, right=2039, bottom=1676

Target 3:
  Label: Subconjunctival hemorrhage
  Confidence: 0.79700476
  Position: left=2045, top=986, right=2691, bottom=1447

Target 4:
  Label: Subconjunctival hemorrhage
  Confidence: 0.68216246
  Position: left=276, top=548, right=745, bottom=1378

==================================================

✓ Annotated image saved to: E:\DATA\WJR\ZOC\POP_Github\POP\output\test1_annotated_20260116_171747.jpg


Please enter image path to detect (enter 'q' or 'quit' to exit): E:\DATA\WJR\ZOC\POP_Github\pop-github\pop-github\test2.jpg 

Detecting image: test2.jpg
------------------------------------------------------------

==================================================
Detection Results
==================================================

Detected 3 target(s):

Target 1:
  Label: Eye
  Confidence: 0.9156853
  Position: left=539, top=128, right=2732, bottom=1641

Target 2:
  Label: Hypopyon
  Confidence: 0.7548054
  Position: left=1201, top=1210, right=1655, bottom=1298

Target 3:
  Label: Infectious keratopathy
  Confidence: 0.53000605
  Position: left=1133, top=708, right=1521, bottom=1081

==================================================

✓ Annotated image saved to: E:\DATA\WJR\ZOC\POP_Github\POP\output\test2_annotated_20260116_171755.jpg


Please enter image path to detect (enter 'q' or 'quit' to exit): E:\DATA\WJR\ZOC\POP_Github\pop-github\pop-github\test3.jpg 

Detecting image: test3.jpg
------------------------------------------------------------

==================================================
Detection Results
==================================================

Detected 2 target(s):

Target 1:
  Label: Eye
  Confidence: 0.8009599
  Position: left=296, top=344, right=2519, bottom=1496

Target 2:
  Label: Subconjunctival hemorrhage
  Confidence: 0.7548635
  Position: left=607, top=714, right=824, bottom=1150

==================================================

✓ Annotated image saved to: E:\DATA\WJR\ZOC\POP_Github\POP\output\test3_annotated_20260116_171803.jpg


Please enter image path to detect (enter 'q' or 'quit' to exit): E:\DATA\WJR\ZOC\POP_Github\pop-github\pop-github\test4.jpg 

Detecting image: test4.jpg
------------------------------------------------------------

==================================================
Detection Results
==================================================

Detected 2 target(s):

Target 1:
  Label: Eye
  Confidence: 0.95196635
  Position: left=25, top=284, right=3837, bottom=2835

Target 2:
  Label: Cataract
  Confidence: 0.90806913
  Position: left=1712, top=1436, right=2232, bottom=1945

==================================================

✓ Annotated image saved to: E:\DATA\WJR\ZOC\POP_Github\POP\output\test4_annotated_20260116_171811.jpg


Please enter image path to detect (enter 'q' or 'quit' to exit): E:\DATA\WJR\ZOC\POP_Github\pop-github\pop-github\test5.jpg 

Detecting image: test5.jpg
------------------------------------------------------------

==================================================
Detection Results
==================================================

Detected 2 target(s):

Target 1:
  Label: Eye
  Confidence: 0.92827266
  Position: left=-6, top=266, right=2552, bottom=1453

Target 2:
  Label: Entropion
  Confidence: 0.74804825
  Position: left=211, top=900, right=2428, bottom=1462

==================================================

✓ Annotated image saved to: E:\DATA\WJR\ZOC\POP_Github\POP\output\test5_annotated_20260116_171815.jpg


Please enter image path to detect (enter 'q' or 'quit' to exit): E:\DATA\WJR\ZOC\POP_Github\pop-github\pop-github\test6.jpg 

Detecting image: test6.jpg
------------------------------------------------------------

==================================================
Detection Results
==================================================

Detected 2 target(s):

Target 1:
  Label: Eye
  Confidence: 0.9301589
  Position: left=104, top=239, right=1267, bottom=714

Target 2:
  Label: Conjunctivitis
  Confidence: 0.8921671
  Position: left=307, top=313, right=889, bottom=635

==================================================

✓ Annotated image saved to: E:\DATA\WJR\ZOC\POP_Github\POP\output\test6_annotated_20260116_171820.jpg


Please enter image path to detect (enter 'q' or 'quit' to exit): E:\DATA\WJR\ZOC\POP_Github\pop-github\pop-github\test7.jpg 

Detecting image: test7.jpg
------------------------------------------------------------

==================================================
Detection Results
==================================================

Detected 3 target(s):

Target 1:
  Label: Eye
  Confidence: 0.92795515
  Position: left=20, top=201, right=1278, bottom=842

Target 2:
  Label: Conjunctivitis
  Confidence: 0.78334343
  Position: left=974, top=550, right=1276, bottom=744

Target 3:
  Label: Stye
  Confidence: 0.8232242
  Position: left=306, top=258, right=624, bottom=411

==================================================

✓ Annotated image saved to: E:\DATA\WJR\ZOC\POP_Github\POP\output\test7_annotated_20260116_171824.jpg


Please enter image path to detect (enter 'q' or 'quit' to exit): E:\DATA\WJR\ZOC\POP_Github\pop-github\pop-github\test8.jpg 

Detecting image: test8.jpg
------------------------------------------------------------

==================================================
Detection Results
==================================================

Detected 3 target(s):

Target 1:
  Label: Eye
  Confidence: 0.9049707
  Position: left=4, top=23, right=4008, bottom=2776

Target 2:
  Label: Cataract
  Confidence: 0.90168506
  Position: left=821, top=691, right=2515, bottom=2366

Target 3:
  Label: Pterygium
  Confidence: 0.74473095
  Position: left=2050, top=1103, right=3758, bottom=2595

==================================================

✓ Annotated image saved to: E:\DATA\WJR\ZOC\POP_Github\POP\output\test8_annotated_20260116_171833.jpg


Please enter image path to detect (enter 'q' or 'quit' to exit): q

Thank you for using, goodbye!



```
![test1_2](https://github.com/user-attachments/assets/14f5c80a-9dbe-49e7-b966-d468c248e0b9)

![test3_4](https://github.com/user-attachments/assets/9a44f755-f288-4d79-a563-21d87b0ca529)

![test5_6](https://github.com/user-attachments/assets/745430c3-6f27-40a0-9266-04a7009086d4)

![test7_8](https://github.com/user-attachments/assets/cef1fe39-8c9b-4482-adb6-8f9e7e253efe)


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
