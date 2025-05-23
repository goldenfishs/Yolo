from collections import defaultdict

import cv2
import numpy as np

from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolo11n.pt")
# model = YOLO("yolov8n.pt")
# model = YOLO("your_yolo_model.pt")

# Open the video file
# video_path = "path/to/video.mp4"
cap = cv2.VideoCapture(0)

# Store the track history
track_history = defaultdict(lambda: [])

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        results = model.track(frame, persist=True)
        # print(results)
        boxes = results[0].boxes.xywh.cpu()
        track_ids = results[0].boxes.id

        if track_ids is not None:
            track_ids = track_ids.int().cpu().tolist()
        
            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Plot the tracks
            for box, track_id in zip(boxes, track_ids):
                x, y, w, h = box
                track = track_history[track_id]
                track.append((float(x), float(y)))  # x, y center point
                if len(track) > 30:  # retain 90 tracks for 90 frames
                    track.pop(0)

                # Draw the tracking lines
                points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=10)
        else:
            annotated_frame = frame

        # Display the annotated frame
        cv2.imshow("YOLO11 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()