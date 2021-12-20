from random_brain import random_brain
import os
import unittest


class TestStringMethods(unittest.TestCase):

    # test if we can import a whole dir of models
    def test_import_dir(self):
        brain = random_brain()
        import_path = os.path.join(os.getcwd()+ '/testing_models') 
        brain.import_models(model_path=import_path)
        look_a_like = os.listdir(os.path.join(os.getcwd() + '/testing_models'))
        look_a_like.remove('sub')
        self.assertEqual(brain.show_brain(), look_a_like)

    # test if we can import a single model
    def test_import_single(self):
        brain = random_brain()
        import_path = os.path.join(os.getcwd() + '/testing_models/eeg_eye_state.h5') 
        brain.import_models(model_path=import_path)
        self.assertEqual(brain.show_brain(), ['eeg_eye_state.h5'])

    # import a single item and a whole dir
    def test_import_single_and_dir(self):
        brain = random_brain()
        # path 1
        import_path = os.path.join(os.getcwd() + '/testing_models') 
        brain.import_models(model_path=import_path)
        # path 2
        import_path = os.path.join(os.getcwd() + '/testing_models/eeg_eye_state.h5') 
        brain.import_models(model_path=import_path)
        # path 2 with another dir
        import_path = os.path.join(os.getcwd() + '/testing_models/sub') 
        brain.import_models(import_path)

        # what our model should hold
        look_a_like = os.listdir(os.path.join(os.getcwd() + '/testing_models'))
        look_a_like.remove('sub')
        look_a_like.append('eeg_eye_stateCopy.h5')

        self.assertEqual(brain.show_brain(), look_a_like)

    # make sure we can clear the brain
    def test_clear_brain(self):
        # clear single item
        brain = random_brain()
        import_path = os.path.join(os.getcwd() + '/testing_models')
        brain.import_models(model_path=import_path)
        brain.clear_brain(['eeg_eye_state.h5'])
		
        items = os.listdir(os.path.join(os.getcwd() + '/testing_models'))
        items.remove('eeg_eye_state.h5')
        items.remove('sub')
        self.assertEqual(brain.show_brain(), items)

        # clear whole brain
        brain.clear_brain()
        self.assertEqual(brain.show_brain(), [])


    # make sure we can save and load the brain
    # def test_save_load_brain(self):
    #     brain = random_brain()
    #     import_path = os.path.join(os.getcwd() + '/testing_models')
    #     brain.import_models(model_path=import_path)
    #     file_path = os.path.join(os.getcwd() + '/test.pkl')
    #     print(file_path)

    #     # save
    #     brain.save_brain(file_path)
    #     self.assertEqual(os.path.isfile(file_path) , True)

    #     # clear and load
    #     brain.clear_brain()
    #     brain.load_brain(file_path)

    #     look_a_like = os.listdir(os.path.join(os.getcwd() + '/testing_models'))
    #     look_a_like.remove('sub')

    #     self.assertEqual(brain.show_brain(), look_a_like)


    # not sure of how to do tests here



    def test_classification(self):
        brain = random_brain()

        import_path = os.path.join(os.getcwd() + '/testing_models')
        brain.import_models(model_path=import_path)

        import pandas as pd
        from scipy.io.arff import loadarff
        from keras.utils import np_utils
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        import numpy as np
        from sklearn.metrics import classification_report
        

        home = os.getcwd()
        data_frame=home+'/testing_data/EEG Eye State.arff'
        raw_data = loadarff(data_frame)
        df_data = pd.DataFrame(raw_data[0])


        # Preprocess Data
        # split into data and targets
        data_targets=df_data.iloc[:,-1]
        data=df_data.iloc[:,:-1]

        # data normalization with sklearn z-score
        scaler = StandardScaler()
        scaler.fit(data)
        data = scaler.transform(data)

        # convert targets into 1 or 0
        data_targets=np_utils.to_categorical(data_targets, num_classes=2)

        # split the data
        xTrain, xTest, yTrain, yTest = train_test_split(data, data_targets, test_size = 0.1)


        # run predictions
        votes = brain.predict(xTest)

        # find the mean of votes (should add this natively into brain)
        votes = votes.mean(axis=0)
        prediction = np.where(votes > 0.5, 1, 0) # convert into 0 or 1
        # print(prediction)
        # print(yTest)

        # generate report
        report = classification_report(yTest, prediction)
        print(report)



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