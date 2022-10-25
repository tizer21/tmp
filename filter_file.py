from typing import Iterator, List, TextIO


def is_suitable_line(line: str, lowered_words: List[str]) -> bool:
    for word in line.split():
        if word.lower() in lowered_words:
            return True

    return False


def filter_fileobj(fileobj: TextIO, words: List[str]) -> Iterator[str]:
    lowered_words = [word.lower() for word in words]

    return filter(lambda line: is_suitable_line(line, lowered_words), fileobj)


def filter_file(file_name: str, words: List[str]) -> Iterator[str]:
    fileobj = open(file_name, 'r')

    return filter_fileobj(fileobj, words)
