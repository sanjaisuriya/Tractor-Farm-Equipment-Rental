from PIL import Image

def crop_and_save(src_path, dest_path, target_size=(800, 520), crop_anchor='center', quality=90):
    with Image.open(src_path) as im:
        im = im.convert('RGB')
        w, h = im.size
        tw, th = target_size
        target_ratio = tw / th
        current_ratio = w / h

        if current_ratio > target_ratio:
            new_w = int(h * target_ratio)
            if crop_anchor == 'center':
                left = (w - new_w) // 2
            elif crop_anchor == 'left':
                left = 0
            else:
                left = w - new_w
            box = (left, 0, left + new_w, h)
        else:
            new_h = int(w / target_ratio)
            if crop_anchor == 'top':
                top = 0
            elif crop_anchor == 'center':
                top = (h - new_h) // 2
            else:
                top = h - new_h
            box = (0, top, w, top + new_h)

        cropped = im.crop(box)
        resized = cropped.resize(target_size, Image.LANCZOS)
        resized.save(dest_path, 'JPEG', quality=quality)
        print(f"Saved {dest_path}: {resized.size}")

crop_and_save('scratch/taun_gusi_paddy_ploughing.jpg', 'scratch/test_kharif_1.jpg', crop_anchor='center')
crop_and_save('scratch/muthuvara_paddy.jpg', 'scratch/test_kharif_2.jpg', crop_anchor='center')
crop_and_save('scratch/vang_vieng_rice_tractor.jpg', 'scratch/test_kharif_3.jpg', crop_anchor='center')
