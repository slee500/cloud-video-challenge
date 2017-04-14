import tensorflow as tf

# Today I attempt to learn how to read stuff a tfrecords file, working with frame-level data
# Designed to work with Python 3.5

# Resources
# https://indico.io/blog/tensorflow-data-inputs-part1-placeholders-protobufs-queues/

# http://warmspringwinds.github.io/tensorflow/tf-slim/2016/12/21/tfrecords-guide/
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/how_tos/reading_data/fully_connected_reader.py

# Frame-level features are stored as 'tensorflow.SequenceExample' protocol buffers. 

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

###############################################

for serialized_example in tf.python_io.tf_record_iterator(filename):
    example = tf.train.Example()
    example.ParseFromString(serialized_example)

    # traverse the Example format to get data
    image = example.features.feature['rgb'].bytes_list.value
    label = example.features.feature['labels'].int64_list.value
    # do something
    print (type(image), label)

# print(tf.summary.image('frames', rgb))