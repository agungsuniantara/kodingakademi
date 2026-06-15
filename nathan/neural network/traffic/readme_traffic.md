Traffic Sign Recognition – Experiment Results

I ran several experiments to see how the number of convolutional layers affected the model's accuracy in recognizing traffic signs using the GTSRB dataset.

1. One Convolutional Layer
The first model had only one convolutional layer and one max pooling layer.
The result was poor, with an accuracy of around 5–6 percent and a loss of about 3.5.
( 333/333 - 1s - 2ms/step - accuracy: 0.0560 - loss: 3.4931 )
The model was clearly underfitting and could not learn meaningful patterns.

2. Two Convolutional Layers
After adding a second convolutional layer, performance improved dramatically.
Training accuracy reached about 89–90 percent and testing accuracy around 97 percent.
( 333/333 - 1s - 2ms/step - accuracy: 0.9709 - loss: 0.1138 )
Loss decreased to about 0.11, showing that the model learned much better and generalized well.

3. Three Convolutional Layers
The third model used three convolutional layers.
It achieved around 94 percent training accuracy and 95 percent testing accuracy, with a loss near 0.16.
( 333/333 - 1s - 3ms/step - accuracy: 0.9551 - loss: 0.1621 )
The network became more stable, though the improvement over the two layer model was smaller.

Conclusion :
Adding more convolutional layers increased the model’s ability to recognize patterns, especially when going from one to two layers.
The model with three convolutional layers gave the best and most balanced results between training and testing accuracy.