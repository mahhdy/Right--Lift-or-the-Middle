import re
import sys

def estimate_text_width(text, font_size=9):
    """Estimate text width in pixels based on character count and Persian chars"""
    # Persian chars generally wider than Latin (~10px/char at 9pt)
    persian_chars = 'ابتثجحخدذرزژسشصضطظعغفقکگلمنوهیءآأؤإئ'
    persian_count = sum(1 for c in text if c in persian_chars)
    latin_count = len(text) - persian_count
    
    # Width estimation (pixels at font-size=9)
    persian_width = persian_count * 10.5  # Persian chars ~10.5px
    latin_width = latin_count * 7.5        # Latin chars ~7.5px
    total_width = persian_width + latin_width + 8  # +padding
    
    # Dynamic width + 25% buffer
    dynamic_width = int(total_width * 1.25)
    return max(dynamic_width, 70)  # Minimum 70px

def fix_svg_text_legibility(svg_content):
    """Dynamic white background boxes based on text length"""
    
    # Pattern: Match circle + following text
    pattern = r'(<circle\s+cx="([^"]+)"\s+cy="([^"]+)"\s+r="[^"]+"\s+fill="[^"]+"[^>]*filter="url\(\#dropshadow\)"?/?>)\s*\n\s*(<text[^>]*>(.*?)</text>)'
    
    def replace_match(match):
        circle = match.group(1)
        cx = match.group(2)
        cy = match.group(3)
        text_tag = match.group(4)
        text_content = match.group(5)
        
        # Calculate text center
        text_center_y = str(float(cy) + 4)
        
        # DYNAMIC WIDTH based on text length
        text_width = estimate_text_width(text_content)
        half_width = text_width // 2
        
        return f'''<g transform="translate({cx},{text_center_y})">
  {circle.replace(f'cx="{cx}"', 'cx="0"').replace(f'cy="{cy}"', 'cy="-2"')}
  <rect x="-{half_width}" y="-14" width="{text_width}" height="26" rx="6" fill="white" fill-opacity="0.95" stroke="#666" stroke-width="0.2"/>
{text_tag.replace(f'x="{cx}"', 'x="0"').replace(f'y="{text_center_y}"', 'y="2"')}
</g>'''
    
    fixed_svg = re.sub(pattern, replace_match, svg_content, flags=re.DOTALL | re.MULTILINE)
    return fixed_svg

# MAIN
if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            svg_content = f.read()
    else:
        svg_content = sys.stdin.read()
    
    fixed_svg = fix_svg_text_legibility(svg_content)
    
    if len(sys.argv) > 2:
        with open(sys.argv[2], 'w', encoding='utf-8') as f:
            f.write(fixed_svg)
        print(f"✅ Fixed SVG saved to {sys.argv[2]}")
        print(f"📏 Processed {len(re.findall(r'<text.*?</text>', svg_content))} text elements")
    else:
        print(fixed_svg)
