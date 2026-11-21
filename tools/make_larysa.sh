#!/bin/sh
# Build Larysa's student site (A2+). Usage: sh make_larysa.sh /path/to/bp-larysa
set -e; D=$1; T=$(dirname "$0"); C=eea83833e26343c1
python3 $T/build_contents.py $D/index.html cfg_larysa
python3 $T/build_a2p_1-2.py $D/lessons/1-2 $C
python3 $T/build_a2p_flip_1-2.py $D/lessons/1-2/all/flip.html $C
python3 $T/build_a2p_hw_1-2.py $D/lessons/1-2/all/hw.html $C
python3 $T/build_a2p_extra_1-2.py $D/lessons/1-2/all/extra.html $C
python3 $T/build_a2p_speak_1-2.py $D/lessons/1-2/all/speak.html $C
mkdir -p $D/lessons/1-2/audio && cp $T/../lessons/1-2/audio/*.mp3 $D/lessons/1-2/audio/
python3 $T/build_vocab.py $D/vocab.html vocab_a2p A2+ "$C" "#3fa9ad" "#e6f4f4" "#2b8185"
python3 $T/build_glossary.py $D/glossary.html glossary_a2p A2+ "#3fa9ad" "#e6f4f4" "#2b8185"
echo built $D
