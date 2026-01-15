"""
Image annotation module for drawing detection results on images
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from typing import Dict, List, Optional
import os

from .font_manager import get_font_path
from .label_mapping import get_english_label


class ImageAnnotator:
    """Class for annotating images with detection results"""
    
    def __init__(self, font_size: int = 20):
        """
        Initialize ImageAnnotator
        
        Args:
            font_size: Font size for labels
        """
        self.font_size = font_size
        self.font_path = get_font_path()
        self.font = None
        self._load_font()
    
    def _load_font(self):
        """Load font for drawing text"""
        try:
            if self.font_path:
                self.font = ImageFont.truetype(self.font_path, self.font_size)
            else:
                # Fallback to default font (may not support Chinese)
                self.font = ImageFont.load_default()
                print("Warning: Using default font which may not support Chinese characters")
        except Exception as e:
            print(f"Warning: Failed to load font: {e}")
            self.font = ImageFont.load_default()
    
    def annotate_image(
        self,
        image_path: str,
        detections: List[Dict],
        output_path: str,
        box_color: str = "red",
        text_color: str = "yellow",
        box_width: int = 2
    ) -> bool:
        """
        Annotate image with detection results
        
        Args:
            image_path: Path to input image
            detections: List of detection dictionaries
            output_path: Path to save annotated image
            box_color: Color of bounding box
            text_color: Color of text
            box_width: Width of bounding box line
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Open image
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)
            
            # Draw each detection
            for detection in detections:
                left = detection.get('left', 0)
                top = detection.get('top', 0)
                right = detection.get('right', 0)
                bottom = detection.get('bottom', 0)
                label = detection.get('label', '')
                score = detection.get('score', '0')
                
                # Draw bounding box
                draw.rectangle(
                    [(left, top), (right, bottom)],
                    outline=box_color,
                    width=box_width
                )
                
                # Prepare label text with score (use Chinese label on image)
                label_text = f"{label} ({score})"
                
                # Calculate text position (above the box)
                text_y = max(0, top - 25)
                
                # Draw text background for better visibility
                try:
                    # Get text bounding box
                    bbox = draw.textbbox((left, text_y), label_text, font=self.font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]
                    
                    # Draw semi-transparent background
                    overlay = Image.new('RGBA', image.size, (0, 0, 0, 0))
                    overlay_draw = ImageDraw.Draw(overlay)
                    overlay_draw.rectangle(
                        [(left, text_y), (left + text_width + 4, text_y + text_height + 4)],
                        fill=(0, 0, 0, 180)  # Semi-transparent black
                    )
                    image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
                    draw = ImageDraw.Draw(image)
                except:
                    pass
                
                # Draw text
                draw.text(
                    (left + 2, text_y + 2),
                    label_text,
                    fill=text_color,
                    font=self.font
                )
            
            # Ensure output directory exists
            output_dir = Path(output_path).parent
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Save annotated image
            image.save(output_path, quality=95)
            return True
            
        except Exception as e:
            print(f"Error annotating image: {e}")
            return False
