#!/bin/bash

# Star Wars CLI Tests Runner

echo "🚀 Running Star Wars CLI Tests..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run tests with pytest
echo "🧪 Executing tests..."
python -m pytest tests/ -v

echo "✅ Tests completed!"