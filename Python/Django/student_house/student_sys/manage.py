#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    profile = os.environ.get('STUDENT_PROFILE', 'product')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "student_sys.settings.{}".format(profile))
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    execute_from_command_line(sys.argv)
