# Import the AudioSegment class for processing audio and the 
# split_on_silence function for separating out silent chunks.
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

def listdir(path):#获取目录下的文件列表
    dirlist = []
    file_list=os.listdir(path)
    # print(file_list)
    global file_count, folder_count
    #遍历文件列表，如果当前文件不是文件夹，则文件数量+1，如果是文件夹，则文件夹数量+1且再调用统计文件个数的方法
    for temp in file_list:
        #path_now = path + "\\" + temp
        path_now = os.path.join(path, temp)
        if os.path.isdir(path_now)==True:
            dirlist.append(path_now)
    return dirlist

# Define a function to normalize a chunk to a target amplitude.
def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)
targetdir = listdir('../../SFXClassified/')
#print(listdir('../test/'))
for src_dir in targetdir:
    for root , dirs, files in os.walk(src_dir):
        #file =os.path.splitext(files)
        for name in files:
            if name.endswith('.wav'):
                targetAudio = AudioSegment.from_wav(os.path.join(root,name))
                chunks = split_on_silence (
                    # Use the loaded audio.
                    targetAudio, 
                    # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
                    min_silence_len = 600,
                    # Consider a chunk silent if it's quieter than -16 dBFS.
                    # (You may want to adjust this parameter.)
                    silence_thresh = -60
                )
                if len(chunks)>2:
                    for i, chunk in enumerate(chunks):
                        print(name[:-4]+"_chunk{0}.wav".format(i))
                        chunk.export(
                            os.path.join(root,name[:-4]+"_chunk{0}.wav".format(i)),
                            bitrate = "2304k",
                            format = "wav"
                        )



'''
# Load your audio.
targetAudio = AudioSegment.from_wav("your_audio.mp3")

# Split track where the silence is 2 seconds or more and get chunks using 
# the imported function.
chunks = split_on_silence (
    # Use the loaded audio.
    targetAudio, 
    # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
    min_silence_len = 600,
    # Consider a chunk silent if it's quieter than -16 dBFS.
    # (You may want to adjust this parameter.)
    silence_thresh = -60
)

# Process each chunk with your parameters
for i, chunk in enumerate(chunks):
    # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
    #silence_chunk = AudioSegment.silent(duration=500)

    # Add the padding chunk to beginning and end of the entire chunk.
    #audio_chunk = silence_chunk + chunk + silence_chunk

    # Normalize the entire chunk.
    #normalized_chunk = match_target_amplitude(audio_chunk, -20.0)

    # Export the audio chunk with new bitrate.
    print("Exporting chunk{0}.wav.".format(i))
    chunk.export(
        ".//chunk{0}.wav".format(i),
        bitrate = "2304k",
        format = "wav"
    )
'''