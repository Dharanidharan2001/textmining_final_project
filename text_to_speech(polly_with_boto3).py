import boto3
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

polly = boto3.client('polly')

try:
    response = polly.synthesize_speech(Text="""One day, a fox became very hungry as he went to search for some food. He searched high and low, but couldn’t find something that he could eat.

Finally, as his stomach rumbled, he stumbled upon a farmer’s wall. At the top of the wall, he saw the biggest, juiciest grapes he’d ever seen. They had a rich, purple color, telling the fox they were ready to be eaten.

To reach the grapes, the fox had to jump high in the air. As he jumped, he opened his mouth to catch the grapes, but he missed. The fox tried again but missed yet again.

He tried a few more times but kept failing.Finally, the fox decided it was time to give up and go home. While he walked away""", OutputFormat="mp3", VoiceId="Joanna")
except (BotoCoreError, ClientError) as error:
    print(error)
    sys.exit(-1)

# Access the audio stream from the response
if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "speech.mp3")
            try:
            # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
            # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)
else:
    # The response didn't contain audio data, exit gracefully
    print("Could not stream audio")
    sys.exit(-1)
# Play the audio using the platform's default player
if sys.platform == "win32":
    os.startfile(output)
else:
    # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, output])
