import os
import whisper


# model = whisper.load_model("base")
model = whisper.load_model("medium.en")
# podcast = os.listdir('podcast/SGU/2023')[-1]
podcast='2023.04.27 ETH stake flippening, Polygon governance and more - The Daily Gwei Refuel #575 - Ethereum Updates.mp3'

result = model.transcribe(podcast, fp16=False, language='English')
print(result["text"])

import ipdb; ipdb.set_trace()
