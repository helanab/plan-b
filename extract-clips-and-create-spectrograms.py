import os
import subprocess
import sys

#def extract_clips_and_create_spectrograms(): later
source_filepath = ".\wav"
target_filepath = ".\spect"

STEP_SIZE = 1.5

for filename in os.listdir(source_filepath):
    id, ext = filename.split(".")
    print(os.path.join(source_filepath, filename))
    if ext == "wav":
        sox_call = subprocess.run(['sox', '-D',
                                   os.path.join(source_filepath, filename)],
                                   stdout=subprocess.PIPE)
        duration = int(float(soxi_call.stdout))

        for start in [x * 0.5 for x in range(2 * duration - 2)]:

            end = start + STEP_SIZE
            timestamp = "%.3f_%.3f" % (start, end)
            timestamp = timestamp.replace(".", "")

            subprocess.run(['sox',
                             os.path.join(source_filepath, filename),
                             os.path.join("/tmp", f"{id}_{timestamp}.{ext}"),
                             "trim",
                             str(start),
                             str(STEP_SIZE)])

            subprocess.run(['sox',
                             os.path.join("/tmp", f"{id}_{timestamp}.{ext}"),
                             "-n",
                             "spectrogram",
                             "-r",
                             "-l",
                             "-a",
                             "-X",
                             str(172),
                             "-Y",
                             str(257),
                             "-o",
                             os.path.join("/tmp", f"{id}_{timestamp}.png")])

            subprocess.run(['convert',
                             os.path.join("/tmp", f"{id}_{timestamp}.png"),
                             "-gravity",
                             "center",
                             "-extent",
                             "256x256",
                             "-resize",
                             "256x256^",
                             os.path.join(target_filepath, f"{id}_{timestamp}.png")])

            subprocess.run(['rm',
                            "-v",
                             os.path.join("/tmp", f"{id}_{timestamp}.png")])
            subprocess.run(['rm',
                            "-v",
                             os.path.join("/tmp", f"{id}_{timestamp}.{ext}")])
