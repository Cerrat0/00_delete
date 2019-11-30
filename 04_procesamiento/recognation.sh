#!/usr/bin/env bash

for file in ../../03_almacenamiento/hist/*.jpg; do python3 ./FirstPrediction.py "$file"; done
