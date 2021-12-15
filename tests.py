from random_brain import random_brain
import os
import unittest


brain = random_brain()


class TestStringMethods(unittest.TestCase):

    # test if we can import a whole dir of models
    def test_import_dir(self):
        import_path = os.path.join(os.getcwd()+ '/testing_models') 
        brain.import_models(model_path=import_path)
        self.assertEqual(brain.show_brain(), os.listdir(os.path.join(os.getcwd()+ '/testing_models')))

    # test if we can import a single model
    def test_import_single(self):
        pass


    def test_import_single_and_dir(self):
        pass


    def test_classification(self):
        pass


    def test_regression(self):
        pass


    def test_save_brain(self):
        pass


    def test_load_brain(self):
        pass



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