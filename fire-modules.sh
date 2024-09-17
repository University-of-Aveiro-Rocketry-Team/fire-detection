#!/bin/bash

SOURCE=https://github.com/AlimTleuliyev/wildfire-detection/raw/refs/heads/main/fire-models
MODEL=${1:-fire_n}
MODEL_PATH=$SOURCE/$MODEL.pt
DESTINATION=fire-models

mkdir -p $DESTINATION

echo "Downloading $MODEL model from..."
echo "$MODEL_PATH"

wget -O $DESTINATION/$MODEL.pt $MODEL_PATH

echo "Model downloaded to $DESTINATION/$MODEL.pt"