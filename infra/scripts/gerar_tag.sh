#!/bin/bash
set -e

LAST_TAG=$(git tag --list 'rc[0-9]*' | sort -V | tail -n 1)

if [ -z "$LAST_TAG" ]; then
    LAST_TAG="rc0.0.0"
fi

COMMITS=$(git log ${LAST_TAG}..HEAD --pretty=format:"%s%n%b")

if echo "$COMMITS" | grep -q "BREAKING CHANGE:"; then
    BUMP="major"
elif echo "$COMMITS" | grep -q "feat:"; then
    BUMP="minor"
else
    BUMP="patch"
fi

VERSION=$(echo $LAST_TAG | sed 's/^rc//')
IFS='.' read -r MAJOR MINOR PATCH <<<"$VERSION"

if [ "$BUMP" = "major" ]; then
    MAJOR=$((MAJOR + 1))
    MINOR=0
    PATCH=0
elif [ "$BUMP" = "minor" ]; then
    MINOR=$((MINOR + 1))
    PATCH=0
else
    PATCH=$((PATCH + 1))
fi

NEW_TAG="rc${MAJOR}.${MINOR}.${PATCH}"
echo "$NEW_TAG"