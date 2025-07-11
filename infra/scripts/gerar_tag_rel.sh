#!/bin/bash
set -e

LAST_RC_TAG=$(git tag --list 'rc[0-9]*' | sort -V | tail -n 1)

if [ -z "$LAST_RC_TAG" ]; then
    echo "Nenhuma tag rc encontrada."
    exit 1
fi

VERSION=$(echo "$LAST_RC_TAG" | sed 's/^rc//')

NEW_TAG="rel${VERSION}"
echo "$NEW_TAG"
