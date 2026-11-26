#!/bin/sh
# Build the B1 template (bp-b1) and every B1 student site in one go, so new lessons are copied everywhere automatically.
# Usage: sh make_b1.sh PARENT_DIR   (PARENT_DIR contains bp-b1, bp-kate, bp-taras …)
# A student sees a lesson as open only if it is in ASSIGNED of cfg_<name>.py; files are copied to every site anyway.
set -e; R=$(cd "$1" && pwd); cd "$(dirname "$0")"
STUDENTS="kate taras"
build() { D=$1; C=$2
  python3 build_b1_1-1.py $D/lessons/1-1/all $C >/dev/null
  python3 build_b1_1-1_extra.py $D/lessons/1-1/all $C >/dev/null
  python3 build_b1_1-1_words.py $D/lessons/1-1/all $C >/dev/null
  python3 build_b1_1-1_speak.py $D/lessons/1-1/all $C >/dev/null
  [ -z "$C" ] && python3 build_b1_1-1_clean.py $D/lessons/1-1/all >/dev/null  # DRAFT: template only until Vale approves
  python3 build_b1_4-2.py $D/lessons/4-2/all $C >/dev/null
  python3 build_b1_4-3.py $D/lessons/4-3/all $C >/dev/null
  python3 build_b1_4-4.py $D/lessons/4-4/all $C >/dev/null
  python3 build_b1_4-5.py $D/lessons/4-5 $C >/dev/null
  BP_DRAFT=$([ -z "$C" ] && echo 1) python3 build_vocab.py $D/vocab.html vocab_b1 B1 "$C" >/dev/null
  python3 build_glossary.py $D/glossary.html glossary_b1 ${L:-B1} "#e07a3f" "#fdf0e7" "#b85a24" >/dev/null
}
build $R/bp-b1 ""
python3 build_contents.py $R/bp-b1/index.html cfg_b1 >/dev/null
python3 build_b1_teacher.py $R/bp-b1/teacher >/dev/null
echo "template bp-b1 ✓"
for S in $STUDENTS; do
  [ -d $R/bp-$S ] || { echo "skip bp-$S (no folder)"; continue; }
  C=$(python3 -c "import cfg_$S as c; print(c.STUDENT['code'])")
  L=student build $R/bp-$S $C
  python3 build_contents.py $R/bp-$S/index.html cfg_$S >/dev/null
  python3 build_student_home.py $R/bp-$S/index.html cfg_$S >/dev/null
  echo "bp-$S ✓"
done
