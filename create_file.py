import json
import argparse

content = "hey"

def write_file():
    with open('./{}_to_write.json'.format(content),'w+') as f:
        f.write(content)

write_file()