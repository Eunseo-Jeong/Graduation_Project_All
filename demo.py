from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from pymongo import MongoClient

import _init_paths


import logging
import os
import os.path as osp
from opts import opts
from tracking_utils.utils import mkdir_if_missing
from tracking_utils.log import logger
import datasets.dataset.jde as datasets
from track import eval_seq
from variable import variableClass
import cv2


logger.setLevel(logging.INFO)


def demo(opt):
    result_root = opt.output_root if opt.output_root != '' else '.'
    mkdir_if_missing(result_root)

    logger.info('Starting tracking...')
    # cap = cv2.VideoCapture('./videos/MOT16-03.mp4')
    # while(cap.isOpened()):
    #     print("dddddddddddddddd")
    #     ret, frame = cap.read()
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     cv2.imshow('frame', gray)
    #
    #     if cv2.waitKey(1)&0xFF == ord('q'):
    #         break
    # cap.release()
    # cv2.destroyAllWindows()
    #
    # result_root = ../demos
    # opt.input_video = ../videos/MOT16-03.mp4
    # opt.img_size = (1088, 608)
    # print("dddddddddddd",os.listdir(os.getcwd()))

    # mongo db
    connection = MongoClient('localhost', 27017)
    db = connection.get_database('teamA')
    print(db.list_collection_names())
    collection = db.get_collection('localInfo')

    # db.localInfo.remove()
    # db.createCollection('localInfo')

    ####video make

    # dataloader = datasets.LoadVideo('../videos/our.mp4', opt.img_size)
    num = 2 #count camera
    videos_list = ['../videos/0218_part1.mp4', '../videos/0218_part2.mp4']
    result_filename_list = ['../demos/results1.txt','../demos/results2.txt']

    variable_list = {}

    for i in range(num):
        variable_list[i] = variableClass(opt, videos_list[i], result_filename_list[i], result_root, i)



    # dataloader = datasets.MultiLoadVideo(dataloader1,dataloader2)


    #'''
    # eval_seq(track) -> plot_tracking(visualization)
    eval_seq(num, opt, variable_list, 'mot', collection, show_image=False)

    if opt.output_format == 'video':
        output_video_path = osp.join(result_root, '0218_part1_new2.mp4')
        cmd_str = 'ffmpeg -f image2 -i {}/%05d.jpg -b 5000k -c:v mpeg4 {}'.format(osp.join(result_root, 'frame'), output_video_path)
        os.system(cmd_str)
    #'''


if __name__ == '__main__':
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    opt = opts().init()
    demo(opt)
