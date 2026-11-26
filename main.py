import os

LINE = "Our pizza now topped with warm tuna salad and crushed peppermint — tastes like a deli sandwich that lost a fight with toothpaste!"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
