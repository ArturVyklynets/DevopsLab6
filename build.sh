#!/usr/bin/env bash
set -euo pipefail

echo "Виконуємо імітацію збірки Flask‑проекту..."

mkdir -p build_output

cp -r *.py build_output/ 2>/dev/null || echo "Немає .py файлів у корені"
cp requirements.txt build_output/ 2>/dev/null || echo "Немає requirements.txt"

echo "Build completed at $(date)" > build_output/build_info.txt

echo "Збірка завершена. Артефакти в build_output/"
