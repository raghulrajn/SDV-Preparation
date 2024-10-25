import ecal.core.core as ecal
import ecal.core.subscriber as ecal_subscriber
from video_pb2 import VideoFrame, VideoStream
import cv2
import numpy as np
import sys
import time

def on_receive(topic_name, msg, time):
    print("Received message on topic:", topic_name)  # Debugging: Confirm the topic name
    video_stream = VideoStream()

    for frame in msg.frames:
        # Process each received frame
        print(f"Received frame of size: {len(frame.frame_data)} "
              f"Width: {frame.width} "
              f"Height: {frame.height} "
              f"Timestamp: {frame.timestamp}")

        # Decode the frame data
        nparr = np.frombuffer(frame.frame_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        cv2.imshow('Received Frame', img)
        cv2.waitKey(1)

def main():
    ecal.initialize(sys.argv, "VideoStreamReceiver")

    subscriber = ecal_subscriber.ProtoSubscriber("VideoStream", 
                                                 VideoStream)
    subscriber.set_callback(on_receive)

    while ecal.ok():
        time.sleep(0.1)

    # Clean up
    cv2.destroyAllWindows()
    ecal.finalize()


if __name__ == "__main__":
    main()
