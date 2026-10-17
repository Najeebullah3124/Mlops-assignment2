#!/bin/bash
# Generate PDF from HTML using macOS Safari

HTML_FILE="MLOPS_ASSIGNMENT_REPORT.html"
PDF_FILE="MLOPS_ASSIGNMENT_REPORT.pdf"

echo "Generating PDF from HTML..."
echo "HTML file: $HTML_FILE"
echo "PDF file: $PDF_FILE"
echo ""

# Method 1: Try using Safari's print-to-PDF via AppleScript
if command -v osascript &> /dev/null; then
    echo "Attempting to generate PDF using Safari..."
    osascript <<EOF
tell application "Safari"
    activate
    open file POSIX file "$(pwd)/$HTML_FILE"
    delay 2
    tell application "System Events"
        keystroke "p" using {command down}
        delay 1
        keystroke "s" using {command down}
        delay 1
        keystroke "$(pwd)/$PDF_FILE"
        delay 1
        keystroke return
        delay 2
    end tell
    quit
end tell
EOF
    
    if [ -f "$PDF_FILE" ]; then
        echo "✅ PDF generated successfully: $PDF_FILE"
        exit 0
    fi
fi

# Method 2: Instructions for manual generation
echo ""
echo "============================================================"
echo "Manual PDF Generation (Recommended)"
echo "============================================================"
echo ""
echo "The HTML file has been opened in your browser."
echo ""
echo "To generate PDF:"
echo "1. In the browser, press Cmd+P (or go to File > Print)"
echo "2. In the print dialog, click 'PDF' button (bottom left)"
echo "3. Select 'Save as PDF'"
echo "4. Save as: $PDF_FILE"
echo ""
echo "The HTML file is ready at: $HTML_FILE"
echo "============================================================"

