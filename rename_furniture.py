"""
家具素材重命名脚本
放到项目根目录运行：python rename_furniture.py
"""

import os
import shutil

FURNITURE_DIR = "assets/furniture"

RENAME_MAP = {
    "sprite-002.png": "工位1.png",
    "sprite-003.png": "工位2.png",
    "sprite-004.png": "电梯.png",
    "sprite-005.png": "饮水机.png",
    "sprite-006.png": "零食柜.png",
    "sprite-007.png": "茶水间.png",
    "sprite-008.png": "飞书后台.png",
}

# 长名字的工位文件（包含逗号的那个）
WORKSTATION_LONG = "工位3"

def rename():
    if not os.path.isdir(FURNITURE_DIR):
        print(f"❌ 找不到目录：{FURNITURE_DIR}")
        return

    files = os.listdir(FURNITURE_DIR)
    print(f"当前文件列表：")
    for f in sorted(files):
        print(f"  {f}")
    print()

    # 处理标准重命名
    for src_name, dst_name in RENAME_MAP.items():
        src = os.path.join(FURNITURE_DIR, src_name)
        dst = os.path.join(FURNITURE_DIR, dst_name)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            os.remove(src)
            print(f"✅ {src_name} → {dst_name}")
        else:
            print(f"⚠️  {src_name} 不存在，跳过")

    # 处理长名字的工位文件
    for f in os.listdir(FURNITURE_DIR):
        if "电脑" in f and f.endswith(".png") and f not in RENAME_MAP.values():
            src = os.path.join(FURNITURE_DIR, f)
            dst = os.path.join(FURNITURE_DIR, f"{WORKSTATION_LONG}.png")
            shutil.copy2(src, dst)
            os.remove(src)
            print(f"✅ {f} → {WORKSTATION_LONG}.png")
            break

    print(f"\n整理完成！当前文件：")
    for f in sorted(os.listdir(FURNITURE_DIR)):
        print(f"  {f}")

if __name__ == "__main__":
    rename()