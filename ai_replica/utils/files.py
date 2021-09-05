import glob
import ntpath

"""Tools to work with files"""


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
