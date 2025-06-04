#!/bin/bash

# This script installs required Python libraries for OWL conversion using Python 3.12

# Abort on errors
set -e

# Check that Python 3.12 is installed
if ! command -v python3.12 &> /dev/null
then
    echo "❌ Python 3.12 is not installed. Install it first (e.g., via Homebrew: brew install python@3.12)"
    exit 1
fi

echo "🐍 Creating virtual environment with Python 3.12..."
python3.12 -m venv venv
source venv/bin/activate

echo "⬆️ Upgrading pip..."
python -m pip install --upgrade pip

echo "📦 Installing core libraries..."
pip install rdflib pyshacl

echo "🧠 Installing reasoning and validation extensions..."
pip install owlrl

echo "🌐 Installing PyLODE for HTML rendering..."
pip install pylode

echo "✅ All libraries installed successfully!"
echo "👉 To activate the virtual environment later, run:"
echo "source venv/bin/activate"

