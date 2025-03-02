#!/usr/bin/env bash
#
# compile_ui.sh
# Quick script to recompile all .ui files and the .qrc resource file

VIEW_DIR="src/view"
RES_DIR="$VIEW_DIR/res"
GEN_DIR="$VIEW_DIR/generated"

# 1. Compile resource file into resources_rc.py
pyside6-rcc "$RES_DIR/resources.qrc" -o resources_rc.py

# 2. Re-compile each .ui file in view/res/
#    This loops through all .ui files found in the folder.
for ui_file in "$RES_DIR*.ui"
do
  # get the basename without extension, e.g. "main_window"
  filename="$(basename "$ui_file" .ui)"
  
  # generate a python file in view/generated named ui_<filename>.py
  pyside6-uic "$ui_file" -o "$GEN_DIR/ui_${filename}.py"
  
  echo "Compiled $ui_file → $GEN_DIR/ui_${filename}.py"
done

echo "All done!"
