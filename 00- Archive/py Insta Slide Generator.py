import os
from pathlib import Path

# Configuration
OUTPUT_DIR = Path(r"D:\Code\Apps\chatMergerTool\output\Left-Right-The-Middle\slides")
WIDTH = 1080
HEIGHT = 1350

# Color Palette
COLORS = {
    'navy': '#1A237E',
    'navy_light': '#3949AB',
    'gold': '#F9A825',
    'gold_light': '#FFD54F',
    'emerald': '#2E7D32',
    'emerald_light': '#66BB6A',
    'red_left': '#C81E1E',
    'red_light': '#EF5350',
    'white': '#FFFFFF',
    'off_white': '#FAF8F5',
    'dark_gray': '#3C3C3C',
    'light_gray': '#E0E0E0',
    'purple': '#6A1B9A',
    'purple_light': '#AB47BC',
    'teal': '#00695C',
    'orange': '#E65100',
}

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def get_base_styles():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&amp;display=swap');
        
        * {
            font-family: 'Vazirmatn', 'Segoe UI', Tahoma, Arial, sans-serif;
        }
        
        .title {
            font-size: 52px;
            font-weight: 800;
            fill: white;
        }
        
        .subtitle {
            font-size: 32px;
            font-weight: 600;
            fill: white;
        }
        
        .body-text {
            font-size: 28px;
            font-weight: 400;
            fill: #3C3C3C;
        }
        
        .highlight {
            font-weight: 700;
        }
        
        .gold-text {
            fill: #F9A825;
        }
        
        .small-text {
            font-size: 22px;
            fill: #666666;
        }
        
        .card {
            fill: white;
            filter: drop-shadow(0 4px 12px rgba(0,0,0,0.08));
        }
        
        .stat-number {
            font-size: 72px;
            font-weight: 900;
        }
        
        .quote-text {
            font-size: 34px;
            font-weight: 500;
            font-style: italic;
        }
    </style>
    """

def create_slide_1_cover():
    """Cover Slide - Book Introduction"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <!-- Gradient Background -->
    <defs>
        <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{COLORS['navy']};stop-opacity:1" />
            <stop offset="50%" style="stop-color:#283593;stop-opacity:1" />
            <stop offset="100%" style="stop-color:{COLORS['purple']};stop-opacity:1" />
        </linearGradient>
        <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:{COLORS['red_left']};stop-opacity:1" />
            <stop offset="50%" style="stop-color:{COLORS['gold']};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{COLORS['navy_light']};stop-opacity:1" />
        </linearGradient>
        <filter id="glow">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bgGrad1)"/>
    
    <!-- Decorative Circles -->
    <circle cx="150" cy="200" r="180" fill="{COLORS['red_left']}" opacity="0.15"/>
    <circle cx="930" cy="200" r="180" fill="{COLORS['navy_light']}" opacity="0.15"/>
    <circle cx="540" cy="1200" r="250" fill="{COLORS['gold']}" opacity="0.1"/>
    
    <!-- Spectrum Line -->
    <rect x="100" y="380" width="880" height="12" rx="6" fill="url(#goldGrad)" filter="url(#glow)"/>
    
    <!-- Position Markers -->
    <circle cx="150" cy="386" r="20" fill="{COLORS['red_left']}" stroke="white" stroke-width="3"/>
    <circle cx="540" cy="386" r="20" fill="{COLORS['gold']}" stroke="white" stroke-width="3"/>
    <circle cx="930" cy="386" r="20" fill="{COLORS['navy_light']}" stroke="white" stroke-width="3"/>
    
    <!-- Labels -->
    <foreignObject x="60" y="420" width="180" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:24px; font-weight:600;">چپ</div>
    </foreignObject>
    <foreignObject x="450" y="420" width="180" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['gold']}; font-size:24px; font-weight:700;">میانه؟</div>
    </foreignObject>
    <foreignObject x="840" y="420" width="180" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:24px; font-weight:600;">راست</div>
    </foreignObject>
    
    <!-- Main Title -->
    <foreignObject x="40" y="520" width="1000" height="200">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:68px; font-weight:900; line-height:1.3; text-shadow: 0 4px 20px rgba(0,0,0,0.3);">
            راست یا چپ؛<br/>میانه کجاست؟
        </div>
    </foreignObject>
    
    <!-- Subtitle -->
    <foreignObject x="80" y="750" width="920" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['gold_light']}; font-size:28px; font-weight:500;">
            سفری جامع در تاریخ و فلسفه طیف سیاسی
        </div>
    </foreignObject>
    
    <!-- Book Icon -->
    <rect x="440" y="880" width="200" height="260" rx="10" fill="white" opacity="0.95"/>
    <rect x="455" y="895" width="170" height="230" rx="5" fill="{COLORS['navy']}"/>
    <rect x="465" y="950" width="150" height="8" rx="4" fill="{COLORS['gold']}"/>
    <rect x="465" y="975" width="120" height="6" rx="3" fill="white" opacity="0.5"/>
    <rect x="465" y="995" width="140" height="6" rx="3" fill="white" opacity="0.5"/>
    <rect x="465" y="1015" width="100" height="6" rx="3" fill="white" opacity="0.5"/>
    
    <!-- Author Info -->
    <foreignObject x="80" y="1180" width="920" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:26px; font-weight:600;">
            مهدی سالم
        </div>
    </foreignObject>
    
    <!-- Call to Action -->
    <rect x="340" y="1250" width="400" height="60" rx="30" fill="{COLORS['gold']}" filter="url(#glow)"/>
    <foreignObject x="340" y="1250" width="400" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:24px; font-weight:700; line-height:60px;">
            ← بیشتر بخوانید
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_2_key_question():
    """Provocative Question Slide"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#0D0D0D;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#1a1a2e;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bgGrad2)"/>
    
    <!-- Large Question Mark Background -->
    <text x="540" y="750" text-anchor="middle" font-size="800" font-weight="900" fill="{COLORS['gold']}" opacity="0.08">؟</text>
    
    <!-- Header Badge -->
    <rect x="340" y="80" width="400" height="50" rx="25" fill="{COLORS['gold']}" opacity="0.9"/>
    <foreignObject x="340" y="80" width="400" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:22px; font-weight:700; line-height:50px;">
            🤔 یک لحظه فکر کنید
        </div>
    </foreignObject>
    
    <!-- Main Question -->
    <foreignObject x="60" y="220" width="960" height="300">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:44px; font-weight:700; line-height:1.6;">
            آیا می‌دانید مفهوم<br/>
            <span style="color:{COLORS['gold']};">«چپ و راست»</span><br/>
            از کجا آمده است؟
        </div>
    </foreignObject>
    
    <!-- Divider -->
    <line x1="300" y1="560" x2="780" y2="560" stroke="{COLORS['gold']}" stroke-width="2" opacity="0.5"/>
    
    <!-- Fact Box -->
    <rect x="80" y="620" width="920" height="400" rx="20" fill="white" opacity="0.05"/>
    <rect x="80" y="620" width="920" height="400" rx="20" stroke="{COLORS['gold']}" stroke-width="2" fill="none" opacity="0.3"/>
    
    <foreignObject x="100" y="660" width="880" height="340">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:30px; font-weight:400; line-height:1.8;">
            <span style="color:{COLORS['gold']}; font-size:48px; font-weight:800;">۱۷۸۹</span><br/><br/>
            در مجلس ملی فرانسه،<br/>
            طرفداران <span style="color:{COLORS['red_light']};">تغییر</span> در سمت چپ<br/>
            و حامیان <span style="color:{COLORS['navy_light']};">سنت</span> در سمت راست نشستند.<br/><br/>
            <span style="font-size:24px; color:{COLORS['gold_light']};">و اینگونه تاریخ سیاست نوشته شد...</span>
        </div>
    </foreignObject>
    
    <!-- Bottom CTA -->
    <foreignObject x="80" y="1100" width="920" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['gold']}; font-size:26px; font-weight:600;">
            📖 داستان کامل را در کتاب بخوانید
        </div>
    </foreignObject>
    
    <!-- Swipe Indicator -->
    <foreignObject x="80" y="1250" width="920" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:20px; opacity:0.6;">
            ← برای ادامه بکشید
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_3_timeline():
    """Historical Timeline Slide"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['off_white']}"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="{WIDTH}" height="140" fill="{COLORS['navy']}"/>
    <foreignObject x="40" y="40" width="1000" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:38px; font-weight:800;">
            ⏳ تایم‌لاین تحولات طیف سیاسی
        </div>
    </foreignObject>
    
    <!-- Timeline Line -->
    <line x1="540" y1="200" x2="540" y2="1200" stroke="{COLORS['navy']}" stroke-width="6" stroke-linecap="round"/>
    
    <!-- Timeline Events -->
    <!-- Event 1 -->
    <circle cx="540" cy="250" r="18" fill="{COLORS['red_left']}"/>
    <rect x="580" y="210" width="420" height="80" rx="10" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.1))"/>
    <foreignObject x="590" y="215" width="400" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:20px; font-weight:700;">
            ۱۷۸۹ - انقلاب فرانسه
            <div style="font-weight:400; color:#666; font-size:16px; margin-top:5px;">زایش مفهوم چپ و راست</div>
        </div>
    </foreignObject>
    
    <!-- Event 2 -->
    <circle cx="540" cy="380" r="18" fill="{COLORS['gold']}"/>
    <rect x="80" y="340" width="420" height="80" rx="10" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.1))"/>
    <foreignObject x="90" y="345" width="400" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:20px; font-weight:700;">
            ۱۸۴۸ - مانیفست کمونیست
            <div style="font-weight:400; color:#666; font-size:16px; margin-top:5px;">تئوری‌پردازی چپ رادیکال</div>
        </div>
    </foreignObject>
    
    <!-- Event 3 -->
    <circle cx="540" cy="510" r="18" fill="{COLORS['red_left']}"/>
    <rect x="580" y="470" width="420" height="80" rx="10" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.1))"/>
    <foreignObject x="590" y="475" width="400" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:20px; font-weight:700;">
            ۱۹۱۷ - انقلاب روسیه
            <div style="font-weight:400; color:#666; font-size:16px; margin-top:5px;">نخستین دولت کمونیستی</div>
        </div>
    </foreignObject>
    
    <!-- Event 4 -->
    <circle cx="540" cy="640" r="18" fill="{COLORS['purple']}"/>
    <rect x="80" y="600" width="420" height="80" rx="10" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.1))"/>
    <foreignObject x="90" y="605" width="400" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:20px; font-weight:700;">
            ۱۹۳۳ - ظهور نازیسم
            <div style="font-weight:400; color:#666; font-size:16px; margin-top:5px;">راست افراطی به قدرت می‌رسد</div>
        </div>
    </foreignObject>
    
    <!-- Event 5 -->
    <circle cx="540" cy="770" r="18" fill="{COLORS['emerald']}"/>
    <rect x="580" y="730" width="420" height="80" rx="10" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.1))"/>
    <foreignObject x="590" y="735" width="400" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:20px; font-weight:700;">
            ۱۹۴۵ - دولت رفاه
            <div style="font-weight:400; color:#666; font-size:16px; margin-top:5px;">سوسیال دموکراسی رشد می‌کند</div>
        </div>
    </foreignObject>
    
    <!-- Event 6 -->
    <circle cx="540" cy="900" r="18" fill="{COLORS['navy_light']}"/>
    <rect x="80" y="860" width="420" height="80" rx="10" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.1))"/>
    <foreignObject x="90" y="865" width="400" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:20px; font-weight:700;">
            ۱۹۷۹ - انقلاب نئولیبرال
            <div style="font-weight:400; color:#666; font-size:16px; margin-top:5px;">تاچر و ریگان</div>
        </div>
    </foreignObject>
    
    <!-- Event 7 -->
    <circle cx="540" cy="1030" r="18" fill="{COLORS['gold']}"/>
    <rect x="580" y="990" width="420" height="80" rx="10" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.1))"/>
    <foreignObject x="590" y="995" width="400" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:20px; font-weight:700;">
            ۱۹۹۱ - فروپاشی شوروی
            <div style="font-weight:400; color:#666; font-size:16px; margin-top:5px;">پایان جنگ سرد</div>
        </div>
    </foreignObject>
    
    <!-- Event 8 -->
    <circle cx="540" cy="1160" r="18" fill="{COLORS['orange']}"/>
    <rect x="80" y="1120" width="420" height="80" rx="10" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.1))"/>
    <foreignObject x="90" y="1125" width="400" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:20px; font-weight:700;">
            ۲۰۱۶ - پوپولیسم جدید
            <div style="font-weight:400; color:#666; font-size:16px; margin-top:5px;">برگزیت و ترامپ</div>
        </div>
    </foreignObject>
    
    <!-- Page Number -->
    <circle cx="540" cy="1290" r="25" fill="{COLORS['navy']}"/>
    <text x="540" y="1298" text-anchor="middle" font-size="20" font-weight="700" fill="white">۳</text>
</svg>'''
    return svg


def create_slide_4_left_spectrum():
    """Left Political Spectrum Overview"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="leftGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#B71C1C;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#C62828;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#leftGrad)"/>
    
    <!-- Decorative Elements -->
    <circle cx="100" cy="100" r="200" fill="white" opacity="0.05"/>
    <circle cx="980" cy="1250" r="300" fill="white" opacity="0.05"/>
    
    <!-- Header -->
    <foreignObject x="40" y="60" width="1000" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:52px; font-weight:900;">
            ☭ جهان چپ
        </div>
    </foreignObject>
    
    <foreignObject x="80" y="160" width="920" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.8); font-size:24px;">
            از آرمان برابری تا واقعیت‌های تاریخی
        </div>
    </foreignObject>
    
    <!-- Cards -->
    <!-- Card 1: Socialism -->
    <rect x="60" y="260" width="460" height="200" rx="16" fill="white" opacity="0.95"/>
    <rect x="60" y="260" width="10" height="200" rx="5" fill="{COLORS['red_left']}"/>
    <foreignObject x="90" y="280" width="420" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="color:{COLORS['red_left']}; font-size:28px; font-weight:800; margin-bottom:10px;">سوسیالیسم</div>
            <div style="color:#333; font-size:20px; line-height:1.6;">
                مالکیت اجتماعی بر ابزار تولید<br/>
                عدالت اقتصادی و اجتماعی<br/>
                از سن‌سیمون تا سندرز
            </div>
        </div>
    </foreignObject>
    
    <!-- Card 2: Communism -->
    <rect x="560" y="260" width="460" height="200" rx="16" fill="white" opacity="0.95"/>
    <rect x="560" y="260" width="10" height="200" rx="5" fill="#D32F2F"/>
    <foreignObject x="590" y="280" width="420" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="color:#D32F2F; font-size:28px; font-weight:800; margin-bottom:10px;">کمونیسم</div>
            <div style="color:#333; font-size:20px; line-height:1.6;">
                لغو مالکیت خصوصی<br/>
                جامعه بی‌طبقه<br/>
                از مارکس تا مائو
            </div>
        </div>
    </foreignObject>
    
    <!-- Card 3: Anarchism -->
    <rect x="60" y="490" width="460" height="200" rx="16" fill="white" opacity="0.95"/>
    <rect x="60" y="490" width="10" height="200" rx="5" fill="#212121"/>
    <foreignObject x="90" y="510" width="420" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="color:#212121; font-size:28px; font-weight:800; margin-bottom:10px;">آنارشیسم</div>
            <div style="color:#333; font-size:20px; line-height:1.6;">
                نفی دولت و سلسله‌مراتب<br/>
                آزادی فردی و جمعی<br/>
                از باکونین تا چامسکی
            </div>
        </div>
    </foreignObject>
    
    <!-- Card 4: Social Democracy -->
    <rect x="560" y="490" width="460" height="200" rx="16" fill="white" opacity="0.95"/>
    <rect x="560" y="490" width="10" height="200" rx="5" fill="{COLORS['emerald']}"/>
    <foreignObject x="590" y="510" width="420" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="color:{COLORS['emerald']}; font-size:28px; font-weight:800; margin-bottom:10px;">سوسیال دموکراسی</div>
            <div style="color:#333; font-size:20px; line-height:1.6;">
                دولت رفاه و بازار<br/>
                اصلاح‌طلبی دموکراتیک<br/>
                مدل اسکاندیناوی
            </div>
        </div>
    </foreignObject>
    
    <!-- Key Concepts Box -->
    <rect x="60" y="720" width="960" height="260" rx="16" fill="rgba(255,255,255,0.1)" stroke="white" stroke-width="2"/>
    <foreignObject x="80" y="740" width="920" height="230">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:white;">
            <div style="font-size:26px; font-weight:700; margin-bottom:15px; text-align:center;">💡 ارزش‌های کلیدی چپ</div>
            <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:15px; font-size:20px;">
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">برابری</span>
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">همبستگی</span>
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">عدالت اجتماعی</span>
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">حقوق کارگران</span>
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">تغییر</span>
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">پیشرفت</span>
            </div>
        </div>
    </foreignObject>
    
    <!-- Key Figures -->
    <foreignObject x="60" y="1020" width="960" height="200">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:white; text-align:center;">
            <div style="font-size:22px; font-weight:600; margin-bottom:15px;">👤 چهره‌های کلیدی</div>
            <div style="font-size:20px; line-height:2; opacity:0.9;">
                کارل مارکس • فردریش انگلس • لنین • رزا لوکزامبورگ<br/>
                آنتونیو گرامشی • چه گوارا • برنی سندرز
            </div>
        </div>
    </foreignObject>
    
    <!-- Page Indicator -->
    <foreignObject x="40" y="1260" width="1000" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.6); font-size:18px;">
            بخش دوم کتاب: جهان چپ (فصل‌های ۴ تا ۸)
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_5_right_spectrum():
    """Right Political Spectrum Overview"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="rightGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{COLORS['navy']};stop-opacity:1" />
            <stop offset="100%" style="stop-color:#1565C0;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#rightGrad)"/>
    
    <!-- Decorative Elements -->
    <circle cx="980" cy="100" r="200" fill="white" opacity="0.05"/>
    <circle cx="100" cy="1250" r="300" fill="white" opacity="0.05"/>
    
    <!-- Header -->
    <foreignObject x="40" y="60" width="1000" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:52px; font-weight:900;">
            🏛️ جهان راست
        </div>
    </foreignObject>
    
    <foreignObject x="80" y="160" width="920" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.8); font-size:24px;">
            از حفظ سنت تا آزادی بازار
        </div>
    </foreignObject>
    
    <!-- Cards -->
    <!-- Card 1: Conservatism -->
    <rect x="60" y="260" width="460" height="200" rx="16" fill="white" opacity="0.95"/>
    <rect x="60" y="260" width="10" height="200" rx="5" fill="{COLORS['navy']}"/>
    <foreignObject x="90" y="280" width="420" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="color:{COLORS['navy']}; font-size:28px; font-weight:800; margin-bottom:10px;">محافظه‌کاری</div>
            <div style="color:#333; font-size:20px; line-height:1.6;">
                حفظ نهادها و سنت‌ها<br/>
                تغییر تدریجی و محتاطانه<br/>
                از برک تا راجر اسکروتن
            </div>
        </div>
    </foreignObject>
    
    <!-- Card 2: Liberalism -->
    <rect x="560" y="260" width="460" height="200" rx="16" fill="white" opacity="0.95"/>
    <rect x="560" y="260" width="10" height="200" rx="5" fill="{COLORS['gold']}"/>
    <foreignObject x="590" y="280" width="420" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="color:{COLORS['gold']}; font-size:28px; font-weight:800; margin-bottom:10px;">لیبرالیسم کلاسیک</div>
            <div style="color:#333; font-size:20px; line-height:1.6;">
                آزادی فردی و اقتصادی<br/>
                دولت محدود<br/>
                از لاک تا هایک
            </div>
        </div>
    </foreignObject>
    
    <!-- Card 3: Libertarianism -->
    <rect x="60" y="490" width="460" height="200" rx="16" fill="white" opacity="0.95"/>
    <rect x="60" y="490" width="10" height="200" rx="5" fill="{COLORS['teal']}"/>
    <foreignObject x="90" y="510" width="420" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="color:{COLORS['teal']}; font-size:28px; font-weight:800; margin-bottom:10px;">لیبرتارینیسم</div>
            <div style="color:#333; font-size:20px; line-height:1.6;">
                حداقل دخالت دولت<br/>
                حقوق مالکیت مطلق<br/>
                از نوزیک تا ران پال
            </div>
        </div>
    </foreignObject>
    
    <!-- Card 4: New Right -->
    <rect x="560" y="490" width="460" height="200" rx="16" fill="white" opacity="0.95"/>
    <rect x="560" y="490" width="10" height="200" rx="5" fill="{COLORS['orange']}"/>
    <foreignObject x="590" y="510" width="420" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="color:{COLORS['orange']}; font-size:28px; font-weight:800; margin-bottom:10px;">راست نو</div>
            <div style="color:#333; font-size:20px; line-height:1.6;">
                ناسیونالیسم و هویت<br/>
                نقد جهانی‌شدن<br/>
                پوپولیسم معاصر
            </div>
        </div>
    </foreignObject>
    
    <!-- Key Concepts Box -->
    <rect x="60" y="720" width="960" height="260" rx="16" fill="rgba(255,255,255,0.1)" stroke="white" stroke-width="2"/>
    <foreignObject x="80" y="740" width="920" height="230">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:white;">
            <div style="font-size:26px; font-weight:700; margin-bottom:15px; text-align:center;">💡 ارزش‌های کلیدی راست</div>
            <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:15px; font-size:20px;">
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">آزادی</span>
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">سنت</span>
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">مالکیت</span>
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">نظم</span>
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">ملت</span>
                <span style="background:rgba(255,255,255,0.2); padding:10px 20px; border-radius:20px;">خانواده</span>
            </div>
        </div>
    </foreignObject>
    
    <!-- Key Figures -->
    <foreignObject x="60" y="1020" width="960" height="200">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:white; text-align:center;">
            <div style="font-size:22px; font-weight:600; margin-bottom:15px;">👤 چهره‌های کلیدی</div>
            <div style="font-size:20px; line-height:2; opacity:0.9;">
                ادموند برک • فردریش هایک • میلتون فریدمن<br/>
                مارگارت تاچر • رونالد ریگان • راجر اسکروتن
            </div>
        </div>
    </foreignObject>
    
    <!-- Page Indicator -->
    <foreignObject x="40" y="1260" width="1000" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.6); font-size:18px;">
            بخش سوم کتاب: جهان راست (فصل‌های ۹ تا ۱۳)
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_6_philosophers():
    """Key Philosophers and Thinkers"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['off_white']}"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="{WIDTH}" height="160" fill="{COLORS['purple']}"/>
    <foreignObject x="40" y="50" width="1000" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:42px; font-weight:900;">🎓 متفکران کلیدی</div>
            <div style="font-size:22px; opacity:0.9; margin-top:10px;">فیلسوفانی که طیف سیاسی را شکل دادند</div>
        </div>
    </foreignObject>
    
    <!-- Philosopher Cards - Row 1 -->
    <!-- Burke -->
    <rect x="60" y="200" width="300" height="340" rx="16" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.1))"/>
    <rect x="60" y="200" width="300" height="80" rx="16" fill="{COLORS['navy']}"/>
    <rect x="60" y="265" width="300" height="15" fill="{COLORS['navy']}"/>
    <circle cx="210" cy="240" r="50" fill="white" stroke="{COLORS['gold']}" stroke-width="3"/>
    <text x="210" y="255" text-anchor="middle" font-size="50">🧔</text>
    <foreignObject x="70" y="300" width="280" height="230">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn;">
            <div style="color:{COLORS['navy']}; font-size:24px; font-weight:800;">ادموند برک</div>
            <div style="color:#666; font-size:16px; margin:8px 0;">۱۷۲۹-۱۷۹۷</div>
            <div style="color:{COLORS['navy']}; font-size:14px; font-weight:600; background:{COLORS['light_gray']}; padding:5px 10px; border-radius:10px; display:inline-block;">محافظه‌کاری</div>
            <div style="color:#444; font-size:16px; line-height:1.5; margin-top:15px;">
                «سنت، خرد انباشته نسل‌هاست»
            </div>
        </div>
    </foreignObject>
    
    <!-- Marx -->
    <rect x="390" y="200" width="300" height="340" rx="16" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.1))"/>
    <rect x="390" y="200" width="300" height="80" rx="16" fill="{COLORS['red_left']}"/>
    <rect x="390" y="265" width="300" height="15" fill="{COLORS['red_left']}"/>
    <circle cx="540" cy="240" r="50" fill="white" stroke="{COLORS['gold']}" stroke-width="3"/>
    <text x="540" y="255" text-anchor="middle" font-size="50">👨‍🦳</text>
    <foreignObject x="400" y="300" width="280" height="230">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn;">
            <div style="color:{COLORS['red_left']}; font-size:24px; font-weight:800;">کارل مارکس</div>
            <div style="color:#666; font-size:16px; margin:8px 0;">۱۸۱۸-۱۸۸۳</div>
            <div style="color:{COLORS['red_left']}; font-size:14px; font-weight:600; background:#FFEBEE; padding:5px 10px; border-radius:10px; display:inline-block;">کمونیسم</div>
            <div style="color:#444; font-size:16px; line-height:1.5; margin-top:15px;">
                «تاریخ، تاریخ مبارزه طبقاتی است»
            </div>
        </div>
    </foreignObject>
    
    <!-- Hayek -->
    <rect x="720" y="200" width="300" height="340" rx="16" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.1))"/>
    <rect x="720" y="200" width="300" height="80" rx="16" fill="{COLORS['gold']}"/>
    <rect x="720" y="265" width="300" height="15" fill="{COLORS['gold']}"/>
    <circle cx="870" cy="240" r="50" fill="white" stroke="{COLORS['navy']}" stroke-width="3"/>
    <text x="870" y="255" text-anchor="middle" font-size="50">👴</text>
    <foreignObject x="730" y="300" width="280" height="230">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn;">
            <div style="color:#B8860B; font-size:24px; font-weight:800;">فردریش هایک</div>
            <div style="color:#666; font-size:16px; margin:8px 0;">۱۸۹۹-۱۹۹۲</div>
            <div style="color:#B8860B; font-size:14px; font-weight:600; background:#FFF8E1; padding:5px 10px; border-radius:10px; display:inline-block;">لیبرالیسم</div>
            <div style="color:#444; font-size:16px; line-height:1.5; margin-top:15px;">
                «برنامه‌ریزی متمرکز راه بردگی است»
            </div>
        </div>
    </foreignObject>
    
    <!-- Philosopher Cards - Row 2 -->
    <!-- Rawls -->
    <rect x="140" y="580" width="300" height="340" rx="16" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.1))"/>
    <rect x="140" y="580" width="300" height="80" rx="16" fill="{COLORS['emerald']}"/>
    <rect x="140" y="645" width="300" height="15" fill="{COLORS['emerald']}"/>
    <circle cx="290" cy="620" r="50" fill="white" stroke="{COLORS['gold']}" stroke-width="3"/>
    <text x="290" y="635" text-anchor="middle" font-size="50">🎓</text>
    <foreignObject x="150" y="680" width="280" height="230">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn;">
            <div style="color:{COLORS['emerald']}; font-size:24px; font-weight:800;">جان رالز</div>
            <div style="color:#666; font-size:16px; margin:8px 0;">۱۹۲۱-۲۰۰۲</div>
            <div style="color:{COLORS['emerald']}; font-size:14px; font-weight:600; background:#E8F5E9; padding:5px 10px; border-radius:10px; display:inline-block;">لیبرالیسم برابری‌خواه</div>
            <div style="color:#444; font-size:16px; line-height:1.5; margin-top:15px;">
                «عدالت نخستین فضیلت نهادهاست»
            </div>
        </div>
    </foreignObject>
    
    <!-- Foucault -->
    <rect x="640" y="580" width="300" height="340" rx="16" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.1))"/>
    <rect x="640" y="580" width="300" height="80" rx="16" fill="{COLORS['purple']}"/>
    <rect x="640" y="645" width="300" height="15" fill="{COLORS['purple']}"/>
    <circle cx="790" cy="620" r="50" fill="white" stroke="{COLORS['gold']}" stroke-width="3"/>
    <text x="790" y="635" text-anchor="middle" font-size="50">🧑‍🦲</text>
    <foreignObject x="650" y="680" width="280" height="230">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn;">
            <div style="color:{COLORS['purple']}; font-size:24px; font-weight:800;">میشل فوکو</div>
            <div style="color:#666; font-size:16px; margin:8px 0;">۱۹۲۶-۱۹۸۴</div>
            <div style="color:{COLORS['purple']}; font-size:14px; font-weight:600; background:#F3E5F5; padding:5px 10px; border-radius:10px; display:inline-block;">پست‌مدرنیسم</div>
            <div style="color:#444; font-size:16px; line-height:1.5; margin-top:15px;">
                «قدرت همه‌جا حاضر است»
            </div>
        </div>
    </foreignObject>
    
    <!-- Bottom Info -->
    <rect x="60" y="960" width="960" height="120" rx="16" fill="{COLORS['navy']}" opacity="0.05"/>
    <foreignObject x="80" y="980" width="920" height="90">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['navy']};">
            <div style="font-size:22px; font-weight:700;">📚 در ضمیمه ۲ کتاب</div>
            <div style="font-size:18px; margin-top:8px; opacity:0.8;">شناخت‌نامه ۱۰۰ چهره کلیدی تاریخ اندیشه سیاسی</div>
        </div>
    </foreignObject>
    
    <!-- Page Number -->
    <foreignObject x="40" y="1100" width="1000" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#999; font-size:18px;">
            فصل ۲: فلسفه و معرفت‌شناسی چپ و راست
        </div>
    </foreignObject>
</svg>'''
    return svg


