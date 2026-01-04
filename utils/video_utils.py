# Extraction frames vidéo



import cv2
import os

def extract_frames(video_path, output_dir="frames", max_frames=30):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frames = []
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret or count >= max_frames:
            break
        frame_path = os.path.join(output_dir, f"frame_{count}.jpg")
        cv2.imwrite(frame_path, frame)
        frames.append(frame_path)
        count += 1
    cap.release()
    return frames
