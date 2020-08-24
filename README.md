# video_to_imgs
transfer an video to images.

constructed by LOVEYRR

A.how to create a github repository???
简书或博客连接都有的
https://www.jianshu.com/p/de2d99752924


代码：video_to_imgs.py
中的参数设置：输入输出文件夹
args = parser.parse_args(['--input', r'/home/fly/AWYY/interaction/train_test_data/cwj/1-0-0-2.mp4',
                              r'--output', '/home/fly/AWYY/interaction/train_test_data/img-cwj/1-0-0-2'])

--skip_frame 为跳过多少帧获取一张图

读取视频的核心代码：cap = cv2.VideoCapture(i_video)  # 捕获视频

保存图片的核心代码：cv2.imwrite(os.path.join(o_video, str(count) + expand_name), frame)  # 写图片

然后就能运行main函数跑了

