import csv
import json

from typing import Dict


class BaseReader:
    def read(self, fileobj):
        pass


class BaseWriter:
    def dump(self, data, data):
        pass


class CsvReader(BaseReader):
    def read(self, fileobj) -> List[List[str]]:
        return [s for s in csv.reader(fileobj)]


class CsvWriter(BaseWriter):
    def dump(self, data: List[List[str]], fileobj) -> None:
        writer = csv.writer(fileobj)
        writer.writerows(data)


class JsonReader(BaseReader):
    def read(self, fileobj) -> Dict:
        return json.load(fileobj)


class JsonWriter(BaseWriter):
    def dump(self, data: Dict, fileobj) -> None:
        json.dump(data, fileobj)


class TxtReader(BaseReader):
    def read(self, fileobj) -> List[str]:
        return fileobj.readlines()


class TxtWriter(BaseWriter):
    def dump(self, data: List[str], fileobj) -> None:
        fileobj.writelines(data)


def read_data(fileobj, reader: BaseReader):
    return reader.read(fileobj)


def dump_data(data, fileobj, writer: BaseWriter):
    writer.dump(data, fileobj)
