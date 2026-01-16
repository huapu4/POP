# POP口袋眼科医生图像检测接口调用工具

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com)
<img width="4096" height="686" alt="ZOC_logo_" src="https://github.com/user-attachments/assets/9f99255a-328f-4187-9450-a826390e1d13" />

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

### 1.1 关于POP口袋眼科医生

**POP口袋眼科医生**是基于人工智能技术训练具有一定先验知识的裂隙灯眼前节病灶检测模型，实现对眼前节裂隙灯图像中的常见病进行病灶识别，包含白内障、角膜病变、翼状胬肉、结膜下出血等16种常见眼病。

- 🌐 **官网链接**：https://pop.gzzoc.org.cn/
- 🎥 **视频展示**：


https://github.com/user-attachments/assets/c6228443-aec1-430b-b3ab-491142edbf2a


### 1.2 关于本项目

本项目是一个使用Python调用POP口袋眼科医生检测接口的轻量级工具库。通过简单的API调用，你可以上传图片并获取详细的检测结果，包括目标标签、置信度分数和边界框坐标等信息。

本项目特别适用于：

- 🏥 **医疗图像分析**：检测眼部疾病（白内障、翼状胬肉等）
- 🎯 **目标识别**：识别图片中的特定目标

---

## 2. Features

| 特性                   | 描述                                       |
| ---------------------- | ------------------------------------------ |
| 📸**图片上传**   | 支持上传图片文件进行检测                   |
| 🔍**详细结果**   | 返回边界框、标签、置信度等完整信息         |
| 🖼️**图片标注** | 自动在图片上标注检测目标，包括边界框和标签 |
| 🛡️**错误处理** | 完善的异常处理和错误提示                   |
| 🔄**交互式使用** | 支持循环输入多张图片进行检测               |

## 3. Installation

### 3.1 系统要求

- Python 3.7 或更高版本
- pip 包管理器

### 3.2 安装步骤

**步骤1：克隆项目**

```bash
git clone https://github.com/huapu4/POP.git
cd POP
```

**步骤2：安装依赖**

```bash
pip install -r requirements.txt
```

> 💡 **Note**: 如果使用Python 3，可能需要使用 `pip3` 命令。建议使用虚拟环境来管理依赖。

---

## 4. Quick Start

### 4.1 交互式使用

运行程序后，按提示输入图片路径即可：

```bash
python run.py
```

**使用示例：**

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
![test1_2](https://github.com/user-attachments/assets/d02ed245-bb42-4c19-b5c2-39427067a09a)

![test3_4](https://github.com/user-attachments/assets/a179e487-671b-4782-927e-4e3c75975e3d)

![test5_6](https://github.com/user-attachments/assets/baa96be3-c8f1-4e02-8633-dfad3bd653fb)

![test7_8](https://github.com/user-attachments/assets/02e22663-8261-4767-baae-5c456f43e57f)


### 4.2 功能说明

- ✅ **交互式检测**：运行程序后，可以循环输入多张图片路径进行检测
- ✅ **格式化输出**：检测结果以英文格式清晰显示在控制台
- ✅ **图片标注**：自动在图片上标注检测到的目标，包括边界框和标签，保存到 `output/` 文件夹
- ✅ **标签翻译**：控制台输出自动将中文标签翻译为英文
- ✅ **错误处理**：自动检查文件是否存在、格式是否支持

---

## 5. Project Structure

```
.
├── run.py                    # 程序入口文件（运行此文件启动程序）
├── src/                      # 源代码目录
│   └── main.py              # 主程序文件
├── config/                   # 配置目录
│   └── config.py            # API配置文件
├── utils/                    # 工具模块目录
│   ├── api_client.py        # API客户端模块
│   ├── label_mapping.py     # 中英文标签映射
│   ├── image_annotator.py   # 图片标注模块
│   ├── font_manager.py      # 字体管理模块
│   └── fonts/               # 字体文件目录
│       └── simhei.ttf       # 黑体字体文件
├── output/                   # 输出目录（标注后的图片保存在此）
├── requirements.txt          # 依赖包列表
└── README.md                # 项目说明文档
```

### 文件说明

| 文件/目录                    | 描述                                       |
| ---------------------------- | ------------------------------------------ |
| `run.py`                   | 程序入口文件，运行此文件启动程序           |
| `src/main.py`              | 核心代码文件，包含主函数和图片处理逻辑     |
| `config/config.py`         | API配置文件                                |
| `utils/api_client.py`      | API客户端模块，用于发送检测请求            |
| `utils/label_mapping.py`   | 中英文标签映射字典                         |
| `utils/image_annotator.py` | 图片标注模块，用于在图片上绘制边界框和标签 |
| `utils/font_manager.py`    | 字体管理模块，用于加载中文字体             |
| `utils/fonts/simhei.ttf`   | 黑体字体文件，用于在图片上渲染中文文字     |
| `output/`                  | 输出目录，标注后的图片保存在此             |
| `requirements.txt`         | Python依赖包列表                           |
| `README.md`                | 项目说明文档                               |

---

## 6. Error Handling

程序包含完善的错误处理机制：

| 错误类型     | 处理方式                                      |
| ------------ | --------------------------------------------- |
| 文件不存在   | 抛出 `FileNotFoundError` 异常，提示文件路径 |
| 网络请求异常 | 捕获并打印详细错误信息，返回 `None`         |
| JSON解析错误 | 捕获并打印响应内容，便于调试                  |
| 其他异常     | 统一异常处理，确保程序稳定运行                |

### 错误示例

**文件不存在：**

```
FileNotFoundError: 图片文件不存在: wrong_path.jpg
```

**网络错误：**

```
请求失败: Connection timeout
错误详情: [错误详情信息]
```

**API错误：**

```
请求失败: 400 Bad Request
错误详情: [API返回的错误信息]
```

---

## 7. Configuration

### 7.1 依赖包

| 包名         | 版本     | 用途               |
| ------------ | -------- | ------------------ |
| `requests` | >=2.31.0 | 用于发送HTTP请求   |
| `Pillow`   | >=10.0.0 | 用于图片处理和标注 |

### 7.2 注意事项

> ⚠️ **Important Notes**:
>
> 1. 确保图片文件路径有效
> 3. 网络连接正常

---

## 8. Contact

如有任何问题，请通过以下方式联系：

- 🐛 **Issues**: [GitHub Issues](https://github.com/huapu4/POP/issues)
- 💬 **讨论**: 欢迎提交Issue和Pull Request！

---

## Acknowledgments

感谢所有为本项目做出贡献的开发者！

---

**⭐ 如果这个项目对你有帮助，请给个Star支持一下！**



