#!/bin/bash
git add .
read -p "cmmit description: " desc
git commit -m "$desc"
git push origin main
