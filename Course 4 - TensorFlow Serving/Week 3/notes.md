Tensorboard is installed natively with Tensorflow

# TensorBoard.dev
https://tensorboard.dev/ is a website where you can store your model and access visualization from there


## Scalar values
Scalar values are (accuracy, loss ...etc)
Tensorboard use log to see these scalars.
the logs are setup by callbacks during training:

```python
log_dir = "logs/train_data/" + datetime.now().strftime("%Y%m%d-%H%M%S")

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir, histogram_freq=1)

model.fit(x, y, epochs=5,
        callbacks=[tensorboard_callback])

```

## Histogram Frequency
in tensorboard histogram are visualization of weights over time.
Can be helpfull to see if the weight are getting crazy

So histogram_frequ=1 in TensorBoard callback is saying to record the weight at every epochs.

By creating log_dir with timestamp we can load different training metadata in tensorboard

## upload logs
`!tensorboard dev upload --logdir ./logs`

Will upload all logs in this directory to the hosted tensorboard site


# Local Tensorboard
Previously we upload the logs to a server. 
On this seccion we see how to run tensorboard on the notebook (or collab).
This version have more features then tensorboard.dev actually!
It usually run on http://localhost:6006/


Same log directory and callback thing.

## visualize log
`%tensorboard  --logdir ./logs`


## Graphics
You can also explore your images in tensorboard.
In that case you write directly to the log_dir without going through a callback.

Use a filewriter and not a callback

```python
file_writer = tf.summary.create_file_writer(logdir)
with file_writer.as_default():
    tf.summary.image("Training data", img, step=0)

with file_writer.as_default():
    tf.summary.image("Training data", images, max_outputs=25, step=0)
```

Can write actually many data types: scalar, audio, images, text


## Confusion matrix
Example of another plot that can be done for tensorboard

1. Plot confusion matrix in matplotlib 
2. translate the confusion matrix to an image .png that can be logged in tensorboard
3. convert the image to a tf.image
4. use file_writer to write the image to the logs.

to plot the confusion matrix at every epoch you still need to use a callback to record the history
at each epoch the callback execute the function writing a new confusion matrix image to the file_writer