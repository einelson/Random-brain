from random_brain import random_brain
import os
import unittest


class TestStringMethods(unittest.TestCase):

    # test if we can import a whole dir of models
    def test_import_dir(self):
        brain = random_brain()
        import_path = os.path.join(os.getcwd()+ '/testing_models') 
        brain.import_models(model_path=import_path)
        self.assertEqual(brain.show_brain(), os.listdir(os.path.join(os.getcwd() + '/testing_models')))

    # test if we can import a single model
    def test_import_single(self):
        brain = random_brain()
        import_path = os.path.join(os.getcwd()+ '/testing_models/eeg_eye_state.h5') 
        brain.import_models(model_path=import_path)
        self.assertEqual(brain.show_brain(), os.path.join(os.getcwd() + '/testing_models/eeg_eye_state.h5').split('!')) # need to change the ! delimeter, but should work if no ! in path. Just needs to be a list with one item

    # import a single item and a whole dir
    def test_import_single_and_dir(self):
        brain = random_brain()



    def test_classification(self):
        brain = random_brain()



    def test_regression(self):
        brain = random_brain()



    def test_save_brain(self):
        brain = random_brain()



    def test_load_brain(self):
        brain = random_brain()




if __name__ == '__main__':
    unittest.main()


# migrate below to above for automated testing

'''
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


'''