#!/data/data/com.termux/files/usr/bin/bash

echo "Installing TermPassX - The Ultimate Termux Password Generator..."

# Update package repository
pkg update -y

# Install required packages
pkg install -y python termux-api

# Create directory for the tool
mkdir -p $HOME/.termpassx

# Copy the Python script and requirements
cp termpassx.py requirements.txt $HOME/.termpassx/

# Install Python packages from requirements file
pip install -r $HOME/.termpassx/requirements.txt

# Create launcher script
echo '#!/data/data/com.termux/files/usr/bin/bash
python $HOME/.termpassx/termpassx.py "$@"' > $PREFIX/bin/termpassx

# Make launcher executable
chmod +x $PREFIX/bin/termpassx

echo "Installation complete! Run 'termpassx' to start the tool."
echo "Note: Make sure to install Termux:API app from F-Droid for clipboard support."