# CONTINUING SLIDE 7 - Economic Spectrum (completion)

def create_slide_7_economic_spectrum():
    """Economic Systems Comparison - COMPLETE"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="econGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:{COLORS['red_left']};stop-opacity:1" />
            <stop offset="50%" style="stop-color:{COLORS['emerald']};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{COLORS['navy']};stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="#F5F5F5"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="{WIDTH}" height="140" fill="{COLORS['navy']}"/>
    <foreignObject x="40" y="40" width="1000" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:38px; font-weight:800;">
            💰 طیف اقتصادی: از برنامه‌ریزی تا بازار آزاد
        </div>
    </foreignObject>
    
    <!-- Spectrum Bar -->
    <rect x="60" y="180" width="960" height="30" rx="15" fill="url(#econGrad)"/>
    
    <!-- Spectrum Labels -->
    <foreignObject x="40" y="220" width="200" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:{COLORS['red_left']}; font-size:18px; font-weight:700;">
            اقتصاد برنامه‌ریزی شده
        </div>
    </foreignObject>
    <foreignObject x="440" y="220" width="200" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['emerald']}; font-size:18px; font-weight:700;">
            اقتصاد مختلط
        </div>
    </foreignObject>
    <foreignObject x="820" y="220" width="200" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:left; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:18px; font-weight:700;">
            بازار آزاد
        </div>
    </foreignObject>
    
    <!-- System Cards -->
    <!-- Card 1: Command Economy -->
    <rect x="60" y="290" width="300" height="280" rx="12" fill="white" filter="drop-shadow(0 3px 10px rgba(0,0,0,0.1))"/>
    <rect x="60" y="290" width="300" height="60" rx="12" fill="{COLORS['red_left']}"/>
    <rect x="60" y="340" width="300" height="10" fill="{COLORS['red_left']}"/>
    <foreignObject x="70" y="300" width="280" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:22px; font-weight:700;">
            اقتصاد دستوری
        </div>
    </foreignObject>
    <foreignObject x="70" y="370" width="280" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#333; font-size:17px; line-height:1.7;">
            <div style="margin-bottom:10px;">✓ مالکیت دولتی</div>
            <div style="margin-bottom:10px;">✓ برنامه‌ریزی متمرکز</div>
            <div style="margin-bottom:10px;">✓ قیمت‌گذاری دولتی</div>
            <div style="color:#888; font-size:15px; margin-top:15px;">
                نمونه: شوروی، کوبا
            </div>
        </div>
    </foreignObject>
    
    <!-- Card 2: Mixed Economy -->
    <rect x="390" y="290" width="300" height="280" rx="12" fill="white" filter="drop-shadow(0 3px 10px rgba(0,0,0,0.1))"/>
    <rect x="390" y="290" width="300" height="60" rx="12" fill="{COLORS['emerald']}"/>
    <rect x="390" y="340" width="300" height="10" fill="{COLORS['emerald']}"/>
    <foreignObject x="400" y="300" width="280" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:22px; font-weight:700;">
            اقتصاد مختلط
        </div>
    </foreignObject>
    <foreignObject x="400" y="370" width="280" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#333; font-size:17px; line-height:1.7;">
            <div style="margin-bottom:10px;">✓ بخش خصوصی + دولتی</div>
            <div style="margin-bottom:10px;">✓ دولت رفاه</div>
            <div style="margin-bottom:10px;">✓ تنظیم‌گری</div>
            <div style="color:#888; font-size:15px; margin-top:15px;">
                نمونه: اسکاندیناوی، آلمان
            </div>
        </div>
    </foreignObject>
    
    <!-- Card 3: Free Market -->
    <rect x="720" y="290" width="300" height="280" rx="12" fill="white" filter="drop-shadow(0 3px 10px rgba(0,0,0,0.1))"/>
    <rect x="720" y="290" width="300" height="60" rx="12" fill="{COLORS['navy']}"/>
    <rect x="720" y="340" width="300" height="10" fill="{COLORS['navy']}"/>
    <foreignObject x="730" y="300" width="280" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:22px; font-weight:700;">
            بازار آزاد
        </div>
    </foreignObject>
    <foreignObject x="730" y="370" width="280" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#333; font-size:17px; line-height:1.7;">
            <div style="margin-bottom:10px;">✓ مالکیت خصوصی</div>
            <div style="margin-bottom:10px;">✓ دخالت حداقلی دولت</div>
            <div style="margin-bottom:10px;">✓ قیمت‌گذاری بازار</div>
            <div style="color:#888; font-size:15px; margin-top:15px;">
                نمونه: هنگ‌کنگ، سنگاپور
            </div>
        </div>
    </foreignObject>
    
    <!-- Famous Debate Box -->
    <rect x="60" y="600" width="960" height="220" rx="16" fill="{COLORS['gold']}" opacity="0.1"/>
    <rect x="60" y="600" width="960" height="220" rx="16" fill="none" stroke="{COLORS['gold']}" stroke-width="3"/>
    <foreignObject x="80" y="620" width="920" height="180">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="text-align:center; color:{COLORS['navy']}; font-size:26px; font-weight:800; margin-bottom:15px;">
                ⚔️ مناظره بزرگ قرن بیستم
            </div>
            <div style="display:flex; justify-content:space-around; align-items:center;">
                <div style="text-align:center; width:45%;">
                    <div style="font-size:28px; font-weight:700; color:{COLORS['red_left']};">اقتصاد برنامه‌ریزی</div>
                    <div style="font-size:18px; color:#555; margin-top:8px;">"کارایی و عدالت"</div>
                    <div style="font-size:16px; color:#777; margin-top:5px;">لانگه، تیلور</div>
                </div>
                <div style="font-size:48px; color:{COLORS['gold']};">VS</div>
                <div style="text-align:center; width:45%;">
                    <div style="font-size:28px; font-weight:700; color:{COLORS['navy']};">محاسبه غیرممکن است</div>
                    <div style="font-size:18px; color:#555; margin-top:8px;">"دانش پراکنده"</div>
                    <div style="font-size:16px; color:#777; margin-top:5px;">میزس، هایک</div>
                </div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Key Insight -->
    <rect x="80" y="850" width="920" height="140" rx="12" fill="{COLORS['navy']}" opacity="0.05"/>
    <foreignObject x="100" y="870" width="880" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:20px; line-height:1.8;">
            💡 امروز بیشتر کشورها در <span style="font-weight:700; color:{COLORS['emerald']};">میانه این طیف</span> قرار دارند<br/>
            سوال این است: چقدر دولت و چقدر بازار؟
        </div>
    </foreignObject>
    
    <!-- Bottom Reference -->
    <foreignObject x="40" y="1020" width="1000" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#666; font-size:18px;">
            📖 فصل ۳: اقتصاد سیاسی و جدال بنیادین<br/>
            <span style="font-size:16px;">مناظره محاسبه سوسیالیستی (۱۹۲۰-۱۹۴۰)</span>
        </div>
    </foreignObject>
    
    <!-- Page Number -->
    <circle cx="540" cy="1280" r="28" fill="{COLORS['navy']}"/>
    <text x="540" y="1290" text-anchor="middle" font-size="22" font-weight="700" fill="white">۷</text>
</svg>'''
    return svg


def create_slide_8_marx_vs_bakunin():
    """Famous Debate: Marx vs Bakunin"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="debateGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#1a1a1a;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#2d2d2d;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#debateGrad)"/>
    
    <!-- Lightning Background -->
    <path d="M 540 100 L 520 400 L 560 400 L 540 700" stroke="{COLORS['gold']}" stroke-width="3" fill="none" opacity="0.2"/>
    
    <!-- Header Badge -->
    <rect x="290" y="40" width="500" height="70" rx="35" fill="{COLORS['gold']}"/>
    <foreignObject x="290" y="40" width="500" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#1a1a1a; font-size:32px; font-weight:900; line-height:70px;">
            ⚔️ نبرد تاریخی: چپ علیه چپ
        </div>
    </foreignObject>
    
    <!-- Title -->
    <foreignObject x="60" y="140" width="960" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:28px; font-weight:600;">
            جدال مارکس و باکونین در انترناسیونال اول (۱۸۷۲)
        </div>
    </foreignObject>
    
    <!-- Marx Side -->
    <rect x="60" y="250" width="450" height="700" rx="20" fill="white" opacity="0.05"/>
    <rect x="60" y="250" width="450" height="700" rx="20" fill="none" stroke="{COLORS['red_left']}" stroke-width="3"/>
    
    <!-- Marx Portrait -->
    <circle cx="285" cy="320" r="60" fill="{COLORS['red_left']}"/>
    <text x="285" y="340" text-anchor="middle" font-size="70" fill="white">👨‍🦳</text>
    
    <foreignObject x="80" y="400" width="410" height="530">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:white;">
            <div style="text-align:center; font-size:32px; font-weight:800; color:{COLORS['red_light']}; margin-bottom:20px;">
                کارل مارکس
            </div>
            
            <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:12px; margin-bottom:15px;">
                <div style="font-size:20px; font-weight:700; color:{COLORS['gold']}; margin-bottom:10px;">✓ دولت انتقالی</div>
                <div style="font-size:17px; line-height:1.6;">
                    دیکتاتوری پرولتاریا برای سرکوب بورژوازی ضروری است
                </div>
            </div>
            
            <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:12px; margin-bottom:15px;">
                <div style="font-size:20px; font-weight:700; color:{COLORS['gold']}; margin-bottom:10px;">✓ حزب پیشاهنگ</div>
                <div style="font-size:17px; line-height:1.6;">
                    طبقه کارگر نیاز به رهبری متمرکز دارد
                </div>
            </div>
            
            <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:12px; margin-bottom:15px;">
                <div style="font-size:20px; font-weight:700; color:{COLORS['gold']}; margin-bottom:10px;">✓ تسخیر قدرت</div>
                <div style="font-size:17px; line-height:1.6;">
                    ابتدا کنترل دولت، سپس حذف تدریجی آن
                </div>
            </div>
            
            <div style="text-align:center; margin-top:20px; font-size:15px; font-style:italic; color:{COLORS['gold_light']};">
                "بین جامعه سرمایه‌داری و کمونیستی، دوره تبدیل انقلابی یکی به دیگری قرار دارد"
            </div>
        </div>
    </foreignObject>
    
    <!-- VS Badge -->
    <circle cx="540" cy="600" r="70" fill="{COLORS['gold']}"/>
    <text x="540" y="625" text-anchor="middle" font-size="54" font-weight="900" fill="#1a1a1a">VS</text>
    
    <!-- Bakunin Side -->
    <rect x="570" y="250" width="450" height="700" rx="20" fill="white" opacity="0.05"/>
    <rect x="570" y="250" width="450" height="700" rx="20" fill="none" stroke="#212121" stroke-width="3"/>
    
    <!-- Bakunin Portrait -->
    <circle cx="795" cy="320" r="60" fill="#212121"/>
    <text x="795" y="340" text-anchor="middle" font-size="70" fill="white">🧔</text>
    
    <foreignObject x="590" y="400" width="410" height="530">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:white;">
            <div style="text-align:center; font-size:32px; font-weight:800; color:#BDBDBD; margin-bottom:20px;">
                میخائیل باکونین
            </div>
            
            <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:12px; margin-bottom:15px;">
                <div style="font-size:20px; font-weight:700; color:{COLORS['gold']}; margin-bottom:10px;">✗ الغای فوری دولت</div>
                <div style="font-size:17px; line-height:1.6;">
                    هر دولتی، حتی دولت کارگری، به استبداد منجر می‌شود
                </div>
            </div>
            
            <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:12px; margin-bottom:15px;">
                <div style="font-size:20px; font-weight:700; color:{COLORS['gold']}; margin-bottom:10px;">✗ نفی سلسله‌مراتب</div>
                <div style="font-size:17px; line-height:1.6;">
                    هیچ نخبه‌ای حق رهبری مردم را ندارد
                </div>
            </div>
            
            <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:12px; margin-bottom:15px;">
                <div style="font-size:20px; font-weight:700; color:{COLORS['gold']}; margin-bottom:10px;">✗ فدراسیون آزاد</div>
                <div style="font-size:17px; line-height:1.6;">
                    شوراهای محلی خودمختار به جای دولت مرکزی
                </div>
            </div>
            
            <div style="text-align:center; margin-top:20px; font-size:15px; font-style:italic; color:{COLORS['gold_light']};">
                "قدرت سیاسی و ثروت همواره دست به دست هم می‌دهند"
            </div>
        </div>
    </foreignObject>
    
    <!-- Bottom Outcome Box -->
    <rect x="100" y="990" width="880" height="180" rx="16" fill="{COLORS['red_left']}" opacity="0.9"/>
    <foreignObject x="120" y="1010" width="840" height="150">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:24px; font-weight:800; margin-bottom:12px;">📊 نتیجه تاریخی</div>
            <div style="font-size:19px; line-height:1.7;">
                مارکس باکونین را از انترناسیونال اخراج کرد (۱۸۷۲)<br/>
                اما تاریخ به باکونین حق داد: دولت‌های «کارگری» به استبداد تبدیل شدند<br/>
                <span style="color:{COLORS['gold_light']};">این جدال هنوز ادامه دارد: دولت ابزار رهایی است یا مانع؟</span>
            </div>
        </div>
    </foreignObject>
    
    <!-- Page Number -->
    <circle cx="540" cy="1280" r="28" fill="{COLORS['gold']}"/>
    <text x="540" y="1290" text-anchor="middle" font-size="22" font-weight="700" fill="#1a1a1a">۸</text>
