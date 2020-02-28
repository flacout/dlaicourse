# tf.data.Dataset
Usefull if data doesn't fit in memory
Help create input pipeline. 
Expl:
- Extracting words from raw text.
- convert to embeddings.
- batch together sequences of different length

## Load from pandas


## Load from file
This is more usefull if the file is huge has it use generator to read from it.
tf.data.experimental.make_csv_dataset    


# tf.feature_column
Once the features are defines they serve has input layer of a Keras model
Then during the training you simply pass the tf.data.Dataset
You can save your model which now contain in its input layers all the preprocesing:
normalization, one_hot encoding , etc...

## tf.numerical_columns

## bucketized 
Is when a binned number is represented in one hot encoding.
0          1              2              
-inf-1960   1980-2000     2000-+inf
100        010           001

tf.feature_column.bucketized_column(years, boundaries=[1960,1980, 2000])
there is 3 boudaries will give 4 BUCKETS!!!  (inner boundaries)
years variable is numeric values [1866, 1944, 2001, ...]

## categorical_column_with_identity
simple a one-hot encoding of a categorical
indicator column = one hot encoding

## One hot encoding of words
tf.feature_column.categorical_column_with_vocabulary_list()
tf.feature_column.categorical_column_with_vocabulary_file()

encode ["kitchen", "electronic", "sports"]   to [100, 010, 001]

## Hashed Column
tf.feature_column.categorical_column_with_hash_bucket()
If the list of strings is very long you can use Hash function to place them in a hash table.
If two string fall in the same bucket they are consider in the same bucket, so be carefull with  
the cardinality of the hashing (length of the array)

## Crosseed Column (polynomial feature)
Make new feature with two feature. (typically by multiplying them)
Example latitude * longitude

tf.feature_column.crossed_column([latidue, longitude], 5000)


## Embedding column
Rule of thumb : embedding dimension = forth root of nb words. (3 for 81 vocab word).

tf.feature_column.embedding_column(
    categorical_column=categorical_column,
    dimension=embedding_dimension
)




# TfRecord
Is used when Dataset is too big to fit memory.
Usually it will read from a stream or several files.
The files need to be in TFRecord format :(