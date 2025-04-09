

import warnings
warnings.filterwarnings("ignore")
bucketname = "summery_bucket"
from pydub import AudioSegment
import io
import os


warnings.filterwarnings("ignore")
from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech_v1p1beta1 import enums
from google.cloud.speech_v1p1beta1 import types
import wave
from google.cloud import storage
import requests
from google.cloud import storage
# WARNING; WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload link.
storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024* 1024 # 5 MB
storage.blob._MAX_MULTIPART_SIZE = 5 * 1024* 1024 # 5 MB
import warnings

warnings.filterwarnings("ignore")

def mp3_to_wav(audio_file_name):
    print("20%: Checking File is Wav or not")
    if audio_file_name.split('.')[1] == 'mp3':
        sound = AudioSegment.from_mp3(audio_file_name)
        audio_file_name = audio_file_name.split('.')[0] + '.wav'
        sound.export(audio_file_name, format="wav")


def frame_rate_channel(audio_file_name):
    with wave.open(audio_file_name, "rb") as wave_file:
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        print("30%: Checking frame rate channel")
        print(frame_rate)
        return frame_rate, channels


def stereo_to_mono(audio_file_name):

    sound = AudioSegment.from_wav(audio_file_name)
    sound = sound.set_channels(1)
    sound.export(audio_file_name, format="wav")


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    print("50%: Uploading Blob to Bucket")
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)


def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    print("100%: Deleting blob from bucket")
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()


def google_transcribe(audio_file_name,count):
    print("10% :Getting File Name")
    file_name =audio_file_name




    frame_rate, channels = frame_rate_channel(file_name)

    if channels > 1:
        print("40%: Converting to Mono Channel")
        stereo_to_mono(file_name)

    bucket_name = 'summery_bucket'
    source_file_name =  audio_file_name
    destination_blob_name = audio_file_name

    upload_blob(bucket_name, source_file_name, destination_blob_name)

    gcs_uri = 'gs://summery_bucket/' + audio_file_name
    transcript = ''

    client = speech.SpeechClient()
    audio = types.RecognitionAudio(uri=gcs_uri)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=frame_rate,
        language_code='en-US',
        enable_speaker_diarization=True,
        enable_automatic_punctuation=True,
        use_enhanced=True,


        diarization_speaker_count=count)
    print("60%: Converting Audio to text")
    # Detects speech in the audio file
    operation = client.long_running_recognize(config, audio)
    response = operation.result(timeout=10000)
    print("response")

    result = response.results[-1]
    words_info = result.alternatives[0].words

    tag = 1
    speaker = ""

    for word_info in words_info:
        if word_info.speaker_tag == tag:
            speaker = speaker + " " + word_info.word
        else:
            transcript += "Speaker{}: {}".format(tag, speaker) + '\n'
            tag = word_info.speaker_tag
            speaker = "" + word_info.word

    transcript += "Speaker{}: {}".format(tag, speaker)
    print("70%: Conversion Complete")
    delete_blob(bucket_name, destination_blob_name)
    return transcript


def write_transcripts(transcript_filename, transcript):
    # The name of the text file to be saved (GIVE SPECIFIC PATH)
    f = open("Speech_Text1.txt", "w")
    f.write(transcript)
    f.close()


if __name__ == "__main__":
    # The name of the audio file to transcribe (GIVE SPECIFIC PATH)
            import warnings

            warnings.filterwarnings("ignore")
            #count = 3
            #audio_file_name='meet.wav'
            #transcript = google_transcribe(audio_file_name,count)

            #transcript_filename = audio_file_name.split('.')[0] + '.txt'
            #write_transcripts(transcript_filename, transcript)