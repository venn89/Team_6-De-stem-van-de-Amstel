"""
Use Azure's Voice for Text to Speech (TTS)
"""
import azure.cognitiveservices.speech as speechsdk

# Replace with your Azure values
speech_key = "AZURE_SPEECH_KEY"
speech_endpoint = "https://westeurope.api.cognitive.microsoft.com/"  # e.g., "westeurope"

# Configure speech service
speech_config = speechsdk.SpeechConfig(subscription=speech_key, endpoint=speech_endpoint)

# Use Dutch voice (see https://json2video.com/ai-voices/azure/languages/dutch/ for more Dutch voices)
voice_name = "nl-NL-MaartenNeural"
speech_config.speech_synthesis_voice_name = voice_name

# Set output format to MP3
speech_config.set_speech_synthesis_output_format(
    speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3
)

# Output file path
file_name = f"output_{voice_name}.mp3"

# Set up file audio output
audio_config = speechsdk.audio.AudioOutputConfig(filename=file_name)

# Create synthesizer
speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config
)

# Receives a text from console input.
text = "Kort gezegd is AI een verzamelnaam voor algoritmes en methoden die taken uitvoeren waarvan werd gedacht dat daar menselijke intelligentie voor nodig is. Artificiële intelligentie verwijst naar systemen die intelligent gedrag vertonen door hun omgeving te analyseren en - met een zekere mate van zelfstandigheid - actie ondernemen om specifieke doelen te bereiken."

# Synthesizes the received text to speech.
# The synthesized speech is expected to be heard on the speaker with this line executed.
result = speech_synthesizer.speak_text_async(text).get()

# Checks result.
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to speaker for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")