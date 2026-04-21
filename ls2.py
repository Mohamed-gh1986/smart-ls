# Project: Smart LS for Windows
# Author: Mohamed Gharbi (github.com/Mohamed-gh1986)
# Version: 1.1
# License: MIT

import sys
import os

# محاولة استيراد الألوان
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        GREEN = BLUE = YELLOW = WHITE = CYAN = RED = ""

    class Style:
        BRIGHT = RESET_ALL = ""


def by_argv(directory):
    try:
        abs_path = os.path.abspath(directory)

        if not os.path.exists(abs_path):
            print(f"{Fore.RED}Error: directory '{abs_path}' not found!")
            return

        # استخدام scandir للسرعة القصوى على الأجهزة الاقتصادية
        with os.scandir(abs_path) as entries:
            all_items = list(entries)

        if not all_items:
            print(f"{Fore.YELLOW}Current Path: {abs_path}")
            print("The directory is empty.")
            return

        # ترتيب حسب طول الاسم
        all_items.sort(key=lambda e: len(e.name))

        # --- الحسابات الديناميكية مع ميزة الاختصار الجديدة ---

        # تحديد سقف لعرض الاسم (50 حرفاً كما طلبت)
        MAX_LIMIT = 50

        processed_data = []
        for entry in all_items:
            raw_name = entry.name
            # منطق الاختصار: إذا طال الاسم عن 50، نأخذ 47 + "..."
            display_name = (
                raw_name[:35] + "...") if len(raw_name) >= MAX_LIMIT else raw_name

            try:
                if entry.is_dir():
                    item_type = "DIR"
                    size_kb = "0.00"
                    size_bytes = 0
                else:
                    item_type = "FILE"
                    size_bytes = entry.stat().st_size
                    size_kb = f"{round(size_bytes / 1024, 2):,.2f}"
            except OSError:
                item_type = "ERROR"
                size_kb = "0.00"
                size_bytes = 0

            processed_data.append({
                'display_name': display_name,
                'type': item_type,
                'size_kb': size_kb,
                'size_bytes': size_bytes,
                'is_dir': entry.is_dir()
            })

        # حساب عرض الأعمدة بناءً على البيانات المعالجة
        max_name_width = max(len(d['display_name']) for d in processed_data)
        max_name_width = max(max_name_width, len("Name")) + 2

        max_size_width = max(len(d['size_kb']) for d in processed_data)
        max_size_width = max(max_size_width, len("Size (KB)"))

        type_width = 6
        total_width = max_name_width + type_width + max_size_width + 9

        # --- الطباعة ---
        print(f"\n{Fore.CYAN}{Style.BRIGHT}Active Path: {Fore.WHITE}{abs_path}")
        print(f"{Fore.CYAN}{'=' * total_width}")

        header = f"{'Name':<{max_name_width}} | {'Type':<{type_width}} | {'Size (KB)':>{max_size_width}}"
        print(f"{Fore.YELLOW}{Style.BRIGHT}{header}")
        print(f"{Fore.CYAN}{'-' * total_width}")

        total_files_size = 0
        for item in processed_data:
            if item['is_dir']:
                color = Fore.BLUE + Style.BRIGHT
            else:
                color = Fore.GREEN
                total_files_size += item['size_bytes']

            print(
                f"{color}{item['display_name']:<{max_name_width}}{Fore.WHITE} | {item['type']:<{type_width}} | {Fore.YELLOW}{item['size_kb']:>{max_size_width}} KB")

        print(f"{Fore.CYAN}{'-' * total_width}")
        total_kb = round(total_files_size / 1024, 2)
        print(f"{Fore.CYAN}Summary: {Fore.WHITE}{len(processed_data)} Items | {Fore.YELLOW}{total_kb:,.2f} KB Total Files")
        print(f"{Fore.CYAN}{'=' * total_width}\n")

    except Exception as e:
        print(f'{Fore.RED}An error occurred: {e}')


if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    by_argv(target_dir)
