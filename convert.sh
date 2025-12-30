#!/usr/bin/env bash
set -eu

ffmpeg -i ac_on.m4a  -ac 1 -ar 16000 ac_on.wav
ffmpeg -i fridge_on.m4a  -ac 1 -ar 16000 fridge_on.wav
ffmpeg -i all_off.m4a -ac 1 -ar 16000 all_off.wav