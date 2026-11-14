#!/bin/bash

# Скрипт для підрахунку файлів у директорії

# Директорія та розширення файлів
TARGET_DIR="${1:-/etc}"
EXTENSION="${2:-conf}"

# Перевірка існування директорії
if [ ! -d "$TARGET_DIR" ]; then
    echo "Помилка: директорія $TARGET_DIR не існує"
    exit 1
fi

# Підрахунок звичайних файлів у директорії
file_count=$(find "$TARGET_DIR" -maxdepth 1 -type f | wc -l)

# Підрахунок файлів із заданим розширенням
ext_count=$(find "$TARGET_DIR" -maxdepth 1 -type f -name "*.$EXTENSION" | wc -l)

# Рекурсивний підрахунок файлів
recursive_count=$(find "$TARGET_DIR" -type f | wc -l)

# Загальний розмір файлів із заданим розширенням
total_size=$(find "$TARGET_DIR" -type f -name "*.$EXTENSION" -printf '%s\n' | awk '{sum += $1} END {print sum+0}')

# Виведення результатів
echo "======================================"
echo "Підрахунок файлів у директорії $TARGET_DIR"
echo "======================================"
echo ""
echo "Кількість звичайних файлів: $file_count"
echo "Кількість файлів .$EXTENSION: $ext_count"
echo "Кількість файлів рекурсивно: $recursive_count"
echo "Загальний розмір файлів .$EXTENSION: $total_size байт"
echo ""
echo "(Директорії та символічні посилання не враховані)"

exit 0