</svg>'''
    return svg


def create_slide_9_burke_vs_paine():
    """Famous Debate: Burke vs Paine"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="oldDebateGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#2C1810;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#1A0F0A;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#oldDebateGrad)"/>
    
    <!-- Decorative paper texture -->
    <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="url(#oldDebateGrad)" opacity="0.3"/>
    
    <!-- Vintage Banner -->
    <rect x="100" y="50" width="880" height="90" rx="10" fill="#D4AF37" opacity="0.9"/>
    <foreignObject x="120" y="65" width="840" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#1A0F0A; font-size:28px; font-weight:900; line-height:70px;">
            📜 نخستین مناظره بزرگ: چپ و راست متولد می‌شوند (۱۷۹۰)
        </div>
    </foreignObject>
    
    <!-- Context Box -->
    <rect x="80" y="170" width="920" height="100" rx="12" fill="rgba(255,255,255,0.1)"/>
    <foreignObject x="100" y="185" width="880" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['gold_light']}; font-size:20px; line-height:1.6;">
            پس از انقلاب فرانسه (۱۷۸۹)، دو متفکر بریتانیایی<br/>
            مناظره‌ای آغاز کردند که بنیان تفکر سیاسی مدرن را شکل داد
        </div>
    </foreignObject>
    
    <!-- Burke Side -->
    <rect x="60" y="300" width="460" height="750" rx="16" fill="#F5F5DC" opacity="0.95"/>
    <rect x="60" y="300" width="460" height="80" rx="16" fill="{COLORS['navy']}"/>
    <foreignObject x="70" y="320" width="440" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:26px; font-weight:800;">
            ⚖️ محافظه‌کار (راست)
        </div>
    </foreignObject>
    
    <!-- Burke Portrait -->
    <circle cx="290" cy="430" r="55" fill="{COLORS['navy']}" opacity="0.2"/>
    <text x="290" y="450" text-anchor="middle" font-size="70">🧔</text>
    
    <foreignObject x="80" y="510" width="420" height="520">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#1a1a1a;">
            <div style="text-align:center; font-size:28px; font-weight:800; color:{COLORS['navy']}; margin-bottom:15px;">
                ادموند برک
            </div>
            <div style="text-align:center; font-size:16px; color:#666; margin-bottom:20px;">
                Reflections on the Revolution (۱۷۹۰)
            </div>
            
            <div style="background:{COLORS['navy']}; color:white; padding:12px; border-radius:10px; margin-bottom:12px;">
                <div style="font-size:18px; font-weight:700; margin-bottom:8px;">🏛️ سنت برتر از عقل است</div>
                <div style="font-size:15px; opacity:0.9;">
                    نسل‌ها تجربه انباشته کرده‌اند که نباید با یک انقلاب نابود شود
                </div>
            </div>
            
            <div style="background:{COLORS['navy']}; color:white; padding:12px; border-radius:10px; margin-bottom:12px;">
                <div style="font-size:18px; font-weight:700; margin-bottom:8px;">⚠️ خطر عقل‌گرایی افراطی</div>
                <div style="font-size:15px; opacity:0.9;">
                    انقلاب فرانسه به خونریزی و آنارشی منجر خواهد شد
                </div>
            </div>
            
            <div style="background:{COLORS['navy']}; color:white; padding:12px; border-radius:10px; margin-bottom:12px;">
                <div style="font-size:18px; font-weight:700; margin-bottom:8px;">👑 نقش اشراف</div>
                <div style="font-size:15px; opacity:0.9;">
                    نخبگان با فرهنگ، جامعه را از هرج‌ومرج حفظ می‌کنند
                </div>
            </div>
            
            <div style="border-right:4px solid {COLORS['gold']}; padding:10px; background:rgba(26,35,126,0.05); font-size:14px; font-style:italic; margin-top:15px;">
                "جامعه قراردادی بین زندگان، مردگان و نامتولدان است"
            </div>
        </div>
    </foreignObject>
    
    <!-- Paine Side -->
    <rect x="560" y="300" width="460" height="750" rx="16" fill="#F5F5DC" opacity="0.95"/>
    <rect x="560" y="300" width="460" height="80" rx="16" fill="{COLORS['red_left']}"/>
    <foreignObject x="570" y="320" width="440" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:26px; font-weight:800;">
            🔥 رادیکال (چپ)
        </div>
    </foreignObject>
    
    <!-- Paine Portrait -->
    <circle cx="790" cy="430" r="55" fill="{COLORS['red_left']}" opacity="0.2"/>
    <text x="790" y="450" text-anchor="middle" font-size="70">✍️</text>
    
    <foreignObject x="580" y="510" width="420" height="520">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#1a1a1a;">
            <div style="text-align:center; font-size:28px; font-weight:800; color:{COLORS['red_left']}; margin-bottom:15px;">
                توماس پین
            </div>
            <div style="text-align:center; font-size:16px; color:#666; margin-bottom:20px;">
                Rights of Man (۱۷۹۱)
            </div>
            
            <div style="background:{COLORS['red_left']}; color:white; padding:12px; border-radius:10px; margin-bottom:12px;">
                <div style="font-size:18px; font-weight:700; margin-bottom:8px;">✊ حقوق طبیعی</div>
                <div style="font-size:15px; opacity:0.9;">
                    هر نسلی حق دارد حکومت خود را انتخاب کند، نه وراث گذشته
                </div>
            </div>
            
            <div style="background:{COLORS['red_left']}; color:white; padding:12px; border-radius:10px; margin-bottom:12px;">
                <div style="font-size:18px; font-weight:700; margin-bottom:8px;">🗽 دموکراسی و عقل</div>
                <div style="font-size:15px; opacity:0.9;">
                    سنت‌های کهنه اغلب توجیه ظلم و نابرابری هستند
                </div>
            </div>
            
            <div style="background:{COLORS['red_left']}; color:white; padding:12px; border-radius:10px; margin-bottom:12px;">
                <div style="font-size:18px; font-weight:700; margin-bottom:8px;">⚖️ برابری انسان‌ها</div>
                <div style="font-size:15px; opacity:0.9;">
                    هیچ کس به دلیل خانواده‌اش حق حکومت بر دیگران را ندارد
                </div>
            </div>
            
            <div style="border-right:4px solid {COLORS['gold']}; padding:10px; background:rgba(200,30,30,0.05); font-size:14px; font-style:italic; margin-top:15px;">
                "زمان‌ها عوض می‌شوند و با آن‌ها باید نظام‌ها نیز عوض شوند"
            </div>
        </div>
    </foreignObject>
    
    <!-- Bottom Legacy Box -->
    <rect x="80" y="1080" width="920" height="190" rx="16" fill="{COLORS['gold']}" opacity="0.95"/>
    <foreignObject x="100" y="1100" width="880" height="160">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#1A0F0A;">
            <div style="font-size:26px; font-weight:900; margin-bottom:12px;">🎯 میراث تاریخی</div>
            <div style="font-size:18px; line-height:1.8; font-weight:500;">
                این مناظره الگوی همه بحث‌های چپ-راست شد:<br/>
                <span style="font-weight:700;">سنت vs تغییر | تدریج vs انقلاب | نظم vs آزادی</span><br/>
                هر دو کتاب میلیون‌ها نسخه فروخته شد و دو جریان فکری را پایه‌گذاری کرد
            </div>
        </div>
    </foreignObject>
    
    <!-- Page Number -->
    <circle cx="540" cy="1295" r="28" fill="{COLORS['gold']}"/>
    <text x="540" y="1305" text-anchor="middle" font-size="22" font-weight="700" fill="#1A0F0A">۹</text>
</svg>'''
    return svg


def create_slide_10_side_switchers():
    """Scholars Who Switched Sides"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="switchGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{COLORS['red_left']};stop-opacity:0.3" />
            <stop offset="50%" style="stop-color:#424242;stop-opacity:1" />
            <stop offset="100%" style="stop-color:{COLORS['navy']};stop-opacity:0.3" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="#1a1a1a"/>
    
    <!-- Gradient overlay -->
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#switchGrad)" opacity="0.6"/>
    
    <!-- Header -->
    <rect x="100" y="50" width="880" height="100" rx="20" fill="{COLORS['purple']}" opacity="0.9"/>
    <foreignObject x="120" y="70" width="840" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:36px; font-weight:900;">🔄 کسانی که طرف عوض کردند</div>
            <div style="font-size:20px; opacity:0.9; margin-top:5px;">از چپ به راست و بالعکس</div>
        </div>
    </foreignObject>
    
    <!-- Switcher Card 1: Mussolini -->
    <rect x="60" y="180" width="960" height="210" rx="16" fill="white" opacity="0.95"/>
    <circle cx="130" cy="285" r="45" fill="{COLORS['red_left']}"/>
    <text x="130" y="300" text-anchor="middle" font-size="50">👤</text>
    <path d="M 185 285 L 230 285" stroke="{COLORS['gold']}" stroke-width="4" marker-end="url(#arrowGold)"/>
    <circle cx="275" cy="285" r="45" fill="{COLORS['purple']}"/>
    <text x="275" y="300" text-anchor="middle" font-size="50">👤</text>
    
    <foreignObject x="340" y="200" width="660" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#1a1a1a;">
            <div style="font-size:26px; font-weight:800; color:{COLORS['purple']}; margin-bottom:8px;">
                بنیتو موسولینی (۱۸۸۳-۱۹۴۵)
            </div>
            <div style="font-size:18px; line-height:1.6; color:#333;">
                <span style="color:{COLORS['red_left']}; font-weight:700;">سوسیالیست رادیکال</span> ← 
                <span style="color:{COLORS['purple']}; font-weight:700;">بنیان‌گذار فاشیسم</span><br/>
                <span style="font-size:16px; color:#666;">دلیل: ناامیدی از بین‌الملل‌گرایی + باور به قدرت ملت</span>
            </div>
            <div style="background:#FFF3E0; padding:8px 12px; border-radius:8px; margin-top:10px; font-size:15px; color:#E65100;">
                💬 "از مارکس آموختم چگونه انقلاب کنم، اما نه برای کدام طبقه"
            </div>
        </div>
    </foreignObject>
    
    <!-- Switcher Card 2: Christopher Hitchens -->
    <rect x="60" y="410" width="960" height="210" rx="16" fill="white" opacity="0.95"/>
    <circle cx="130" cy="515" r="45" fill="{COLORS['red_left']}"/>
    <text x="130" y="530" text-anchor="middle" font-size="50">📝</text>
    <path d="M 185 515 L 230 515" stroke="{COLORS['gold']}" stroke-width="4"/>
    <circle cx="275" cy="515" r="45" fill="{COLORS['navy']}"/>
    <text x="275" y="530" text-anchor="middle" font-size="50">📝</text>
    
    <foreignObject x="340" y="430" width="660" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#1a1a1a;">
            <div style="font-size:26px; font-weight:800; color:{COLORS['navy']}; margin-bottom:8px;">
                کریستوفر هیچنز (۱۹۴۹-۲۰۱۱)
            </div>
            <div style="font-size:18px; line-height:1.6; color:#333;">
                <span style="color:{COLORS['red_left']}; font-weight:700;">تروتسکیست</span> ← 
                <span style="color:{COLORS['navy']}; font-weight:700;">حامی جنگ عراق</span><br/>
                <span style="font-size:16px; color:#666;">دلیل: مبارزه با اسلام‌گرایی + دفاع از روشنگری</span>
            </div>
            <div style="background:#E3F2FD; padding:8px 12px; border-radius:8px; margin-top:10px; font-size:15px; color:#1565C0;">
                💬 "در مقابل فاشیسم مذهبی، من همچنان چپم"
            </div>
        </div>
    </foreignObject>
    
    <!-- Switcher Card 3: David Horowitz -->
    <rect x="60" y="640" width="960" height="210" rx="16" fill="white" opacity="0.95"/>
    <circle cx="130" cy="745" r="45" fill="{COLORS['red_left']}"/>
    <text x="130" y="760" text-anchor="middle" font-size="50">✊</text>
    <path d="M 185 745 L 230 745" stroke="{COLORS['gold']}" stroke-width="4"/>
    <circle cx="275" cy="745" r="45" fill="{COLORS['navy']}"/>
    <text x="275" y="760" text-anchor="middle" font-size="50">🇺🇸</text>
    
    <foreignObject x="340" y="660" width="660" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#1a1a1a;">
            <div style="font-size:26px; font-weight:800; color:{COLORS['navy']}; margin-bottom:8px;">
                دیوید هورویتز (۱۹۳۹-)
            </div>
            <div style="font-size:18px; line-height:1.6; color:#333;">
                <span style="color:{COLORS['red_left']}; font-weight:700;">مارکسیست و فعال چپ نو</span> ← 
                <span style="color:{COLORS['navy']}; font-weight:700;">نومحافظه‌کار</span><br/>
                <span style="font-size:16px; color:#666;">دلیل: دیدن خشونت پلنگ سیاهان + سقوط شوروی</span>
            </div>
            <div style="background:#E3F2FD; padding:8px 12px; border-radius:8px; margin-top:10px; font-size:15px; color:#1565C0;">
                💬 "چپ نه برای فقرا، بلکه برای قدرت می‌جنگد"
            </div>
        </div>
    </foreignObject>
    
    <!-- Reverse Direction Example -->
    <rect x="60" y="870" width="960" height="210" rx="16" fill="white" opacity="0.95"/>
    <circle cx="130" cy="975" r="45" fill="{COLORS['navy']}"/>
    <text x="130" y="990" text-anchor="middle" font-size="50">🎩</text>
    <path d="M 185 975 L 230 975" stroke="{COLORS['gold']}" stroke-width="4"/>
    <circle cx="275" cy="975" r="45" fill="{COLORS['emerald']}"/>
    <text x="275" y="990" text-anchor="middle" font-size="50">🌹</text>
    
    <foreignObject x="340" y="890" width="660" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#1a1a1a;">
            <div style="font-size:26px; font-weight:800; color:{COLORS['emerald']}; margin-bottom:8px;">
                جرج اورول (۱۹۰۳-۱۹۵۰)
            </div>
            <div style="font-size:18px; line-height:1.6; color:#333;">
                <span style="color:{COLORS['navy']}; font-weight:700;">محافظه‌کار سنتی</span> → 
                <span style="color:{COLORS['emerald']}; font-weight:700;">سوسیالیست دموکراتیک</span><br/>
                <span style="font-size:16px; color:#666;">دلیل: مشاهده فقر در لندن + تجربه جنگ داخلی اسپانیا</span>
            </div>
            <div style="background:#E8F5E9; padding:8px 12px; border-radius:8px; margin-top:10px; font-size:15px; color:#2E7D32;">
                💬 "هر خط که نوشته‌ام علیه توتالیتاریسم بوده، اما برای سوسیالیسم دموکراتیک"
            </div>
        </div>
    </foreignObject>
    
    <!-- Bottom Insight -->
    <rect x="80" y="1100" width="920" height="140" rx="16" fill="{COLORS['gold']}" opacity="0.15"/>
    <rect x="80" y="1100" width="920" height="140" rx="16" fill="none" stroke="{COLORS['gold']}" stroke-width="2"/>
    <foreignObject x="100" y="1120" width="880" height="110">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:20px; line-height:1.7;">
            💡 <span style="font-weight:700; color:{COLORS['gold']};">درس تاریخی:</span><br/>
            ایدئولوژی‌ها ثابت نیستند. تجربیات شخصی، رویدادهای تاریخی،<br/>
            و تحولات فکری می‌توانند حتی متعهدترین افراد را تغییر جهت دهند
        </div>
    </foreignObject>
    
    <!-- Page Number -->
    <circle cx="540" cy="1280" r="28" fill="{COLORS['purple']}"/>
    <text x="540" y="1290" text-anchor="middle" font-size="20" font-weight="700" fill="white">۱۰</text>
    
    <!-- Arrow marker definition -->
    <defs>
        <marker id="arrowGold" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto">
            <polygon points="0,0 10,5 0,10" fill="{COLORS['gold']}" />
        </marker>
    </defs>
</svg>'''
    return svg


def create_slide_11_hayek_vs_keynes():
    """Famous Debate: Hayek vs Keynes"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="#1a1a2e"/>
    
    <!-- Title Banner -->
    <rect x="60" y="40" width="960" height="110" rx="16" fill="{COLORS['gold']}"/>
    <foreignObject x="80" y="60" width="920" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#1a1a1a;">
            <div style="font-size:40px; font-weight:900;">💰 نبرد قرن: هایک علیه کینز</div>
            <div style="font-size:20px; font-weight:600; margin-top:5px;">مناظره‌ای که جهان اقتصاد را دوشکاف کرد (۱۹۳۰-۱۹۴۰)</div>
        </div>
    </foreignObject>
    
    <!-- Context Box -->
    <rect x="80" y="170" width="920" height="80" rx="12" fill="rgba(249,168,37,0.1)"/>
    <foreignObject x="100" y="185" width="880" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['gold_light']}; font-size:19px; line-height:1.5;">
            <strong>بحران بزرگ ۱۹۲۹:</strong> آیا دولت باید دخالت کند یا بازار خود را اصلاح می‌کند؟
        </div>
    </foreignObject>
    
    <!-- Hayek Side -->
    <rect x="60" y="270" width="460" height="680" rx="16" fill="white" opacity="0.05"/>
    <rect x="60" y="270" width="460" height="680" rx="16" fill="none" stroke="{COLORS['navy']}" stroke-width="3"/>
    
    <circle cx="290" cy="340" r="55" fill="{COLORS['navy']}"/>
    <text x="290" y="360" text-anchor="middle" font-size="60" fill="white">👴</text>
    
    <foreignObject x="80" y="410" width="420" height="520">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:white;">
            <div style="text-align:center; font-size:30px; font-weight:800; color:{COLORS['navy_light']}; margin-bottom:10px;">
                فردریش هایک
            </div>
            <div style="text-align:center; font-size:16px; color:#aaa; margin-bottom:20px;">
                "راه بردگی" (۱۹۴۴)
            </div>
            
            <div style="background:rgba(26,35,126,0.3); padding:14px; border-radius:12px; border-right:4px solid {COLORS['navy']}; margin-bottom:14px;">
                <div style="font-size:19px; font-weight:700; margin-bottom:8px;">🧠 دانش پراکنده</div>
                <div style="font-size:16px; line-height:1.6;">
                    هیچ برنامه‌ریز مرکزی نمی‌تواند اطلاعات میلیون‌ها فرد را بداند
                </div>
            </div>
            
            <div style="background:rgba(26,35,126,0.3); padding:14px; border-radius:12px; border-right:4px solid {COLORS['navy']}; margin-bottom:14px;">
                <div style="font-size:19px; font-weight:700; margin-bottom:8px;">💼 بازار خودتنظیم</div>
                <div style="font-size:16px; line-height:1.6;">
                    رکود بخشی از چرخه است. دخالت دولت آن را بدتر می‌کند
                </div>
            </div>
            
            <div style="background:rgba(26,35,126,0.3); padding:14px; border-radius:12px; border-right:4px solid {COLORS['navy']}; margin-bottom:14px;">
                <div style="font-size:19px; font-weight:700; margin-bottom:8px;">⚠️ هشدار توتالیتاریسم</div>
                <div style="font-size:16px; line-height:1.6;">
                    برنامه‌ریزی اقتصادی به استبداد سیاسی منجر می‌شود
                </div>
            </div>
            
            <div style="background:{COLORS['gold']}; color:#1a1a1a; padding:12px; border-radius:10px; text-align:center; font-size:15px; font-style:italic; margin-top:15px;">
                "به سوی برده‌داری می‌رویم، حتی با بهترین نیت‌ها"
            </div>
        </div>
    </foreignObject>
    
    <!-- VS Symbol -->
    <circle cx="540" cy="610" r="65" fill="{COLORS['gold']}"/>
    <text x="540" y="635" text-anchor="middle" font-size="50" font-weight="900" fill="#1a1a1a">VS</text>
    
    <!-- Keynes Side -->
    <rect x="560" y="270" width="460" height="680" rx="16" fill="white" opacity="0.05"/>
    <rect x="560" y="270" width="460" height="680" rx="16" fill="none" stroke="{COLORS['emerald']}" stroke-width="3"/>
    
    <circle cx="790" cy="340" r="55" fill="{COLORS['emerald']}"/>
    <text x="790" y="360" text-anchor="middle" font-size="60" fill="white">🎩</text>
    
    <foreignObject x="580" y="410" width="420" height="520">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:white;">
            <div style="text-align:center; font-size:30px; font-weight:800; color:{COLORS['emerald_light']}; margin-bottom:10px;">
                جان مینارد کینز
            </div>
            <div style="text-align:center; font-size:16px; color:#aaa; margin-bottom:20px;">
                "نظریه عمومی" (۱۹۳۶)
            </div>
            
            <div style="background:rgba(46,125,50,0.3); padding:14px; border-radius:12px; border-right:4px solid {COLORS['emerald']}; margin-bottom:14px;">
                <div style="font-size:19px; font-weight:700; margin-bottom:8px;">📉 بازار ناکارآمد است</div>
                <div style="font-size:16px; line-height:1.6;">
                    رکود می‌تواند سال‌ها ادامه یابد. بیکاری انبوه فاجعه است
                </div>
            </div>
            
            <div style="background:rgba(46,125,50,0.3); padding:14px; border-radius:12px; border-right:4px solid {COLORS['emerald']}; margin-bottom:14px;">
                <div style="font-size:19px; font-weight:700; margin-bottom:8px;">💉 دخالت ضروری</div>
                <div style="font-size:16px; line-height:1.6;">
                    دولت باید با هزینه‌کرد تقاضا را تحریک و اقتصاد را نجات دهد
                </div>
            </div>
            
            <div style="background:rgba(46,125,50,0.3); padding:14px; border-radius:12px; border-right:4px solid {COLORS['emerald']}; margin-bottom:14px;">
                <div style="font-size:19px; font-weight:700; margin-bottom:8px;">⏱️ کوتاه‌مدت مهم است</div>
                <div style="font-size:16px; line-height:1.6;">
                    منتظر «بلندمدت» نمانیم؛ در بلندمدت همه مرده‌ایم!
                </div>
            </div>
            
            <div style="background:{COLORS['gold']}; color:#1a1a1a; padding:12px; border-radius:10px; text-align:center; font-size:15px; font-style:italic; margin-top:15px;">
                "بازار می‌تواند بی‌منطق بماند بیش از آنکه شما بتوانید بی‌پول بمانید"
            </div>
        </div>
    </foreignObject>
    
    <!-- Winner Box -->
    <rect x="80" y="970" width="920" height="200" rx="16" fill="{COLORS['emerald']}" opacity="0.9"/>
    <foreignObject x="100" y="990" width="880" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:28px; font-weight:900; margin-bottom:15px;">🏆 چه کسی برنده شد؟</div>
            <div style="font-size:20px; line-height:1.8; font-weight:500;">
                <strong style="color:{COLORS['gold']};">۱۹۴۵-۱۹۷۵:</strong> کینز پیروز بود (دولت رفاه، رشد اقتصادی)<br/>
                <strong style="color:{COLORS['gold']};">۱۹۸۰-۲۰۰۸:</strong> هایک برگشت (نئولیبرالیسم، تاچر و ریگان)<br/>
                <strong style="color:{COLORS['gold']};">۲۰۰۸-امروز:</strong> کینز دوباره مد شد (بحران مالی + کرونا)
            </div>
        </div>
    </foreignObject>
    
    <!-- Bottom note -->
    <foreignObject x="60" y="1190" width="960" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['gold_light']}; font-size:18px; line-height:1.6;">
            📖 این مناظره هنوز ادامه دارد. هر بحران اقتصادی آن را دوباره زنده می‌کند
        </div>
    </foreignObject>
    
    <!-- Page Number -->
    <circle cx="540" cy="1295" r="28" fill="{COLORS['gold']}"/>
    <text x="540" y="1305" text-anchor="middle" font-size="20" font-weight="700" fill="#1a1a1a">۱۱</text>
