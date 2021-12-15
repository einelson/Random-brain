from random_brain import random_brain
import os

if __name__ == "__main__":
    # run tests

    print('init')
    brain = random_brain()

    # import dir
    print('import model dir')
    import_path = os.path.join(os.getcwd, '/models') 
    brain.import_models(model_path=import_path)

    print('showing random brain with dir')
    brain.show_brain()

    print('clearing brain')


    # import 1 model classification
    print('showing cleared brain')

    print('showing random brain with one model')


    # add in the dir with the one model classification

    # make a prediction classification

    # clear brain


    # import dir for regression

    # make prediction


    # save brain

    # clear brain

    # load brain


    # make prediction with imported brain (regression)


