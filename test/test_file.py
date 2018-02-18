import unittest
from shutil import rmtree
from os import listdir
from os.path import join, abspath, split
from seaborn_file.file import *

TEST_PATH = split(abspath(__file__))[0]
TEST_DIRS = 'tmp'
TEST_DATA = 'data'
TEST_FILE = 'hello_world.txt'
TEST_CONT = 'Hello\nWorld'
TEST_CODE = 'test_file.py'

PATH_NAME = split(TEST_PATH)[1]


class TestFile(unittest.TestCase):

    def tearDown(self):
        rmtree(join(TEST_PATH, TEST_DIRS), ignore_errors=True)

    def test_mkdir(self):
        mkdir(join(TEST_PATH, TEST_DIRS))
        self.assertIn(TEST_DIRS, listdir(TEST_PATH))

    def test_mkdir_for_file(self):
        mkdir_for_file(join(TEST_PATH, TEST_DIRS, TEST_FILE))
        self.assertIn(TEST_DIRS, listdir(TEST_PATH))

    def test_find_folder(self):
        self.assertEqual(TEST_PATH, find_folder('test'))

    def test_find_file(self):
        self.assertEqual(find_file(TEST_CODE),
                         join(TEST_PATH, TEST_CODE))

    def test_sync_folder(self):
        sync_folder(join(TEST_PATH, TEST_DATA), join(TEST_PATH, TEST_DIRS))
        self.assertIn(TEST_FILE, listdir(join(TEST_PATH, TEST_DIRS)))

    def test_read_local_file(self):
        self.assertEqual(read_local_file(join(TEST_DATA, TEST_FILE)),
                         'Hello\nWorld')

    def test_relative_path(self):
        mkdir(join(TEST_PATH, TEST_DIRS))
        mkdir(join(TEST_PATH, TEST_DIRS, TEST_DIRS))
        self.assertEqual(
            relative_path(join(TEST_DIRS, TEST_DIRS)),
            join(TEST_PATH, TEST_DIRS, TEST_DIRS))

    def test_read_file(self):
        self.assertEqual(read_file(join(TEST_PATH, TEST_DATA, TEST_FILE)),
                         TEST_CONT)

    def test_copy_file(self):
        copy_file(join(TEST_PATH, TEST_DATA, TEST_FILE),
                  join(TEST_PATH, TEST_DIRS, TEST_FILE))
        with open(join(TEST_PATH, TEST_DIRS, TEST_FILE), 'r') as fp:
            self.assertEqual(fp.read(), TEST_CONT)

    def test_read_folder(self):
        result = read_folder(TEST_PATH)
        self.assertEqual(TEST_CONT, result['%s/%s'%(TEST_DATA, TEST_FILE)])

    def test_find_path(self):
        self.assertTrue(find_path("hello_world.txt").endswith('\data\hello_world.txt'),
                        "Did not find correct directory")

if __name__ == '__main__':
    unittest.main()
