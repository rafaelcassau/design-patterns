"""
Facade is structural design pattern that provides a simplified
(but limited) interface to a library, a framework, or any other
complex set of classes.
"""
import tempfile


class VideoFile:

    def __init__(self, name: str):
        self.name = name
        self.codec_type = name.split('.')[0]

    def get_codec_type(self) -> str:
        return self.codec_type

    def get_name(self) -> str:
        return self.name


class CodecInterface:

    def get_type(self):
        raise NotImplementedError()


class MPEG4CompressionCodec(CodecInterface):

    def get_type(self) -> str:
        return 'mp4'


class OggCompressionCodec(CodecInterface):

    def get_type(self) -> str:
        return 'ogg'


class CodecFactory:

    @staticmethod
    def extract(file: VideoFile) -> CodecInterface:
        type = file.get_codec_type()
        if type == 'mp4':
            print('CodecFactory: extracting mpeg audio...')
            return MPEG4CompressionCodec()
        else:
            print('CodecFactory: extracting ogg audio...')
            return OggCompressionCodec()


class BitrateReader:

    @staticmethod
    def read(file: VideoFile, codec: CodecInterface) -> VideoFile:
        print('BitrateReader: reading file...')
        return file

    @staticmethod
    def convert(buffer: VideoFile, codec: CodecInterface) -> VideoFile:
        print('BitrateReader: writing file...')
        return buffer


class AudioMixer:

    def fix(self, result: VideoFile):
        print('AudioMixer: fixing audio...')
        temp = tempfile.TemporaryFile()
        return temp


class VideoConversionFacade:

    def convert_video(self, file_name: str, format: str):
        print('VideoConversionFacade: conversion started.')
        file = VideoFile(file_name)
        source_codec = CodecFactory.extract(file)

        if format == 'mp4':
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer = BitrateReader.read(file, source_codec)
        intermediate_result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer().fix(intermediate_result)
        print('VideoConversionFacade: conversion completed.')

        return result


converter = VideoConversionFacade()
mp4_video = converter.convert_video('youtubevideo.ogg', 'mp4')
