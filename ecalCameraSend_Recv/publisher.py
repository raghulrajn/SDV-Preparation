import ecal.core.core as ecal
import ecal.core.publisher as ecal_publisher
from video_pb2 import VideoFrame, VideoStream
import cv2  # For capturing video frames
import time
import sys
def main():
    ecal.initialize(sys.argv, "VideoStreamPublisher")

    # Create a publisher
    publisher = ecal_publisher.ProtoPublisher("VideoStream")

    # Open video capture (0 for the default camera)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Encode the frame as JPEG
        _, encoded_frame = cv2.imencode('.jpg', frame)

        # Create a VideoFrame message
        video_frame = VideoFrame()
        video_frame.frame_data = encoded_frame.tobytes()
        video_frame.width = frame.shape[1]
        video_frame.height = frame.shape[0]
        video_frame.timestamp = int(time.time() * 1e6)  # Microseconds

        # Create a VideoStream message and add the frame
        video_stream = VideoStream()
        video_stream.frames.append(video_frame)

        # Send the message
        publisher.send(video_stream)

        # Sleep to control frame rate
        time.sleep(0.033)  # ~30 FPS

    cap.release()
    ecal.finalize()

if __name__ == "__main__":
    main()
