# 使用前需要安装Pillow pip install Pillow

from PIL import Image
import os

def resize_to_1080p(image_path):
    try:
        with Image.open(image_path) as img:
            # 获取图像的原始尺寸
            original_width, original_height = img.size
            target_size = (1920, 1080)

            # 等比例缩放图像
            img.thumbnail(target_size, Image.LANCZOS)
            img.save(image_path)
            print(f"图像已调整大小: {image_path}")
    except Exception as e:
        print(f"处理图像时发生错误: {e}")

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(root, file)
                resize_to_1080p(image_path)

if __name__ == "__main__":
    folder_path = r"E:\School\R\Robocon\垃圾桶\数据集"
    process_folder(folder_path)