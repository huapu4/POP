"""
Pocket Ophthalmologist (POP) Tool
A Python tool for calling Pocket Ophthalmologist (POP) API,
uploading images and getting detection results
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.api_client import ImageDetectionAPI
from utils.label_mapping import get_english_label
from utils.image_annotator import ImageAnnotator
from typing import Optional


def print_detections(result: dict):
    """
    Format and print detection results in English
    
    Args:
        result: API returned detection result
    """
    if not result:
        print("No detection results")
        return
    
    print("\n" + "="*50)
    print("Detection Results")
    print("="*50)
    
    if 'detections' in result:
        detections = result['detections']
        print(f"\nDetected {len(detections)} target(s):\n")
        
        for i, detection in enumerate(detections, 1):
            chinese_label = detection.get('label', 'N/A')
            english_label = get_english_label(chinese_label)
            score = detection.get('score', 'N/A')
            
            print(f"Target {i}:")
            print(f"  Label: {english_label}")
            print(f"  Confidence: {score}")
            print(f"  Position: left={detection.get('left')}, top={detection.get('top')}, "
                  f"right={detection.get('right')}, bottom={detection.get('bottom')}")
            print()
    
    print("="*50 + "\n")


def save_annotated_image(image_path: str, result: dict, output_dir: str = "output") -> Optional[str]:
    """
    Save annotated image to output directory
    
    Args:
        image_path: Path to original image
        result: Detection result dictionary
        output_dir: Output directory path
        
    Returns:
        Path to saved annotated image, or None if failed
    """
    if not result or 'detections' not in result:
        return None
    
    detections = result['detections']
    if not detections:
        return None
    
    try:
        # Create output directory (relative to project root)
        project_root = Path(__file__).parent.parent
        output_path = project_root / output_dir
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Generate output filename
        original_path = Path(image_path)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{original_path.stem}_annotated_{timestamp}{original_path.suffix}"
        output_file = output_path / output_filename
        
        # Annotate image
        annotator = ImageAnnotator(font_size=20)
        success = annotator.annotate_image(
            image_path=str(image_path),
            detections=detections,
            output_path=str(output_file)
        )
        
        if success:
            return str(output_file)
        else:
            return None
            
    except Exception as e:
        print(f"Error saving annotated image: {e}")
        return None


def main():
    """Interactive main function"""
    # Add config directory to path
    project_root = Path(__file__).parent.parent
    config_path = project_root / "config"
    sys.path.insert(0, str(config_path))
    
    try:
        from config import API_URL
        # Check if API URL is configured
        if not API_URL or API_URL == "POP口袋眼科医生图像检测接口地址":
            print("❌ Error: Please configure API endpoint address in config/config.py file")
            print("\nConfiguration steps:")
            print("1. Copy config template: cp config/config.example.py config/config.py")
            print("2. Edit config/config.py, replace API_URL with actual API endpoint address")
            sys.exit(1)
    except ImportError:
        print("❌ Error: config/config.py configuration file not found")
        print("\nPlease follow these steps to create configuration file:")
        print("1. Copy config template: cp config/config.example.py config/config.py")
        print("2. Edit config/config.py, replace API_URL with actual API endpoint address")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: Failed to read configuration file: {e}")
        sys.exit(1)
    
    api_client = ImageDetectionAPI(API_URL)
    
    print("="*60)
    print("Pocket Ophthalmologist (POP) Tool")
    print("="*60)
    print()
    
    while True:
        try:
            # Prompt user for image path
            image_path = input("Please enter image path to detect (enter 'q' or 'quit' to exit): ").strip()
            
            # Check if exit
            if image_path.lower() in ['q', 'quit', 'exit']:
                print("\nThank you for using, goodbye!")
                break
            
            # Check if input is empty
            if not image_path:
                print("⚠️  Image path cannot be empty, please re-enter\n")
                continue
            
            # Remove possible quotes
            image_path = image_path.strip('"').strip("'")
            
            # Check if file exists
            if not os.path.exists(image_path):
                print(f"⚠️  File does not exist: {image_path}\n")
                continue
            
            # Check if it's an image file
            valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
            file_ext = os.path.splitext(image_path)[1].lower()
            if file_ext not in valid_extensions:
                print(f"⚠️  Unsupported image format: {file_ext}")
                print(f"Supported formats: {', '.join(valid_extensions)}\n")
                continue
            
            print(f"\nDetecting image: {os.path.basename(image_path)}")
            print("-" * 60)
            
            # Detect image
            result = api_client.detect_image(image_path)
            
            # Process results
            if result:
                # Print detection results in English
                print_detections(result)
                
                # Save annotated image
                annotated_path = save_annotated_image(image_path, result)
                if annotated_path:
                    print(f"✓ Annotated image saved to: {annotated_path}\n")
                else:
                    print("⚠️  Failed to save annotated image\n")
            else:
                print("❌ Detection failed, please check network connection and API configuration")
                print("Hint: Please confirm API_URL in config/config.py is configured correctly\n")
            
            print()
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user, goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error occurred: {e}\n")


if __name__ == "__main__":
    main()
