"""Render a dialogue to MP3 with Piper voices (one voice per speaker).
Usage: python3 tts_dialog.py OUT.mp3  (dialogue + voice map defined in DIALOGS below, key = basename)
Voices: GitHub release rhasspy/piper v0.0.2 (voice-*.tar.gz) extracted to /tmp/voices.
"""
import sys, wave, os, subprocess, tempfile, io
from piper import PiperVoice
VD = "/tmp/voices/"
from tts_dialog_text import A702, A2P_101, A2_101, OA_8B, OA_8B2
DIALOGS = {"7-02": (A702, {"E": "en-us-lessac-medium", "T": "en-us-ryan-medium"}),
           "1-01": (A2P_101, {"A": "en-us-lessac-medium", "M": "en-us-ryan-medium"}),
           "a2-1-01": (A2_101, {"I": "en-us-lessac-medium", "D": "en-us-ryan-medium"}),
           "8b-street": (OA_8B, {"R": "en-us-lessac-medium", "T": "en-us-ryan-medium", "A": "en-us-amy-low", "G": "en-gb-alan-low"}),
           "8b-radio": (OA_8B2, {"R": "en-us-lessac-medium", "T": "en-us-ryan-medium", "A": "en-us-amy-low", "G": "en-gb-alan-low"})}
out = sys.argv[1]; lines, vm = DIALOGS[os.path.basename(out).rsplit(".", 1)[0]]
voices = {s: PiperVoice.load(VD + m + ".onnx") for s, m in vm.items()}
tmp = tempfile.mkdtemp(); parts = []
for i, (s, t) in enumerate(lines):
    p = os.path.join(tmp, "%03d.wav" % i)
    with wave.open(p, "wb") as w:
        voices[s].synthesize_wav(t, w)
    parts.append(p)
lst = os.path.join(tmp, "l.txt")
open(lst, "w").write("".join("file '%s'\n" % p for p in parts))
# normalise each to 22050 mono, add 0.45 s pause after each line
fl = "".join("[%d:a]aresample=22050,aformat=channel_layouts=mono,apad=pad_dur=0.45[a%d];" % (i, i) for i in range(len(parts)))
fl += "".join("[a%d]" % i for i in range(len(parts))) + "concat=n=%d:v=0:a=1,loudnorm[o]" % len(parts)
cmd = ["ffmpeg", "-y", "-loglevel", "error"] + sum([["-i", p] for p in parts], []) + ["-filter_complex", fl, "-map", "[o]", "-ac", "1", "-b:a", "64k", out]
subprocess.run(cmd, check=True); print("ok", out, os.path.getsize(out))
