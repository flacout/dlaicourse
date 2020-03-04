# Tensorflow Serving
A way to deploy a model to a server an request it with an http API
return the prediction
Tensorflow Serving is part of TFX (tensorflow extended)

## pros
- If you update your model on the server this is reflected to all the clients directly.
(whereas an Android model, the client need to update it himself)

- can leverage cloud infrastructure to auto-scale, with load balancer and manny servers behind.

## installation
can be done with docker (recommended)
or pip install
or apt install on linux

## run  on docker (on crappy window)

docker run -t --rm -p 8501:8501 \
    -v c:/Users/fabrice.lacout/Desktop/labos/labo-tensorflow-serving/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu:/models/half_plus_two \
    -e MODEL_NAME=half_plus_two \
    tensorflow/serving &


call 
curl -d '{"instances": [1.0, 2.0, 5.0]}' \
    -X POST http://localhost:8501/v1/models/half_plus_two:predict