from pytube import YouTube
from pycaption import WebVTTReader, SRTWriter
import os


def get_youtube_video_mp4(url, save_path, language_code='en'):
    # download video
    video = YouTube(url)
    print("Title: ", video.title)
    print("Downloading video...")
    video.streams.filter(file_extension='mp4').first().download(output_path=save_path)
    print("Finished.")

    # get subtitles
    print("Downloading subtitles...")
    print("captions: ", video.captions)
    subtitles = video.captions[language_code]
    xml_sub = subtitles.xml_captions
    # download xml subtitles
    xml_sub_path = os.path.join(save_path, f"{video.title}.xml")
    with open(xml_sub_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_sub)
    xml_file.close()
    # convert to srt
    srt_sub_path = os.path.join(save_path, f"{video.title}.srt")
    convert_xml_to_srt(xml_sub_path, srt_sub_path)


def convert_xml_to_srt(xml_path, srt_path):
    # Load XML captions
    with open(xml_path, 'r', encoding='utf-8') as xml_file:
        xml_content = xml_file.read()
    try:
        # Parse XML captions using WebVTTReader
        reader = WebVTTReader()
        captions = reader.read(xml_content)

        # Write captions in SRT format using SRTWriter
        writer = SRTWriter()
        with open(srt_path, 'w', encoding='utf-8') as srt_file:
            srt_file.write(writer.write(captions))
    except Exception as e:
        print("Exception while parsing XML: ", e)


if __name__ == "__main__":
    save_path = os.path.join('videos')
    get_youtube_video_mp4('https://www.youtube.com/watch?v=Hi7Rx3En7-k', save_path, 'fr')
