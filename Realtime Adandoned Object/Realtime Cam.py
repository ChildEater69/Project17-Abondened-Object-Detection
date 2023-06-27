import numpy as np
import cv2
from collections import Counter, defaultdict
import time

def process_video(duration=20):
    cap = cv2.VideoCapture(0)  # Use camera index 0 for the first camera

    if not cap.isOpened():
        print("Error opening camera")
        return

    ret, first_frame = cap.read()
    if not ret:
        print("Error capturing frame")
        return

    video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the codec for saving the video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_video = cv2.VideoWriter('output.avi', fourcc, fps, (video_width, video_height))

    first_frame_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    first_frame_blur = cv2.GaussianBlur(first_frame_gray, (9, 9), 0)

    # ---------------------------------
    # size the window first
    # ---------------------------------
    cv2.namedWindow('CannyEdgeDet', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Abandoned Object Detection', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Morph_CLOSE', cv2.WINDOW_NORMAL)

    consecutiveframe = 20
    min_area = 200
    max_area = 20000

    track_temp = []
    track_master = []
    track_temp2 = []

    top_contour_dict = defaultdict(int)
    obj_detected_dict = defaultdict(int)

    start_time = time.time()
    frameno = 0  # Initialize frame number
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frameno += 1  # Increment frame number
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_blur = cv2.GaussianBlur(frame_gray, (9, 9), 0)

        frame_diff = cv2.absdiff(first_frame, frame)

        # Canny Edge Detection
        edged = cv2.Canny(frame_diff, 100, 200)
        cv2.imshow('CannyEdgeDet', edged)

        kernel2 = np.ones((5, 5), np.uint8)
        thresh2 = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel2, iterations=2)
        cv2.imshow('Morph_Close', thresh2)

        # Find contours
        cnts, _ = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        mycnts = []
        for c in cnts:
            M = cv2.moments(c)
            if M['m00'] == 0:
                pass
            else:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                if cv2.contourArea(c) < min_area or cv2.contourArea(c) > max_area:
                    pass
                else:
                    mycnts.append(c)

                    (x, y, w, h) = cv2.boundingRect(c)

                    sumcxcy = cx + cy
                    track_temp.append([cx + cy, frameno])

                    track_master.append([cx + cy, frameno])

                    countuniqueframe = set(j for i, j in track_master)
                    if len(countuniqueframe) > consecutiveframe:
                        minframeno = min(j for i, j in track_master)
                        for i, j in track_master:
                            if j != minframeno:
                                track_temp2.append([i, j])

                        track_master = list(track_temp2)
                        track_temp2 = []

                    countcxcy = Counter(i for i, j in track_master)
                    for i, j in countcxcy.items():
                        if j >= consecutiveframe:
                            top_contour_dict[i] += 1

                    if sumcxcy in top_contour_dict:
                        if top_contour_dict[sumcxcy] > 100:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            obj_detected_dict[sumcxcy] += 1
                            cv2.putText(frame, "Abandoned object", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 255, 0), 2)

        cv2.imshow('Abandoned Object Detection', frame)

        # Save frame to the output video
        output_video.write(frame)

        elapsed_time = time.time() - start_time
        if elapsed_time >= duration:
            break

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    output_video.release()
    cv2.destroyAllWindows()

process_video()
