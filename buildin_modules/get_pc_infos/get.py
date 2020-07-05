import inspect
import os
import platform
import re
import socket
import sys

import psutil

sys.getwindowsversion()
sys.version
sys.version_info
sys.platform

platform.uname()
platform.version()
platform.node()
platform.win32_ver()
platform.win32_edition()
platform.system()

socket.gethostname()

with open('infos_inspect.log', 'w') as f:
    member = inspect.getmembers(platform)
    f.write("\n".join('%s %s' % x for x in member))

show_member = [print(k, v) for k, v in member]
print(show_member)

win_service = list(psutil.win_service_iter())
with open('infos_win_service.log', 'w') as f:
    for service in win_service:
        try:
            f.write(str(service) + "\n")
        except Exception:
            pass
s = psutil.win_service_get('alg')
print(s.as_dict())

find_update = re.compile("update")
for service in win_service:
    if find_update.search(str(service)):
        print(service)
