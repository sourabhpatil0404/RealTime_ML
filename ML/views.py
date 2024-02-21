from django.shortcuts import render

import pandas as pd
import pickle


def index(request):
    return render(request, 'index.html')

def classification(request):
    return render(request, 'classification.html')

def regression(request):
    return render(request, 'regression.html')

def predict(request, pk):
    if pk:
        data = request.POST

        class_data = {
            'Age': int(data['age']), 
            'RestingBP': int(data['resting_blood_pressure']), 
            'Cholesterol': int(data['cholesterol']), 
            'MaxHR': int(data['heart_rate']), 
            'Oldpeak': float(data['old_peak'])
        }
        df = pd.DataFrame(class_data, index=[0])


        scaler_pkl_file = "min_max_scaler.pkl"

        with open(scaler_pkl_file, 'rb') as file:
            scaler = pickle.load(file)

        scaled_data = scaler.transform(df)
    

        class_data = {
            'Age': scaled_data[0][0], 
            'RestingBP': scaled_data[0][1], 
            'Cholesterol': scaled_data[0][2], 
            'FastingBS': int(data['blood_sugar']), 
            'MaxHR': scaled_data[0][3], 
            'Oldpeak': scaled_data[0][4],
            'Sex_F': 1 if data['gender'] == 'F' else 0,
            'Sex_M': 1 if data['gender'] == 'M' else 0,
            'ChestPainType_ASY': 1 if data['chest_pain'] == 'ASY' else 0,
            'ChestPainType_ATA': 1 if data['chest_pain'] == 'ATA' else 0,
            'ChestPainType_NAP': 1 if data['chest_pain'] == 'NAP' else 0,
            'ChestPainType_TA': 1 if data['chest_pain'] == 'TA' else 0,
            'RestingECG_LVH': 1 if data['ecg'] == 'LVH' else 0,
            'RestingECG_Normal': 1 if data['ecg'] == 'Normal' else 0,
            'RestingECG_ST': 1 if data['ecg'] == 'ST' else 0,
            'ExerciseAngina_N': 1 if data['exercise_angina'] == 'N' else 0,
            'ExerciseAngina_Y': 1 if data['exercise_angina'] == 'Y' else 0,
            'ST_Slope_Down': 1 if data['peak_st'] == 'Down' else 0,
            'ST_Slope_Flat': 1 if data['peak_st'] == 'Flat' else 0,
            'ST_Slope_Up': 1 if data['peak_st'] == 'Up' else 0
        }
        final_df = pd.DataFrame(class_data, index=[0])


        model_pkl_file = "stacking_classifier_model.pkl"

        with open(model_pkl_file, 'rb') as file:
            model = pickle.load(file)

        prediction = model.predict(final_df)
        result = ''
        
        if prediction == [0]:
            result = 'No heart disease detected, everything is normal!'
        else:
            result = 'Heart disease detected!'
        
        return render(request, 'prediction.html', {'classification': True, 'result': result})
    
    else:
        data = request.POST

        class_data = {
            'cylinders': int(data['cylinders']), 
            'displacement': float(data['displacement']), 
            'horsepower': float(data['horsepower']), 
            'weight': int(data['weight']),
            'acceleration': float(data['acceleration']),
            'model year': int(data['year']),
            'origin': int(data['origin'])
        }
        df = pd.DataFrame(class_data, index=[0])

        model_pkl_file = "stacking_regressor_model.pkl"

        with open(model_pkl_file, 'rb') as file:
            model = pickle.load(file)

        prediction = model.predict(df)
        result = f'The estimated gas consumption is: {prediction[0]:.3f} MPG'

        return render(request, 'prediction.html', {'classification': False, 'result': result})


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
