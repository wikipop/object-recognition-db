import pandas


def filter_list_dir_by_extensions(list_dir: list[str], extensions: list[str] | tuple[str]) -> list[str]:
    return [file for file in list_dir if file.endswith(tuple(extensions))]