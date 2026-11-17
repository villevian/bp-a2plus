"""Render single lines to MP3. Usage: python3 tts_lines.py OUTDIR VOICE PREFIX "line 1" "line 2" ..."""
import sys, wave, os, subprocess, tempfile
from piper import PiperVoice
out, voice, pre, lines = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
v = PiperVoice.load("/tmp/voices/%s.onnx" % voice); os.makedirs(out, exist_ok=True)
for i, t in enumerate(lines, 1):
    w = tempfile.mktemp(suffix=".wav")
    with wave.open(w, "wb") as f: v.synthesize_wav(t, f)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", w, "-af", "loudnorm", "-ac", "1", "-b:a", "48k", os.path.join(out, "%s%d.mp3" % (pre, i))], check=True)
print("ok", len(lines))
