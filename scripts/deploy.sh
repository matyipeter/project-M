#!/bin/bash

set -e

# Deploy project
bash scripts/upload-code.sh
bash scripts/install-code.sh