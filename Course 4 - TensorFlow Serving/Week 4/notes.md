# Federated Data

## Example
Data from 10 customer train 10 mini models. The models are then aggregated to a big one that is distributed to everyone.
--> The data doesn't leave the customer, so better privacy!


## Use Case
ata on mobile phone training on phone.
Sending the model(not the data) to a centralize model (on server) 

--> data stay at the edge


## Mechanic
To aggregate the models it is kind of an average of the weights.
Federated Learning paper :
https://ai.googleblog.com/2017/04/federated-learning-collaborative.html
https://research.google/pubs/pub47976/


## Caution
What if the model send to the server is revrse engineer to get to the customer data?

Sometimes it's not the model that is send to the server but a preprocessed data.
In that case the data can be aggregated for all user so the privacy is kept.

This is called

### Focused collection
The device send only what is needed for the calculation
Example what word to recommend after "Hello"?
Calculate freq of words ["Hello", "world"]
user1  [28, 0]
user2  [25, 10]
...
sum [63000, 10000]
The result is send back to the users who now has a global model.

SAME THING for NN
The neurons (weights) are aggregated as soon as they arrive to the server
So they cannot be reverse-engineer for a single user.


### Masking for secure aggregation
Link to the paper “Practical Secure Aggregation for Privacy-Preserving Machine Learning”
https://eprint.iacr.org/2017/281.pdf

The idea is to hash the data with several masks. 
When looked individualy the data from each user is encrypted several times so difficult to decrypt.
But each mask (encryption hash function) as a reverse mask that cancel out:
mask1(mask1rev(data)) = data

The reverse mask is on another user encryption.
So on the sever all the mask cancel each other and the data is decrypted that way.




## TF federated API 
Example reading temperature on device:
{float32}@CLIENTS  declare a variable of float that exist for manny clients
float32@SERVER is the aggregated variable resulted of the aggregation of {float32}@CLIENTS
the aggregation is a function tff.federated_mean: mean of the values in that case.

the tff function takes care of the distributed communication protocol

- federated ops are the building blocks of a federated learning system