
# nn_xor.py
un edited

Here's a minimal, well-commented example that learns the XOR problem <br>
— the classic "hello world" of neural nets (it's the simplest problem <br>
that requires a hidden layer). Only dependency is NumPy.

##  In Kate: File → New File, paste, save as nn_xor.py.
In Konsole:

sudo apt install python3-pip    # one-time setup<br>
pip install numpy               # one-time setup<br>
python3 nn_xor.py <br>

What's happening, in one line each:


| Line | Meaning |
| :---- | :---- |
| z1 \= X @ W1 \+ b1 | Weighted sum at hidden layer |
| a1 \= sigmoid(z1) | Squash to 0–1 (non-linearity) |
| dz2 \= a2 \- y | How wrong the output was |
| dW1 \= X.T @ dz1 | Gradient: which direction to nudge each weight |
| W1 \-= lr \* dW1 | Take a small step downhill |

That's the entire loop of deep learning: forward pass → measure error → backpropagate → update. Everything in PyTorch/TensorFlow is a more elaborate version of these ~15 lines.