</svg>'''
    return svg


# CONTINUATION OF PREVIOUS CODE...

def create_slide_7_economic_spectrum2():
    """Economic Systems Comparison - COMPLETED"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="econGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:{COLORS['red_left']};stop-opacity:1" />
            <stop offset="50%" style="stop-color:{COLORS['emerald']};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{COLORS['navy']};stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="#F5F5F5"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="{WIDTH}" height="140" fill="{COLORS['navy']}"/>
    <foreignObject x="40" y="40" width="1000" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:38px; font-weight:800;">
            💰 طیف اقتصادی: از برنامه‌ریزی تا بازار آزاد
        </div>
    </foreignObject>
    
    <!-- Spectrum Bar -->
    <rect x="60" y="180" width="960" height="30" rx="15" fill="url(#econGrad)"/>
    
    <!-- Spectrum Labels -->
    <foreignObject x="40" y="220" width="200" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:{COLORS['red_left']}; font-size:16px; font-weight:700;">
            اقتصاد برنامه‌ریزی شده
        </div>
    </foreignObject>
    <foreignObject x="440" y="220" width="200" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['emerald']}; font-size:16px; font-weight:700;">
            اقتصاد مختلط
        </div>
    </foreignObject>
    <foreignObject x="820" y="220" width="200" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:left; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:16px; font-weight:700;">
            بازار آزاد
        </div>
    </foreignObject>
    
    <!-- System Cards -->
    <!-- Card 1: Command Economy -->
    <rect x="60" y="280" width="300" height="260" rx="12" fill="white" filter="drop-shadow(0 3px 10px rgba(0,0,0,0.1))"/>
    <rect x="60" y="280" width="300" height="55" rx="12" fill="{COLORS['red_left']}"/>
    <rect x="60" y="325" width="300" height="10" fill="{COLORS['red_left']}"/>
    <foreignObject x="70" y="290" width="280" height="45">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:20px; font-weight:700;">
            اقتصاد دستوری
        </div>
    </foreignObject>
    <foreignObject x="70" y="350" width="280" height="180">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#333; font-size:16px; line-height:1.7;">
            <div style="margin-bottom:8px;">✓ مالکیت دولتی</div>
            <div style="margin-bottom:8px;">✓ برنامه‌ریزی متمرکز</div>
            <div style="margin-bottom:8px;">✓ قیمت‌گذاری دولتی</div>
            <div style="color:#888; font-size:14px; margin-top:12px;">
                نمونه: شوروی، کوبا
            </div>
        </div>
    </foreignObject>
    
    <!-- Card 2: Mixed Economy -->
    <rect x="390" y="280" width="300" height="260" rx="12" fill="white" filter="drop-shadow(0 3px 10px rgba(0,0,0,0.1))"/>
    <rect x="390" y="280" width="300" height="55" rx="12" fill="{COLORS['emerald']}"/>
    <rect x="390" y="325" width="300" height="10" fill="{COLORS['emerald']}"/>
    <foreignObject x="400" y="290" width="280" height="45">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:20px; font-weight:700;">
            اقتصاد مختلط
        </div>
    </foreignObject>
    <foreignObject x="400" y="350" width="280" height="180">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#333; font-size:16px; line-height:1.7;">
            <div style="margin-bottom:8px;">✓ بازار + دولت رفاه</div>
            <div style="margin-bottom:8px;">✓ تنظیم‌گری دولتی</div>
            <div style="margin-bottom:8px;">✓ خدمات عمومی</div>
            <div style="color:#888; font-size:14px; margin-top:12px;">
                نمونه: سوئد، آلمان
            </div>
        </div>
    </foreignObject>
    
    <!-- Card 3: Free Market -->
    <rect x="720" y="280" width="300" height="260" rx="12" fill="white" filter="drop-shadow(0 3px 10px rgba(0,0,0,0.1))"/>
    <rect x="720" y="280" width="300" height="55" rx="12" fill="{COLORS['navy']}"/>
    <rect x="720" y="325" width="300" height="10" fill="{COLORS['navy']}"/>
    <foreignObject x="730" y="290" width="280" height="45">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:20px; font-weight:700;">
            بازار آزاد
        </div>
    </foreignObject>
    <foreignObject x="730" y="350" width="280" height="180">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:#333; font-size:16px; line-height:1.7;">
            <div style="margin-bottom:8px;">✓ مالکیت خصوصی</div>
            <div style="margin-bottom:8px;">✓ حداقل دخالت دولت</div>
            <div style="margin-bottom:8px;">✓ رقابت آزاد</div>
            <div style="color:#888; font-size:14px; margin-top:12px;">
                نمونه: هنگ‌کنگ، سنگاپور
            </div>
        </div>
    </foreignObject>
    
    <!-- Big Debate Box -->
    <rect x="60" y="580" width="960" height="200" rx="16" fill="#FFF3E0" stroke="{COLORS['orange']}" stroke-width="2"/>
    <foreignObject x="80" y="600" width="920" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="color:{COLORS['orange']}; font-size:24px; font-weight:800; text-align:center; margin-bottom:15px;">
                ⚔️ مناظره بزرگ: میزس-هایک در برابر لانگه
            </div>
            <div style="color:#333; font-size:18px; line-height:1.7; text-align:center;">
                آیا سوسیالیسم می‌تواند بدون قیمت‌های بازار، منابع را به‌درستی تخصیص دهد؟<br/>
                <span style="color:{COLORS['red_left']};">لانگه:</span> بله، با شبیه‌سازی بازار<br/>
                <span style="color:{COLORS['navy']};">هایک:</span> نه، دانش در بازار پراکنده است
            </div>
        </div>
    </foreignObject>
    
    <!-- Key Quote -->
    <rect x="60" y="820" width="960" height="160" rx="16" fill="{COLORS['navy']}" opacity="0.05"/>
    <foreignObject x="80" y="840" width="920" height="130">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn;">
            <div style="color:{COLORS['navy']}; font-size:26px; font-style:italic; line-height:1.6;">
                «مسئله اقتصادی جامعه، مسئله استفاده از دانشی است<br/>که به هیچ‌کس به‌صورت کامل داده نشده است»
            </div>
            <div style="color:#666; font-size:18px; margin-top:15px;">— فردریش هایک</div>
        </div>
    </foreignObject>
    
    <!-- CTA -->
    <foreignObject x="60" y="1020" width="960" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['emerald']}; font-size:22px; font-weight:600;">
            📖 فصل ۳: اقتصاد سیاسی و جدال بنیادین
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_8_marx_vs_bakunin():
    """Famous Debate: Marx vs Bakunin"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="debateGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#1a1a2e;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#16213e;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#debateGrad)"/>
    
    <!-- Decorative VS -->
    <text x="540" y="750" text-anchor="middle" font-size="400" font-weight="900" fill="white" opacity="0.03">VS</text>
    
    <!-- Header Badge -->
    <rect x="290" y="50" width="500" height="60" rx="30" fill="{COLORS['gold']}" opacity="0.9"/>
    <foreignObject x="290" y="50" width="500" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:24px; font-weight:800; line-height:60px;">
            ⚔️ مناظرات تاریخی
        </div>
    </foreignObject>
    
    <!-- Title -->
    <foreignObject x="40" y="140" width="1000" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:38px; font-weight:900;">
            مارکس در برابر باکونین
        </div>
    </foreignObject>
    
    <foreignObject x="80" y="220" width="920" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['gold']}; font-size:22px;">
            انترناسیونال اول • ۱۸۶۴-۱۸۷۶
        </div>
    </foreignObject>
    
    <!-- Marx Card -->
    <rect x="60" y="300" width="450" height="480" rx="20" fill="white" opacity="0.95"/>
    <rect x="60" y="300" width="450" height="100" rx="20" fill="{COLORS['red_left']}"/>
    <rect x="60" y="385" width="450" height="15" fill="{COLORS['red_left']}"/>
    
    <circle cx="285" cy="350" r="55" fill="white" stroke="{COLORS['gold']}" stroke-width="4"/>
    <text x="285" y="368" text-anchor="middle" font-size="60">👨‍🦳</text>
    
    <foreignObject x="80" y="420" width="410" height="350">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; text-align:center;">
            <div style="color:{COLORS['red_left']}; font-size:28px; font-weight:800;">کارل مارکس</div>
            <div style="color:#666; font-size:16px; margin:10px 0;">کمونیسم علمی</div>
            
            <div style="text-align:right; margin-top:20px; color:#333; font-size:18px; line-height:1.8;">
                <div style="margin-bottom:10px;">✦ انقلاب باید متمرکز باشد</div>
                <div style="margin-bottom:10px;">✦ دیکتاتوری پرولتاریا ضروری است</div>
                <div style="margin-bottom:10px;">✦ دولت پس از انقلاب زوال می‌یابد</div>
                <div style="margin-bottom:10px;">✦ حزب پیشاهنگ رهبری کند</div>
            </div>
            
            <div style="background:#FFEBEE; padding:15px; border-radius:10px; margin-top:15px; font-size:16px; color:{COLORS['red_left']}; font-style:italic;">
                «آزادی بدون سوسیالیسم، امتیاز و بی‌عدالتی است»
            </div>
        </div>
    </foreignObject>
    
    <!-- VS Circle -->
    <circle cx="540" cy="540" r="45" fill="{COLORS['gold']}" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.3))"/>
    <text x="540" y="552" text-anchor="middle" font-size="28" font-weight="900" fill="{COLORS['navy']}">VS</text>
    
    <!-- Bakunin Card -->
    <rect x="570" y="300" width="450" height="480" rx="20" fill="white" opacity="0.95"/>
    <rect x="570" y="300" width="450" height="100" rx="20" fill="#212121"/>
    <rect x="570" y="385" width="450" height="15" fill="#212121"/>
    
    <circle cx="795" cy="350" r="55" fill="white" stroke="{COLORS['gold']}" stroke-width="4"/>
    <text x="795" y="368" text-anchor="middle" font-size="60">🧔</text>
    
    <foreignObject x="590" y="420" width="410" height="350">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; text-align:center;">
            <div style="color:#212121; font-size:28px; font-weight:800;">میخائیل باکونین</div>
            <div style="color:#666; font-size:16px; margin:10px 0;">آنارشیسم جمعی</div>
            
            <div style="text-align:right; margin-top:20px; color:#333; font-size:18px; line-height:1.8;">
                <div style="margin-bottom:10px;">✦ هر دولتی سرکوبگر است</div>
                <div style="margin-bottom:10px;">✦ انقلاب باید از پایین باشد</div>
                <div style="margin-bottom:10px;">✦ فدرالیسم و خودگردانی</div>
                <div style="margin-bottom:10px;">✦ نابودی فوری دولت</div>
            </div>
            
            <div style="background:#F5F5F5; padding:15px; border-radius:10px; margin-top:15px; font-size:16px; color:#212121; font-style:italic;">
                «سوسیالیسم بدون آزادی، بردگی و بربریت است»
            </div>
        </div>
    </foreignObject>
    
    <!-- Outcome Box -->
    <rect x="60" y="820" width="960" height="180" rx="16" fill="rgba(255,255,255,0.1)" stroke="{COLORS['gold']}" stroke-width="2"/>
    <foreignObject x="80" y="840" width="920" height="150">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:white; text-align:center;">
            <div style="font-size:22px; font-weight:700; color:{COLORS['gold']}; margin-bottom:15px;">📜 نتیجه تاریخی</div>
            <div style="font-size:18px; line-height:1.7;">
                مارکس پیروز شد و باکونین اخراج شد، اما پیش‌بینی باکونین درست از آب درآمد:<br/>
                <span style="color:{COLORS['gold']};">«دیکتاتوری پرولتاریا به دیکتاتوری بر پرولتاریا تبدیل خواهد شد»</span>
            </div>
        </div>
    </foreignObject>
    
    <!-- Page Footer -->
    <foreignObject x="60" y="1030" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.5); font-size:18px;">
            فصل ۴ و ۶: سوسیالیسم و آنارشیسم
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_9_burke_vs_paine():
    """Famous Debate: Burke vs Paine"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['off_white']}"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="{WIDTH}" height="180" fill="{COLORS['navy']}"/>
    <foreignObject x="40" y="30" width="1000" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:22px; color:{COLORS['gold']}; margin-bottom:10px;">⚔️ مناظره‌ای که جهان را شکل داد</div>
            <div style="font-size:42px; font-weight:900;">برک در برابر پین</div>
            <div style="font-size:20px; opacity:0.8; margin-top:10px;">۱۷۹۰-۱۷۹۲ | انقلاب فرانسه</div>
        </div>
    </foreignObject>
    
    <!-- Context Box -->
    <rect x="60" y="210" width="960" height="100" rx="12" fill="{COLORS['gold']}" opacity="0.15"/>
    <foreignObject x="80" y="230" width="920" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['dark_gray']}; font-size:20px; line-height:1.6;">
            وقتی انقلاب فرانسه شعله‌ور شد، دو دوست قدیمی به دو دشمن فکری تبدیل شدند.<br/>
            این مناظره، تولد رسمی <span style="color:{COLORS['navy']}; font-weight:700;">محافظه‌کاری</span> و <span style="color:{COLORS['red_left']}; font-weight:700;">رادیکالیسم</span> مدرن بود.
        </div>
    </foreignObject>
    
    <!-- Burke Side -->
    <rect x="60" y="340" width="460" height="520" rx="16" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.1))"/>
    <rect x="60" y="340" width="460" height="8" rx="4" fill="{COLORS['navy']}"/>
    
    <foreignObject x="80" y="370" width="420" height="480">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="text-align:center; margin-bottom:20px;">
                <div style="font-size:50px;">🎩</div>
                <div style="color:{COLORS['navy']}; font-size:28px; font-weight:800;">ادموند برک</div>
                <div style="color:#666; font-size:16px;">محافظه‌کار</div>
            </div>
            
            <div style="background:#E8EAF6; padding:15px; border-radius:10px; margin-bottom:15px;">
                <div style="color:{COLORS['navy']}; font-weight:700; font-size:18px; margin-bottom:10px;">📖 تأملاتی درباره انقلاب فرانسه (۱۷۹۰)</div>
            </div>
            
            <div style="color:#333; font-size:17px; line-height:1.8;">
                <div style="margin-bottom:12px;">✦ سنت خرد انباشته نسل‌هاست</div>
                <div style="margin-bottom:12px;">✦ تغییر باید تدریجی باشد</div>
                <div style="margin-bottom:12px;">✦ انقلاب به ترور می‌انجامد</div>
                <div style="margin-bottom:12px;">✦ نهادها را نباید ویران کرد</div>
            </div>
            
            <div style="background:{COLORS['navy']}; color:white; padding:15px; border-radius:10px; margin-top:15px; font-style:italic; font-size:16px; text-align:center;">
                «مردم هرگز حق ندارند آنچه را که دریافت کرده‌اند ویران کنند»
            </div>
        </div>
    </foreignObject>
    
    <!-- VS Connector -->
    <rect x="490" y="580" width="100" height="60" rx="30" fill="{COLORS['gold']}"/>
    <foreignObject x="490" y="580" width="100" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:24px; font-weight:900; line-height:60px;">
            VS
        </div>
    </foreignObject>
    
    <!-- Paine Side -->
    <rect x="560" y="340" width="460" height="520" rx="16" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.1))"/>
    <rect x="560" y="340" width="460" height="8" rx="4" fill="{COLORS['red_left']}"/>
    
    <foreignObject x="580" y="370" width="420" height="480">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="text-align:center; margin-bottom:20px;">
                <div style="font-size:50px;">✊</div>
                <div style="color:{COLORS['red_left']}; font-size:28px; font-weight:800;">توماس پین</div>
                <div style="color:#666; font-size:16px;">رادیکال</div>
            </div>
            
            <div style="background:#FFEBEE; padding:15px; border-radius:10px; margin-bottom:15px;">
                <div style="color:{COLORS['red_left']}; font-weight:700; font-size:18px; margin-bottom:10px;">📖 حقوق انسان (۱۷۹۱)</div>
            </div>
            
            <div style="color:#333; font-size:17px; line-height:1.8;">
                <div style="margin-bottom:12px;">✦ هر نسل حق تعیین سرنوشت دارد</div>
                <div style="margin-bottom:12px;">✦ سنت توجیه ظلم نیست</div>
                <div style="margin-bottom:12px;">✦ حقوق طبیعی مقدم است</div>
                <div style="margin-bottom:12px;">✦ جمهوری بر سلطنت برتر است</div>
            </div>
            
            <div style="background:{COLORS['red_left']}; color:white; padding:15px; border-radius:10px; margin-top:15px; font-style:italic; font-size:16px; text-align:center;">
                «حکومت مردگان بر زندگان مشروع نیست»
            </div>
        </div>
    </foreignObject>
    
    <!-- Legacy Box -->
    <rect x="60" y="890" width="960" height="130" rx="12" fill="{COLORS['emerald']}" opacity="0.1"/>
    <foreignObject x="80" y="910" width="920" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn;">
            <div style="color:{COLORS['emerald']}; font-size:20px; font-weight:700; margin-bottom:10px;">🌍 میراث این مناظره</div>
            <div style="color:#333; font-size:17px; line-height:1.6;">
                این دو کتاب هنوز مرجع اصلی بحث بین محافظه‌کاران و رادیکال‌هاست.<br/>
                هر دو حق داشتند: انقلاب به ترور انجامید، اما نهایتاً دموکراسی پیروز شد.
            </div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="1050" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#999; font-size:18px;">
            فصل ۱: زایش طیف سیاسی | فصل ۹: محافظه‌کاری
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_10_keynes_vs_hayek():
    """Famous Debate: Keynes vs Hayek"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="econDebate" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#1B5E20;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#2E7D32;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#econDebate)"/>
    
    <!-- Decorative Elements -->
    <text x="540" y="700" text-anchor="middle" font-size="500" font-weight="900" fill="white" opacity="0.03">💰</text>
    
    <!-- Header -->
    <foreignObject x="40" y="50" width="1000" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:22px; color:{COLORS['gold_light']};">⚔️ نبرد قرن در اقتصاد</div>
            <div style="font-size:46px; font-weight:900; margin-top:10px;">کینز در برابر هایک</div>
        </div>
    </foreignObject>
    
    <!-- Timeline Bar -->
    <rect x="100" y="190" width="880" height="8" rx="4" fill="rgba(255,255,255,0.3)"/>
    <circle cx="200" cy="194" r="12" fill="{COLORS['gold']}"/>
    <circle cx="540" cy="194" r="12" fill="{COLORS['gold']}"/>
    <circle cx="880" cy="194" r="12" fill="{COLORS['gold']}"/>
    
    <foreignObject x="140" y="210" width="120" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:white; font-size:14px;">۱۹۳۰</div>
    </foreignObject>
    <foreignObject x="480" y="210" width="120" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:white; font-size:14px;">۱۹۴۵</div>
    </foreignObject>
    <foreignObject x="820" y="210" width="120" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:white; font-size:14px;">۱۹۸۰</div>
    </foreignObject>
    
    <!-- Main Cards -->
    <!-- Keynes -->
    <rect x="60" y="270" width="460" height="420" rx="20" fill="white" opacity="0.95"/>
    <foreignObject x="80" y="290" width="420" height="390">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="text-align:center;">
                <div style="font-size:50px;">🎓</div>
                <div style="color:{COLORS['emerald']}; font-size:26px; font-weight:800;">جان مینارد کینز</div>
                <div style="color:#666; font-size:15px;">۱۸۸۳-۱۹۴۶</div>
            </div>
            
            <div style="margin-top:20px; color:#333; font-size:17px; line-height:1.8;">
                <div style="font-weight:700; color:{COLORS['emerald']}; margin-bottom:10px;">💡 ایده اصلی:</div>
                <div style="margin-bottom:8px;">✦ بازار می‌تواند شکست بخورد</div>
                <div style="margin-bottom:8px;">✦ دولت باید تقاضا را مدیریت کند</div>
                <div style="margin-bottom:8px;">✦ در بحران، خرج کنید!</div>
                <div style="margin-bottom:8px;">✦ بیکاری قابل درمان است</div>
            </div>
            
            <div style="background:#E8F5E9; padding:12px; border-radius:10px; margin-top:15px;">
                <div style="color:{COLORS['emerald']}; font-size:15px; font-weight:600;">📈 دوره سلطه: ۱۹۴۵-۱۹۷۵</div>
                <div style="color:#666; font-size:14px; margin-top:5px;">عصر طلایی سرمایه‌داری</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- VS -->
    <circle cx="540" cy="480" r="40" fill="{COLORS['gold']}" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.3))"/>
    <text x="540" y="492" text-anchor="middle" font-size="24" font-weight="900" fill="{COLORS['navy']}">VS</text>
    
    <!-- Hayek -->
    <rect x="560" y="270" width="460" height="420" rx="20" fill="white" opacity="0.95"/>
    <foreignObject x="580" y="290" width="420" height="390">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="text-align:center;">
                <div style="font-size:50px;">📊</div>
                <div style="color:{COLORS['navy']}; font-size:26px; font-weight:800;">فردریش هایک</div>
                <div style="color:#666; font-size:15px;">۱۸۹۹-۱۹۹۲</div>
            </div>
            
            <div style="margin-top:20px; color:#333; font-size:17px; line-height:1.8;">
                <div style="font-weight:700; color:{COLORS['navy']}; margin-bottom:10px;">💡 ایده اصلی:</div>
                <div style="margin-bottom:8px;">✦ بازار خودتنظیم است</div>
                <div style="margin-bottom:8px;">✦ دخالت دولت بدتر می‌کند</div>
                <div style="margin-bottom:8px;">✦ دانش در بازار پراکنده است</div>
                <div style="margin-bottom:8px;">✦ آزادی اقتصادی = آزادی سیاسی</div>
            </div>
            
            <div style="background:#E8EAF6; padding:12px; border-radius:10px; margin-top:15px;">
                <div style="color:{COLORS['navy']}; font-size:15px; font-weight:600;">📈 دوره سلطه: ۱۹۸۰-۲۰۰۸</div>
                <div style="color:#666; font-size:14px; margin-top:5px;">عصر نئولیبرالیسم</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Scoreboard -->
    <rect x="60" y="720" width="960" height="200" rx="16" fill="rgba(255,255,255,0.1)" stroke="white" stroke-width="2"/>
    <foreignObject x="80" y="740" width="920" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:white;">
            <div style="text-align:center; font-size:22px; font-weight:700; color:{COLORS['gold_light']}; margin-bottom:15px;">
                🏆 چه کسی پیروز شد؟
            </div>
            <div style="display:flex; justify-content:space-around; text-align:center;">
                <div style="flex:1;">
                    <div style="font-size:36px; font-weight:800;">{COLORS['emerald']}</div>
                    <div style="font-size:18px;">کینز</div>
                    <div style="font-size:14px; opacity:0.8;">۱۹۴۵-۱۹۷۵</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:36px; font-weight:800;">⚖️</div>
                    <div style="font-size:18px;">امروز</div>
                    <div style="font-size:14px; opacity:0.8;">ترکیب هر دو</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:36px; font-weight:800;">{COLORS['navy']}</div>
                    <div style="font-size:18px;">هایک</div>
                    <div style="font-size:14px; opacity:0.8;">۱۹۸۰-۲۰۰۸</div>
                </div>
            </div>
            <div style="text-align:center; margin-top:15px; font-size:16px; opacity:0.9;">
                بحران ۲۰۰۸ نشان داد: نه بازار کامل است، نه دولت!
            </div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="950" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.6); font-size:18px;">
            فصل ۳: اقتصاد سیاسی | فصل ۱۰: لیبرالیسم و نئولیبرالیسم
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_11_intellectual_converts():
    """Scholars Who Changed Sides"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['off_white']}"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="{WIDTH}" height="160" fill="{COLORS['purple']}"/>
    <foreignObject x="40" y="40" width="1000" height="110">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:42px; font-weight:900;">🔄 روشنفکرانی که طرف عوض کردند</div>
            <div style="font-size:20px; opacity:0.9; margin-top:10px;">چرا برخی از چپ به راست رفتند و برخی برعکس؟</div>
        </div>
    </foreignObject>
    
    <!-- Convert 1: Christopher Hitchens -->
    <rect x="60" y="200" width="960" height="220" rx="16" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.08))"/>
    <rect x="60" y="200" width="12" height="220" rx="6" fill="{COLORS['red_left']}"/>
    <rect x="1008" y="200" width="12" height="220" rx="6" fill="{COLORS['navy']}"/>
    
    <foreignObject x="90" y="220" width="900" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:20px;">
                <div style="text-align:center;">
                    <div style="font-size:50px;">🗣️</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:24px; font-weight:800; color:{COLORS['dark_gray']};">کریستوفر هیچنز</div>
                    <div style="font-size:16px; color:#666; margin:5px 0;">روزنامه‌نگار و نویسنده | ۱۹۴۹-۲۰۱۱</div>
                    <div style="display:flex; align-items:center; gap:10px; margin:15px 0;">
                        <span style="background:{COLORS['red_left']}; color:white; padding:5px 15px; border-radius:15px; font-size:14px;">تروتسکیست</span>
                        <span style="font-size:24px;">→</span>
                        <span style="background:{COLORS['navy']}; color:white; padding:5px 15px; border-radius:15px; font-size:14px;">نومحافظه‌کار</span>
                    </div>
                </div>
            </div>
            <div style="background:#FFF3E0; padding:12px; border-radius:10px; margin-top:10px;">
                <div style="color:{COLORS['orange']}; font-weight:700; font-size:16px;">💡 دلیل تغییر:</div>
                <div style="color:#333; font-size:15px; margin-top:5px;">۱۱ سپتامبر و مخالفت با اسلام‌گرایی، حمایت از جنگ عراق، نقد چپ نسبی‌گرا</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Convert 2: Irving Kristol -->
    <rect x="60" y="450" width="960" height="220" rx="16" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.08))"/>
    <rect x="60" y="450" width="12" height="220" rx="6" fill="{COLORS['red_left']}"/>
    <rect x="1008" y="450" width="12" height="220" rx="6" fill="{COLORS['navy']}"/>
    
    <foreignObject x="90" y="470" width="900" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:20px;">
                <div style="text-align:center;">
                    <div style="font-size:50px;">📚</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:24px; font-weight:800; color:{COLORS['dark_gray']};">اروینگ کریستول</div>
                    <div style="font-size:16px; color:#666; margin:5px 0;">پدرخوانده نومحافظه‌کاری | ۱۹۲۰-۲۰۰۹</div>
                    <div style="display:flex; align-items:center; gap:10px; margin:15px 0;">
                        <span style="background:{COLORS['red_left']}; color:white; padding:5px 15px; border-radius:15px; font-size:14px;">تروتسکیست</span>
                        <span style="font-size:24px;">→</span>
                        <span style="background:{COLORS['navy']}; color:white; padding:5px 15px; border-radius:15px; font-size:14px;">نومحافظه‌کار</span>
                    </div>
                </div>
            </div>
            <div style="background:#FFF3E0; padding:12px; border-radius:10px; margin-top:10px;">
                <div style="color:{COLORS['orange']}; font-weight:700; font-size:16px;">💡 دلیل تغییر:</div>
                <div style="color:#333; font-size:15px; margin-top:5px;">«نومحافظه‌کار، لیبرالی است که واقعیت به او حمله کرده» - انتقاد از دولت رفاه و نسبی‌گرایی اخلاقی</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Convert 3: Reverse - David Horowitz -->
    <rect x="60" y="700" width="960" height="220" rx="16" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.08))"/>
    <rect x="60" y="700" width="12" height="220" rx="6" fill="{COLORS['red_left']}"/>
    <rect x="1008" y="700" width="12" height="220" rx="6" fill="{COLORS['orange']}"/>
    
    <foreignObject x="90" y="720" width="900" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:20px;">
                <div style="text-align:center;">
                    <div style="font-size:50px;">✍️</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:24px; font-weight:800; color:{COLORS['dark_gray']};">دیوید هوروویتس</div>
                    <div style="font-size:16px; color:#666; margin:5px 0;">فعال سیاسی و نویسنده | متولد ۱۹۳۹</div>
                    <div style="display:flex; align-items:center; gap:10px; margin:15px 0;">
                        <span style="background:{COLORS['red_left']}; color:white; padding:5px 15px; border-radius:15px; font-size:14px;">چپ رادیکال</span>
                        <span style="font-size:24px;">→</span>
                        <span style="background:{COLORS['orange']}; color:white; padding:5px 15px; border-radius:15px; font-size:14px;">راست افراطی</span>
                    </div>
                </div>
            </div>
            <div style="background:#FFF3E0; padding:12px; border-radius:10px; margin-top:10px;">
                <div style="color:{COLORS['orange']}; font-weight:700; font-size:16px;">💡 دلیل تغییر:</div>
                <div style="color:#333; font-size:15px; margin-top:5px;">قتل دوستش توسط پلنگ‌های سیاه، سرخوردگی از خشونت چپ رادیکال، انتقاد از دانشگاه‌های چپ‌گرا</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Analysis Box -->
    <rect x="60" y="950" width="960" height="150" rx="16" fill="{COLORS['purple']}" opacity="0.1"/>
    <foreignObject x="80" y="970" width="920" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn;">
            <div style="color:{COLORS['purple']}; font-size:20px; font-weight:700; margin-bottom:10px;">🔍 الگوی مشترک</div>
            <div style="color:#333; font-size:17px; line-height:1.6;">
                بیشتر تغییر جهت‌ها از چپ به راست بوده و معمولاً پس از:<br/>
                <span style="color:{COLORS['purple']}; font-weight:600;">سرخوردگی از آرمان‌ها • مواجهه با خشونت • نقد نسبی‌گرایی</span>
            </div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="1120" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#999; font-size:18px;">
            ضمیمه ۲: شخصیت‌نامه ۱۰۰ چهره کلیدی
        </div>
    </foreignObject>
</svg>'''
    return svg

