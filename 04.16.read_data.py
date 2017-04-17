import tensorflow as tf
import numpy as np

# Today I attempt to learn how to read stuff a tfrecords file, working with frame-level data

# Resources
# https://www.kaggle.com/philschmidt/youtube8m/youtube8m-eda
# https://www.kaggle.com/wendykan/youtube8m/starter-explore-youtube8m-sample-data


filename = 'train-0.tfrecord'
sess = tf.InteractiveSession()

for example in tf.python_io.tf_record_iterator(filename):
    tf_seq_example = tf.train.SequenceExample.FromString(example)

    print (tf_seq_example.context.feature['video_id'].bytes_list.value[0])
    print (len(tf_seq_example.feature_lists.feature_list['rgb'].feature))

    x = tf.cast(tf.decode_raw(tf_seq_example.feature_lists.feature_list['rgb'].feature[0].
        bytes_list.value[0],tf.uint8),tf.float32).eval()

    print (x)

    # traverse the Example format to get data
    # image = example.features.feature['rgb'].features[0].bytes_list.value[0]
    # label = example.features.feature['labels'].int64_list.value
    # # do something
    # print (type(image), label)
    break

# print(tf.summary.image('frames', rgb))