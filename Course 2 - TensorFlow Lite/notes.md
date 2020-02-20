# tensorflow Lite component:
Converter: Converting model to tensorflow lite
Interpreter: Run the model on android or iOS os 

# Optimization
1. Quantization: reduce precision of float number.
2. weight pruning
3. model topology transform: tensor decomposition, distillation

## Quantization
COnvert float to int.
Some operations doesn't allow quantized operation so it might raise error in some cases. (unsuported tensorflow Ops)
--> not every model is convertable with operation.
A representative dataset is used to scale the weights and activation.

### TFSelect
select float operation for the Ops not yet supporting quantization operations

### Summary
No Quantization --> Floating point model
Post Training Quantization    -->
   Only Weight quantized
   Representative Dataset --> 
       Weight+Activations quantized
           --> Limit to INT8 Ops of TFLite (might not work for your model)
           --> Use TFSelect for both int and float model.

Pre Training Quantization --->
    Real quantization. Need to train with specific call.


# process to use TFLite model
- tensorflow model save.  tf.saved_model() is preffered!!
- convert kerasModel or savedModel to .TFLite format
- save the TFLite model to be used on Android system

# the TFLite interpreter can be use locally to test the model before pass it to a android phone.

# Install tensorflow on raspberryPi
## Install Full tensorflow
sudo apt update
sudo apt install python3-dev python3-pip
sudo apt install libatlas-base-dev  # special for raspberryPi
pip install --upgrade tensorflow

## Install tensorflowLite interpreter only
pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
  