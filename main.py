"""
POP口袋眼科医生图像检测接口调用工具
使用Python调用POP口袋眼科医生图像检测接口，上传图片并获取检测结果
"""

import requests
import json
from typing import Dict, List, Optional
from pathlib import Path


class ImageDetectionAPI:
    """POP口袋眼科医生图像检测接口客户端"""
    
    def __init__(self, api_url: str):

        self.api_url = api_url
    
    def detect_image(self, image_path: str) -> Optional[Dict]:
        """
        上传图片并获取检测结果
        
        Args:
            image_path: 图片文件路径
            
        Returns:
            检测结果字典，包含detections和resImage字段
            如果请求失败，返回None
        """

        if not Path(image_path).exists():
            raise FileNotFoundError(f"图片文件不存在: {image_path}")
        
        try:

            with open(image_path, 'rb') as image_file:
                files = {
                    'file': (Path(image_path).name, image_file, 'image/jpeg')
                }
                
                response = requests.post(
                    self.api_url,
                    files=files,
                    timeout=30
                )
                
                
                response.raise_for_status()
                

                result = response.json()
                return result
                
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            if hasattr(e.response, 'text'):
                print(f"错误详情: {e.response.text}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON解析失败: {e}")
            print(f"响应内容: {response.text}")
            return None
        except Exception as e:
            print(f"发生错误: {e}")
            return None
    
    def print_detections(self, result: Dict):
        """
        格式化打印检测结果
        
        Args:
            result: API返回的检测结果
        """
        if not result:
            print("没有检测结果")
            return
        
        print("\n" + "="*50)
        print("检测结果")
        print("="*50)
        
        if 'detections' in result:
            detections = result['detections']
            print(f"\n检测到 {len(detections)} 个目标:\n")
            
            for i, detection in enumerate(detections, 1):
                print(f"目标 {i}:")
                print(f"  标签: {detection.get('label', 'N/A')}")
                print(f"  置信度: {detection.get('score', 'N/A')}")
                print(f"  位置: left={detection.get('left')}, top={detection.get('top')}, "
                      f"right={detection.get('right')}, bottom={detection.get('bottom')}")
                print()
        
        print("="*50 + "\n")


def main():
    """交互式主函数"""
    import os
    import sys
    
    try:
        from config import API_URL
        # 检查API地址是否已配置
        if not API_URL:
            print("❌ 错误: 请在 config.py 文件中配置API接口地址")
            print("\n配置步骤:")
            print("1. 复制配置模板: cp config.example.py config.py")
            print("2. 编辑 config.py，将 API_URL 替换为实际的API接口地址")
            sys.exit(1)
    except ImportError:
        print("❌ 错误: 找不到 config.py 配置文件")
        print("\n请按以下步骤创建配置文件:")
        print("1. 复制配置模板: cp config.example.py config.py")
        print("2. 编辑 config.py，将 API_URL 替换为实际的API接口地址")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 错误: 读取配置文件失败: {e}")
        sys.exit(1)
    
    api_client = ImageDetectionAPI(API_URL)
    
    print("="*60)
    print("POP口袋眼科医生图像检测工具")
    print("="*60)
    print()
    
    while True:
        try:
            # 提示用户输入图片路径
            image_path = input("请输入要检测的图片路径（输入 'q' 或 'quit' 退出）: ").strip()
            
            # 检查是否退出
            if image_path.lower() in ['q', 'quit', 'exit']:
                print("\n感谢使用，再见！")
                break
            
            # 检查输入是否为空
            if not image_path:
                print("⚠️  图片路径不能为空，请重新输入\n")
                continue
            
            # 移除可能的引号
            image_path = image_path.strip('"').strip("'")
            
            # 检查文件是否存在
            if not os.path.exists(image_path):
                print(f"⚠️  文件不存在: {image_path}\n")
                continue
            
            # 检查是否为图片文件
            valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
            file_ext = os.path.splitext(image_path)[1].lower()
            if file_ext not in valid_extensions:
                print(f"⚠️  不支持的图片格式: {file_ext}")
                print(f"支持的格式: {', '.join(valid_extensions)}\n")
                continue
            
            print(f"\n正在检测图片: {os.path.basename(image_path)}")
            print("-" * 60)
            
            # 检测图片
            result = api_client.detect_image(image_path)
            
            # 处理结果
            if result:
                api_client.print_detections(result)
            else:
                print("❌ 检测失败，请检查网络连接和API配置")
                print("提示: 请确认 config.py 中的 API_URL 配置正确\n")
            
            print()  
            
        except KeyboardInterrupt:
            print("\n\n程序被用户中断，再见！")
            break
        except Exception as e:
            print(f"\n❌ 发生错误: {e}\n")


if __name__ == "__main__":
    main()
