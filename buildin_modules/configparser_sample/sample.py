from configparser import ConfigParser
from pathlib import Path

cfg = ConfigParser()
cfg.read('myapp.ini')

# same, get int
assert int(cfg['http']['port']) == cfg['http'].getint('port')

# direct get from section
output_filename = Path(cfg['default']['output'], 'my_output.html')
print(output_filename, cfg['http'].get('host'))

# list all sections
section_list = cfg.sections()
print(section_list)

# list section members
keys_of_default_section = cfg['default'].keys()
values_of_default_section = cfg['default'].values()
print(keys_of_default_section, list(keys_of_default_section))
print(values_of_default_section, list(values_of_default_section))
for key in cfg['default']:
    print(key)

# member check
print("member check:", 'port' in cfg['http'])

# set/get member like dict directly
counter = int(cfg['save']['count'])
counter += 1
cfg['save']['count'] = str(counter)

# write back
with open('myapp.ini', 'w', encoding='cp950') as f:
    cfg.write(f)
