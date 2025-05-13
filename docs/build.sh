#!/bin/bash

DOWNLOAD_DIR="downloads"

for group in urban-data-storytelling urban-data-analytics urban-data-visualization urban-data-management; do
    [ -d "$group" ] || continue
    for subdir in "$group"/*/; do
        [ -d "$subdir" ] || continue
        SUBFOLDER_NAME=$(basename "$subdir")
        ZIP_PATH="$DOWNLOAD_DIR/${SUBFOLDER_NAME}.zip"
        (cd "$subdir" && zip -r "../../$ZIP_PATH" .)
    done
done

rm -r docs/

quarto render

touch docs/.nojekyll