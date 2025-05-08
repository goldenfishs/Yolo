# 用于将文件夹下所有视频拆成图片放到对应文件夹

import os
import cv2

def extract_frames_from_videos(input_folder, output_folder):
    """
    将指定文件夹下的所有视频拆分成图片，并保存到输出文件夹中。
    
    :param input_folder: 包含视频文件的输入文件夹路径
    :param output_folder: 保存图片的输出文件夹路径
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for video_file in os.listdir(input_folder):
        video_path = os.path.join(input_folder, video_file)

        # 检查是否为视频文件（通过扩展名）
        if not video_file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            continue

        # 获取视频文件的前缀名
        video_name = os.path.splitext(video_file)[0]

        # 打开视频文件
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"无法打开视频文件: {video_file}")
            continue

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 保存每一帧为图片，命名格式为 "视频名_帧序号.jpg"
            frame_filename = os.path.join(output_folder, f"{video_name}_frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            frame_count += 1

        cap.release()
        print(f"视频 {video_file} 已处理完成，共提取 {frame_count} 帧。")

if __name__ == "__main__":
    # 输入文件夹路径（包含视频文件）
    input_folder = r"C:\Mac\Home\Desktop\Yolo"
    # 输出文件夹路径（保存图片）
    output_folder = r"C:\Mac\Home\Desktop\Yolo\datasets\images\train"

    extract_frames_from_videos(input_folder, output_folder)