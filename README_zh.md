# POP口袋眼科医生图像检测接口调用工具

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

### 1.1 关于POP口袋眼科医生

**POP口袋眼科医生**是基于人工智能技术训练具有一定先验知识的裂隙灯眼前节病灶检测模型，实现对眼前节裂隙灯图像中的常见病进行病灶识别，包含白内障、角膜病变、翼状胬肉、结膜下出血等16种常见眼病。

- 🌐 **官网链接**：https://pop.gzzoc.org.cn/
- 🎥 **视频展示**：

### 1.2 关于本项目

本项目是一个使用Python调用POP口袋眼科医生检测接口的轻量级工具库。通过简单的API调用，你可以上传图片并获取详细的检测结果，包括目标标签、置信度分数和边界框坐标等信息。

本项目特别适用于：

- 🏥 **医疗图像分析**：检测眼部疾病（白内障、翼状胬肉等）
- 🎯 **目标识别**：识别图片中的特定目标

---

## 2. Features

| 特性                   | 描述                               |
| ---------------------- | ---------------------------------- |
| 📸**图片上传**   | 支持上传图片文件进行检测           |
| 🔍**详细结果**   | 返回边界框、标签、置信度等完整信息 |
| 🛡️**错误处理** | 完善的异常处理和错误提示           |
| 🔄**交互式使用** | 支持循环输入多张图片进行检测       |

## 3. Installation

### 3.1 系统要求

- Python 3.7 或更高版本
- pip 包管理器

### 3.2 安装步骤

**步骤1：克隆项目**

```bash
git clone https://github.com/用户名/仓库名.git
cd 仓库名
```

**步骤2：安装依赖**

```bash
pip install -r requirements.txt
```

> 💡 **Note**: 如果使用Python 3，可能需要使用 `pip3` 命令。建议使用虚拟环境来管理依赖。

---

## 4. Quick Start

### 4.1 配置POP口袋眼科医生图像检测接口地址

**步骤1：创建配置文件**

```bash
# 复制配置模板
cp config.example.py config.py
```

**步骤2：编辑配置文件**

打开 `config.py` 文件，将 `API_URL` 替换为实际的POP口袋眼科医生图像检测接口地址：

```python
API_URL = "POP口袋眼科医生图像检测接口地址"
```

### 4.2 交互式使用

运行程序后，按提示输入图片路径即可：

```bash
python main.py
```

**使用示例：**

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

### 4.3 功能说明

- ✅ **交互式检测**：运行程序后，可以循环输入多张图片路径进行检测
- ✅ **格式化输出**：检测结果以清晰的格式显示在控制台
- ✅ **错误处理**：自动检查文件是否存在、格式是否支持

---

## 5. Project Structure

```
.
├── main.py                    # 主程序文件（包含交互式功能）
├── config.py                 # API配置文件（需自行创建）
├── config.example.py         # 配置文件模板
├── requirements.txt           # 依赖包列表
├── README.md                 # 项目说明文档（本文件）
```

### 文件说明

| 文件                  | 描述                                                      |
| --------------------- | --------------------------------------------------------- |
| `main.py`           | 核心代码文件，包含 `ImageDetectionAPI` 类和交互式主函数 |
| `config.py`         | API配置文件（需从 `config.example.py` 复制并配置）      |
| `config.example.py` | 配置文件模板                                              |
| `requirements.txt`  | Python依赖包列表                                          |
| `README.md`         | 项目说明文档                                              |

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

### 7.1 POP口袋眼科医生图像检测接口地址配置

POP口袋眼科医生图像检测接口地址已封装在配置文件中。

**配置步骤：**

1. 复制配置模板文件：

   ```bash
   cp config.example.py config.py
   ```
2. 编辑 `config.py` 文件，设置POP口袋眼科医生图像检测接口地址：

   ```python
   API_URL = "POP口袋眼科医生图像检测接口地址"
   ```

### 7.2 依赖包

| 包名         | 版本     | 用途             |
| ------------ | -------- | ---------------- |
| `requests` | >=2.31.0 | 用于发送HTTP请求 |

### 7.3 注意事项

> ⚠️ **Important Notes**:
>
> 1. 请确保POP口袋眼科医生图像检测接口地址正确
> 2. 确保图片文件路径有效
> 3. 网络连接正常

---

## 8. Contact

如有任何问题，请通过以下方式联系：

- 🐛 **Issues**: [GitHub Issues](https://github.com/你的用户名/仓库名/issues)
- 💬 **讨论**: 欢迎提交Issue和Pull Request！

---

## Acknowledgments

感谢所有为本项目做出贡献的开发者！

---

**⭐ 如果这个项目对你有帮助，请给个Star支持一下！**
