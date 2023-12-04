from models.content_model import Content
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write, audio_read

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

async def create_melody_service(content: Content):
    try:
        print("-------Start Model Loaded-------")
        model = MusicGen.get_pretrained('facebook/musicgen-melody')
        print("-------Done Model Loaded-------")

        model.set_generation_params(duration=5)  # generate 15 seconds.

        base_audio, sr = audio_read("./assets/bach.mp3")
        duration = 3
        base_audio = base_audio[:, :sr*duration]
        # print(base_audio.shape)

        print("-------Start Stylizing Music-------")
        melody_version = model.generate_with_chroma(descriptions=["happy atmosphere"], melody_wavs=base_audio, melody_sample_rate=sr)
        print("-------Done Stylizing Music-------")
        audio_write("output-audio/bach_output2", melody_version[0].cpu(), sample_rate=model.sample_rate)
        print("-------Finish-------")
        
        return {
            "data": "OK"
        }
    except Exception as e:
        print("Error:",e)
