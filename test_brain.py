# test file
import os
import tensorflow as tf


# Class to act as random forest for neural networks
class random_brain:
    # Init needed data structures/ global vars here
    def __init__(self):
        # forest items
        self.forest = {} #{'file name':'model object'}

    # save brain
    def save_ensemble(self, path):
        pass

    # load brain
    def load_ensemble(self, model_path):
        pass


    # Import models
    def import_models(self, model_path=None):
        # ignore if no model has been selected
        if model_path == None:
            print('No model selected, skipping')
            return

        # check if singular model or dir
        if '.h5' not in model_path:
            # this is a dir
            pass
        else:
            # this is a single file
            self.forest[model_path] = tf.keras.models.load_model(model_path)
            pass
        

        print(os.listdir(os.getcwd()))

    # Show imported models
    def show_forest(self):
        print(self.forest)

    # Clear list or one item
    def clear_forest(self):
        # clearing one item or many
        self.forest = {}

    # Make a prediction
    def predict(self):
        # thread predictions?

        # look for majority 
        # majority of bools or ints

        # if no majority and classificatino return a pseudo random answer

        # if no majority and regression return average?

        pass


if __name__ == "__main__":
    # run tests

    print('init')
    brain = random_brain()

    print('import model')
    brain.import_models()

    print('showing random forest')
    brain.show_forest()

