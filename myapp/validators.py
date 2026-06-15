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
    
    # Whitelist approach: Allow only alphanumeric characters, spaces, and safe punctuation.
    # Excludes <, >, `, \, ^, ~ to prevent any form of code or HTML injection.
    allowed_pattern = re.compile(r'^[\w\s.,!?\'"()\-:;&/@+#%=*\[\]{}|$]*$')
    
    if not allowed_pattern.match(decoded):
        raise ValidationError("Input contains invalid characters. Only alphanumeric characters and standard punctuation are allowed.")
