#!/usr/bin/env bash


# --- Guard against direct execution ---
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "This script is not a standalone executable. It should be sourced."
    exit 1
fi


# --- Configuration ---
ROOT_DIR="corpuscompass"
VIEW_DIR="$ROOT_DIR/view"
RES_DIR="$VIEW_DIR/res"
GEN_DIR="$VIEW_DIR/generated"
MAIN_FILE="$ROOT_DIR/main.py"



# --- Functions ---

#######################################
# Compiles Qt resources (resources.qrc → resources_rc.py).
# Adjust the command or filenames if yours differ.
#######################################
function compile_resources() {
  echo "--> Compiling Qt resources..."
  poetry run pyside6-rcc "$RES_DIR/resources.qrc" -o resources_rc.py
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

# A common preparation step for both builds.
function prepare_build() {
    echo "--> Preparing build environment..."
    compile_resources
    # If you need to compile UI files, uncomment the next line
    compile_ui_files

    mkdir -p "release/mac" "release/win" "build/mac" "build/win"
    echo "    Preparation complete."
}

#######################################
# Builds on macOS using PyInstaller, producing a .app in release/mac/.
#######################################

function build_mac() {
  prepare_build
  echo "--> Building for macOS..."
  poetry run pyinstaller \
    --clean \
    --name "CorpusCompass" \
    --onedir \
    --windowed \
    --noconfirm \
    --icon="includes/icon.icns" \
    --distpath "release/mac" \
    --workpath "build/mac" \
    "$MAIN_FILE"

  echo "    macOS build finished in release/mac/"
}

function build_windows() {
  prepare_build
  echo "--> Building for Windows..."
  poetry run pyinstaller \
    --clean \
    --name "CorpusCompass" \
    --onedir \
    --windowed \
    --noconfirm \
    --icon="includes/icon.ico" \
    --distpath "release/win" \
    --workpath "build/win" \
    "$MAIN_FILE"


  echo "    Windows build finished in release/win/"
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
  #compile_ui_files

  # Detect OS, build accordingly
  if [[ "$OSTYPE" == "darwin"* ]]; then
    build_mac
    #ask_move_to_desktop
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

