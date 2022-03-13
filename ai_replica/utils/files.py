import glob
import ntpath
import json
import os
import pathlib

"""Tools to work with files"""

cprint_verbose7 = True  # if true, the cprint func will print to sdout


def set_cprint_switch(ibool):
    global cprint_verbose7
    cprint_verbose7 = ibool


def cprint(*args):
    """same as print(), but prints only if the cprint_verbose7 == True.
    Useful for debug purposes.
    >>> backup_value = cprint_verbose7
    >>> set_cprint_switch(False)
    >>> cprint("some", {"values" : "here"})
    >>> set_cprint_switch(True)
    >>> cprint("some", {"values" : "here"})
    ('some', {'values': 'here'})
    >>> set_cprint_switch(backup_value)
    """
    if cprint_verbose7:
        print(args)


def get_full_path(filename, fake_parent_location=None):
    """Returns the full path of a file assuming that it's located in the
    same dir as this script.
    If the input is already a full path (with or without "~/"), it will return
    the input without modifications.
    >>> set_cprint_switch(False)
    >>> res = get_full_path('some/path')
    >>> res.endswith('/some/path')
    True
    >>> get_full_path('some/path', fake_parent_location='/home/bot')
    '/home/bot/some/path'
    >>> get_full_path('some/path/', fake_parent_location='/home/bot')
    '/home/bot/some/path/'
    >>> get_full_path('some/path/', fake_parent_location='/home/bot/')
    '/home/bot/some/path/'
    >>> get_full_path(dict())
    >>> get_full_path('~/some/path')
    '~/some/path'
    """
    if isinstance(filename, str):
        if filename.strip()[0:2] == "~/":
            full_path = filename
        else:
            if fake_parent_location is None:
                parent_location = os.path.realpath(
                    os.path.join(os.getcwd(), os.path.dirname(__file__))
                )
            else:
                parent_location = fake_parent_location
            full_path = os.path.join(parent_location, filename)
    else:
        full_path = None
        cprint("Error: this filename is not a string:", str(filename))
    return full_path


def get_main_dir_path(parent_level=1):
    """Returns the path to the dir where all the replica code is located.

    For example, if the path to this very module is '/stuff/AI-replica/ai_replica/utils/files.py',
    then this func will return '/stuff/AI-replica/'

    parent_level indicates how many levels one must go to reach the main dir,
    counting from the level of the dir where this script is located.
    Unless you want to move this module to some other place, there is no reason to change the parent_level.
    """
    parent_dir_location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    return str(pathlib.Path(parent_dir_location).parents[parent_level])


def get_filename_and_ext(path):
    """
    >>> get_filename_and_ext("AI-replica/ai_replica/skills/translate.py")
    ('translate', 'py')

    """
    basename = ntpath.basename(path)
    filename, ext = basename.split(".")
    return filename, ext


def find_files(path, file_type, exclude=None, only_filenames7=False):
    """
    >>> test_path = "ai_replica/resources/mock_data/for_files_tests/"
    >>> find_files(path=test_path, file_type=".py", exclude=None, only_filenames7=False)
    ['ai_replica/resources/mock_data/for_files_tests/file2.py', 'ai_replica/resources/mock_data/for_files_tests/file3.py']
    >>> find_files(path=test_path, file_type=".py", exclude=["2"], only_filenames7=True)
    ['file3']
    """
    raw_files = [f for f in glob.glob(path + "**/*" + file_type, recursive=True)]

    if isinstance(exclude, list):
        filtered_files = []
        for element in exclude:
            for path in raw_files:
                if element not in path:
                    filtered_files.append(path)
    else:
        filtered_files = raw_files

    cleaned_files = []
    if only_filenames7:
        for path in filtered_files:
            filename, _ = get_filename_and_ext(path)
            cleaned_files.append(filename)
    else:
        cleaned_files = filtered_files

    sorted_files = sorted(cleaned_files)  # to make the order of the list deterministic
    res = sorted_files
    return res


def write_to_json(path, data_dict):
    with open(path, "w") as f:
        json.dump(data_dict, f, ensure_ascii=False)


def read_json(path):
    with open(path) as f:
        res = json.load(f)
    return res


def is_file(fpath):
    """Returns True if there is a file at the given path, False otherwise."""
    return os.path.isfile(fpath)


PERSONAL_DATA_DIR = os.path.abspath(os.path.dirname(__file__) + "/../../personal_data")
