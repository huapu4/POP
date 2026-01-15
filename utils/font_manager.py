"""
Font manager for handling Chinese fonts
"""

from pathlib import Path
from typing import Optional


def get_font_path() -> Optional[str]:
    """
    Get path to SimHei font file in utils/fonts directory
    
    Returns:
        Path to font file, or None if not found
    """
    # Font is located in utils/fonts directory
    fonts_dir = Path(__file__).parent / "fonts"
    font_path = fonts_dir / "simhei.ttf"
    
    if font_path.exists():
        return str(font_path)
    
    print(f"Warning: SimHei font not found at: {font_path}")
    print(f"Please ensure simhei.ttf is placed in: {fonts_dir}")
    return None
