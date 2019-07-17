import os
import argparse


def write_file(value):
    path = ['./roles/', './role_mappings/']
    role_names = ['kibana','logrdr','monitoring','reporting']
    for i in path:
        if not os.path.exists(i):
            os.makedirs(i)
    for j in role_names:
        with open('./roles/{}_{}_user.json'.format(value, j), 'w+') as f:
            f.write('{}_{}_user'.format(value, i))
        with open('./role_mappings/{}_{}_user.json'.format(value, j), 'w+') as g:
            g.write('{}_{}_user'.format(value, i))



# def commands():
#     arguments = argparse.ArgumentParser()
#     arguments.add_argument('n', type=str, help='name of the app to be created')
#     val = arguments.parse_args()
#     write_file(val.n)

if __name__=="__main__":
    # content in the file to be written
    with open('roles.list', 'r+') as i:
        roles = i.readlines()
        for i in roles:
            write_file(i.split('\n')[0])