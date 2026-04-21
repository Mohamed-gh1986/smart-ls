![App Screenshot](ls2.jpg)

# Smart LS for Windows 🚀

A lightweight Python tool designed to enhance file listing in the Windows Terminal. It provides a clean, colored, and organized table view, optimized specifically for systems with limited resources (like 4GB RAM).

## Features:

- **High Performance:** Uses `os.scandir` for maximum speed and minimal CPU/RAM usage.
- **Smart Truncation:** Automatically truncates file names longer than 50 characters (e.g., `very_long_name...`) to keep the table structure perfect.
- **Colorized Output:** Distinct colors for Directories (Blue) and Files (Green) using `Colorama`.
- **Dynamic Sorting:** Items are sorted by name length for better scannability.
- **Resource Friendly:** Perfect for older processors (like Intel Pentium G series).

---

## بالعربية: أداة Smart LS لويندوز 🚀

أداة بسيطة وخفيفة مكتوبة بلغة بايثون لتحسين عرض الملفات في سطر الأوامر (Terminal). توفر عرضاً منظماً وملوناً للملفات، وهي مصممة لتعمل بكفاءة عالية على الأجهزة ذات المواصفات المحدودة.

### المميزات:

- **سرعة فائقة:** تعتمد على `os.scandir` لتقليل استهلاك المعالج والذاكرة.
- **تقليص ذكي:** تقوم باختصار الأسماء التي تزيد عن 50 حرفاً تلقائياً لضمان ثبات شكل الجدول.
- **ألوان تفاعلية:** تمييز المجلدات باللون الأزرق والملفات باللون الأخضر.
- **ترتيب ديناميكي:** عرض الملفات مرتبة حسب طول الاسم لتسهيل القراءة.

---

## How to setup the Environment & Run / كيفية إعداد البيئة والتشغيل

### 1. Install Requirements / تثبيت المتطلبات

```bash
pip install -r requirements.txt
```
