import cv2
def video_info(filename1, filename2):

    cap1 = cv2.VideoCapture(filename1)
    cap2 = cv2.VideoCapture(filename2)

    if not cap1.isOpened() and cap2.isOpened():
        print("could not open: ")
        exit(0)

    len = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap1.get(cv2.CAP_PROP_FPS))
    total = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))

    print("video1, before: ", len, width, height, fps, total)

    cap1.set(cv2.CAP_PROP_FPS, 60)
    cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)
    print("video1, after: ", len, width, height, fps, total)


    len = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap2.get(cv2.CAP_PROP_FPS))
    total = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

    print("\nvideo2, before: ", len, width, height, fps, total)

video_info('real_0218_part1.mp4', 'real_0218_part2.mp4')