import subprocess

def text_to_speech(text, output_file="output.wav"):
    """Converts text to speech using pico2wave and saves it to a file."""

    command = ["pico2wave", "-w", output_file, text]
    subprocess.run(command, check=True)

if __name__ == "__main__":
    text = "Hello, world! This is a test of pico2wave."
    text_to_speech(text)
