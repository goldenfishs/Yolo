# 使用前需要安装Pillow pip install Pillow

from PIL import Image
import os

def rotate_to_landscape(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            if height > width:
                # 旋转图像使其变为横向
                rotated_img = img.rotate(90, expand=True)
                rotated_img.save(image_path)
                print(f"图像已旋转: {image_path}")
            else:
                print(f"图像已是横向: {image_path}")
    except Exception as e:
        print(f"处理图像时发生错误: {e}")

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(root, file)
                rotate_to_landscape(image_path)

if __name__ == "__main__":
    folder_path = "E:\School\R\Robocon\垃圾桶\数据集"
    process_folder(folder_path)