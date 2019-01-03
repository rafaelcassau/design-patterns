"""
Decorator is a structural pattern that allows
adding new behaviors to objects dynamically by
placing them inside special wrapper objects.

Using decorator you can wrap objects countless
number of times since both target objects and
decorators follow the same interface. The resulting
object will get a stacking behavior of all wrappers.
"""
import os
import zlib
import base64
import binascii
from pathlib import Path


class DataSourceInterface:

    def write_data(self, data: str) -> None:
        raise NotImplementedError()

    def read_data(self) -> str:
        raise NotImplementedError()


class DataSourceFile(DataSourceInterface):

    def __init__(self, name: str):
        self._name = name

    def write_data(self, data: str) -> None:
        f = open(self._name, 'w')
        f.write(data)
        f.close()

    def read_data(self) -> str:
        f = open(self._name, 'rb')
        data = f.read()
        f.close()
        return data


class DataSourceAbstractDecorator(DataSourceInterface):

    def __init__(self, wrappee: DataSourceInterface):
        self._wrappee = wrappee

    def write_data(self, data: str) -> None:
        self._wrappee.write_data(data)

    def read_data(self) -> str:
        data = self._wrappee.read_data()
        return data


class EncryptionDecorator(DataSourceAbstractDecorator):

    def write_data(self, data: str) -> None:
        data = self.encode(data)
        self._wrappee.write_data(data)

    def read_data(self) -> str:
        data = self._wrappee.read_data()
        return self.decode(data)

    def encode(self, data: str) -> str:
        encoded = base64.b64encode(bytes(data, 'utf8'))
        return str(encoded, encoding='utf8')

    def decode(self, data: str) -> str:
        decoded = base64.b64decode(data)
        return str(decoded, encoding='utf8')


class CompressionDecorator(DataSourceAbstractDecorator):

    def __init__(self, wrappee: DataSourceInterface):
        super().__init__(wrappee)
        self._level = 6

    def write_data(self, data: str) -> None:
        data = self.compress(data)
        self._wrappee.write_data(data)

    def read_data(self) -> str:
        data = self._wrappee.read_data()
        data = self.decompress(data)
        return data

    def set_compress_level(self, level: int) -> None:
        self.level = level

    def get_compress_level(self) -> int:
        return self._level

    def compress(self, data: str) -> str:
        compressed = zlib.compress(bytes(data, 'utf8'), self._level)
        compressed = base64.b64encode(compressed)
        return str(compressed, encoding='utf8')

    def decompress(self, data: str) -> str:
        decompressed = base64.b64decode(data)
        decompressed = zlib.decompress(decompressed)
        return str(decompressed, encoding='utf8')


class Demo:

    def run(self) -> None:
        current_path = Path().resolve()
        file_path = f'{current_path}{os.sep}output_demo.txt'

        salary_records: str = "Name,Salary\nJonh Smith,100000\nSteven Jobs,912000"
        encoded: DataSourceAbstractDecorator = CompressionDecorator(EncryptionDecorator(DataSourceFile(file_path)))
        encoded.write_data(salary_records)

        plain: DataSourceFile = DataSourceFile(file_path)
        
        print('- Input -------------------')
        print(salary_records)
        print('- Encoded -----------------')
        print(plain.read_data())
        print('- Decoded ------------------')
        print(encoded.read_data())


demo: Demo = Demo()
demo.run()