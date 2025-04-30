import joblib
import pandas as pd

model = joblib.load("rf_model.pkl")

# Create sample (hardcode)
sample = pd.DataFrame([{
    "Age": 30,
    "BusinessTravel": 1,
    "DailyRate": 800,
    "Department": 2,
    "DistanceFromHome": 5,
    "Education": 3,
    "EducationField": 1,
    "EnvironmentSatisfaction": 2,
    "Gender": 1,
    "HourlyRate": 70,
    "JobInvolvement": 3,
    "JobLevel": 2,
    "JobRole": 4,
    "JobSatisfaction": 3,
    "MaritalStatus": 2,
    "MonthlyIncome": 4500,
    "MonthlyRate": 13000,
    "NumCompaniesWorked": 2,
    "OverTime": 1,
    "PercentSalaryHike": 15,
    "PerformanceRating": 3,
    "RelationshipSatisfaction": 3,
    "StockOptionLevel": 1,
    "TotalWorkingYears": 6,
    "TrainingTimesLastYear": 3,
    "WorkLifeBalance": 2,
    "YearsAtCompany": 3,
    "YearsInCurrentRole": 2,
    "YearsSinceLastPromotion": 1,
    "YearsWithCurrManager": 2
}])

pred = model.predict(sample)

if pred[0] == 1:
  print("Karyawan berpotensi resign")
else:
  print("Karyawan tidak berpotensi resign")