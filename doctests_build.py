import unittest
import doctest

from ai_replica.utils.files import find_files

"""Builds doctests for the doctests_run bash script."""

if __name__ == "__main__":
    file_names = find_files("", ".py")
    module_names = []
    for name in file_names:
        print(name)
        if "venv" not in name and ".git" not in name:
            clean_name = name.split(".")[0]
            clean_name = clean_name.replace("/", ".")
            module_names.append(clean_name)
    print(f"search complete, found {len(module_names)} modules: {module_names}")

    loader = unittest.TestLoader()
    test_suite = loader.discover("ai_replica")
    for name in module_names:
        test_suite.addTests(doctest.DocTestSuite(name))

    unittest.TextTestRunner(verbosity=1).run(test_suite)
