import os
import sys
from pathlib import Path

# change working dir to the location of this script
os.chdir(sys.path[0])

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"  # disable import pygame message
import pygame  # noqa: E402


def resource(path: str):
    " get resource path (Windows only) "
    base_path = Path(getattr(sys, "_MEIPASS", "."))
    return base_path / path


print("Start silence music")

music_file = "silence.ogg"
# music_file = "sample.mp3" # for testing

pygame.mixer.init()
pygame.mixer.music.load(resource(music_file))
pygame.mixer.music.play(loops=-1)

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

try:
    while pygame.mixer.music.get_busy():
        clock.tick(10)  # tick every 10 ms
        time = pygame.time.get_ticks() - start_time

        time_seconds = int(time / 1000 % 60)
        time_minutes = int(time / 1000 / 60 % 60)
        time_hours = int(time / 1000 / 60 / 60 % 60)
        print(
            f"Playing since {time_hours:02}:{time_minutes:02}:{time_seconds:02}",
            end="\r",
        )

except KeyboardInterrupt:
    print(flush=True)
    print("Stop silence music")
