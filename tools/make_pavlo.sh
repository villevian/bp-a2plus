#!/bin/sh
# Build Pavlo's student site. Usage: sh make_pavlo.sh /path/to/bp-pavlo [STUDENT_CODE]
set -e; D=$1; C=${2:-}; T=$(dirname "$0"); A2=$T/../../bp-a2
sed -i "s/\"code\": \"[^\"]*\"/\"code\": \"$C\"/" $T/cfg_pavlo.py
python3 $T/build_contents.py $D/index.html cfg_pavlo
python3 $T/build_a2_7-2.py $D/lessons/7-2 $C
python3 $T/build_a2_hw_7-2.py $D/lessons/7-2/all/hw.html $C
python3 $T/build_a2_extra_7-2.py $D/lessons/7-2/all/extra.html $C
python3 $T/build_a2_games_7-2.py $D/lessons/7-2/all/games.html $C
cp $D/lessons/7-2/all/hw.html $D/lessons/7-2/all/extra.html $D/lessons/7-2/all/games.html $D/lessons/7-2/all-classic/
mkdir -p $D/lessons/7-2/audio && cp $A2/lessons/7-2/audio/7-02.mp3 $D/lessons/7-2/audio/
python3 $T/build_a2_7-3.py $D/lessons/7-3 $C
python3 $T/build_a2_hw_7-3.py $D/lessons/7-3/all/hw.html $C
python3 $T/build_a2_extra_7-3.py $D/lessons/7-3/all/extra.html $C
python3 $T/build_a2_games_7-3.py $D/lessons/7-3/all/games.html $C
cp $D/lessons/7-3/all/hw.html $D/lessons/7-3/all/extra.html $D/lessons/7-3/all/games.html $D/lessons/7-3/all-classic/
rm -f $D/lessons/7-3/index.html
python3 $T/build_vocab.py $D/vocab.html vocab_a2 A2 "$C" "#3b7dd8" "#e3eefb" "#2a5fb0"
printf "# Business Partner A2 — Pavlo\n\nStudent site (GitHub Pages). Built by bp-a2plus/tools/make_pavlo.sh\n" > $D/README.md
echo built $D
