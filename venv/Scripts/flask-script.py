#!"c:\users\chuks nnadozie\pycharmprojects\nanowize2\venv\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'Python-dev==2.0.0.dev0','console_scripts','flask'
__requires__ = 'Python-dev==2.0.0.dev0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Python-dev==2.0.0.dev0', 'console_scripts', 'flask')()
    )
