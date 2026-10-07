"""
せんせいの いかり 画像の後処理スクリプト (process_images.py)

機能:
1. img/ の画像を適切なサイズに縮小
   - face0〜face4（いかりの だんかいごとの 先生の顔）, boom（ばくはつ後）: 512x512 におさまるように
   - bg（背景）: 1600x1000 におさまるように
2. 先生の画像（face*, boom）は 緑の背景（クロマキー）を とうめいにして PNG で保存
   （画像生成では「plain flat pure green background」と指定して作る）
3. 各画像をWeb向けに軽量化 (JPEG品質 82, 最適化)
4. img/list.json を再生成（index.html はこれを見て、ある画像だけ読み込む）

画像が1枚も無くても index.html は先生の絵を描いて動きます。
"""

import json
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR = BASE_DIR / "img"
EXTS = [".png", ".jpg", ".jpeg", ".webp"]

# 縦横比は そのままで、この大きさに おさまるように 縮小する
RESIZE_RULES = {
    "face0": (512, 512),
    "face1": (512, 512),
    "face2": (512, 512),
    "face3": (512, 512),
    "face4": (512, 512),
    "boom": (512, 512),
    "bg": (1600, 1000),
}


KEY_STEMS = {"face0", "face1", "face2", "face3", "face4", "boom"}


def is_green_bg(im):
    """四すみが 緑なら クロマキーの背景とみなす"""
    rgb = im.convert("RGB")
    w, h = rgb.size
    for x, y in [(2, 2), (w - 3, 2), (2, h - 3), (w - 3, h - 3)]:
        r, g, b = rgb.getpixel((x, y))
        if not (g > 120 and g > r * 1.5 and g > b * 1.5):
            return False
    return True


def remove_green(im):
    """緑の背景を とうめいにする（ふちの 緑っぽさも おさえる）"""
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            m = max(r, b)
            d = g - m  # 緑が どれだけ 強いか
            if d > 60:
                px[x, y] = (r, g, b, 0)
            elif d > 20:
                # ふち：半とうめいにして 緑を ぬく
                px[x, y] = (r, m, b, int(a * (60 - d) / 40))
            elif d > 0:
                px[x, y] = (r, m, b, a)
    return im


def chroma_key():
    """img/ の face*/boom が 緑背景の jpg なら、とうめい PNG に変換する"""
    for img_path in sorted(IMG_DIR.iterdir()):
        stem = img_path.stem.lower()
        if stem not in KEY_STEMS or img_path.suffix.lower() not in [".jpg", ".jpeg", ".png", ".webp"]:
            continue
        with Image.open(img_path) as im:
            if im.mode == "RGBA" and im.getpixel((2, 2))[3] == 0:
                continue  # もう とうめいに なっている
            if not is_green_bg(im):
                continue
            target = RESIZE_RULES.get(stem)
            im = im.copy()
            if target:
                im.thumbnail(target, Image.Resampling.LANCZOS)
            out = remove_green(im)
        out_path = img_path.with_suffix(".png")
        out.save(out_path, optimize=True)
        if out_path != img_path:
            img_path.unlink()
        print(f"Chroma key: {img_path.name} -> {out_path.name}")


def process_images():
    if not IMG_DIR.exists():
        IMG_DIR.mkdir()
        print(f"Created {IMG_DIR}")

    chroma_key()

    for img_path in sorted(IMG_DIR.iterdir()):
        if not img_path.is_file():
            continue
        ext = img_path.suffix.lower()
        if ext not in EXTS:
            continue

        stem = img_path.stem.lower()
        target_size = RESIZE_RULES.get(stem)
        try:
            with Image.open(img_path) as im:
                orig_size = im.size
                if target_size and (orig_size[0] > target_size[0] or orig_size[1] > target_size[1]):
                    im = im.copy()
                    im.thumbnail(target_size, Image.Resampling.LANCZOS)
                    print(f"Resizing {img_path.name} from {orig_size} to {im.size}...")
                    if ext in [".jpg", ".jpeg"]:
                        im.convert("RGB").save(img_path, quality=82, optimize=True)
                    else:
                        im.save(img_path, optimize=True)
                elif ext in [".jpg", ".jpeg"]:
                    # JPEG 圧縮の最適化（大きすぎるファイルを適正化）
                    file_size_kb = img_path.stat().st_size / 1024
                    if file_size_kb > 500:
                        print(f"Compressing {img_path.name} ({file_size_kb:.1f} KB)...")
                        im.convert("RGB").save(img_path, quality=82, optimize=True)
        except Exception as e:
            print(f"Error processing {img_path}: {e}")

    update_list_json()


def update_list_json():
    files = sorted(
        p.name for p in IMG_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in EXTS + [".gif"]
    )
    list_json_path = IMG_DIR / "list.json"
    with open(list_json_path, "w", encoding="utf-8") as f:
        json.dump(files, f, ensure_ascii=False, indent=1)
    print(f"Updated {list_json_path}")
    print(json.dumps(files, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    process_images()
