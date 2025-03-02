#!/bin/bash
set -e

# Navigate to the project root directory
# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Navigate to the parent directory (project root)
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
cd "$PROJECT_ROOT"

echo "===== Publishing to Production PyPI ====="
echo "Using project directory: $PROJECT_ROOT"
echo "IMPORTANT: Make sure you've tested on Test PyPI first!"
read -p "Are you sure you want to publish to Production PyPI? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Aborted."
    exit 1
fi

echo "Cleaning up old build artifacts..."
rm -rf build/ dist/ *.egg-info/

echo "Checking dependencies..."
pip install --upgrade build twine

# Run version check script if it exists
if [ -f "$SCRIPT_DIR/check_version.py" ]; then
    echo "Checking and updating version..."
    python "$SCRIPT_DIR/check_version.py"
    if [ $? -ne 0 ]; then
        echo "Version check failed. Aborting."
        exit 1
    fi
fi

echo "Building package..."
python -m build

echo "Uploading to Production PyPI..."
python -m twine upload dist/*

echo "===== Upload Complete ====="
echo "To install from PyPI, run:"
echo "pip install mqtt-docker-controller"