import cv2
import argparse
import os


def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Process pic')
    parser.add_argument('--input', help='video to process', dest='input', default=None, type=str)
    parser.add_argument('--output', help='pic to store', dest='output', default=None, type=str)
    # default为间隔多少帧截取一张图片；我这里用10刚刚好！
    parser.add_argument('--skip_frame', dest='skip_frame', help='skip number of video', default=10, type=int)
    # input为输入视频的路径 ，output为输出存放图片的路径
    args = parser.parse_args(['--input', r'/home/fly/AWYY/interaction/train_test_data/cwj/1-0-0-2.mp4',
                              r'--output', '/home/fly/AWYY/interaction/train_test_data/img-cwj/1-0-0-2'])
    return args


# 处理过程
def process_video_imgs(i_video, o_video, num):
    cap = cv2.VideoCapture(i_video)  # 捕获视频
    num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 有多少帧
    expand_name = '.jpg'  # 扩展维jpg
    if not cap.isOpened():
        print("Please check the path.")
    cnt = 0
    count = 0  # 计数器
    while 1:
        ret, frame = cap.read()  # 读一帧
        cnt += 1

        if cnt % num == 0:  # 每num帧保存一张图片
            count += 1
            cv2.imwrite(os.path.join(o_video, str(count) + expand_name), frame)  # 写图片

        if not ret:  # ret为false就意味着视频帧没了
            break


if __name__ == '__main__':
    args = parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)  # 输出没有的话，自建
    print('Called with args:')
    print(args)
    process_video_imgs(args.input, args.output, args.skip_frame)
