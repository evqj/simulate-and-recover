#!/bin/bash

# Get the absolute path to the project root directory
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo $PROJECT_ROOT

# Add project root to PYTHONPATH so tests can find the src package
export PYTHONPATH="$PROJECT_ROOT:$PYTHONPATH"

# Ensure dependencies are installed (Docker should handle this in the image)

# Run the EZ diffusion simulation
python3 $PROJECT_ROOT/src/main.py

# Print completion message
echo "Simulation complete. Results saved in ez_diffusion_simulation_results.txt"