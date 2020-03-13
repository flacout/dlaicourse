# Tensorflow-Hub
## General
On the webswite: https://tfhub.dev/

Look for a model, and find its url Handle: https://tfhub.dev/google/imagenet/mobilenet_v2_100_160/classification/4

Then load it with tensorflow-hub: module = hub.load(MODULE_HANDLE)

You can now use it as a Layer in a keras model.

## Feature Vector version
https://tfhub.dev/google/imagenet/mobilenet_v2_100_160/feature_vector/4/

When it says feature vectore it means the lasts dense layers are removed, 
so you can use it for transfert learning

## Storage
after hub.load(...)
By default the saved_model are stored in the tensoflow_hub library folder
under tmp folder

### custom storage
You can set the storage location manually with an env var 
os.environ['TFHUB_CACHE_DIR'] = '/home/fabrice/models'


# Text Example
Word embedding from tfhub often take care of the preprocessing:
You feed an entire sentence and they do tokenization steming etc...

Words embedding from tfhub can also do sentence embeding is you pass the entire sentence (not tokenized).
It first create token and embeddingd of each token then combine them in a sentence embedding!