# CONTINUATION FROM WHERE WE LEFT OFF...

def create_slide_12_left_to_right_stories():
    """More Conversion Stories - Left to Right - COMPLETED"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="convGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:{COLORS['red_left']};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{COLORS['navy']};stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="#1a1a2e"/>
    
    <!-- Header -->
    <foreignObject x="40" y="50" width="1000" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:40px; font-weight:900;">🔄 سفر از چپ به راست</div>
            <div style="font-size:20px; color:{COLORS['gold']}; margin-top:10px;">داستان‌های واقعی تغییر ایدئولوژیک</div>
        </div>
    </foreignObject>
    
    <!-- Arrow -->
    <rect x="100" y="180" width="880" height="20" rx="10" fill="url(#convGrad)"/>
    <polygon points="980,190 950,170 950,210" fill="{COLORS['navy']}"/>
    
    <!-- Mussolini Card -->
    <rect x="60" y="240" width="470" height="280" rx="16" fill="rgba(255,255,255,0.95)"/>
    <foreignObject x="80" y="260" width="430" height="250">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px; margin-bottom:15px;">
                <div style="font-size:45px;">⚡</div>
                <div>
                    <div style="font-size:22px; font-weight:800; color:{COLORS['dark_gray']};">بنیتو موسولینی</div>
                    <div style="font-size:14px; color:#666;">۱۸۸۳-۱۹۴۵</div>
                </div>
            </div>
            <div style="display:flex; gap:10px; margin-bottom:15px;">
                <span style="background:{COLORS['red_left']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">سوسیالیست</span>
                <span style="font-size:18px;">→</span>
                <span style="background:#212121; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">فاشیست</span>
            </div>
            <div style="color:#333; font-size:15px; line-height:1.7;">
                سردبیر روزنامه سوسیالیست‌ها بود، اما جنگ جهانی اول او را متحول کرد. ملی‌گرایی جای طبقه‌گرایی را گرفت.
            </div>
            <div style="background:#FFEBEE; padding:10px; border-radius:8px; margin-top:12px;">
                <div style="color:{COLORS['red_left']}; font-size:13px; font-style:italic;">«فاشیسم، سوسیالیسمی است که به ملت رسیده»</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Chambers Card -->
    <rect x="550" y="240" width="470" height="280" rx="16" fill="rgba(255,255,255,0.95)"/>
    <foreignObject x="570" y="260" width="430" height="250">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px; margin-bottom:15px;">
                <div style="font-size:45px;">🕵️</div>
                <div>
                    <div style="font-size:22px; font-weight:800; color:{COLORS['dark_gray']};">ویتیکر چمبرز</div>
                    <div style="font-size:14px; color:#666;">۱۹۰۱-۱۹۶۱</div>
                </div>
            </div>
            <div style="display:flex; gap:10px; margin-bottom:15px;">
                <span style="background:{COLORS['red_left']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">جاسوس شوروی</span>
                <span style="font-size:18px;">→</span>
                <span style="background:{COLORS['navy']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">ضدکمونیست</span>
            </div>
            <div style="color:#333; font-size:15px; line-height:1.7;">
                جاسوس شوروی که توبه کرد. کتابش «شاهد» انجیل محافظه‌کاری آمریکایی شد.
            </div>
            <div style="background:#E8EAF6; padding:10px; border-radius:8px; margin-top:12px;">
                <div style="color:{COLORS['navy']}; font-size:13px; font-style:italic;">«از طرف بازنده به طرف برنده گذشتم... نه، از برنده به بازنده»</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Orwell Card -->
    <rect x="60" y="550" width="470" height="280" rx="16" fill="rgba(255,255,255,0.95)"/>
    <foreignObject x="80" y="570" width="430" height="250">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px; margin-bottom:15px;">
                <div style="font-size:45px;">✍️</div>
                <div>
                    <div style="font-size:22px; font-weight:800; color:{COLORS['dark_gray']};">جورج اورول</div>
                    <div style="font-size:14px; color:#666;">۱۹۰۳-۱۹۵۰</div>
                </div>
            </div>
            <div style="display:flex; gap:10px; margin-bottom:15px;">
                <span style="background:{COLORS['red_left']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">سوسیالیست</span>
                <span style="font-size:18px;">⚠️</span>
                <span style="background:{COLORS['emerald']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">منتقد چپ اقتدارگرا</span>
            </div>
            <div style="color:#333; font-size:15px; line-height:1.7;">
                تا آخر سوسیالیست ماند، اما تجربه جنگ اسپانیا و استالینیسم او را به منتقد سرسخت توتالیتاریسم چپ تبدیل کرد.
            </div>
            <div style="background:#E8F5E9; padding:10px; border-radius:8px; margin-top:12px;">
                <div style="color:{COLORS['emerald']}; font-size:13px; font-style:italic;">«همه حیوانات برابرند، اما بعضی برابرترند»</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Hayek Card -->
    <rect x="550" y="550" width="470" height="280" rx="16" fill="rgba(255,255,255,0.95)"/>
    <foreignObject x="570" y="570" width="430" height="250">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px; margin-bottom:15px;">
                <div style="font-size:45px;">📊</div>
                <div>
                    <div style="font-size:22px; font-weight:800; color:{COLORS['dark_gray']};">فردریش هایک</div>
                    <div style="font-size:14px; color:#666;">۱۸۹۹-۱۹۹۲</div>
                </div>
            </div>
            <div style="display:flex; gap:10px; margin-bottom:15px;">
                <span style="background:{COLORS['emerald']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">سوسیالیست فابیان</span>
                <span style="font-size:18px;">→</span>
                <span style="background:{COLORS['gold']}; color:{COLORS['navy']}; padding:4px 12px; border-radius:12px; font-size:13px;">لیبرال کلاسیک</span>
            </div>
            <div style="color:#333; font-size:15px; line-height:1.7;">
                در جوانی سوسیالیست بود، اما تأثیر میزس و مطالعه اقتصاد اتریشی او را به مدافع سرسخت بازار آزاد تبدیل کرد.
            </div>
            <div style="background:#FFF8E1; padding:10px; border-radius:8px; margin-top:12px;">
                <div style="color:#B8860B; font-size:13px; font-style:italic;">«کسی که در ۲۰ سالگی سوسیالیست نباشد، قلب ندارد...»</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Bottom Insight -->
    <rect x="60" y="870" width="960" height="130" rx="16" fill="rgba(249,168,37,0.15)" stroke="{COLORS['gold']}" stroke-width="2"/>
    <foreignObject x="80" y="890" width="920" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn;">
            <div style="color:{COLORS['gold']}; font-size:22px; font-weight:700;">🧠 بینش کلیدی</div>
            <div style="color:white; font-size:17px; line-height:1.6; margin-top:10px;">
                تجربه عملی ایدئولوژی‌ها — نه فقط نظریه‌ها — عامل اصلی تغییر فکری روشنفکران بوده است.
            </div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="1030" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.5); font-size:16px;">
            📖 ادامه در اسلاید بعدی...
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_13_right_to_left_stories():
    """Scholars Who Moved Right to Left"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="convGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:{COLORS['navy']};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{COLORS['red_left']};stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="#0d1b2a"/>
    
    <!-- Header -->
    <foreignObject x="40" y="50" width="1000" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:40px; font-weight:900;">🔄 سفر از راست به چپ</div>
            <div style="font-size:20px; color:{COLORS['gold']}; margin-top:10px;">و کسانی که در هیچ طیفی نگنجیدند</div>
        </div>
    </foreignObject>
    
    <!-- Reverse Arrow -->
    <rect x="100" y="180" width="880" height="20" rx="10" fill="url(#convGrad2)"/>
    <polygon points="100,190 130,170 130,210" fill="{COLORS['red_left']}"/>
    
    <!-- Engels Card -->
    <rect x="60" y="240" width="470" height="250" rx="16" fill="rgba(255,255,255,0.95)"/>
    <foreignObject x="80" y="260" width="430" height="220">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px; margin-bottom:12px;">
                <div style="font-size:45px;">🏭</div>
                <div>
                    <div style="font-size:22px; font-weight:800; color:{COLORS['dark_gray']};">فردریش انگلس</div>
                    <div style="font-size:14px; color:#666;">۱۸۲۰-۱۸۹۵</div>
                </div>
            </div>
            <div style="display:flex; gap:10px; margin-bottom:12px;">
                <span style="background:{COLORS['navy']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">وارث کارخانه‌دار</span>
                <span style="font-size:18px;">→</span>
                <span style="background:{COLORS['red_left']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">کمونیست</span>
            </div>
            <div style="color:#333; font-size:15px; line-height:1.7;">
                پسر یک صنعتگر ثروتمند که با دیدن فقر کارگران منچستر، به مبارز انقلابی تبدیل شد و با پول خانواده، مارکس را تأمین مالی کرد.
            </div>
            <div style="background:#FFEBEE; padding:8px; border-radius:8px; margin-top:10px;">
                <div style="color:{COLORS['red_left']}; font-size:13px; font-style:italic;">«وضعیت طبقه کارگر در انگلستان» - ۱۸۴۵</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Kropotkin Card -->
    <rect x="550" y="240" width="470" height="250" rx="16" fill="rgba(255,255,255,0.95)"/>
    <foreignObject x="570" y="260" width="430" height="220">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px; margin-bottom:12px;">
                <div style="font-size:45px;">👑</div>
                <div>
                    <div style="font-size:22px; font-weight:800; color:{COLORS['dark_gray']};">پیوتر کروپوتکین</div>
                    <div style="font-size:14px; color:#666;">۱۸۴۲-۱۹۲۱</div>
                </div>
            </div>
            <div style="display:flex; gap:10px; margin-bottom:12px;">
                <span style="background:{COLORS['navy']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">شاهزاده روس</span>
                <span style="font-size:18px;">→</span>
                <span style="background:#212121; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">آنارشیست</span>
            </div>
            <div style="color:#333; font-size:15px; line-height:1.7;">
                شاهزاده‌ای که عنوان اشرافیت را رد کرد و زندگی خود را وقف مبارزه با دولت و سرمایه‌داری نمود. نظریه «کمک متقابل» را در برابر داروینیسم اجتماعی مطرح کرد.
            </div>
        </div>
    </foreignObject>
    
    <!-- Noam Chomsky Card -->
    <rect x="60" y="520" width="470" height="250" rx="16" fill="rgba(255,255,255,0.95)"/>
    <foreignObject x="80" y="540" width="430" height="220">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px; margin-bottom:12px;">
                <div style="font-size:45px;">🎤</div>
                <div>
                    <div style="font-size:22px; font-weight:800; color:{COLORS['dark_gray']};">نائومی کلاین</div>
                    <div style="font-size:14px; color:#666;">متولد ۱۹۷۰</div>
                </div>
            </div>
            <div style="display:flex; gap:10px; margin-bottom:12px;">
                <span style="background:{COLORS['gold']}; color:{COLORS['navy']}; padding:4px 12px; border-radius:12px; font-size:13px;">لیبرال</span>
                <span style="font-size:18px;">→</span>
                <span style="background:{COLORS['red_left']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">چپ رادیکال</span>
            </div>
            <div style="color:#333; font-size:15px; line-height:1.7;">
                تحقیق درباره سیاست‌های نئولیبرال و «دکترین شوک» او را از لیبرالیسم به سمت سوسیالیسم دموکراتیک و اکوسوسیالیسم سوق داد.
            </div>
            <div style="background:#FFEBEE; padding:8px; border-radius:8px; margin-top:8px;">
                <div style="color:{COLORS['red_left']}; font-size:13px; font-style:italic;">«سرمایه‌داری با بقای سیاره سازگار نیست»</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Francis Fukuyama Card -->
    <rect x="550" y="520" width="470" height="250" rx="16" fill="rgba(255,255,255,0.95)"/>
    <foreignObject x="570" y="540" width="430" height="220">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px; margin-bottom:12px;">
                <div style="font-size:45px;">📖</div>
                <div>
                    <div style="font-size:22px; font-weight:800; color:{COLORS['dark_gray']};">فرانسیس فوکویاما</div>
                    <div style="font-size:14px; color:#666;">متولد ۱۹۵۲</div>
                </div>
            </div>
            <div style="display:flex; gap:10px; margin-bottom:12px;">
                <span style="background:{COLORS['navy']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">نومحافظه‌کار</span>
                <span style="font-size:18px;">→</span>
                <span style="background:{COLORS['emerald']}; color:white; padding:4px 12px; border-radius:12px; font-size:13px;">لیبرال میانه</span>
            </div>
            <div style="color:#333; font-size:15px; line-height:1.7;">
                نویسنده «پایان تاریخ» که نومحافظه‌کار بود، اما پس از فاجعه جنگ عراق از جنبش نومحافظه‌کاری فاصله گرفت و به لیبرالیسم بازگشت.
            </div>
            <div style="background:#E8F5E9; padding:8px; border-radius:8px; margin-top:8px;">
                <div style="color:{COLORS['emerald']}; font-size:13px; font-style:italic;">«نومحافظه‌کاری به لنینیسم راست تبدیل شد»</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Analysis Box -->
    <rect x="60" y="810" width="960" height="170" rx="16" fill="rgba(255,255,255,0.08)" stroke="{COLORS['gold']}" stroke-width="2"/>
    <foreignObject x="80" y="830" width="920" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:22px; font-weight:700; color:{COLORS['gold']}; margin-bottom:12px;">📊 چرا مردم طرف عوض می‌کنند؟</div>
            <div style="display:flex; justify-content:space-around; font-size:16px; margin-top:10px;">
                <div style="flex:1; padding:10px;">
                    <div style="font-size:30px; margin-bottom:5px;">😤</div>
                    <div style="color:{COLORS['gold_light']}; font-weight:600;">سرخوردگی</div>
                    <div style="opacity:0.8; font-size:14px; margin-top:5px;">از شکست آرمان‌ها</div>
                </div>
                <div style="flex:1; padding:10px;">
                    <div style="font-size:30px; margin-bottom:5px;">🌍</div>
                    <div style="color:{COLORS['gold_light']}; font-weight:600;">تجربه واقعی</div>
                    <div style="opacity:0.8; font-size:14px; margin-top:5px;">دیدن نتایج عملی</div>
                </div>
                <div style="flex:1; padding:10px;">
                    <div style="font-size:30px; margin-bottom:5px;">🔬</div>
                    <div style="color:{COLORS['gold_light']}; font-weight:600;">بازاندیشی</div>
                    <div style="opacity:0.8; font-size:14px; margin-top:5px;">تکامل فکری صادقانه</div>
                </div>
                <div style="flex:1; padding:10px;">
                    <div style="font-size:30px; margin-bottom:5px;">⚡</div>
                    <div style="color:{COLORS['gold_light']}; font-weight:600;">رویداد تاریخی</div>
                    <div style="opacity:0.8; font-size:14px; margin-top:5px;">جنگ، انقلاب، بحران</div>
                </div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="1010" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.5); font-size:16px;">
            📖 بیشتر بخوانید در فصل‌های ۸ و ۱۳ کتاب
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_14_overton_window():
    """Overton Window - Where is the Middle?"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['off_white']}"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="{WIDTH}" height="170" fill="{COLORS['navy']}"/>
    <foreignObject x="40" y="30" width="1000" height="130">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:22px; color:{COLORS['gold']};">فصل ۱۴: میانه‌روی</div>
            <div style="font-size:42px; font-weight:900; margin-top:10px;">پنجره اورتون</div>
            <div style="font-size:20px; opacity:0.8; margin-top:8px;">چگونه «میانه» جابه‌جا می‌شود؟</div>
        </div>
    </foreignObject>
    
    <!-- Overton Window Diagram -->
    <!-- Full Spectrum Bar -->
    <rect x="60" y="230" width="960" height="60" rx="8" fill="#E0E0E0"/>
    
    <!-- Zones -->
    <rect x="60" y="230" width="120" height="60" rx="8" fill="#B71C1C" opacity="0.8"/>
    <rect x="180" y="230" width="140" height="60" fill="#E53935" opacity="0.7"/>
    <rect x="320" y="230" width="160" height="60" fill="#FF8A65" opacity="0.6"/>
    <rect x="480" y="230" width="200" height="60" fill="{COLORS['emerald']}" opacity="0.7"/>
    <rect x="680" y="230" width="140" height="60" fill="#42A5F5" opacity="0.6"/>
    <rect x="820" y="230" width="120" height="60" fill="{COLORS['navy_light']}" opacity="0.7"/>
    <rect x="940" y="230" width="80" height="60" rx="8" fill="{COLORS['navy']}" opacity="0.8"/>
    
    <!-- Labels -->
    <foreignObject x="60" y="300" width="120" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:#B71C1C; font-size:11px; font-weight:700;">غیرقابل تصور</div>
    </foreignObject>
    <foreignObject x="180" y="300" width="140" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:#E53935; font-size:11px; font-weight:700;">رادیکال</div>
    </foreignObject>
    <foreignObject x="320" y="300" width="160" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:#E64A19; font-size:11px; font-weight:700;">قابل قبول</div>
    </foreignObject>
    <foreignObject x="480" y="300" width="200" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:{COLORS['emerald']}; font-size:13px; font-weight:800;">محبوب / سیاست‌گذاری</div>
    </foreignObject>
    <foreignObject x="680" y="300" width="140" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:#1565C0; font-size:11px; font-weight:700;">قابل قبول</div>
    </foreignObject>
    <foreignObject x="820" y="300" width="120" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:{COLORS['navy_light']}; font-size:11px; font-weight:700;">رادیکال</div>
    </foreignObject>
    <foreignObject x="940" y="300" width="80" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:11px; font-weight:700;">غیرقابل تصور</div>
    </foreignObject>
    
    <!-- Window Bracket -->
    <rect x="320" y="220" width="500" height="80" rx="8" fill="none" stroke="{COLORS['gold']}" stroke-width="4" stroke-dasharray="none"/>
    <foreignObject x="420" y="190" width="240" height="35">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; background:{COLORS['gold']}; color:{COLORS['navy']}; font-size:16px; font-weight:800; padding:5px; border-radius:5px;">
            🪟 پنجره اورتون
        </div>
    </foreignObject>
    
    <!-- Example Section -->
    <foreignObject x="60" y="370" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:22px; font-weight:700;">
            📌 مثال: حداقل دستمزد در آمریکا
        </div>
    </foreignObject>
    
    <!-- 1950s Window -->
    <rect x="60" y="440" width="960" height="150" rx="12" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.08))"/>
    <foreignObject x="80" y="460" width="920" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="color:{COLORS['navy']}; font-size:20px; font-weight:700; margin-bottom:10px;">🕐 دهه ۱۹۵۰ (دوره کینزی)</div>
            <div style="display:flex; gap:10px; flex-wrap:wrap; justify-content:center;">
                <span style="background:#FFEBEE; padding:8px 15px; border-radius:20px; font-size:14px; color:#B71C1C;">لغو مالکیت خصوصی ❌</span>
                <span style="background:#FFF3E0; padding:8px 15px; border-radius:20px; font-size:14px; color:#E65100;">مالیات ۹۰٪ ⚠️</span>
                <span style="background:#E8F5E9; padding:8px 15px; border-radius:20px; font-size:14px; color:{COLORS['emerald']}; font-weight:700;">حداقل دستمزد بالا ✅</span>
                <span style="background:#E8F5E9; padding:8px 15px; border-radius:20px; font-size:14px; color:{COLORS['emerald']}; font-weight:700;">دولت رفاه ✅</span>
                <span style="background:#FFF3E0; padding:8px 15px; border-radius:20px; font-size:14px; color:#E65100;">لغو حداقل دستمزد ⚠️</span>
            </div>
        </div>
    </foreignObject>
    
    <!-- Arrow Down -->
    <foreignObject x="480" y="600" width="120" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-size:30px;">⬇️</div>
    </foreignObject>
    
    <!-- 2020s Window -->
    <rect x="60" y="650" width="960" height="150" rx="12" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.08))"/>
    <foreignObject x="80" y="670" width="920" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="color:{COLORS['orange']}; font-size:20px; font-weight:700; margin-bottom:10px;">🕐 دهه ۲۰۲۰ (دوره پسانئولیبرال)</div>
            <div style="display:flex; gap:10px; flex-wrap:wrap; justify-content:center;">
                <span style="background:#FFEBEE; padding:8px 15px; border-radius:20px; font-size:14px; color:#B71C1C;">مالیات ۹۰٪ ❌</span>
                <span style="background:#FFF3E0; padding:8px 15px; border-radius:20px; font-size:14px; color:#E65100;">$۱۵ حداقل دستمزد ⚠️</span>
                <span style="background:#E8F5E9; padding:8px 15px; border-radius:20px; font-size:14px; color:{COLORS['emerald']}; font-weight:700;">مقررات‌زدایی ✅</span>
                <span style="background:#E8F5E9; padding:8px 15px; border-radius:20px; font-size:14px; color:{COLORS['emerald']}; font-weight:700;">کاهش مالیات ✅</span>
                <span style="background:#FFF3E0; padding:8px 15px; border-radius:20px; font-size:14px; color:#E65100;">دولت رفاه جامع ⚠️</span>
            </div>
        </div>
    </foreignObject>
    
    <!-- Key Insight -->
    <rect x="60" y="840" width="960" height="150" rx="16" fill="{COLORS['gold']}" opacity="0.15"/>
    <foreignObject x="80" y="860" width="920" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn;">
            <div style="color:{COLORS['navy']}; font-size:26px; font-weight:800; margin-bottom:10px;">💡 نتیجه‌گیری کلیدی</div>
            <div style="color:{COLORS['dark_gray']}; font-size:19px; line-height:1.6;">
                «میانه» یک نقطه ثابت نیست!<br/>
                میانه ۱۹۵۰ امروز <span style="color:{COLORS['red_left']}; font-weight:700;">چپ رادیکال</span> محسوب می‌شود<br/>
                و میانه ۲۰۲۰ در ۱۹۵۰ <span style="color:{COLORS['navy']}; font-weight:700;">راست افراطی</span> به نظر می‌رسید.
            </div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="1020" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#999; font-size:18px;">
            فصل ۱۴: میانه‌روی - هنر یا بی‌اصالتی؟
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_15_horseshoe_theory():
    """Horseshoe Theory & Political Models"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="modelGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#1a1a2e;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#0f3460;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#modelGrad)"/>
    
    <!-- Header -->
    <foreignObject x="40" y="40" width="1000" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:38px; font-weight:900;">🧲 نظریه نعل اسب</div>
            <div style="font-size:20px; color:{COLORS['gold']}; margin-top:8px;">آیا افراطی‌های چپ و راست شبیه هم‌اند؟</div>
        </div>
    </foreignObject>
    
    <!-- Horseshoe Diagram -->
    <path d="M 200,650 Q 200,300 540,280 Q 880,300 880,650" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="40" stroke-linecap="round"/>
    
    <!-- Gradient overlay on horseshoe -->
    <path d="M 200,650 Q 200,300 540,280" fill="none" stroke="{COLORS['red_left']}" stroke-width="35" stroke-linecap="round" opacity="0.6"/>
    <path d="Q 540,280 Q 880,300 880,650" fill="none" stroke="{COLORS['navy_light']}" stroke-width="35" stroke-linecap="round" opacity="0.6"/>
    
    <!-- Points on horseshoe -->
    <!-- Far Left -->
    <circle cx="200" cy="650" r="30" fill="{COLORS['red_left']}" stroke="white" stroke-width="3"/>
    <foreignObject x="70" y="690" width="260" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['red_light']}; font-size:18px; font-weight:700;">
            چپ افراطی<br/><span style="font-size:14px; color:rgba(255,255,255,0.7);">استالینیسم، مائوئیسم</span>
        </div>
    </foreignObject>
    
    <!-- Far Right -->
    <circle cx="880" cy="650" r="30" fill="{COLORS['navy_light']}" stroke="white" stroke-width="3"/>
    <foreignObject x="750" y="690" width="260" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#64B5F6; font-size:18px; font-weight:700;">
            راست افراطی<br/><span style="font-size:14px; color:rgba(255,255,255,0.7);">فاشیسم، نازیسم</span>
        </div>
    </foreignObject>
    
    <!-- Center Top -->
    <circle cx="540" cy="280" r="30" fill="{COLORS['emerald']}" stroke="white" stroke-width="3"/>
    <foreignObject x="410" y="210" width="260" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['emerald_light']}; font-size:18px; font-weight:700;">
            میانه / دموکراسی لیبرال
        </div>
    </foreignObject>
    
    <!-- Connection Lines between extremes -->
    <line x1="220" y1="640" x2="860" y2="640" stroke="{COLORS['gold']}" stroke-width="2" stroke-dasharray="10,5" opacity="0.5"/>
    
    <!-- Proximity Label -->
    <foreignObject x="380" y="600" width="320" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:{COLORS['gold']}; font-size:16px; font-weight:700;">
            ⚡ نقاط اشتراک: اقتدارگرایی، خشونت، تک‌حزبی
        </div>
    </foreignObject>
    
    <!-- Shared Traits Box -->
    <rect x="60" y="790" width="960" height="200" rx="16" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
    <foreignObject x="80" y="810" width="920" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; color:white;">
            <div style="text-align:center; font-size:20px; font-weight:700; color:{COLORS['gold']}; margin-bottom:15px;">
                🔍 شباهت‌های عجیب افراطی‌های چپ و راست
            </div>
            <div style="display:flex; justify-content:space-around; text-align:center; font-size:15px;">
                <div style="flex:1; padding:8px;">
                    <div style="font-size:28px; margin-bottom:5px;">👊</div>
                    <div style="font-weight:600;">خشونت انقلابی</div>
                    <div style="opacity:0.7; font-size:13px; margin-top:3px;">هر دو معتقد به تغییر قهری</div>
                </div>
                <div style="flex:1; padding:8px;">
                    <div style="font-size:28px; margin-bottom:5px;">🏛️</div>
                    <div style="font-weight:600;">تک‌حزبی</div>
                    <div style="opacity:0.7; font-size:13px; margin-top:3px;">نفی کثرت‌گرایی</div>
                </div>
                <div style="flex:1; padding:8px;">
                    <div style="font-size:28px; margin-bottom:5px;">📢</div>
                    <div style="font-weight:600;">پروپاگاندا</div>
                    <div style="opacity:0.7; font-size:13px; margin-top:3px;">کنترل رسانه و فرهنگ</div>
                </div>
                <div style="flex:1; padding:8px;">
                    <div style="font-size:28px; margin-bottom:5px;">🎯</div>
                    <div style="font-weight:600;">دشمن‌سازی</div>
                    <div style="opacity:0.7; font-size:13px; margin-top:3px;">بورژوا / یهودی / مهاجر</div>
                </div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Criticism Note -->
    <rect x="60" y="1020" width="960" height="100" rx="12" fill="rgba(239,83,80,0.15)" stroke="{COLORS['red_light']}" stroke-width="1"/>
    <foreignObject x="80" y="1035" width="920" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:16px; font-weight:600; color:{COLORS['red_light']};">⚠️ نقد: بسیاری از محققان این نظریه را ساده‌سازانه می‌دانند</div>
            <div style="font-size:14px; opacity:0.8; margin-top:5px;">تفاوت‌های اساسی در اهداف، ارزش‌ها و پایگاه اجتماعی وجود دارد</div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="1140" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.5); font-size:16px;">
            فصل ۱۷: آینده طیف سیاسی
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_16_trotsky_vs_stalin():
    """Famous Debate: Trotsky vs Stalin"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="#2c0000"/>
    
    <!-- Subtle texture -->
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#noisePattern)" opacity="0.03"/>
    
    <!-- Header -->
    <foreignObject x="40" y="40" width="1000" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:22px; color:{COLORS['gold']};">⚔️ جدال خونین درون چپ</div>
            <div style="font-size:42px; font-weight:900; margin-top:8px;">تروتسکی در برابر استالین</div>
            <div style="font-size:18px; opacity:0.7; margin-top:5px;">نبردی که سرنوشت قرن بیستم را تعیین کرد</div>
        </div>
    </foreignObject>
    
    <!-- Trotsky Card -->
    <rect x="60" y="200" width="460" height="500" rx="20" fill="rgba(255,255,255,0.95)"/>
    <rect x="60" y="200" width="460" height="8" rx="4" fill="{COLORS['red_left']}"/>
    
    <foreignObject x="80" y="220" width="420" height="470">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="text-align:center; margin-bottom:15px;">
                <div style="font-size:55px;">🔥</div>
                <div style="color:{COLORS['red_left']}; font-size:26px; font-weight:800;">لئون تروتسکی</div>
                <div style="color:#666; font-size:15px;">انقلاب مداوم</div>
            </div>
            
            <div style="color:#333; font-size:16px; line-height:1.8;">
                <div style="font-weight:700; color:{COLORS['red_left']}; margin-bottom:10px;">موضع‌گیری‌ها:</div>
                <div style="margin-bottom:8px;">✦ انقلاب باید جهانی شود</div>
                <div style="margin-bottom:8px;">✦ دموکراسی درون‌حزبی</div>
                <div style="margin-bottom:8px;">✦ نقد بوروکراسی</div>
                <div style="margin-bottom:8px;">✦ صنعتی‌سازی سریع ولی انسانی</div>
                <div style="margin-bottom:8px;">✦ ارتش سرخ را ساخت</div>
            </div>
            
            <div style="background:#FFEBEE; padding:12px; border-radius:10px; margin-top:12px;">
                <div style="color:{COLORS['red_left']}; font-size:14px; font-style:italic; text-align:center;">
                    «انقلاب خیانت شد:<br/>بوروکراسی جای طبقه کارگر نشست»
                </div>
            </div>
            
            <div style="text-align:center; margin-top:15px;">
                <span style="background:#B71C1C; color:white; padding:5px 15px; border-radius:15px; font-size:13px;">💀 ترور شد: ۱۹۴۰ مکزیک</span>
            </div>
        </div>
    </foreignObject>
    
    <!-- VS -->
    <circle cx="540" cy="450" r="45" fill="{COLORS['gold']}" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.5))"/>
    <text x="540" y="462" text-anchor="middle" font-size="28" font-weight="900" fill="#2c0000">VS</text>
    
    <!-- Stalin Card -->
    <rect x="560" y="200" width="460" height="500" rx="20" fill="rgba(255,255,255,0.95)"/>
    <rect x="560" y="200" width="460" height="8" rx="4" fill="#4A0000"/>
    
    <foreignObject x="580" y="220" width="420" height="470">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="text-align:center; margin-bottom:15px;">
                <div style="font-size:55px;">⚙️</div>
                <div style="color:#4A0000; font-size:26px; font-weight:800;">یوسف استالین</div>
                <div style="color:#666; font-size:15px;">سوسیالیسم در یک کشور</div>
            </div>
            
            <div style="color:#333; font-size:16px; line-height:1.8;">
                <div style="font-weight:700; color:#4A0000; margin-bottom:10px;">موضع‌گیری‌ها:</div>
                <div style="margin-bottom:8px;">✦ ابتدا شوروی را بسازیم</div>
                <div style="margin-bottom:8px;">✦ رهبری متمرکز ضروری است</div>
                <div style="margin-bottom:8px;">✦ صنعتی‌سازی به هر قیمت</div>
                <div style="margin-bottom:8px;">✦ اشتراکی‌سازی اجباری کشاورزی</div>
                <div style="margin-bottom:8px;">✦ پاک‌سازی مخالفان</div>
            </div>
            
            <div style="background:#F3E5F5; padding:12px; border-radius:10px; margin-top:12px;">
                <div style="color:#4A0000; font-size:14px; font-style:italic; text-align:center;">
                    «مرگ یک نفر تراژدی است،<br/>مرگ یک میلیون نفر آمار»
                </div>
            </div>
            
            <div style="text-align:center; margin-top:15px;">
                <span style="background:#4A0000; color:white; padding:5px 15px; border-radius:15px; font-size:13px;">💀 ۲۰ میلیون قربانی</span>
            </div>
        </div>
    </foreignObject>
    
    <!-- Lesson Box -->
    <rect x="60" y="740" width="960" height="200" rx="16" fill="rgba(249,168,37,0.1)" stroke="{COLORS['gold']}" stroke-width="2"/>
    <foreignObject x="80" y="760" width="920" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:22px; font-weight:700; color:{COLORS['gold']}; margin-bottom:12px;">📖 درس تاریخ</div>
            <div style="font-size:18px; line-height:1.7;">
                این جدال نشان داد که حتی درون یک ایدئولوژی واحد،<br/>
                اختلاف بر سر <span style="color:{COLORS['gold']};">قدرت</span> و <span style="color:{COLORS['gold']};">روش</span> می‌تواند مرگبار باشد.<br/><br/>
                <span style="font-size:16px; opacity:0.8;">
                    تروتسکی هشدار داد: «دیکتاتوری حزب ← دیکتاتوری دبیرکل»<br/>
                    و تاریخ حق را به او داد.
                </span>
            </div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="970" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.4); font-size:16px;">
            فصل ۵: کمونیسم - از مارکس تا مائو
        </div>
    </foreignObject>
</svg>'''
    return svg

# CONTINUATION - Completing slide 17 and remaining slides + main execution

def create_slide_17_rawls_vs_nozick():
    """Famous Debate: Rawls vs Nozick - COMPLETED"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['off_white']}"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="{WIDTH}" height="170" fill="{COLORS['purple']}"/>
    <foreignObject x="40" y="30" width="1000" height="130">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:22px; color:{COLORS['gold_light']};">⚔️ مناظره فلسفی قرن</div>
            <div style="font-size:42px; font-weight:900; margin-top:8px;">رالز در برابر نوزیک</div>
            <div style="font-size:18px; opacity:0.8; margin-top:5px;">عدالت توزیعی یا حقوق مالکیت؟ | هاروارد ۱۹۷۱-۱۹۷۴</div>
        </div>
    </foreignObject>
    
    <!-- Rawls Card -->
    <rect x="60" y="210" width="460" height="480" rx="20" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.1))"/>
    <rect x="60" y="210" width="460" height="8" rx="4" fill="{COLORS['emerald']}"/>
    
    <foreignObject x="80" y="230" width="420" height="450">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="text-align:center; margin-bottom:15px;">
                <div style="font-size:50px;">⚖️</div>
                <div style="color:{COLORS['emerald']}; font-size:26px; font-weight:800;">جان رالز</div>
                <div style="color:#666; font-size:15px;">نظریه عدالت (۱۹۷۱)</div>
            </div>
            
            <div style="background:#E8F5E9; padding:12px; border-radius:10px; margin-bottom:15px;">
                <div style="color:{COLORS['emerald']}; font-weight:700; font-size:16px;">🧪 آزمایش فکری: پرده جهل</div>
                <div style="color:#333; font-size:14px; margin-top:5px;">اگر نمی‌دانستید ثروتمند یا فقیر به دنیا می‌آیید، چه قوانینی می‌خواستید؟</div>
            </div>
            
            <div style="color:#333; font-size:16px; line-height:1.8;">
                <div style="margin-bottom:8px;">✦ آزادی‌های پایه برابر برای همه</div>
                <div style="margin-bottom:8px;">✦ نابرابری فقط اگر به نفع ضعیف‌ترین‌ها باشد</div>
                <div style="margin-bottom:8px;">✦ فرصت‌های برابر واقعی</div>
                <div style="margin-bottom:8px;">✦ بازتوزیع ثروت مشروع است</div>
            </div>
            
            <div style="background:{COLORS['emerald']}; color:white; padding:12px; border-radius:10px; margin-top:12px; text-align:center; font-style:italic; font-size:15px;">
                «عدالت، نخستین فضیلت نهادهای اجتماعی است»
            </div>
        </div>
    </foreignObject>
    
    <!-- VS -->
    <rect x="490" y="420" width="100" height="60" rx="30" fill="{COLORS['gold']}"/>
    <foreignObject x="490" y="420" width="100" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:24px; font-weight:900; line-height:60px;">VS</div>
    </foreignObject>
    
    <!-- Nozick Card -->
    <rect x="560" y="210" width="460" height="480" rx="20" fill="white" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.1))"/>
    <rect x="560" y="210" width="460" height="8" rx="4" fill="{COLORS['gold']}"/>
    
    <foreignObject x="580" y="230" width="420" height="450">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="text-align:center; margin-bottom:15px;">
                <div style="font-size:50px;">🏛️</div>
                <div style="color:#B8860B; font-size:26px; font-weight:800;">رابرت نوزیک</div>
                <div style="color:#666; font-size:15px;">آنارشی، دولت و آرمان‌شهر (۱۹۷۴)</div>
            </div>
            
            <div style="background:#FFF8E1; padding:12px; border-radius:10px; margin-bottom:15px;">
                <div style="color:#B8860B; font-weight:700; font-size:16px;">🧪 آزمایش فکری: ویلت چمبرلین</div>
                <div style="color:#333; font-size:14px; margin-top:5px;">اگر مردم داوطلبانه پولشان را به کسی بدهند، دولت حق مصادره ندارد</div>
            </div>
            
            <div style="color:#333; font-size:16px; line-height:1.8;">
                <div style="margin-bottom:8px;">✦ حقوق مالکیت مقدم بر عدالت توزیعی</div>
                <div style="margin-bottom:8px;">✦ دولت حداقلی (فقط حفاظت)</div>
                <div style="margin-bottom:8px;">✦ مالیات = کار اجباری</div>
                <div style="margin-bottom:8px;">✦ عدالت در فرآیند، نه نتیجه</div>
            </div>
            
            <div style="background:#B8860B; color:white; padding:12px; border-radius:10px; margin-top:12px; text-align:center; font-style:italic; font-size:15px;">
                «افراد حقوقی دارند و هیچ‌کس حق تجاوز به آن‌ها را ندارد»
            </div>
        </div>
    </foreignObject>
    
    <!-- Key Difference Box -->
    <rect x="60" y="720" width="960" height="160" rx="16" fill="{COLORS['purple']}" opacity="0.08"/>
    <foreignObject x="80" y="740" width="920" height="130">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; text-align:center;">
            <div style="color:{COLORS['purple']}; font-size:22px; font-weight:700; margin-bottom:12px;">🎯 تفاوت بنیادین</div>
            <div style="display:flex; justify-content:space-around;">
                <div style="flex:1; padding:10px;">
                    <div style="color:{COLORS['emerald']}; font-weight:700; font-size:17px;">رالز (چپ لیبرال)</div>
                    <div style="color:#555; font-size:15px; margin-top:5px;">عدالت = نتیجه منصفانه</div>
                    <div style="color:#555; font-size:15px;">فقر ناعادلانه است حتی اگر کسی مقصر نباشد</div>
                </div>
                <div style="width:2px; background:{COLORS['purple']}; opacity:0.3;"></div>
                <div style="flex:1; padding:10px;">
                    <div style="color:#B8860B; font-weight:700; font-size:17px;">نوزیک (لیبرتارین)</div>
                    <div style="color:#555; font-size:15px; margin-top:5px;">عدالت = فرآیند منصفانه</div>
                    <div style="color:#555; font-size:15px;">اگر کسب قانونی بود، نتیجه عادلانه است</div>
                </div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Fun Fact -->
    <rect x="60" y="910" width="960" height="100" rx="12" fill="{COLORS['gold']}" opacity="0.15"/>
    <foreignObject x="80" y="925" width="920" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn;">
            <div style="color:{COLORS['dark_gray']}; font-size:18px; line-height:1.6;">
                🤝 <span style="font-weight:700;">نکته جالب:</span> رالز و نوزیک هر دو استاد هاروارد بودند و دفتر کارشان کنار هم بود!<br/>
                با وجود اختلافات فکری عمیق، دوستان صمیمی باقی ماندند.
            </div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="1040" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#999; font-size:18px;">
            فصل ۲: فلسفه و معرفت‌شناسی | فصل ۱۱: لیبرتارینیسم
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_18_shocking_facts():
    """Shocking Facts & Statistics"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="factGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#0D0D0D;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#1a1a2e;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#factGrad)"/>
    
    <!-- Header -->
    <foreignObject x="40" y="40" width="1000" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:42px; font-weight:900;">⚡ حقایق شگفت‌انگیز</div>
            <div style="font-size:20px; color:{COLORS['gold']}; margin-top:8px;">اعداد و ارقامی که باورتان نمی‌شود</div>
        </div>
    </foreignObject>
    
    <!-- Fact 1 -->
    <rect x="60" y="180" width="460" height="220" rx="16" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
    <foreignObject x="80" y="200" width="420" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:70px; font-weight:900; color:{COLORS['gold']};">۲۳۵</div>
            <div style="font-size:18px; font-weight:600; margin-top:10px;">سال از تولد مفهوم چپ و راست</div>
            <div style="font-size:14px; opacity:0.6; margin-top:8px;">از مجلس ملی فرانسه ۱۷۸۹ تا امروز</div>
        </div>
    </foreignObject>
    
    <!-- Fact 2 -->
    <rect x="560" y="180" width="460" height="220" rx="16" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
    <foreignObject x="580" y="200" width="420" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:70px; font-weight:900; color:{COLORS['red_light']};">۱۰۰+</div>
            <div style="font-size:18px; font-weight:600; margin-top:10px;">میلیون قربانی ایدئولوژی‌ها</div>
            <div style="font-size:14px; opacity:0.6; margin-top:8px;">فاشیسم + کمونیسم در قرن بیستم</div>
        </div>
    </foreignObject>
    
    <!-- Fact 3 -->
    <rect x="60" y="430" width="460" height="220" rx="16" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
    <foreignObject x="80" y="450" width="420" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:70px; font-weight:900; color:{COLORS['emerald_light']};">۸۰٪</div>
            <div style="font-size:18px; font-weight:600; margin-top:10px;">مردم خود را «میانه» می‌دانند</div>
            <div style="font-size:14px; opacity:0.6; margin-top:8px;">اما تعریف میانه هر ده سال تغییر می‌کند</div>
        </div>
    </foreignObject>
    
    <!-- Fact 4 -->
    <rect x="560" y="430" width="460" height="220" rx="16" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
    <foreignObject x="580" y="450" width="420" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:70px; font-weight:900; color:{COLORS['purple_light']};">۱۷</div>
            <div style="font-size:18px; font-weight:600; margin-top:10px;">فصل تحلیلی در این کتاب</div>
            <div style="font-size:14px; opacity:0.6; margin-top:8px;">از انقلاب فرانسه تا آینده طیف سیاسی</div>
        </div>
    </foreignObject>
    
    <!-- Fact 5 -->
    <rect x="60" y="680" width="460" height="220" rx="16" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
    <foreignObject x="80" y="700" width="420" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:70px; font-weight:900; color:{COLORS['gold_light']};">۴</div>
            <div style="font-size:18px; font-weight:600; margin-top:10px;">مدل مختلف طیف سیاسی</div>
            <div style="font-size:14px; opacity:0.6; margin-top:8px;">خطی • دوبعدی • سه‌بعدی • نعل اسب</div>
        </div>
    </foreignObject>
    
    <!-- Fact 6 -->
    <rect x="560" y="680" width="460" height="220" rx="16" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
    <foreignObject x="580" y="700" width="420" height="190">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:70px; font-weight:900; color:#64B5F6;">۱۰۰</div>
            <div style="font-size:18px; font-weight:600; margin-top:10px;">چهره کلیدی تاریخ اندیشه</div>
            <div style="font-size:14px; opacity:0.6; margin-top:8px;">با شناخت‌نامه کامل در ضمیمه کتاب</div>
        </div>
    </foreignObject>
    
    <!-- Bottom Quote -->
    <rect x="60" y="940" width="960" height="120" rx="16" fill="rgba(249,168,37,0.1)" stroke="{COLORS['gold']}" stroke-width="2"/>
    <foreignObject x="80" y="960" width="920" height="90">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:22px; font-style:italic; line-height:1.6;">
                «هر که تاریخ را نداند، محکوم به تکرار آن است»
            </div>
            <div style="font-size:16px; color:{COLORS['gold']}; margin-top:8px;">— جورج سانتایانا</div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="1090" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.4); font-size:16px;">
            📚 راست یا چپ؛ میانه کجاست؟ | مهدی سالم
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_19_book_structure():
    """Book Structure Overview"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['off_white']}"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="{WIDTH}" height="150" fill="{COLORS['navy']}"/>
    <foreignObject x="40" y="40" width="1000" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:40px; font-weight:900;">📚 ساختار کتاب</div>
            <div style="font-size:20px; opacity:0.8; margin-top:8px;">یک سفر جامع در ۵ بخش و ۱۷ فصل</div>
        </div>
    </foreignObject>
    
    <!-- Part 1 -->
    <rect x="60" y="185" width="960" height="130" rx="12" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.08))"/>
    <rect x="60" y="185" width="12" height="130" rx="6" fill="{COLORS['gold']}"/>
    <foreignObject x="90" y="195" width="910" height="110">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px;">
                <div style="background:{COLORS['gold']}; color:{COLORS['navy']}; width:50px; height:50px; border-radius:25px; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:900;">۱</div>
                <div>
                    <div style="color:{COLORS['navy']}; font-size:22px; font-weight:800;">مبانی و مفاهیم</div>
                    <div style="color:#666; font-size:15px; margin-top:5px;">فصل ۱-۳ | زایش طیف سیاسی • فلسفه چپ و راست • اقتصاد سیاسی</div>
                </div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Part 2 -->
    <rect x="60" y="340" width="960" height="130" rx="12" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.08))"/>
    <rect x="60" y="340" width="12" height="130" rx="6" fill="{COLORS['red_left']}"/>
    <foreignObject x="90" y="350" width="910" height="110">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px;">
                <div style="background:{COLORS['red_left']}; color:white; width:50px; height:50px; border-radius:25px; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:900;">۲</div>
                <div>
                    <div style="color:{COLORS['red_left']}; font-size:22px; font-weight:800;">جهان چپ</div>
                    <div style="color:#666; font-size:15px; margin-top:5px;">فصل ۴-۸ | سوسیالیسم • کمونیسم • آنارشیسم • سوسیال دموکراسی • چپ نو</div>
                </div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Part 3 -->
    <rect x="60" y="495" width="960" height="130" rx="12" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.08))"/>
    <rect x="60" y="495" width="12" height="130" rx="6" fill="{COLORS['navy']}"/>
    <foreignObject x="90" y="505" width="910" height="110">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px;">
                <div style="background:{COLORS['navy']}; color:white; width:50px; height:50px; border-radius:25px; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:900;">۳</div>
                <div>
                    <div style="color:{COLORS['navy']}; font-size:22px; font-weight:800;">جهان راست</div>
                    <div style="color:#666; font-size:15px; margin-top:5px;">فصل ۹-۱۳ | محافظه‌کاری • لیبرالیسم • لیبرتارینیسم • ناسیونالیسم • راست نو</div>
                </div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Part 4 -->
    <rect x="60" y="650" width="960" height="130" rx="12" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.08))"/>
    <rect x="60" y="650" width="12" height="130" rx="6" fill="{COLORS['emerald']}"/>
    <foreignObject x="90" y="660" width="910" height="110">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px;">
                <div style="background:{COLORS['emerald']}; color:white; width:50px; height:50px; border-radius:25px; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:900;">۴</div>
                <div>
                    <div style="color:{COLORS['emerald']}; font-size:22px; font-weight:800;">میانه و ترکیب</div>
                    <div style="color:#666; font-size:15px; margin-top:5px;">فصل ۱۴-۱۵ | میانه‌روی: هنر یا بی‌اصالتی؟ • راه سوم</div>
                </div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Part 5 -->
    <rect x="60" y="805" width="960" height="130" rx="12" fill="white" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.08))"/>
    <rect x="60" y="805" width="12" height="130" rx="6" fill="{COLORS['purple']}"/>
    <foreignObject x="90" y="815" width="910" height="110">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="display:flex; align-items:center; gap:15px;">
                <div style="background:{COLORS['purple']}; color:white; width:50px; height:50px; border-radius:25px; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:900;">۵</div>
                <div>
                    <div style="color:{COLORS['purple']}; font-size:22px; font-weight:800;">تحلیل و آینده‌نگری</div>
                    <div style="color:#666; font-size:15px; margin-top:5px;">فصل ۱۶-۱۷ | طیف در جهان غیرغربی • آینده طیف سیاسی • جمع‌بندی</div>
                </div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Appendix -->
    <rect x="60" y="960" width="960" height="100" rx="12" fill="{COLORS['navy']}" opacity="0.05"/>
    <foreignObject x="80" y="975" width="920" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['navy']};">
            <div style="font-size:18px; font-weight:600;">📎 ضمائم: تایم‌لاین جامع • ۱۰۰ چهره کلیدی • واژه‌نامه تخصصی • کتاب‌شناسی</div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="1080" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:#999; font-size:16px;">
            نویسنده: مهدی سالم | ریچموندهیل
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_20_cta_final():
    """Final Call to Action Slide"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="finalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{COLORS['navy']};stop-opacity:1" />
            <stop offset="50%" style="stop-color:#283593;stop-opacity:1" />
            <stop offset="100%" style="stop-color:{COLORS['purple']};stop-opacity:1" />
        </linearGradient>
        <linearGradient id="spectrumFinal" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:{COLORS['red_left']};stop-opacity:1" />
            <stop offset="25%" style="stop-color:{COLORS['orange']};stop-opacity:1" />
            <stop offset="50%" style="stop-color:{COLORS['gold']};stop-opacity:1" />
            <stop offset="75%" style="stop-color:{COLORS['emerald']};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{COLORS['navy_light']};stop-opacity:1" />
        </linearGradient>
        <filter id="bigGlow">
            <feGaussianBlur stdDeviation="6" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#finalGrad)"/>
    
    <!-- Decorative Elements -->
    <circle cx="100" cy="150" r="200" fill="white" opacity="0.03"/>
    <circle cx="980" cy="200" r="250" fill="white" opacity="0.03"/>
    <circle cx="540" cy="1300" r="350" fill="{COLORS['gold']}" opacity="0.05"/>
    
    <!-- Top Quote -->
    <foreignObject x="80" y="60" width="920" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.6); font-size:22px; font-style:italic; line-height:1.6;">
            «برای فهم جهان، ابتدا باید زبان آن را آموخت»
        </div>
    </foreignObject>
    
    <!-- Spectrum Line -->
    <rect x="100" y="200" width="880" height="16" rx="8" fill="url(#spectrumFinal)" filter="url(#bigGlow)"/>
    
    <!-- Main Title -->
    <foreignObject x="40" y="280" width="1000" height="240">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:72px; font-weight:900; line-height:1.2; text-shadow: 0 4px 30px rgba(0,0,0,0.3);">
                راست یا چپ؛<br/>میانه کجاست؟
            </div>
        </div>
    </foreignObject>
    
    <!-- Subtitle -->
    <foreignObject x="80" y="540" width="920" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['gold_light']}; font-size:26px; font-weight:500; line-height:1.5;">
            جامع‌ترین راهنمای فارسی‌زبان برای فهم<br/>
            طیف سیاسی، ایدئولوژی‌ها و جهان معاصر
        </div>
    </foreignObject>
    
    <!-- Feature Boxes -->
    <foreignObject x="60" y="660" width="960" height="180">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; display:flex; gap:15px; justify-content:center; flex-wrap:wrap;">
            <div style="background:rgba(255,255,255,0.1); padding:15px 25px; border-radius:15px; text-align:center; color:white;">
                <div style="font-size:28px; margin-bottom:5px;">📖</div>
                <div style="font-size:16px; font-weight:600;">۱۷ فصل</div>
            </div>
            <div style="background:rgba(255,255,255,0.1); padding:15px 25px; border-radius:15px; text-align:center; color:white;">
                <div style="font-size:28px; margin-bottom:5px;">👤</div>
                <div style="font-size:16px; font-weight:600;">۱۰۰ شخصیت</div>
            </div>
            <div style="background:rgba(255,255,255,0.1); padding:15px 25px; border-radius:15px; text-align:center; color:white;">
                <div style="font-size:28px; margin-bottom:5px;">📊</div>
                <div style="font-size:16px; font-weight:600;">نمودار و تایم‌لاین</div>
            </div>
            <div style="background:rgba(255,255,255,0.1); padding:15px 25px; border-radius:15px; text-align:center; color:white;">
                <div style="font-size:28px; margin-bottom:5px;">🌍</div>
                <div style="font-size:16px; font-weight:600;">دید جهانی</div>
            </div>
            <div style="background:rgba(255,255,255,0.1); padding:15px 25px; border-radius:15px; text-align:center; color:white;">
                <div style="font-size:28px; margin-bottom:5px;">⚖️</div>
                <div style="font-size:16px; font-weight:600;">بی‌طرفانه</div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Author -->
    <foreignObject x="80" y="870" width="920" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:28px; font-weight:700;">✍️ مهدی سالم</div>
            <div style="font-size:18px; opacity:0.7; margin-top:5px;">ریچموندهیل</div>
        </div>
    </foreignObject>
    
    <!-- CTA Buttons -->
    <rect x="290" y="990" width="500" height="70" rx="35" fill="{COLORS['gold']}" filter="url(#bigGlow)"/>
    <foreignObject x="290" y="990" width="500" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:{COLORS['navy']}; font-size:26px; font-weight:800; line-height:70px;">
            📖 همین حالا بخوانید
        </div>
    </foreignObject>
    
    <!-- Link Placeholder -->
    <rect x="340" y="1090" width="400" height="50" rx="25" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>
    <foreignObject x="340" y="1090" width="400" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white; font-size:18px; line-height:50px; opacity:0.8;">
            🔗 لینک در بیو
        </div>
    </foreignObject>
    
    <!-- Social -->
    <foreignObject x="60" y="1170" width="960" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.5); font-size:16px; line-height:1.6;">
            ذخیره کنید 🔖 | به اشتراک بگذارید 📤 | نظرتان را بگویید 💬<br/>
            برای محتوای بیشتر فالو کنید ✨
        </div>
    </foreignObject>
</svg>'''
    return svg


def create_slide_21_rosa_vs_lenin():
    """Famous Debate: Rosa Luxemburg vs Lenin"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">
    {get_base_styles()}
    
    <defs>
        <linearGradient id="rosaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#4A0000;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#800000;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#rosaGrad)"/>
    
    <!-- Header -->
    <foreignObject x="40" y="40" width="1000" height="130">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:22px; color:{COLORS['gold']};">⚔️ نبرد درون چپ انقلابی</div>
            <div style="font-size:42px; font-weight:900; margin-top:8px;">رزا لوکزامبورگ در برابر لنین</div>
            <div style="font-size:18px; opacity:0.7; margin-top:5px;">آزادی یا انضباط حزبی؟</div>
        </div>
    </foreignObject>
    
    <!-- Rosa Card -->
    <rect x="60" y="210" width="460" height="440" rx="20" fill="rgba(255,255,255,0.95)"/>
    <rect x="60" y="210" width="460" height="8" rx="4" fill="#E91E63"/>
    
    <foreignObject x="80" y="230" width="420" height="410">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="text-align:center; margin-bottom:15px;">
                <div style="font-size:50px;">🌹</div>
                <div style="color:#C2185B; font-size:26px; font-weight:800;">رزا لوکزامبورگ</div>
                <div style="color:#666; font-size:15px;">۱۸۷۱-۱۹۱۹ | لهستان/آلمان</div>
            </div>
            
            <div style="color:#333; font-size:16px; line-height:1.8; margin-top:15px;">
                <div style="font-weight:700; color:#C2185B; margin-bottom:10px;">💡 مواضع:</div>
                <div style="margin-bottom:8px;">✦ انقلاب باید خودجوش و توده‌ای باشد</div>
                <div style="margin-bottom:8px;">✦ دموکراسی در انقلاب ضروری است</div>
                <div style="margin-bottom:8px;">✦ حزب نباید جایگزین طبقه شود</div>
                <div style="margin-bottom:8px;">✦ آزادی = آزادی دگراندیشان</div>
            </div>
            
            <div style="background:#FCE4EC; padding:12px; border-radius:10px; margin-top:15px;">
                <div style="color:#C2185B; font-size:14px; font-style:italic; text-align:center;">
                    «آزادی فقط برای هواداران دولت، آزادی نیست.<br/>
                    آزادی همیشه آزادی دگراندیش است.»
                </div>
            </div>
        </div>
    </foreignObject>
    
    <!-- VS -->
    <circle cx="540" cy="430" r="40" fill="{COLORS['gold']}" filter="drop-shadow(0 4px 15px rgba(0,0,0,0.4))"/>
    <text x="540" y="442" text-anchor="middle" font-size="24" font-weight="900" fill="#4A0000">VS</text>
    
    <!-- Lenin Card -->
    <rect x="560" y="210" width="460" height="440" rx="20" fill="rgba(255,255,255,0.95)"/>
    <rect x="560" y="210" width="460" height="8" rx="4" fill="{COLORS['red_left']}"/>
    
    <foreignObject x="580" y="230" width="420" height="410">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn;">
            <div style="text-align:center; margin-bottom:15px;">
                <div style="font-size:50px;">⭐</div>
                <div style="color:{COLORS['red_left']}; font-size:26px; font-weight:800;">ولادیمیر لنین</div>
                <div style="color:#666; font-size:15px;">۱۸۷۰-۱۹۲۴ | روسیه</div>
            </div>
            
            <div style="color:#333; font-size:16px; line-height:1.8; margin-top:15px;">
                <div style="font-weight:700; color:{COLORS['red_left']}; margin-bottom:10px;">💡 مواضع:</div>
                <div style="margin-bottom:8px;">✦ حزب پیشاهنگ انقلابیون حرفه‌ای</div>
                <div style="margin-bottom:8px;">✦ سانترالیسم دموکراتیک</div>
                <div style="margin-bottom:8px;">✦ انضباط آهنین حزبی</div>
                <div style="margin-bottom:8px;">✦ «چه باید کرد؟» — رهبری از بالا</div>
            </div>
            
            <div style="background:#FFEBEE; padding:12px; border-radius:10px; margin-top:15px;">
                <div style="color:{COLORS['red_left']}; font-size:14px; font-style:italic; text-align:center;">
                    «بدون حزب پیشاهنگ، طبقه کارگر<br/>
                    فراتر از آگاهی صنفی نمی‌رود.»
                </div>
            </div>
        </div>
    </foreignObject>
    
    <!-- Outcome -->
    <rect x="60" y="690" width="960" height="200" rx="16" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
    <foreignObject x="80" y="710" width="920" height="170">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:white;">
            <div style="font-size:22px; font-weight:700; color:{COLORS['gold']}; margin-bottom:12px;">📜 پیامد تاریخی</div>
            <div style="font-size:17px; line-height:1.7;">
                لنین انقلاب را رهبری کرد و رزا ترور شد.<br/>
                اما هشدارهای رزا محقق شد: حزب جای طبقه نشست،<br/>
                و «دیکتاتوری پرولتاریا» به <span style="color:{COLORS['gold']};">دیکتاتوری بر پرولتاریا</span> تبدیل شد.<br/><br/>
                <span style="font-size:15px; opacity:0.8;">
                    این مناظره هنوز در چپ معاصر زنده است:
                    <span style="color:{COLORS['gold']};">دموکراسی مشارکتی یا رهبری متمرکز؟</span>
                </span>
            </div>
        </div>
    </foreignObject>
    
    <!-- Footer -->
    <foreignObject x="60" y="920" width="960" height="50">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; text-align:center; font-family:Vazirmatn; color:rgba(255,255,255,0.4); font-size:16px;">
            فصل ۴: سوسیالیسم | فصل ۵: کمونیسم
        </div>
    </foreignObject>
