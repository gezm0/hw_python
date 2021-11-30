# how to work with os using os module

import os

print(f"I'm here: {os.getcwd()}")
dir_name = 'test_dir'

# checking if it's a directory (not recommended to use)
# this returns 'true' or 'false', 'true' in our case
if os.path.isdir('test_dir'):
    print('this dir exists')
else:
# making a dir
    os.mkdir(dir_name)
    print(f"{dir_name} was created")

os.chdir(dir_name)
print(f"Now I'm here {os.getcwd()}")

# chdir one level up
os.chdir('../')
print(f"And now there {os.getcwd()}")

# that's how to get environment value from system
#os.environ.get('env_name')