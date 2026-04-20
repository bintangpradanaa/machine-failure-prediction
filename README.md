# Machine Failure Prediction in Manufacturing Industry

## Resources
- 📊 [Presentation Deck](https://drive.google.com/file/d/1SeO9nRQNwcRTNMjpwA3B7bz2GcVhI3fj/view?usp=sharing)  
- 🚀 [Model Deployment](https://machine-failure-prediction-bintangpradanaa.streamlit.app/)

## Project Overview
In a manufacturing environment, unexpected machine failures can lead to production downtime, increased operational costs, and reduced efficiency.

As a **Data Scientist in a manufacturing company**, I developed a predictive maintenance solution using machine sensor data to detect potential failures early and support proactive maintenance decisions.

## Business Understanding
Unplanned machine breakdowns can significantly impact production performance. To reduce this risk, the company aims to implement a **predictive maintenance strategy** based on sensor data analysis. By identifying early patterns of failure from machine sensor readings, maintenance can be scheduled proactively, reducing downtime and optimizing operational costs.

## Objective
- Maximize **Recall** to ensure most machine failures are correctly detected early  
- Optimize **F1 Score** to maintain balance between precision and recall  
- Minimize both:
  - Missed failure detection (false negatives)
  - Unnecessary maintenance actions (false positives)

## Key Results
- **Best Model:** Optimized K-Nearest Neighbors (KNN)
- **Recall Score:** 94.5%
- **F1 Score:** 93.21%

## Conclusion
- The optimized KNN model successfully detects the majority of machine failures with high accuracy while maintaining a balanced error rate.
- This makes it a reliable solution for early failure detection and preventive maintenance planning in manufacturing operations.

## Recommendations
- Use **Optimized KNN** as the primary production model for failure prediction  
- Integrate the model into a real-time monitoring system for early alerts  
- Continuously retrain the model with new sensor data to maintain performance accuracy  
- Develop a simple **dashboard interface** to visualize predictions for technical teams  
- Provide training for maintenance teams to ensure proper response to failure alerts  
