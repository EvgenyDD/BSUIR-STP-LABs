import os
print('Current working dir: ' + str(os.getcwd()))
print('Change dir: os.chdir(\'new_dir\')')
print('Absolute path os.path.realpath(\'chapter_3.py\'): ' + os.path.realpath('chapter_3.py')) 
print('os.path.join(\'/home/user/BSUIR-STP-LABS/test\', \'chapter_3.py\'):')
print('\t' + str(os.path.join('/home/user/BSUIR-STP-LABS/test', 'chapter_3.py')))
print('os.path.expanduser(\'~\')')
print('\t' + str(os.path.expanduser('~')))
print('os.path.split(pathname)')
pathname = '/home/user/BSUIR-STP-LABS/chapter3.py'
print('Path name: ' + pathname)
(dirname, filename) = os.path.split(pathname)
print('\tDir. name: ' + dirname)
print('\tFile name: ' + filename)
print('os.path.splitext(filename)')
(shortname, extension) = os.path.splitext(filename)
print('\tShort name: ' + shortname)
print('\tExtension: ' + extension)
print('\n\n')
print('Module glob - view files')
import glob
import time
print('All scripts in cur. folder: glob.glob(\'*.py\')')
print(glob.glob('*.py'))
print('\n\nFile info - os.stat(\'filename\')')
metadata = os.stat('chapter3.py')
print('Write time: ')
print(time.localtime(metadata.st_mtime))
print('File size: ' + str(metadata.st_size) + ' bytes')
print('\n\nList generators:')
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('a_list: ' + str(a_list))
print('[elem * 2 for elem in a_list]: ' + str([elem * 2 for elem in a_list]))
print('[elem * 2 for elem in a_list if elem > 5]: ' + str([elem * 2 for elem in a_list if elem > 5]))
print('[os.path.realpath(f) for f in glob.glob(\'*.py\')]: ')
print('\t' + str([os.path.realpath(f) for f in glob.glob('*.py')]))
print('[(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob(\'*.py\')]: ')
print('\t' + str([(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')]))
print('Dict. generators: {f:os.stat(f) for f in glob.glob(\'*test*.py\')}')
print({f:os.stat(f) for f in glob.glob('*.py')})

a_dict = {'a': 1, 'b': 2, 'c': 3}
{value:key for key, value in a_dict.items()}

a_set = set(range(10))
{x ** 2 for x in a_set}
{x for x in a_set if x % 2 == 0}
{2**x for x in range(10)}
