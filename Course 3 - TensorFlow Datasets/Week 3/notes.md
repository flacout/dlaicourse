# Performance
- Extract: load data local (HDD/SDD), Remote (HDFS)   CPU job
- transform: shuffling batching augmentation...       CPU job
- load: load transformed data to model.               GPU job

# CPU botleneck
The CPU step can become a bottleneck
On distributed setting the loading of the data can also be a problem.

## Without Pipelining:
CPU prepare1 | CPU idle   | CPU prepare2 | CPU idle   |
GPU idle     | GPU train1 | GPU idle     | GPU train2 |

## With pipelining
CPU prepare1 | CPU prepare2  | CPU prepare3 | 
GPU idle     | GPU train1    | GPU train2   |


## caching
you can cache a Dataset after transformation, if it fits in memory.
After the first epoch, the transformed data is cache so you don't have to apply the transformation again.

In memory
```python
train = dataset.cache()
model.fit(train, epochs=10, ...)
```

Disk caching. Save the transformation to disk
```python
train = dataset.cache(filename='cache')
model.fit(train, epochs=10, ...)
```

## Parallelism
1. tf.data.Dataset.map(func,  num_parallel_calls=)
parallell_calls define the nb of cpu cores it can use

How manny cores can I use?
For local use this call: `multiprocessing.cpu_count()`
For virtualize env it will not work.

```python
def augment(features):
    x = tf.image.random_flip_up_down(features['image'])
    x = tf.image.random_brightness(x)
    ...
    return image, features['label']


dataset = tfds.load('cats_vs_dogs', split='train')
cores = multiprocessing.cpu_count()
augmented_dataset = dataset.map(augment, num_parallel_calls=cores)
```

2. tf.data.Dataset.prefetch()
allow this config with good pipelining:
CPU prepare1 | CPU prepare2  | CPU prepare3 | 
GPU train1 0 | GPU train1    | GPU train2   |

```python
dataset = tfds.load('cats_vs_dogs', split='train')
train_dataset = dataset.map(format_image).prefetch(tf.data.experimental.AUTOTUNE)
# decouple the time the data is produced and the time the data is consume
```

prefetch internally run a bakground thread and a buffer to prefetch element from the dataset ahead of time.
The Nb of item prefetch should be equal or higher than the number of batches consumed by a training step.
You can also wset it automatically with AUTOTUNE



3. tf.data.Dataset.interleave()
Parallelize IO to have them
CPU1  I/o  | Map  | I/O | Map
CPU2  I/o  | Map  | I/O | Map

and not sequentially
CPU1  I/o  | I/o   |   I/O  |   I/O 
           |  Map  | Map    | Map


When you load a Dataset it is present locally as TFRecords.
You need to point this TFRecords directory containing the data
```python
TFRECOEDS_DIR = '/root/tensorflow_datasets/cats_vs_dogs/{info.version}/{dataset_name}-train.tfrecord*'
files = tf.data.Dataset.list_files(TFRECOEDS_DIR)

dataset = files.interleave(
    tf.data.TFRecordDataset,
    cycle_length=4,
    num_parallel_calls=AUTOTUNE
)
```


#### Magical Autotune
feature to ajust automatically at runtime the preprocessing depending on the computing resources available at the moment.
It tweak:
- Buffer size (map, prefetch, shuffle)
- CPU budget(num_parallel_calls)
- I/O (num_parallel_read)

```pyton
from tensorflow.data.experimental import AUTOTUNE

augmented_dataset = dataset.map(augment, num_parallel_calls=AUTOTUNE)
```


# Good practice

Ordering of the functions.

1. Vectorize map() on batch, instead of one item a t the time:
`dataset = dataset.batch(BATCH_SIZE).map(func)` 

2. If transformation map is heavy in computation. Applty cache() after it
`transf_dataset = dataset.map(transforms).cahe()`

3. `repeat()` repeat the transformation a number of time.

`shuffle().repeat()` is stupid has it shuffle manny times

`repeat().shuffle()` better performance