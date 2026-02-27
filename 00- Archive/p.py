#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
پرامپت‌ساز کتاب «راست یا چپ؛ میانه کجاست؟»
نویسنده: مهدی سالم
---
این اسکریپت پرامپت کامل هر چت را از فایل prompt.mdx استخراج و آماده می‌کند.
"""

import re
import sys
import os

# تلاش برای import کتابخانه کلیپ‌بورد
try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False
    print("⚠️  کتابخانه pyperclip نصب نیست.")
    print("   برای نصب: pip install pyperclip")
    print("   فعلاً خروجی فقط در فایل ذخیره می‌شود.\n")


def load_prompt_file(filepath: str) -> str:
    """خواندن فایل پرامپت"""
    if not os.path.exists(filepath):
        print(f"❌ خطا: فایل '{filepath}' یافت نشد!")
        sys.exit(1)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def extract_base_prompt(content: str) -> str:
    """استخراج پرامپت پایه"""
    
    # الگوی جستجو برای پرامپت پایه
    # از "پرامپت پایه برای همه چت‌ها" تا قبل از "بخش چهارم" یا "اسپرینت"
    pattern = r'## پرامپت پایه برای همه چت‌ها\s*\n```markdown\s*\n(.*?)```'
    
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    
    # الگوی جایگزین
    pattern2 = r'(═{10,}.*?🎓 پرامپت پایه.*?═{10,}.*?🎨 پالت رنگی کتاب.*?```)'
    match2 = re.search(pattern2, content, re.DOTALL)
    
    if match2:
        return match2.group(1).strip()
    
    print("❌ خطا: پرامپت پایه یافت نشد!")
    return ""


def extract_chat_prompt(content: str, chat_number: int) -> str:
    """استخراج پرامپت یک چت خاص"""
    
    # تبدیل اعداد فارسی به انگلیسی برای جستجو
    persian_num = convert_to_persian(chat_number)
    
    # الگوهای مختلف برای یافتن چت
    patterns = [
        rf'## 🔷 چت {chat_number}:.*?\n```markdown\s*\n(.*?)```',
        rf'## 🔷 چت {persian_num}:.*?\n```markdown\s*\n(.*?)```',
        rf'## 🔷 چت {chat_number}[:\s].*?(═{{10,}}.*?═{{10,}}.*?المان‌های گرافیکی.*?•[^\n]+)',
        rf'## 🔷 چت {persian_num}[:\s].*?(═{{10,}}.*?═{{10,}}.*?المان‌های گرافیکی.*?•[^\n]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return match.group(1).strip()
    
    # جستجوی ساده‌تر
    # پیدا کردن شروع چت
    start_patterns = [
        rf'## 🔷 چت {chat_number}:',
        rf'## 🔷 چت {persian_num}:',
        rf'چت {chat_number} از',
        rf'چت {persian_num} از',
    ]
    
    start_pos = -1
    for sp in start_patterns:
        match = re.search(sp, content)
        if match:
            start_pos = match.start()
            break
    
    if start_pos == -1:
        print(f"❌ خطا: چت شماره {chat_number} یافت نشد!")
        return ""
    
    # پیدا کردن پایان (شروع چت بعدی یا بخش بعدی)
    next_chat = chat_number + 1
    next_persian = convert_to_persian(next_chat)
    
    end_patterns = [
        rf'## 🔷 چت {next_chat}:',
        rf'## 🔷 چت {next_persian}:',
        r'# 📊 بخش ششم',
        r'# ✅ خلاصه اجرایی',
        r'---\s*\n\s*#',
    ]
    
    end_pos = len(content)
    for ep in end_patterns:
        match = re.search(ep, content[start_pos + 10:])
        if match:
            end_pos = min(end_pos, start_pos + 10 + match.start())
    
    extracted = content[start_pos:end_pos].strip()
    
    # حذف عنوان چت از ابتدا
    extracted = re.sub(r'^## 🔷 چت \d+:.*?\n', '', extracted)
    extracted = re.sub(r'^## 🔷 چت [۰-۹]+:.*?\n', '', extracted)
    
    return extracted


def convert_to_persian(num: int) -> str:
    """تبدیل عدد انگلیسی به فارسی"""
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    return ''.join(persian_digits[int(d)] for d in str(num))


def convert_to_english(persian_num: str) -> int:
    """تبدیل عدد فارسی به انگلیسی"""
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    result = persian_num
    for p, e in zip(persian_digits, english_digits):
        result = result.replace(p, e)
    try:
        return int(result)
    except ValueError:
        return -1


def combine_prompts(base_prompt: str, chat_prompt: str) -> str:
    """ترکیب پرامپت پایه و پرامپت چت"""
    
    # جایگزین‌های احتمالی
    placeholders = [
        '[پرامپت پایه را اینجا کپی کنید]',
        '[پرامپت پایه]',
        '**[پرامپت پایه را اینجا کپی کنید]**',
    ]
    
    result = chat_prompt
    replaced = False
    
    for placeholder in placeholders:
        if placeholder in result:
            result = result.replace(placeholder, base_prompt)
            replaced = True
            break
    
    if not replaced:
        # اگر جایگزین پیدا نشد، پرامپت پایه را به ابتدا اضافه کن
        result = base_prompt + "\n\n" + "═" * 70 + "\n\n" + chat_prompt
    
    return result


def save_to_file(content: str, chat_number: int) -> str:
    """ذخیره در فایل"""
    filename = f"chat_{chat_number:02d}_prompt.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return filename


def print_header():
    """چاپ هدر برنامه"""
    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║     📚 پرامپت‌ساز کتاب «راست یا چپ؛ میانه کجاست؟»           ║")
    print("║                    نویسنده: مهدی سالم                       ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print("║  این ابزار پرامپت کامل هر چت را آماده و کپی می‌کند.        ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()


def print_stats(content: str):
    """نمایش آمار"""
    lines = content.count('\n')
    chars = len(content)
    words = len(content.split())
    
    print(f"\n📊 آمار پرامپت:")
    print(f"   • تعداد خطوط: {lines:,}")
    print(f"   • تعداد کاراکتر: {chars:,}")
    print(f"   • تعداد کلمه (تقریبی): {words:,}")


def main():
    print_header()
    
    # مسیر فایل پرامپت
    prompt_file = "prompt.mdx"
    
    # اگر آرگومان خط فرمان داده شده
    if len(sys.argv) > 1:
        # بررسی آرگومان اول برای مسیر فایل
        if sys.argv[1].endswith('.mdx') or sys.argv[1].endswith('.md'):
            prompt_file = sys.argv[1]
            chat_input = sys.argv[2] if len(sys.argv) > 2 else None
        else:
            chat_input = sys.argv[1]
    else:
        chat_input = None
    
    # خواندن فایل
    print(f"📂 در حال خواندن فایل: {prompt_file}")
    content = load_prompt_file(prompt_file)
    print(f"✅ فایل خوانده شد ({len(content):,} کاراکتر)")
    
    # استخراج پرامپت پایه
    print("🔍 در حال استخراج پرامپت پایه...")
    base_prompt = extract_base_prompt(content)
    if base_prompt:
        print(f"✅ پرامپت پایه استخراج شد ({len(base_prompt):,} کاراکتر)")
    else:
        print("❌ پرامپت پایه یافت نشد!")
        sys.exit(1)
    
    # حلقه اصلی
    while True:
        print("\n" + "─" * 50)
        
        if chat_input:
            user_input = chat_input
            chat_input = None  # فقط بار اول از آرگومان استفاده شود
        else:
            user_input = input("🔢 شماره چت را وارد کنید (1-20) یا 'q' برای خروج: ").strip()
        
        # بررسی خروج
        if user_input.lower() in ['q', 'quit', 'exit', 'خروج']:
            print("\n👋 خداحافظ!")
            break
        
        # تبدیل ورودی به عدد
        try:
            if any(c in user_input for c in '۰۱۲۳۴۵۶۷۸۹'):
                chat_number = convert_to_english(user_input)
            else:
                chat_number = int(user_input)
        except ValueError:
            print("❌ لطفاً یک عدد معتبر وارد کنید!")
            continue
        
        # بررسی محدوده
        if chat_number < 1 or chat_number > 20:
            print("❌ شماره چت باید بین 1 تا 20 باشد!")
            continue
        
        print(f"\n🔍 در حال استخراج پرامپت چت {chat_number}...")
        
        # استخراج پرامپت چت
        chat_prompt = extract_chat_prompt(content, chat_number)
        
        if not chat_prompt:
            print(f"❌ پرامپت چت {chat_number} یافت نشد!")
            continue
        
        print(f"✅ پرامپت چت {chat_number} استخراج شد")
        
        # ترکیب پرامپت‌ها
        print("🔧 در حال ترکیب پرامپت‌ها...")
        final_prompt = combine_prompts(base_prompt, chat_prompt)
        
        # ذخیره در فایل
        saved_file = save_to_file(final_prompt, chat_number)
        print(f"💾 ذخیره شد در: {saved_file}")
        
        # کپی در کلیپ‌بورد
        # if CLIPBOARD_AVAILABLE:
            # try:
            #     pyperclip.copy(final_prompt)
            #     print("📋 ✅ در کلیپ‌بورد کپی شد!")
            # except Exception as e:
            #     print(f"⚠️  خطا در کپی کلیپ‌بورد: {e}")
        
        # نمایش آمار
        print_stats(final_prompt)
        
        # نمایش پیش‌نمایش
        print("\n📄 پیش‌نمایش (۵۰۰ کاراکتر اول):")
        print("─" * 40)
        preview = final_prompt[:500]
        # if len(final_prompt) > 500:
        #     preview += "\n... [ادامه دارد]"
        print(preview)
        print("─" * 40)


if __name__ == "__main__":
    main()