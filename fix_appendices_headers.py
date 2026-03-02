import re
import glob

def fix_appendix_headers():
    for file_path in glob.glob('appendices/annx*.tex'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if \markboth exists already
        if '\\markboth' in content:
            continue

        # Look for \addcontentsline{toc}{chapter}{TITLE}
        pattern = r'(\\addcontentsline\{toc\}\{chapter\}\{(.*?)\})'
        
        def repl(m):
            title = m.group(2)
            # Add \markboth{title}{title} right after it
            return f"{m.group(1)}\n\\markboth{{{title}}}{{{title}}}"
        
        new_content = re.sub(pattern, repl, content, count=1)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed headers for {file_path}")

if __name__ == '__main__':
    fix_appendix_headers()
