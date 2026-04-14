#!/usr/bin/env python
import sys
import os

# Fix for 'cgi' removal in Python 3.14
try:
    import cgi
except ImportError:
    from types import ModuleType
    import collections
    mock_cgi = ModuleType('cgi')
    mock_cgi.FieldStorage = lambda: None
    sys.modules['cgi'] = mock_cgi

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()