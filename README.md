# Health and Fitness Recommendation System

## 🔍 Overview
This is a data-driven health recommendation tool that helps users improve their fitness by offering personalized advice based on their age, gender, weight, dream weight, heart rate, and workout intensity. The system provides insights, visualizations, and calorie predictions using simple ML.

## ✨ Features
- 📊 Analyzes user workout and health data
- 🧮 Calculates BMI and classifies intensity
- 🧠 Provides personalized weight recommendations (gain, lose, maintain)
- 🔥 Predicts calories burned using linear regression
- 📝 Interactive form to take user inputs
- 📈 Visualizes exercise and body data trends

## 🗃️ Dataset
We use a dataset with the following columns:
- ID
- Exercise
- Dream Weight
- Actual Weight
- Age
- Gender
- Duration (in minutes)
- Heart Rate
- BMI
- Weather Conditions
- Exercise Intensity

## ⚙️ System Workflow
1. Load dataset and clean missing data
2. Analyze BMI and Intensity categories
3. Train calorie-burn prediction model
4. Generate user-specific advice
5. Save recommendations to a CSV file

## 🧪 Setup Instructions

1. Clone this repository or download files
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open and run the notebook:
   ```bash
   jupyter notebook fitness_recomendation_system.ipynb
   ```

## 🛠️ Usage
- Modify the last section of the notebook to input your own data.
- The system will output a recommendation and estimated calories burned.
- You can save the results to CSV using the provided code.

## 📌 Example User Input
```python
recommend_fitness(age=24, gender='Male', weight=70, dream_weight=65, duration=30, heart_rate=140, bmi=23.4, exercise_intensity='Moderate')
```

## 🖼️ Screenshots
- 📷 Dataset preview table
- 📷 Dream weight histogram
- 📷 BMI or Heart rate vs Calories plot
- 📷 Output recommendation table


