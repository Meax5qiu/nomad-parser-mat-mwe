#!/bin/sh

rsync -avh nomad-mwe12345/ .
rm -rfv nomad-mwe12345
