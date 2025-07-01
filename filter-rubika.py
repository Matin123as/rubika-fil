import os
import time
import sys

def create_chunk(filename, size_gb):
    size_bytes = size_gb * 1024 * 1024 * 1024
    chunk_size = 256 * 1024 * 1024
    chunk = b'\0' * chunk_size

    written = 0
    try:
        with open(filename, 'wb') as f:
            while written < size_bytes:
                write_size = min(chunk_size, size_bytes - written)
                f.write(chunk[:write_size])
                written += write_size
    except Exception as e:
        print(f"\n[!] خطا هنگام نوشتن: {e}")
    return written

def flashy_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("▉▉▉▉▉▉▉▉▉▉▉▉ TERMINAL ▉▉▉▉▉▉▉▉▉▉▉▉")
    for _ in range(15):
        print("█▓▒░ در حال اتصال به سرور ناشناس ░▒▓█")
        time.sleep(0.05)
    print()

def loading_animation(msg="در حال کد زنی"):
    for _ in range(3):
        for dot in ['.', '..', '...']:
            print(f"\r{msg}{dot}", end='', flush=True)
            time.sleep(0.5)
    print()

def start_download_chunks(base_filename, total_gb):
    folder_count = total_gb // 5
    for i in range(folder_count):
        folder_name = f"chunk_{i+1:02}"
        os.makedirs(folder_name, exist_ok=True)
        filepath = os.path.join(folder_name, f"{base_filename}_part{i+1:02}.bin")
        print(f"\n⬇ در حال ساخت پارت {i+1} از {folder_count}...")
        size = create_chunk(filepath, 5)
        print(f"✅ {size // (1024*1024)} MB  گزارش زده شد لطفا منتظر بمانید.")

if __name__ == "__main__":
    flashy_terminal()
    try:
        user_id = input("لطفاً آیدی کاربر را وارد کنید: ").strip()
        if not user_id:
            print("❌ آیدی معتبر نیست.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n❌ عملیات لغو شد.")
        sys.exit(1)

    loading_animation("در حال کد زنی")
    start_download_chunks("bigdata_resilient", 80)
    print("\n✅ تمام پارت‌ها با موفقیت ساخته شدند.")