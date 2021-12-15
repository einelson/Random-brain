# test file
import os
import pickle
from tensorflow import keras


# Class to act as random brain for neural networks
class random_brain:
    # Init needed data structures/ global vars here
    def __init__(self):
        # brain items
        self.brain = {} #{'file name':'model object'}

    # save brain
    def save_brain(self, path='random_brain.pkl'):
        if '.pkl' in path:
            try:
                with open(path, 'wb') as f:
                    pickle.dump(self.brain, f)
            except:
                raise Exception('Unable to save brain as pkl')
        else:
            raise Exception('Path mush be in format \'xxxxx.pkl\'')

    # load brain
    def load_brain(self, path='random_brain.pkl'):
        if '.pkl' in path:
            try:
                with open('saved_dictionary.pkl', 'rb') as f:
                    self.brain = pickle.load(f)
            except:
                raise Exception('Unable to open pkl')
        else:
            raise Exception('Path mush be in format \'xxxxx.pkl\'')

    # Import models (keras)  # model.save(os.getcwd()+'/saved models/model.h5') 
    def import_models(self, model_path=None):
        # ignore if no model has been selected
        if model_path == None:
            print('No model selected, skipping')
            return

        # check if singular model or dir
        if '.h5' not in model_path:
            dir = os.listdir(model_path)
            for model in dir:
                self.brain[model] = keras.models.load_model(model)
        else:
            # this is a single file
            self.brain[model_path] = keras.models.load_model(model_path)

    # Show imported models
    def show_brain(self):
        print(self.brain)

    # Clear list or one item
    def clear_brain(self, item_list=[]):
        # clearing one item or many
        if item_list == []:
            self.brain = {}
        else:
            for item in item_list:
                try:
                    del self.brain[item]
                except:
                    raise Exception(f'Unable to remove item: {item}')


    # Make a prediction
    def predict(self, get_vote=False, threaded=False, prediction_input=None): # maybe add in argument for regression or classification based answer
        # thread predictions?
        votes = []

        if prediction_input == None:
            raise Exception('Need to send in input')
        for model in self.brain.values:
             votes.append(model.predict(prediction_input))

        print(votes)
        # look for majority 
        # majority of bools or ints

        # if no majority and classification return a pseudo random answer

        # if no majority and regression return average?

        pass

