import os
from pathlib import Path
import tensorflow as tf

# Global vars used in TensorFlow tutorial
AUTOTUNE = tf.data.experimental.AUTOTUNE
BATCH_SIZE = 32
IMG_HEIGHT = 224
IMG_WIDTH = 224
CLASS_NAMES = [str(f) for f in list(Path("data/training_set").glob("*"))
               if f.is_dir()]


def get_label(file_path):
    # convert the path to a list of path components
    parts = tf.strings.split(file_path, os.path.sep)
    # The second to last is the class-directory
    return parts[-2] == CLASS_NAMES


def decode_img(img):
    # convert the compressed string to a 3D uint8 tensor
    # NOTE: expand_animations must be set to false because of .gif files
    # See: https://www.tensorflow.org/api_docs/python/tf/io/decode_image
    img = tf.image.decode_image(img, channels=3, expand_animations=False)
    # Use `convert_image_dtype` to convert to floats in the [0,1] range.
    img = tf.image.convert_image_dtype(img, tf.float32)
    # resize the image to the desired size.
    return tf.image.resize(img, [IMG_HEIGHT, IMG_WIDTH])


def process_path(file_path):
    label = get_label(file_path)
    # load the raw data from the file as a string
    img = tf.io.read_file(file_path)
    img = decode_img(img)
    return img, label


def prepare_dataset(ds, cache=False, shuffle_buffer_size=1000):
    # This is a small dataset, only load it once, and keep it in memory.
    # use `.cache(filename)` to cache preprocessing work for datasets that don't
    # fit in memory.
    if cache:
        if isinstance(cache, str):
          ds = ds.cache(cache)
        else:
          ds = ds.cache()

    ds = ds.shuffle(buffer_size=shuffle_buffer_size)

    # Repeat forever
    ds = ds.repeat()

    ds = ds.batch(BATCH_SIZE)

    # `prefetch` lets the dataset fetch batches in the background while the
    # model is training.
    ds = ds.prefetch(buffer_size=AUTOTUNE)

    return ds


def get_dataset(data_dir):
    # Precaution, because test/training set includes .DS_STORE files
    img_types = [".bmp", ".gif", ".jpg", ".jpeg", ".png"]
    img_globs = [str(data_dir/f'*/*{t}') for t in img_types]

    list_ds = tf.data.Dataset.list_files(img_globs)
    labeled_ds = list_ds.map(process_path, num_parallel_calls=AUTOTUNE)
    prepared_ds = prepare_dataset(labeled_ds)

    return prepared_ds