"""
API client for POP image detection
"""

import requests
import json
from typing import Dict, Optional
from pathlib import Path


class ImageDetectionAPI:
    """Pocket Ophthalmologist (POP) API Client"""
    
    def __init__(self, api_url: str):
        """
        Initialize API client
        
        Args:
            api_url: API endpoint URL
        """
        self.api_url = api_url
    
    def detect_image(self, image_path: str) -> Optional[Dict]:
        """
        Upload image and get detection results
        
        Args:
            image_path: Path to image file
            
        Returns:
            Detection result dictionary containing detections and resImage fields
            Returns None if request fails
        """
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
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
            print(f"Request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Error details: {e.response.text}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON parsing failed: {e}")
            if 'response' in locals():
                print(f"Response content: {response.text}")
            return None
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
