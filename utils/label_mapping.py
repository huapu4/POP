"""
Label mapping between Chinese and English
"""

# Chinese to English label mapping
LABEL_MAPPING = {
    "目标眼": "Eye",
    "结膜炎": "Conjunctivitis",
    "麦粒肿/霰粒肿": "Stye",
    "睑缘炎": "Blepharitis",
    "前房积血": "Hyphema",
    "瞳孔欠规则": "Irregular pupils",
    "前房积脓": "Hypopyon",
    "结膜下出血": "Subconjunctival hemorrhage",
    "结膜结石": "Conjunctival concretions",
    "角膜移植术后": "Corneal transplant status",
    "感染性角膜病变": "Infectious keratopathy",
    "非感染性角膜病变": "Non-infectious keratopathy",
    "睑内翻": "Entropion",
    "睑外翻": "Ectropion",
    "突眼": "Exophthalmos",
    "白内障": "Cataract",
    "翼状胬肉": "Pterygium"
}


def get_english_label(chinese_label: str) -> str:
    """
    Get English label from Chinese label
    
    Args:
        chinese_label: Chinese label
        
    Returns:
        English label, or original label if not found in mapping
    """
    return LABEL_MAPPING.get(chinese_label, chinese_label)


def get_chinese_label(english_label: str) -> str:
    """
    Get Chinese label from English label
    
    Args:
        english_label: English label
        
    Returns:
        Chinese label, or original label if not found in mapping
    """
    # Reverse mapping
    reverse_mapping = {v: k for k, v in LABEL_MAPPING.items()}
    return reverse_mapping.get(english_label, english_label)
