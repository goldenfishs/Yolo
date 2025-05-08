# 使用前需要安装Pillow pip install Pillow

from PIL import Image
import os

def resize_and_convert_to_jpg(image_path):
    try:
        with Image.open(image_path) as img:
            # 获取图像的原始尺寸
            original_width, original_height = img.size
            target_size = (1920, 1080)

            # 等比例缩放图像
            img.thumbnail(target_size, Image.LANCZOS)

            # 转换为 RGB 模式（确保兼容 JPG 格式）
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # 修改文件扩展名为 .jpg
            new_image_path = os.path.splitext(image_path)[0] + ".jpg"

            # 保存为 JPG 格式
            img.save(new_image_path, format="JPEG")
            print(f"图像已调整大小并转换为 JPG: {new_image_path}")

            # 如果原文件不是 JPG，删除原文件
            if new_image_path != image_path:
                os.remove(image_path)
    except Exception as e:
        print(f"处理图像时发生错误: {e}")

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(root, file)
                resize_and_convert_to_jpg(image_path)

if __name__ == "__main__":
    folder_path = r"datasets\images\train"
    process_folder(folder_path)