import os
import re
import urllib.parse
import html

import magic
from django.core.exceptions import ValidationError

ALLOWED_MIME_TYPES = [
    "image/jpeg",
    "image/png",
    "image/webp",
    "application/pdf",
    "application/msword",
]

BLOCKED_EXTENSIONS = [".py", ".php", ".js", ".html", ".sh", ".svg"]


def validate_file(file):
    print("validating....")
    mime = magic.from_buffer(file.read(2048), mime=True)
    file.seek(0)

    if mime not in ALLOWED_MIME_TYPES:
        raise ValidationError("Invalid file type")


def validate_extension(file):
    print("validating extension ....")
    ext = os.path.splitext(file.name)[1].lower()
    if ext in BLOCKED_EXTENSIONS:
        raise ValidationError("File type not allowed")


def validate_size(file):
    print("validating size ....")
    if file.size > 5 * 1024 * 1024:
        raise ValidationError("File too large (max 5MB)")

def no_html_validator(value):
    # Convert to string and normalize
    text = str(value)
    
    # URL Decoding and HTML Entity Decoding
    # We unquote twice to handle potential double encoding and then unescape HTML entities
    decoded = html.unescape(urllib.parse.unquote(urllib.parse.unquote(text)))
    
    # Check for HTML tags
    if re.search(r'<.*?>', decoded):
        raise ValidationError("HTML content or encoded HTML characters are not allowed.")

    # Check for dangerous patterns frequently used in XSS injections
    dangerous_patterns = [
        r'javascript:',
        r'data:text/html',
        r'vbscript:',
        r'on\w+\s*=',  # Event handlers like onclick, onload, etc.
        r'<script',
        r'expression\(', # Legacy IE
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, decoded, re.IGNORECASE):
            raise ValidationError("Encoded injection patterns or script content detected.")