</svg>'''
    return svg


# ═══════════════════════════════════════════════════════════════════
#                    🚀 MAIN EXECUTION BLOCK
# ═══════════════════════════════════════════════════════════════════

def main():
    """Generate all slides and save to output directory"""
    
    print("=" * 70)
    print("📊 Instagram Slides Generator")
    print("📚 Book: راست یا چپ؛ میانه کجاست؟")
    print("✍️  Author: مهدی سالم")
    print("=" * 70)
    print()
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"📁 Output Directory: {OUTPUT_DIR}")
    print()
    
    # Define all slides with names and generators
    slides = [
        ("01_cover_book_intro", create_slide_1_cover, "جلد و معرفی کتاب"),
        ("02_key_question_origin", create_slide_2_key_question, "سؤال کلیدی: مفهوم از کجا آمد؟"),
        ("03_historical_timeline", create_slide_3_timeline, "تایم‌لاین تاریخی"),
        ("04_left_spectrum_overview", create_slide_4_left_spectrum, "جهان چپ"),
        ("05_right_spectrum_overview", create_slide_5_right_spectrum, "جهان راست"),
        ("06_key_philosophers", create_slide_6_philosophers, "متفکران کلیدی"),
        ("07_economic_spectrum", create_slide_7_economic_spectrum, "طیف اقتصادی"),
        ("08_debate_marx_vs_bakunin", create_slide_8_marx_vs_bakunin, "مناظره: مارکس در برابر باکونین"),
        ("09_debate_burke_vs_paine", create_slide_9_burke_vs_paine, "مناظره: برک در برابر پین"),
        ("10_debate_keynes_vs_hayek", create_slide_10_keynes_vs_hayek, "مناظره: کینز در برابر هایک"),
        ("11_intellectual_converts", create_slide_11_intellectual_converts, "روشنفکرانی که طرف عوض کردند"),
        ("12_left_to_right_stories", create_slide_12_left_to_right_stories, "سفر از چپ به راست"),
        ("13_right_to_left_stories", create_slide_13_right_to_left_stories, "سفر از راست به چپ"),
        ("14_overton_window", create_slide_14_overton_window, "پنجره اورتون"),
        ("15_horseshoe_theory", create_slide_15_horseshoe_theory, "نظریه نعل اسب"),
        ("16_debate_trotsky_vs_stalin", create_slide_16_trotsky_vs_stalin, "مناظره: تروتسکی در برابر استالین"),
        ("17_debate_rawls_vs_nozick", create_slide_17_rawls_vs_nozick, "مناظره: رالز در برابر نوزیک"),
        ("18_shocking_facts", create_slide_18_shocking_facts, "حقایق شگفت‌انگیز"),
        ("19_book_structure", create_slide_19_book_structure, "ساختار کتاب"),
        ("20_cta_final", create_slide_20_cta_final, "اسلاید نهایی و فراخوان"),
        ("21_debate_rosa_vs_lenin", create_slide_21_rosa_vs_lenin, "مناظره: رزا لوکزامبورگ در برابر لنین"),
    ]
    
    # Generate and save
    success_count = 0
    error_count = 0
    
    for filename, generator, description in slides:
        try:
            svg_content = generator()
            filepath = OUTPUT_DIR / f"{filename}.svg"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            
            file_size = filepath.stat().st_size / 1024
            print(f"  ✅ {filename}.svg ({file_size:.1f} KB)")
            print(f"     📝 {description}")
            success_count += 1
            
        except Exception as e:
            print(f"  ❌ {filename}.svg — ERROR: {e}")
            error_count += 1
    
    print()
    print("=" * 70)
    print(f"📊 Generation Complete!")
    print(f"  ✅ Successful: {success_count}")
    print(f"  ❌ Errors: {error_count}")
    print(f"  📁 Location: {OUTPUT_DIR}")
    print("=" * 70)
    print()
    
    # Generate index HTML for easy preview
    generate_preview_html(slides)
    
    print("💡 Tips:")
    print("  • Open preview.html in browser to see all slides")
    print("  • SVGs can be opened in Inkscape, Figma, or any browser")
    print("  • For Instagram: Export SVGs to PNG at 1080x1350")
    print("  • Use Inkscape CLI: inkscape input.svg -o output.png -w 1080 -h 1350")
    print()


def generate_preview_html(slides):
    """Generate an HTML preview page for all slides"""
    
    html_content = '''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📚 پیش‌نمایش اسلایدها | راست یا چپ؛ میانه کجاست؟</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;600;700;800;900&display=swap');
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Vazirmatn', sans-serif;
            background: #1a1a2e;
            color: white;
            padding: 40px;
        }
        
        h1 {
            text-align: center;
            font-size: 36px;
            margin-bottom: 10px;
            color: #F9A825;
        }
        
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: rgba(255,255,255,0.6);
            margin-bottom: 40px;
        }
        
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 30px;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .card {
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            overflow: hidden;
            transition: transform 0.3s;
            border: 1px solid rgba(255,255,255,0.1);
        }
        
        .card:hover {
            transform: translateY(-5px);
            border-color: #F9A825;
        }
        
        .card img {
            width: 100%;
            display: block;
        }
        
        .card-info {
            padding: 15px;
        }
        
        .card-info .number {
            color: #F9A825;
            font-weight: 800;
            font-size: 14px;
        }
        
        .card-info .name {
            font-size: 16px;
            font-weight: 600;
            margin-top: 5px;
        }
        
        .card-info .desc {
            font-size: 14px;
            opacity: 0.6;
            margin-top: 5px;
        }
        
        .footer-info {
            text-align: center;
            margin-top: 50px;
            padding: 30px;
            background: rgba(255,255,255,0.03);
            border-radius: 16px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .footer-info p {
            margin: 8px 0;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <h1>📚 راست یا چپ؛ میانه کجاست؟</h1>
    <div class="subtitle">پیش‌نمایش اسلایدهای اینستاگرام | ۱۰۸۰×۱۳۵۰ پیکسل</div>
    
    <div class="grid">
'''
    
    for i, (filename, _, description) in enumerate(slides):
        html_content += f'''        <div class="card">
            <img src="{filename}.svg" alt="{description}" loading="lazy"/>
            <div class="card-info">
                <div class="number">اسلاید {i+1}</div>
                <div class="name">{filename}</div>
                <div class="desc">{description}</div>
            </div>
        </div>
'''
    
    html_content += '''    </div>
    
    <div class="footer-info">
        <h3>💡 راهنمای استفاده</h3>
        <p>فایل‌های SVG را می‌توانید در مرورگر، Inkscape یا Figma باز کنید</p>
        <p>برای تبدیل به PNG از Inkscape استفاده کنید:</p>
        <code style="background:rgba(255,255,255,0.1); padding:10px; border-radius:8px; display:block; margin:10px 0; direction:ltr; text-align:left;">
            inkscape input.svg -o output.png -w 1080 -h 1350
        </code>
        <p>یا از ابزار آنلاین svgtopng.com استفاده کنید</p>
        <p style="margin-top:20px; color:#F9A825;">✍️ نویسنده: مهدی سالم | ریچموندهیل</p>
    </div>
</body>
</html>'''
    
    preview_path = OUTPUT_DIR / "preview.html"
    with open(preview_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"  🌐 preview.html generated for browser preview")


# ═══════════════════════════════════════════════════════════════════
#           PNG EXPORT UTILITY (Optional - requires Inkscape)
# ═══════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════
#   CONTINUATION - Completing export_to_png + batch converter + run
# ═══════════════════════════════════════════════════════════════════

def export_to_png():
    """
    Optional: Export all SVGs to PNG using Inkscape CLI
    Requires Inkscape installed and in PATH
    """
    import subprocess
    import shutil
    
    inkscape_path = shutil.which("inkscape")
    if not inkscape_path:
        # Try common Windows paths
        common_paths = [
            r"C:\Program Files\Inkscape\bin\inkscape.exe",
            r"C:\Program Files (x86)\Inkscape\bin\inkscape.exe",
            r"C:\Program Files\Inkscape\inkscape.exe",
        ]
        for p in common_paths:
            if Path(p).exists():
                inkscape_path = p
                break
    
    if not inkscape_path:
        print("⚠️  Inkscape not found. Skipping PNG export.")
        print("   Install Inkscape: https://inkscape.org/release/")
        print("   Or use the PowerShell script generated below.")
        generate_powershell_converter()
        return
    
    png_dir = OUTPUT_DIR / "png"
    png_dir.mkdir(exist_ok=True)
    
    print(f"\n🖼️  Exporting SVGs to PNG using: {inkscape_path}")
    print(f"📁 PNG Output: {png_dir}\n")
    
    svg_files = sorted(OUTPUT_DIR.glob("*.svg"))
    success = 0
    errors = 0
    
    for svg_file in svg_files:
        png_file = png_dir / f"{svg_file.stem}.png"
        try:
            result = subprocess.run(
                [
                    inkscape_path,
                    str(svg_file),
                    "--export-type=png",
                    f"--export-filename={str(png_file)}",
                    "--export-width=1080",
                    "--export-height=1350",
                    "--export-background=#FFFFFF",
                    "--export-background-opacity=1.0",
                ],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if png_file.exists():
                size_kb = png_file.stat().st_size / 1024
                print(f"  ✅ {svg_file.stem}.png ({size_kb:.0f} KB)")
                success += 1
            else:
                print(f"  ❌ {svg_file.stem}.png — File not created")
                if result.stderr:
                    print(f"     Error: {result.stderr[:200]}")
                errors += 1
                
        except subprocess.TimeoutExpired:
            print(f"  ⏰ {svg_file.stem}.png — Timeout")
            errors += 1
        except Exception as e:
            print(f"  ❌ {svg_file.stem}.png — {e}")
            errors += 1
    
    print(f"\n📊 PNG Export: ✅ {success} | ❌ {errors}")


def generate_batch_rename_script():
    """Generate a script to rename files for Instagram carousel order"""
    
    bat_content = f'''@echo off
chcp 65001 >nul
echo ═══════════════════════════════════════════════════
echo   📱 Instagram Carousel Organizer
echo   📚 راست یا چپ؛ میانه کجاست؟
echo ═══════════════════════════════════════════════════
echo.

set "SRCDIR={OUTPUT_DIR}\\png"

if not exist "%SRCDIR%" (
    echo ❌ PNG directory not found: %SRCDIR%
    echo    Run the Python script first, then convert SVGs to PNG.
    pause
    exit /b
)

echo 📁 Source: %SRCDIR%
echo.
echo 📋 Carousel Order:
echo    1. Cover ^& Introduction
echo    2. Key Question
echo    3. Timeline
echo    4-5. Left ^& Right Spectrum
echo    6-7. Philosophers ^& Economics
echo    8-10. Famous Debates
echo    11-13. Intellectual Converts
echo    14-15. Overton Window ^& Horseshoe
echo    16-17. More Debates
echo    18-19. Facts ^& Book Structure  
echo    20. Final CTA
echo.

echo ✅ Files are already numbered in carousel order!
echo.
echo 💡 Upload to Instagram in numerical order (01-20)
echo.
pause
'''
    
    bat_path = OUTPUT_DIR / "carousel_order.bat"
    with open(bat_path, 'w', encoding='utf-8') as f:
        f.write(bat_content)


def generate_figma_import_guide():
    """Generate a guide for importing into Figma"""
    
    guide = f'''# 🎨 راهنمای ویرایش و استفاده از اسلایدها
## «راست یا چپ؛ میانه کجاست؟»

---

## 📁 فایل‌ها
- **SVG**: فایل‌های اصلی قابل ویرایش  
- **PNG**: تصاویر نهایی برای اینستاگرام (1080×1350)
- **preview.html**: پیش‌نمایش مرورگری

---

## 🛠️ ویرایش در Figma
1. وارد Figma شوید
2. File → Import → فایل SVG را انتخاب کنید
3. فونت Vazirmatn را نصب کنید: https://fonts.google.com/specimen/Vazirmatn
4. ویرایش کنید و Export as PNG (1080×1350)

## 🛠️ ویرایش در Inkscape
1. فایل SVG را باز کنید
2. فونت Vazirmatn را نصب کنید
3. ویرایش و ذخیره
4. File → Export PNG → 1080×1350

## 🛠️ ویرایش در Canva
1. در Canva یک صفحه 1080×1350 بسازید
2. SVG را آپلود و Import کنید
3. ویرایش و دانلود PNG

---

## 📱 ترتیب کاروسل اینستاگرام

| # | اسلاید | نوع |
|---|--------|-----|
| 1 | جلد و معرفی | Cover |
| 2 | سؤال کلیدی | Hook |
| 3 | تایم‌لاین تاریخی | Info |
| 4 | جهان چپ | Info |
| 5 | جهان راست | Info |
| 6 | متفکران کلیدی | Info |
| 7 | طیف اقتصادی | Info |
| 8 | مارکس vs باکونین | Debate |
| 9 | برک vs پین | Debate |
| 10 | کینز vs هایک | Debate |

**پست دوم (کاروسل ۲):**

| # | اسلاید | نوع |
|---|--------|-----|
| 1 | روشنفکران تغییر کرده | Story |
| 2 | چپ به راست | Story |
| 3 | راست به چپ | Story |
| 4 | پنجره اورتون | Concept |
| 5 | نظریه نعل اسب | Concept |
| 6 | تروتسکی vs استالین | Debate |
| 7 | رالز vs نوزیک | Debate |
| 8 | رزا vs لنین | Debate |
| 9 | حقایق شگفت‌انگیز | Facts |
| 10 | ساختار کتاب + CTA | CTA |

---

## ✏️ کپشن‌های پیشنهادی

### پست ۱:
📚 «راست یا چپ؛ میانه کجاست؟»

آیا می‌دونید مفهوم چپ و راست از کجا اومده؟ 🤔

۲۳۵ سال پیش، توی مجلس ملی فرانسه، یه تصادف ساده در نشستن باعث شد تاریخ سیاست برای همیشه عوض بشه...

📖 این کتاب سفری جامع در تاریخ ایدئولوژی‌هاست:
✦ از مارکس تا هایک
✦ از انقلاب فرانسه تا برگزیت
✦ از سوسیالیسم تا لیبرتارینیسم

🔗 لینک مطالعه در بیو

#کتاب #سیاست #فلسفه_سیاسی #چپ_و_راست #ایدئولوژی
#مطالعه #کتاب‌خوانی #تاریخ #اقتصاد_سیاسی #آگاهی

text

### پست ۲:
⚔️ مناظرات تاریخی که جهان رو شکل دادن

از برک و پین در ۱۷۹۰ تا رالز و نوزیک در هاروارد...

🔥 بعضی روشنفکران حتی طرف عوض کردن:
← هایک از سوسیالیست به لیبرال
← فوکویاما از نومحافظه‌کار به لیبرال
← موسولینی از سوسیالیست به فاشیست!

💡 و یه حقیقت عجیب: «میانه» هر ده سال جابه‌جا می‌شه...

📖 همه این داستان‌ها در کتاب «راست یا چپ؛ میانه کجاست؟»

🔗 لینک در بیو

#مناظره #تاریخ_سیاسی #فلسفه #روشنفکری

text

---

## 🎨 فونت‌ها
- **اصلی**: Vazirmatn (نصب از Google Fonts)
- **جایگزین**: Segoe UI, Tahoma
- **لینک**: https://fonts.google.com/specimen/Vazirmatn

## 🎨 پالت رنگی
- Navy: #1A237E (هدرها)
- Gold: #F9A825 (تأکید)
- Emerald: #2E7D32 (میانه/راه‌حل)
- Red: #C81E1E (چپ)
- Purple: #6A1B9A (فلسفه)
- Dark: #3C3C3C (متن)

---

✍️ نویسنده: مهدی سالم | ریچموندهیل
'''
    
    guide_path = OUTPUT_DIR / "GUIDE.md"
    with open(guide_path, 'w', encoding='utf-8') as f:
        f.write(guide)
    
    print(f"  📖 Usage guide saved: {guide_path}")


# ═══════════════════════════════════════════════════════════════════
#                 🎯 FINAL MAIN EXECUTION
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    
    print()
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║  📚 Instagram Slides Generator                          ║")
    print("║  📖 «راست یا چپ؛ میانه کجاست؟»                          ║")
    print("║  ✍️  Author: مهدی سالم                                   ║")
    print("║  📐 Size: 1080×1350 (Instagram Post/Carousel)           ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print()
    
    # Step 1: Generate SVG slides
    main()
    
    # Step 2: Generate helper scripts
    print("\n📦 Generating helper files...")
    # generate_powershell_converter()
    generate_batch_rename_script()
    generate_figma_import_guide()
    
    # Step 3: Try PNG export
    print("\n" + "=" * 60)
    try_png = input("🖼️  Try to export PNGs now? (y/n): ").strip().lower()
    if try_png == 'y':
        export_to_png()
    else:
        print("⏭️  Skipping PNG export.")
        print(f"   Run later: powershell -File \"{OUTPUT_DIR / 'convert_to_png.ps1'}\"")
    
    # Step 4: Summary
    print()
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║                   ✅ ALL DONE!                           ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print(f"║  📁 Output: {str(OUTPUT_DIR)[:45]:<45} ║")
    print("║                                                         ║")
    print("║  📄 Files Generated:                                    ║")
    print("║     • 21 SVG slides (1080×1350)                         ║")
    print("║     • preview.html (browser preview)                    ║")
    print("║     • convert_to_png.ps1 (PNG converter)                ║")
    print("║     • carousel_order.bat (upload guide)                 ║")
    print("║     • GUIDE.md (full usage guide + captions)            ║")
    print("║                                                         ║")
    print("║  📱 Slide Types:                                        ║")
    print("║     • 1 Cover slide                                     ║")
    print("║     • 2 Overview slides (Left & Right)                  ║")
    print("║     • 6 Famous debate slides                            ║")
    print("║     • 3 Intellectual convert slides                     ║")
    print("║     • 2 Concept slides (Overton, Horseshoe)             ║")
    print("║     • 4 Info slides (Timeline, Facts, Philosophers)     ║")
    print("║     • 2 Book structure + CTA slides                     ║")
    print("║     • 1 Final call-to-action slide                      ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print()
    
    # Open folder
    import platform
    if platform.system() == "Windows":
        try_open = input("📂 Open output folder? (y/n): ").strip().lower()
        if try_open == 'y':
            import subprocess
            subprocess.Popen(f'explorer "{OUTPUT_DIR}"')
    
    print("\n🎉 خسته نباشید! اسلایدهای اینستاگرام آماده‌اند.")
    print("   موفق باشید با کتاب «راست یا چپ؛ میانه کجاست؟» 📚")
    print()