"""Sort a Figma export (ZIP or folder of PNGs) into Files/Assets/Figma/<role folder>/.

Usage: python -I sort_exports.py [zip-or-folder]
Without an argument it takes the newest "OptiTime*.zip" in Downloads.

Frames are matched by their leading number ("20 · لوحة التحكم — ...").
For popups (12, 13, 14, 19, 31, 52, 53) the "Export · NN · ..." composite
(popup drawn over its screen) wins over the bare popup frame. When a name
appears more than once (Figma adds "-1" for the canvas label), the largest
file is kept, since the label exports as a tiny image.
"""
import re
import struct
import sys
import zipfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
BASE = Path(r"C:\Users\abdal\Desktop\OptiTime_new\Files\Assets\Figma")
DOWNLOADS = Path(r"C:\Users\abdal\Downloads")

FOLDERS = {
    "shared": "02 مشتركة - Shared",
    "mobile": "03 الجوال - Mobile",
    "mgmt": "04 الإدارة العليا - Senior Management",
    "coord": "05 منسق الجدولة - Schedule Coordinator",
    "admin": "06 مدير النظام - System Administrator",
    "teacher": "07 عضو هيئة التدريس - Teacher",
    "student": "08 الطالب - Student",
    "guide": "09 دليل النموذج التفاعلي - Prototype Guide",
    "cover": "00 الغلاف والأساسيات - Cover & Foundations",
    "comp": "01 المكوّنات - Components",
}
BY_NUMBER = {}
for nums, key in [((1, 13), "shared"), ((9, 10, 14), "mobile"), ((2, 8, 15, 16, 17, 18, 19), "mgmt"),
                  ((3, 11), "coord"), ((5, 6, 7, 12), "admin"), ((4, *range(20, 33)), "teacher"),
                  (tuple(range(40, 55)), "student")]:
    for n in nums:
        BY_NUMBER[n] = key
POPUPS = {12, 13, 14, 19, 31, 52, 53}
NAMED = {  # frames on the cover and components pages, and the guide
    "Cover": ("cover", "00 - الغلاف - Cover.png"),
    "Foundations": ("cover", "01 - الأساسيات - Foundations.png"),
    "LinkedIn Post": ("cover", "02 - منشور لينكدإن - LinkedIn Post.png"),
    "Icons": ("comp", "01 - الأيقونات - Icons.png"),
    "Core": ("comp", "02 - المكوّنات التفاعلية - Core.png"),
    "Shell": ("comp", "03 - الهيكل والبطاقات - Shell.png"),
    "Interactive": ("comp", "04 - مكوّنات النموذج التفاعلي - Interactive.png"),
    "Prototype guide": ("guide", "دليل النموذج التفاعلي - Prototype guide.png"),
}


def sources(arg):
    """Yield (name, bytes) for every PNG in a zip or folder."""
    p = Path(arg) if arg else max(DOWNLOADS.glob("OptiTime*.zip"), key=lambda f: f.stat().st_mtime)
    print("source:", p)
    if p.is_dir():
        for f in p.rglob("*.png"):
            yield f.name, f.read_bytes()
    else:
        with zipfile.ZipFile(p) as z:
            for i in z.infolist():
                if i.filename.lower().endswith(".png"):
                    yield Path(i.filename).name, z.read(i)


def size_of(data):
    return struct.unpack(">II", data[16:24]) if data[:8] == b"\x89PNG\r\n\x1a\n" else (0, 0)


ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
DRY = "--dry" in sys.argv
# --only=40-54 keeps just that number range plus the "Export · …" composites, so
# a second ZIP can't overwrite good screens with the cropped copies that sit
# inside the composites
ONLY = next((tuple(map(int, a[7:].split("-"))) for a in sys.argv if a.startswith("--only=")), None)
best = {}  # target path -> (rank, bytes, source name)
skipped = []
for name, data in sources(ARGS[0] if ARGS else None):
    stem = re.sub(r"-\d+$", "", Path(name).stem).strip()
    composite = stem.startswith("Export · ")
    if composite:
        stem = stem[len("Export · "):]
    m = re.match(r"^(\d{2})\s*·\s*(.+)$", stem)
    target = None
    if m:
        n = int(m.group(1))
        key = BY_NUMBER.get(n)
        if key:
            target = Path(FOLDERS[key]) / f"{m.group(1)} - {m.group(2)}.png"
            # popups: the composite beats the bare frame
            rank = (2 if composite else 1) if n in POPUPS else 1
    else:
        for prefix, (key, fname) in NAMED.items():
            if stem.startswith(prefix):
                target, rank = Path(FOLDERS[key]) / fname, 1
                break
    if target is None:
        skipped.append(name)
        continue
    if ONLY and not composite and not (m and ONLY[0] <= int(m.group(1)) <= ONLY[1]):
        skipped.append(f"{name} (outside --only)")
        continue
    if m and int(m.group(1)) in POPUPS and not composite and (BASE / target).exists():
        skipped.append(f"{name} (kept the saved popup-over-screen version)")
        continue
    cur = best.get(target)
    if cur is None or (rank, len(data)) > (cur[0], len(cur[1])):
        best[target] = (rank, data, name)

saved = 0
for target, (rank, data, src) in sorted(best.items()):
    w, h = size_of(data)
    if len(data) < 20_000:
        skipped.append(f"{src} (too small: {len(data)} bytes)")
        continue
    if not DRY:
        dest = BASE / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    saved += 1
    flag = "" if w >= 1500 or w == 780 else "  <- 1x, export at 2x for sharper text"
    print(f"{'would save' if DRY else 'ok'} {w}x{h} {len(data) // 1024} KB  {target}{flag}")
print(f"\n{'would save' if DRY else 'saved'} {saved} files; skipped {len(skipped)}:")
for s in skipped:
    print("  -", s)
