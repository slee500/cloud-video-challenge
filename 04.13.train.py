import tensorflow as tf

# Today I learn how to read stuff a tfrecords file, working with frame-level data
# Designed to work with Python 3.5

# Resources
# http://warmspringwinds.github.io/tensorflow/tf-slim/2016/12/21/tfrecords-guide/
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/how_tos/reading_data/fully_connected_reader.py

filename = 'train-0.tfrecord'
filename_queue = tf.train.string_input_producer([filename], num_epochs=1)
print ()
# print (tf.cast(filename_qsueue, tf.string))

reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)
features = tf.parse_single_example(
      serialized_example,
      # Defaults are not specified since both keys are required.
      features={
          'video_id': tf.FixedLenFeature([], tf.string),
          'labels': tf.FixedLenFeature([], tf.int64),
          'rgb': tf.FixedLenFeature([], tf.string),
          'audio': tf.FixedLenFeature([], tf.string),
      })

rgb = tf.decode_raw(features['rgb'], tf.uint8)
video_id = tf.cast(features['video_id'], tf.string)
labels = tf.cast(features['labels'], tf.int64)
print (labels)