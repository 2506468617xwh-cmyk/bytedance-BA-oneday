"""
批量整理角色Sprite命名脚本
每个角色文件夹（格式：姓名_黑_doublebg-sprites）里：
  姓名.png       → 复制到 assets/characters/姓名.png（正面）
  sprite-002.png → 复制到 assets/characters/姓名_back.png（背面）
  sprite-003.png → 复制到 assets/characters/姓名_left.png（左侧）
  右侧由代码镜像左侧，不需要单独图片

放到项目根目录运行：python organize_sprites.py
"""

import os
import shutil

CHARACTERS_DIR = "assets/characters"

SPRITE_MAP = {
    "sprite-002.png": "back",
    "sprite-003.png": "left",
}

def organize():
    if not os.path.isdir(CHARACTERS_DIR):
        print(f"❌ 找不到目录：{CHARACTERS_DIR}")
        return

    # 找所有 _黑_doublebg-sprites 子文件夹
    folders = [
        f for f in os.listdir(CHARACTERS_DIR)
        if os.path.isdir(os.path.join(CHARACTERS_DIR, f))
        and "doublebg-sprites" in f
    ]

    if not folders:
        print("❌ 没有找到角色sprite文件夹（格式应为：姓名_黑_doublebg-sprites）")
        return

    print(f"找到 {len(folders)} 个角色文件夹\n")

    for folder in sorted(folders):
        # 从文件夹名提取角色姓名（取第一个下划线之前的部分）
        char_name = folder.split("_")[0]
        folder_path = os.path.join(CHARACTERS_DIR, folder)

        print(f"📁 处理：{char_name}")

        for sprite_file, direction in SPRITE_MAP.items():
            src = os.path.join(folder_path, sprite_file)
            dst = os.path.join(CHARACTERS_DIR, f"{char_name}_{direction}.png")

            if os.path.exists(src):
                shutil.copy2(src, dst)
                print(f"   ✅ {sprite_file} → {char_name}_{direction}.png")
            else:
                print(f"   ⚠️  {sprite_file} 不存在，跳过")

        # 检查正面图是否存在
        front = os.path.join(CHARACTERS_DIR, f"{char_name}.png")
        if os.path.exists(front):
            print(f"   ✅ {char_name}.png（正面，已存在）")
        else:
            # 尝试从文件夹里找正面
            front_in_folder = os.path.join(folder_path, f"{char_name}.png")
            if os.path.exists(front_in_folder):
                shutil.copy2(front_in_folder, front)
                print(f"   ✅ 正面图从文件夹复制：{char_name}.png")
            else:
                print(f"   ❌ 正面图缺失：{char_name}.png")

    print("\n🎉 整理完成！assets/characters/ 下现在有：")
    result = [
        f for f in os.listdir(CHARACTERS_DIR)
        if f.endswith(".png") and os.path.isfile(os.path.join(CHARACTERS_DIR, f))
    ]
    for f in sorted(result):
        print(f"   {f}")

if __name__ == "__main__":
    organize()