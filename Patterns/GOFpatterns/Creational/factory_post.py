"""
An example of code after implementation of Factory pattern
according to a video on YouTube ArjanCodes channel https://www.youtube.com/watch?v=s_4ZrtQs8Do
"""
import pathlib

from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")


class ExporterFactory(ABC):
    """
    Factory that combines a video and an audio codec
    Doesn't maintain any of the instances it creates
    """

    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance"""

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        """returns a new audio exporter instance"""


class LowQualityExporter(ExporterFactory):
    """
    Factory aimed at providing high speed, lower quality export
    """

    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance"""
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        """returns a new audio exporter instance"""
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    """
    Factory aimed at providing lower speed, higher quality export
    """

    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance"""
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        """returns a new audio exporter instance"""
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    """
    Factory aimed at providing the lowest speed, master quality export
    """

    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance"""
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        """returns a new audio exporter instance"""
        return WAVAudioExporter()


def create_exporter() -> ExporterFactory:
    """
    Constructs and ExporterFactory based on user's input of quality
    :return: ExporterFactory
    """
    # read the desired export quality
    factories = {
        'low': LowQualityExporter(),
        'high': HighQualityExporter(),
        'master': MasterQualityExporter(),
    }
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}.")


def main(factory: ExporterFactory) -> None:
    """Main function."""
    # get the video and audio exporters
    video_exporter = factory.get_video_exporter()
    audio_exporter = factory.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    users_factory = create_exporter()
    main(users_factory)
