"""Make skill modules to be importable from other modules"""

from ai_replica.utils.files import find_files

skills_names = find_files(
    path="ai_replica/skills/",
    file_type=".py",
    exclude=["__init__"],
    only_filenames7=True,
)

__all__ = skills_names
