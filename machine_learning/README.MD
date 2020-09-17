
# TensorFlow
### Conv
### Parameter Counting

  * 9 * 64 + 64 = 640
    * As shown in Listing 1.4.2, the CNN model in Listing 1.4.1 requires a smaller number of parameters at 80,226 compared to 269,322 when MLP layers are used. The conv2d_1 layer has 640 parameters because each kernel has 3 × 3 = 9 parameters, and each of the 64 feature maps has one kernel and one bias parameter. The number of parameters for other convolution layers can be computed in a similar way. Figure 1.4.5 shows the graphical representation of the CNN MNIST digit classifier.
    https://www.coursera.org/learn/introduction-tensorflow/lecture/Lz0FT/implementing-pooling-layers
    https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781788629416/1/ch01lvl1sec08/convolutional-neural-networks-cnns

  * 24 * 24 * 64 + 64 = 36928



  * 9 * 16 * 3 + 16 = 448
    * https://www.coursera.org/learn/introduction-tensorflow/lecture/DzQa3/defining-a-convnet-to-use-complex-images

