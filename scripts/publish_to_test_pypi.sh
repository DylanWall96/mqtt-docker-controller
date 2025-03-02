#!/bin/bash
set -e

# Navigate to the project root directory
# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Navigate to the parent directory (project root)
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
cd "$PROJECT_ROOT"

echo "===== Publishing to Test PyPI ====="
echo "Using project directory: $PROJECT_ROOT"
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

echo "Uploading to Test PyPI..."
python -m twine upload --repository testpypi dist/*

echo "===== Upload Complete ====="
echo "To test installation, run:"
echo "pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple mqtt-docker-controller"