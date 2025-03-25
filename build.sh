#!/usr/bin/env bash
#
# build.sh
# A modular Bash script that builds CorpusCompass as a standalone application
# on either macOS or Windows (Git Bash / MSYS). It:
#   1) Installs dependencies with Poetry
#   2) Compiles Qt resources (and optionally UI files)
#   3) Uses PyInstaller to produce a single .app (macOS) or .exe (Windows)
#   4) Asks user if they'd like to place the final build on the Desktop
#
# Usage:
#   chmod +x build.sh
#   ./build.sh
#

VIEW_DIR="src/view"
RES_DIR="$VIEW_DIR/res"
GEN_DIR="$VIEW_DIR/generated"


set -e  # Exit immediately on error

#######################################
# Compiles Qt resources (resources.qrc → resources_rc.py).
# Adjust the command or filenames if yours differ.
#######################################
function compile_resources() {
  echo "Compiling Qt resources..."
  poetry run pyside6-rcc src/view/res/resources.qrc -o resources_rc.py
  echo "Done compiling Qt resources."
}

#######################################
# Compiles .ui files to Python.
# Uncomment or adapt if you need to do this automatically.
#######################################
function compile_ui_files() {
  echo "Compiling UI files..."
  for ui_file in $RES_DIR/*.ui; do
    base="$(basename "$ui_file" .ui)"
    poetry run pyside6-uic "$ui_file" -o "$GEN_DIR/ui_${base}.py"
    echo "  Compiled $ui_file → ui_${base}.py"
  done
  echo "Done compiling UI files."
}

#######################################
# Builds on macOS using PyInstaller, producing a .app in release/mac/.
#######################################
function build_mac() {
  echo "Building for macOS..."
  poetry run pyinstaller \
    --name "CorpusCompass" \
    --windowed \
    --icon="includes/icon.icns" \
    --distpath "release/mac" \
    --workpath "build/mac" \
    main.py

  echo "macOS build finished."
  echo "You can find the app folder at: release/mac/CorpusCompass.app"
}

#######################################
# Builds on Windows using PyInstaller, producing a one-file .exe in release/win/.
#######################################
function build_windows() {
  echo "Building for Windows (one-file exe)..."
  poetry run pyinstaller \
    --onefile \
    --windowed \
    --name "CorpusCompass" \
    --icon="includes/icon.ico" \
    --distpath "release/win" \
    --workpath "build/win" \
    main.py

  echo "Windows build finished."
  echo "You can find the .exe at: release/win/CorpusCompass.exe"
}

#######################################
# Asks user whether to copy the final build to the Desktop.
# This will try to copy to ~/Desktop/ for Windows or macOS.
#######################################
function ask_move_to_desktop() {
  echo -n "Would you like to copy the build to your Desktop? [y/N]: "
  read answer
  if [[ "$answer" =~ ^[Yy]$ ]]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
      # macOS
      echo "Copying CorpusCompass.app to Desktop..."
      cp -R "release/mac/CorpusCompass.app" "$HOME/Desktop/CorpusCompass.app"
      echo "Copied to your Desktop."
    elif [[ "$OSTYPE" == "msys"* ]] || [[ "$OSTYPE" == "cygwin"* ]] || [[ "$OSTYPE" == "win32"* ]]; then
      # Windows (Git Bash/Cygwin typically sets HOME)
      echo "Copying CorpusCompass.exe to Desktop..."
      cp "release/win/CorpusCompass.exe" "$HOME/Desktop/CorpusCompass.exe"
      echo "Copied to your Desktop."
    else
      echo "Unrecognized OS; skipping Desktop copy."
    fi
  else
    echo "Skipping copy to Desktop."
  fi
}

#######################################
# Main build logic: determines OS, calls the relevant build function,
# and optionally copies final output to Desktop.
#######################################
function main() {
  echo "Installing dependencies via Poetry..."
  poetry install --no-root

  compile_resources
  # If you want to compile UI files automatically, uncomment:
  # compile_ui_files

  # Detect OS, build accordingly
  if [[ "$OSTYPE" == "darwin"* ]]; then
    build_mac
    ask_move_to_desktop
  elif [[ "$OSTYPE" == "msys"* ]] || [[ "$OSTYPE" == "cygwin"* ]] || [[ "$OSTYPE" == "win32"* ]]; then
    build_windows
    ask_move_to_desktop
  else
    echo "Unsupported OS ($OSTYPE)."
    echo "Please run on macOS or Windows for best results."
    exit 1
  fi

  echo "All done! Build artifacts are in the 'release' folder."
}

#######################################
# Invoke main
#######################################
main
