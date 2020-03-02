'''
# Create your own Dataset
TopClasses:
- DatasetBuilder: dataset info and base
- FileAdapterBuilder: feature generation and split
- GeneratorBasedBuilder: Example generation

You can create a script and push it to the offocial tensorflow-dataset repo:
https://github.com/tensorflow/dataset
By specifying the download url the script does the rest.
example /tensorflow_datasets/image/cats_vs_dogs.py


https://github.com/tensorflow/dataset/setup.py contain info about adding dependencies
see DATASET_EXTRAS cat_vs_dog need matplotlibrary


Corrupted data


basic code to implement a Dataset:
'''
import tensorflow_dataset as tfds

class MyDataset(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version('0.1.0')

    def _info(self):
        '''
        dataset info

        urls is places where the dataset can be found, but not the download link
        '''
        return tfds.core.DatasetInfo(
            builder=self, 
            description=("insert description here"),
            features=tfds.features.FeaturesDict(
                {
                    "description": tfds.features.Text(),
                    "image": tfds.features.Image(),
                    "label": tfds.features.ClassLabel(num_classes=5, names=["horse", "human", ...])
                }
            ),
            supervised_keys=("image", "label"),
            urls=['hrrps://dataset-homepage.org'], 
            citation=r"""@article{my-awesome-dataset-2020
                        ...
                        author = {Smith, John},"}"""
            )


    
    def _split_generator(self, df_manager):
        '''
        create the split and feature generation
        
        1. take care of the download and caching
        if login is require to download it have to be done manually and place in manual_dir

        2.split
        '''

        # equivalent to df_manager.extract(dl.manager.download(urls))
        dl_paths = dl_manager.download_and_extract(
            {
                'foo': 'https//example.con/foo.zip',
                'bar': 'https//example.con/bar.zip'
            }
        )
        dl_paths['foo'], dl_paths['bar']

        # split that is arcting after the dataset is downloaded to disc
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                # these will be passed to generate examples
                gen_kwargs={
                    "dir_path": os.path.join(extracted_path, "train"),
                    "labels": os.path.join(extracted_path, "train_labels.csv")
                } 
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                gen_kwargs={
                    "archive": dl_manager.iter_archive(test_path)
                } 
            )
        ]




    def _generate_examples(self):
        '''
        generator to output examples from the dataset
        '''
        for fname, fobj in archive:
            #anything other that .png skip
            res = _NAME_RE.match(fname)
            if not res:
                continue

            label = res.group(1).lower()
            record = {
                "image": fobj,
                "label": label
            }
        yield fname, record
