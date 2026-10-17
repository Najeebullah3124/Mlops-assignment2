#!/usr/bin/env python3
"""
Script to convert MLOPS_ASSIGNMENT_REPORT.md to PDF
Requires: markdown, weasyprint, or can use pandoc
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check if required dependencies are available."""
    dependencies = {
        'pandoc': False,
        'weasyprint': False,
        'markdown': False
    }
    
    # Check pandoc
    try:
        result = subprocess.run(['pandoc', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            dependencies['pandoc'] = True
            print("✅ pandoc found")
    except FileNotFoundError:
        print("❌ pandoc not found")
    
    # Check Python packages
    try:
        import weasyprint
        dependencies['weasyprint'] = True
        print("✅ weasyprint found")
    except ImportError:
        print("❌ weasyprint not found (install: pip install weasyprint)")
    
    try:
        import markdown
        dependencies['markdown'] = True
        print("✅ markdown found")
    except ImportError:
        print("❌ markdown not found (install: pip install markdown)")
    
    return dependencies

def convert_with_pandoc(md_file, pdf_file):
    """Convert Markdown to PDF using pandoc."""
    cmd = [
        'pandoc',
        md_file,
        '-o', pdf_file,
        '--pdf-engine=pdflatex',
        '--variable', 'geometry:margin=1in',
        '--variable', 'fontsize=11pt',
        '--variable', 'documentclass=article'
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ PDF generated: {pdf_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error with pandoc: {e}")
        return False
    except FileNotFoundError:
        print("❌ pandoc not installed")
        return False

def convert_with_weasyprint(md_file, pdf_file):
    """Convert Markdown to PDF using weasyprint."""
    try:
        import markdown
        from weasyprint import HTML, CSS
        from weasyprint.text.fonts import FontConfiguration
        
        # Read markdown
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert to HTML
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
        
        # Add CSS styling
        html_doc = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                @page {{
                    size: A4;
                    margin: 2cm;
                }}
                body {{
                    font-family: 'Times New Roman', serif;
                    line-height: 1.6;
                    color: #333;
                }}
                h1 {{
                    color: #2c3e50;
                    border-bottom: 3px solid #3498db;
                    padding-bottom: 10px;
                }}
                h2 {{
                    color: #34495e;
                    border-bottom: 2px solid #95a5a6;
                    padding-bottom: 5px;
                    margin-top: 30px;
                }}
                h3 {{
                    color: #7f8c8d;
                    margin-top: 20px;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 5px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                    border-left: 4px solid #3498db;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }}
                th {{
                    background-color: #3498db;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f2f2f2;
                }}
                blockquote {{
                    border-left: 4px solid #3498db;
                    margin: 20px 0;
                    padding-left: 20px;
                    color: #555;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Generate PDF
        HTML(string=html_doc).write_pdf(pdf_file)
        print(f"✅ PDF generated: {pdf_file}")
        return True
        
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return False

def create_html_version(md_file, html_file):
    """Create an HTML version that can be printed to PDF from browser."""
    try:
        import markdown
        
        # Read markdown
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert to HTML
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
        
        # Add CSS styling
        html_doc = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>MLOps Assignment Report</title>
            <style>
                @media print {{
                    @page {{
                        size: A4;
                        margin: 2cm;
                    }}
                }}
                body {{
                    font-family: 'Times New Roman', serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 900px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                h1 {{
                    color: #2c3e50;
                    border-bottom: 3px solid #3498db;
                    padding-bottom: 10px;
                }}
                h2 {{
                    color: #34495e;
                    border-bottom: 2px solid #95a5a6;
                    padding-bottom: 5px;
                    margin-top: 30px;
                }}
                h3 {{
                    color: #7f8c8d;
                    margin-top: 20px;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 5px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                    border-left: 4px solid #3498db;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }}
                th {{
                    background-color: #3498db;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f2f2f2;
                }}
                blockquote {{
                    border-left: 4px solid #3498db;
                    margin: 20px 0;
                    padding-left: 20px;
                    color: #555;
                }}
                .print-button {{
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    background-color: #3498db;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
                }}
                .print-button:hover {{
                    background-color: #2980b9;
                }}
                @media print {{
                    .print-button {{
                        display: none;
                    }}
                }}
            </style>
        </head>
        <body>
            <button class="print-button" onclick="window.print()">Print to PDF</button>
            {html_content}
        </body>
        </html>
        """
        
        # Write HTML file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_doc)
        
        print(f"✅ HTML version created: {html_file}")
        print("   Open in browser and use 'Print to PDF' to generate PDF")
        return True
        
    except ImportError:
        print("❌ markdown package not found (install: pip install markdown)")
        return False
    except Exception as e:
        print(f"❌ Error creating HTML: {e}")
        return False

def main():
    """Main function."""
    md_file = 'MLOPS_ASSIGNMENT_REPORT.md'
    pdf_file = 'MLOPS_ASSIGNMENT_REPORT.pdf'
    html_file = 'MLOPS_ASSIGNMENT_REPORT.html'
    
    if not os.path.exists(md_file):
        print(f"❌ Error: {md_file} not found")
        sys.exit(1)
    
    print("=" * 60)
    print("MLOps Assignment Report - PDF Generator")
    print("=" * 60)
    print()
    
    # Check dependencies
    print("Checking dependencies...")
    deps = check_dependencies()
    print()
    
    # Try different conversion methods
    success = False
    
    if deps['pandoc']:
        print("Attempting conversion with pandoc...")
        success = convert_with_pandoc(md_file, pdf_file)
        if success:
            return
    
    if deps['weasyprint']:
        print("Attempting conversion with weasyprint...")
        success = convert_with_weasyprint(md_file, pdf_file)
        if success:
            return
    
    # Fallback: Create HTML version
    print("Creating HTML version (can be printed to PDF from browser)...")
    create_html_version(md_file, html_file)
    print()
    print("=" * 60)
    print("Instructions:")
    print("1. Open MLOPS_ASSIGNMENT_REPORT.html in your browser")
    print("2. Click 'Print to PDF' button or use Ctrl+P (Cmd+P on Mac)")
    print("3. Select 'Save as PDF' as destination")
    print("=" * 60)

if __name__ == '__main__':
    main()

