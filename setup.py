from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Sort code',
    url='http://github.com/valeri7122/clean-folder',
    author='Valerii',
    author_email='xenos@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:fold_sort']}
)