import os

import magic
from django.core.exceptions import ValidationError

ALLOWED_MIME_TYPES = [
    "image/jpeg",
    "image/png",
    "image/webp",
    "application/pdf",
    "application/msword",
]

BLOCKED_EXTENSIONS = [".py", ".php", ".js", ".html", ".sh"]


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
