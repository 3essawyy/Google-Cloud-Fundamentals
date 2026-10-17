import os
import subprocess
import sys

def get_token():
    if not os.path.exists('.env'):
        print("ERROR: .env file not found.")
        sys.exit(1)
    
    with open('.env', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, val = line.split('=', 1)
                if key.strip().lower() in ['gh_token', 'github_token', 'token']:
                    return val.strip().strip('"').strip("'")
            elif line.startswith('ghp_') or line.startswith('github_pat_'):
                return line.strip()
    
    print("ERROR: Could not find GitHub token in .env.")
    sys.exit(1)

def main():
    token = get_token()
    if not token:
        print("ERROR: Token is empty.")
        sys.exit(1)
    
    remote_url = f"https://3essawyy:{token}@github.com/3essawyy/Google-Cloud-Fundamentals.git"
    
    # 1. Update remote URL
    cmd_set_url = ["git", "remote", "set-url", "origin", remote_url]
    res_url = subprocess.run(cmd_set_url, capture_output=True, text=True)
    if res_url.returncode != 0:
        print("ERROR setting remote URL:", res_url.stderr.replace(token, "[MASKED_TOKEN]"))
        sys.exit(res_url.returncode)
    
    print("[OK] Remote origin URL configured with credentials.")
    
    # 2. Push to main
    print("Executing: git push -u origin main...")
    cmd_push = ["git", "push", "-u", "origin", "main"]
    res_push = subprocess.run(cmd_push, capture_output=True, text=True)
    
    safe_stdout = res_push.stdout.replace(token, "[MASKED_TOKEN]")
    safe_stderr = res_push.stderr.replace(token, "[MASKED_TOKEN]")
    
    if safe_stdout:
        print(safe_stdout)
    if safe_stderr:
        print(safe_stderr)
        
    if res_push.returncode == 0:
        print("\n[SUCCESS] Successfully pushed all files to https://github.com/3essawyy/Google-Cloud-Fundamentals on branch 'main'.")
    else:
        print(f"\n[FAILURE] Push failed with exit code {res_push.returncode}.")
        sys.exit(res_push.returncode)

if __name__ == "__main__":
    main()
