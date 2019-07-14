import os
import argparse

#content in the file to be written
roles = ['kibana','logrdr','report','monitor']

def write_file(value):
    for i in roles:
        if not os.path.exists('./roles/'):
            os.makedirs('./roles/')
        elif os.path.exists('./roles/'):
            with open('./roles/{}_{}_user.json'.format(value, i), 'w+') as f:
                f.write('{}_{}_user'.format(value, i))
        else:
            with open('./roles/{}_{}_user.json'.format(value, i), 'w+') as f:
                f.write('{}_{}_user'.format(value, i))

        if not os.path.exists('./role_mappings/'):
            os.makedirs('./role_mappings/')
        elif os.path.exists('./role_mappings/'):
            with open('./role_mappings/{}_{}_user.json'.format(value, i), 'w+') as g:
                g.write('{}_{}_user'.format(value, i))
        else:
            with open('./role_mappings/{}_{}_user.json'.format(value, i), 'w+') as g:
                g.write('{}_{}_user'.format(value, i))


def commands():
    arguments = argparse.ArgumentParser()
    arguments.add_argument('n', type=str, help='name of the app to be created')
    val = arguments.parse_args()
    write_file(val.n)

commands()