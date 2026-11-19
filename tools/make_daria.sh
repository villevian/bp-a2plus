#!/bin/sh
# Build Daria's B2 site from Violeta's (same B2 lessons), with Daria's code. Usage: sh make_daria.sh /path/to/bp-daria CODE
set -e; D=$1; C=$2; T=$(dirname "$0"); V=/home/claude/bp-violeta
sed -i "s/__DARIA_CODE__/$C/" $T/cfg_daria.py
mkdir -p $D/lessons/6-1/all
for f in lessons/6-1/all/lesson.html lessons/6-1/all/hw.html vocab.html; do sed "s/bb2f141b2b75a229c72b4e0bbe753714/$C/g" $V/$f > $D/$f; done
python3 $T/build_contents.py $D/index.html cfg_daria
printf '# Business Partner B2 — Daria\n\nPersonal course page. Lessons are copied from villevian/bp-b2.\nHomework answers sync to Supabase (project "Business Partner").\n' > $D/README.md
echo built $D
