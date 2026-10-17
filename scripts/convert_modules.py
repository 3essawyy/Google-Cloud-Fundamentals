import os
import subprocess
import sys

SCRIPT_PATH = r"C:\Users\yelessaw\.gemini\skills\convert-pptx-pdf2md-v1\scripts\convert_pdf.py"

MODULES = [
    ("M1 _ Introducing Google Cloud v5.2 _ ILT.pdf", r"modules\M1_Introducing_Google_Cloud\M1_Introducing_Google_Cloud.md"),
    ("M2 _ Resouces and Access in the Cloud v5.2 _ ILT.pdf", r"modules\M2_Resources_and_Access\M2_Resources_and_Access.md"),
    ("M3 _ Virtual Machines and Networks in the Cloud v5.2 _ ILT.pdf", r"modules\M3_Virtual_Machines_and_Networks\M3_Virtual_Machines_and_Networks.md"),
    ("M4 _ Storage in the Cloud v5.2 _ ILT.pdf", r"modules\M4_Storage_in_the_Cloud\M4_Storage_in_the_Cloud.md"),
    ("M5 _ Containers in the Cloud v5.2 _ ILT.pdf", r"modules\M5_Containers_in_the_Cloud\M5_Containers_in_the_Cloud.md"),
    ("M6 _ Applications in the Cloud v5.2 _ ILT.pdf", r"modules\M6_Applications_in_the_Cloud\M6_Applications_in_the_Cloud.md"),
    ("M7 _ Course Summary v5.2 _ ILT.pdf", r"modules\M7_Course_Summary\M7_Course_Summary.md"),
]

def main():
    for pdf_name, target_md in MODULES:
        print(f"\n==========================================")
        print(f"Converting: {pdf_name} -> {target_md}")
        print(f"==========================================")
        cmd = [sys.executable, SCRIPT_PATH, pdf_name, target_md, "--manifest"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        print(res.stdout)
        if res.returncode != 0:
            print(f"ERROR converting {pdf_name}:")
            print(res.stderr)
            sys.exit(res.returncode)

    print("\n[SUCCESS] All 7 modules converted successfully.")

if __name__ == "__main__":
    main()
