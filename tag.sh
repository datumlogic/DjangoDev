#!/bin/bash  
git tag
read -p "Tag ID (see above for previous tags): " tag
read -p "Tag description: " desc
git tag -a $tag -m "$desc"
