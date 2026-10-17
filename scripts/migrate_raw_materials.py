import os
import shutil

RAW_FILES = [
    "M0 _ Course Introduction v5.2 _ ILT.pdf",
    "M1 _ Introducing Google Cloud v5.2 _ ILT.pdf",
    "M2 _ Resouces and Access in the Cloud v5.2 _ ILT.pdf",
    "M3 _ Virtual Machines and Networks in the Cloud v5.2 _ ILT.pdf",
    "M4 _ Storage in the Cloud v5.2 _ ILT.pdf",
    "M5 _ Containers in the Cloud v5.2 _ ILT.pdf",
    "M6 _ Applications in the Cloud v5.2 _ ILT.pdf",
    "M7 _ Course Summary v5.2 _ ILT.pdf",
    "Lab1.html",
    "Lab2.html",
    "Lab3.html",
    "Lab4.html"
]

DEST_DIR = "raw_materials"

def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    moved_count = 0
    for filename in RAW_FILES:
        if os.path.exists(filename):
            dest_path = os.path.join(DEST_DIR, filename)
            shutil.move(filename, dest_path)
            print(f"Moved: {filename} -> {dest_path}")
            moved_count += 1
        else:
            print(f"Already moved or not found: {filename}")
    
    print(f"\n[SUCCESS] Migrated {moved_count} raw asset files to '{DEST_DIR}/'.")

if __name__ == "__main__":
    main()
