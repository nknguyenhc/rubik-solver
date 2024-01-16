# rubik-solver
A website to solve rubik's cube using various AI technologies

## Development

1. Install the python dependencies.

```
pip install -r requirements.txt
```

2. Start the development.

3. When finished, indicate the new python dependencies.

```
pip freeze > requirements.txt
```

### Models

All models are under `/models` folder. In particular, for the following subfolders:

* `color-clustering`: given 9 x 6 colours, groups them into 6 colours and returns the 6 values representing the 6 colours.
* `cube-recognition`: given an image, returns the 9 colours of the face of the Rubik's cube.
* `solver`: given a Rubik's cube configuration with 6 distinct colours, returns a sequence of steps to solve the cube.

The `.py` file is the file where we declare the function to be used elsewhere. Please make sure to follow the data type specified.

The `.ipynb` is for us to show our workings only. Do add explanation as markdown where necessary, and add test cases to show what you have tested your model on.

Feel free to add more files as needed (datasets, hyperparameters, etc).
