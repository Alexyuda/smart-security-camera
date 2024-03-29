import argparse


# Parse command line arguments
parser = argparse.ArgumentParser(description="Video processing pipeline")
parser.add_argument("-i", "--input", default="0",
                help="path to input video file or camera identifier")
parser.add_argument("-d", "--display", default=True, help="display video result")
parser.add_argument("-an", "--annotate", default=True, help="Annotate video")
parser.add_argument("-df", "--detect_faces", default=False, help="Detect and recognize faces")
parser.add_argument("-p", "--progress", default=True, help="display progress")

parser.add_argument("--prototxt", default="./models/face_detector/deploy.prototxt.txt",
                help="path to face detection pre-trained model prototxt file")
parser.add_argument("--face_detection_model", default="./models/face_detector/res10_300x300_ssd_iter_140000.caffemodel",
                help="path to face detection pre-trained model caffe model")
parser.add_argument("--face_detection_confidence", type=float, default=0.5,
                help="minimum probability to filter weak face detections")
parser.add_argument("--batch-size", type=int, default=1,
                help="face detection batch size")

parser.add_argument("--face_recognition_model", default="./models/MobileFaceNet_pytorch/mobilefacenet_scripted.pt",
                help="path to face embedding pre-trained model ckpt ")
parser.add_argument("--face_recognition_confidence", type=float, default=0.5,
                help="minimum probability for face recognition")

parser.add_argument("--p_min_motion_area", type=float, default=0.005,
                help="min size of blob in % for motion detection")
parser.add_argument("--select_roi", default=False, help="select a roi for the camera to focus on")

# video recording
parser.add_argument("--vid_dump_dir", type=str, default=r"C:\Users\alexy\Desktop\cam1",
                    help="Dir where videos will be saved")
parser.add_argument("--min_motion_to_save_video_sec", type=int, default=0.1,
                    help="This amount of seconds most include motion to start recording")
parser.add_argument("--min_vid_length_sec", type=int, default=10,
                    help="Lowest limit to video length in seconds")
parser.add_argument("--delete_after_n_days", type=int, default=14,
                    help="Keep your videos for this amount of days")
parser.add_argument("--close_cap_and_start_new_one_after_n_secs", type=float, default=60,
                    help="After recording this amount of seconds start a new video")
