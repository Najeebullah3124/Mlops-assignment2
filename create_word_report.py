#!/usr/bin/env python3
"""
Create Word document from Markdown report
Removes emojis and converts markdown lists to proper formatting
"""

import re
import sys

try:
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
except ImportError:
    print("Installing python-docx...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx", "--quiet"])
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn

def remove_emojis(text):
    """Remove emojis from text."""
    # Remove common emojis
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001F900-\U0001F9FF"  # supplemental symbols
        "\U0001FA00-\U0001FA6F"  # chess symbols
        "\U0001FA70-\U0001FAFF"  # symbols and pictographs
        "\U00002600-\U000026FF"  # miscellaneous symbols
        "\U00002700-\U000027BF"  # dingbats
        "]+", flags=re.UNICODE)
    text = emoji_pattern.sub('', text)
    
    # Remove specific emoji characters
    text = text.replace('✅', '')
    text = text.replace('⚠️', '')
    text = text.replace('❌', '')
    text = text.replace('🚀', '')
    text = text.replace('📋', '')
    text = text.replace('📊', '')
    text = text.replace('📝', '')
    text = text.replace('🎯', '')
    text = text.replace('✨', '')
    text = text.replace('🔧', '')
    text = text.replace('📄', '')
    text = text.replace('📋', '')
    
    return text.strip()

def clean_markdown_line(line):
    """Clean markdown line - remove list hyphens and emojis."""
    line = remove_emojis(line)
    
    # Remove markdown list hyphens at start of line
    line = re.sub(r'^[\s]*[-]\s+', '', line)
    line = re.sub(r'^[\s]*\*\s+', '', line)
    
    # Remove numbered list markers but keep the number
    line = re.sub(r'^(\d+)\.\s+', r'\1. ', line)
    
    return line.strip()

def parse_markdown_to_doc(md_file, docx_file):
    """Parse markdown file and create Word document."""
    doc = Document()
    
    # Set default font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(11)
    
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    i = 0
    in_code_block = False
    code_block_lines = []
    in_list = False
    
    while i < len(lines):
        line = lines[i].rstrip()
        original_line = line
        
        # Handle code blocks
        if line.startswith('```'):
            if in_code_block:
                # End code block
                if code_block_lines:
                    code_para = doc.add_paragraph()
                    code_run = code_para.add_run('\n'.join(code_block_lines))
                    code_run.font.name = 'Courier New'
                    code_run.font.size = Pt(9)
                    code_para.style = 'No Spacing'
                code_block_lines = []
                in_code_block = False
            else:
                # Start code block
                in_code_block = True
            i += 1
            continue
        
        if in_code_block:
            code_block_lines.append(line)
            i += 1
            continue
        
        # Clean the line
        cleaned = clean_markdown_line(line)
        
        # Handle headers
        if line.startswith('# '):
            para = doc.add_heading(cleaned, level=1)
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            in_list = False
        elif line.startswith('## '):
            para = doc.add_heading(cleaned, level=2)
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            in_list = False
        elif line.startswith('### '):
            para = doc.add_heading(cleaned, level=3)
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            in_list = False
        elif line.startswith('#### '):
            para = doc.add_heading(cleaned, level=4)
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            in_list = False
        # Handle horizontal rules
        elif line.strip() == '---' or line.strip() == '***':
            doc.add_paragraph('_' * 80)
            in_list = False
        # Handle empty lines
        elif not cleaned and not original_line.strip().startswith('-') and not original_line.strip().startswith('*'):
            if not in_list:
                doc.add_paragraph()
            in_list = False
        # Handle list items (without hyphens)
        elif original_line.strip().startswith('-') or original_line.strip().startswith('*') or (original_line.strip() and re.match(r'^\d+\.', original_line.strip())):
            if cleaned:
                para = doc.add_paragraph(cleaned, style='List Bullet' if not re.match(r'^\d+\.', original_line.strip()) else 'List Number')
                in_list = True
        # Handle regular paragraphs
        elif cleaned:
            para = doc.add_paragraph(cleaned)
            in_list = False
        else:
            i += 1
            continue
        
        i += 1
    
    # Save document
    doc.save(docx_file)
    print(f"Word document created: {docx_file}")

def main():
    md_file = 'MLOPS_ASSIGNMENT_REPORT.md'
    docx_file = 'MLOPS_ASSIGNMENT_REPORT.docx'
    
    try:
        parse_markdown_to_doc(md_file, docx_file)
        print(f"Successfully created Word document: {docx_file}")
    except Exception as e:
        print(f"Error creating Word document: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()

