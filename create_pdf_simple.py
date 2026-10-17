#!/usr/bin/env python3
"""
Simple PDF generation script using markdown and HTML
Creates a PDF-ready HTML file that can be converted using browser print
"""

import os
import subprocess
import sys

def create_pdf_from_html():
    """Create PDF from HTML using macOS tools or provide instructions."""
    html_file = 'MLOPS_ASSIGNMENT_REPORT.html'
    pdf_file = 'MLOPS_ASSIGNMENT_REPORT.pdf'
    
    if not os.path.exists(html_file):
        print(f"❌ Error: {html_file} not found")
        return False
    
    # Try using macOS's built-in tools
    print("Attempting to generate PDF...")
    
    # Method 1: Try using wkhtmltopdf if available
    try:
        result = subprocess.run(['which', 'wkhtmltopdf'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            cmd = ['wkhtmltopdf', '--page-size', 'A4', 
                   '--margin-top', '20mm', '--margin-bottom', '20mm',
                   '--margin-left', '20mm', '--margin-right', '20mm',
                   html_file, pdf_file]
            subprocess.run(cmd, check=True)
            print(f"✅ PDF generated: {pdf_file}")
            return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass
    
    # Method 2: Try using Python's weasyprint (if system deps available)
    try:
        from weasyprint import HTML
        HTML(filename=html_file).write_pdf(pdf_file)
        print(f"✅ PDF generated: {pdf_file}")
        return True
    except Exception as e:
        print(f"⚠️  WeasyPrint not available: {e}")
    
    # Method 3: Open in browser with instructions
    print("\n" + "="*60)
    print("PDF Generation Instructions")
    print("="*60)
    print(f"\n✅ HTML file ready: {html_file}")
    print("\nTo generate PDF:")
    print("1. Open the HTML file in your browser:")
    print(f"   open {html_file}")
    print("\n2. Press Cmd+P (or Ctrl+P) to print")
    print("3. Select 'Save as PDF' as destination")
    print("4. Choose location and save")
    print("\nAlternatively, you can:")
    print("- Use online converters (e.g., html2pdf.com)")
    print("- Use Adobe Acrobat or other PDF tools")
    print("- Use pandoc if installed: pandoc MLOPS_ASSIGNMENT_REPORT.md -o report.pdf")
    print("="*60)
    
    # Try to open the file
    try:
        if sys.platform == 'darwin':  # macOS
            subprocess.run(['open', html_file])
            print(f"\n✅ Opened {html_file} in your default browser")
        elif sys.platform == 'linux':
            subprocess.run(['xdg-open', html_file])
        elif sys.platform == 'win32':
            subprocess.run(['start', html_file], shell=True)
    except Exception:
        pass
    
    return False

if __name__ == '__main__':
    create_pdf_from_html()

