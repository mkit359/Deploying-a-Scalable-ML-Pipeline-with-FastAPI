# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
**Model Date:** 2025 July 

**Model Type:** Traing model utilizing RandomForestClassifer for Machine Learning
**Framework:** Scikit-learn
**Version:**  1.0.0
**Owner:** Megan Kitner, mrob359@wgu.edu

## Intended Use
To predict whether a person would be making over $50,000 a year based off of census data variables, such as age, marital-status, and gender, while using a scalable machine learning pipeline.

## Training Data
**Data Provided by:** 
Kohavi, R. (1996). Census Income [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5GP7S.

**Project Supported by:** Udacity, Part of Accenture, Machine Learning DevOps
**Project Kit Provided:** https://github.com/udacity/Deploying-a-Scalable-ML-Pipeline-with-FastAPI.git

**Training/Testing:** Eighty percent of the data was used for training while 20 was utilized for a test set

## Evaluation Data
Twenty percent of the data was used for evaluatating.

## Metrics
**Precision:** 0.7427
**Recall:** 0.6302
**F1:** 0.6818

## Ethical Considerations
While this dataset is publicy accesible for everyone, it may contain biases that were present in 1994 when the Census data was collected. An example of this would be females being more likely to be stay at home wives, which would skew the data for income equality and could not be a good reporesentation if attempting to use this model for current day analysis. Personally identifiable information is not contained on this dataset, allowing those who participated to stay anonymous.  

## Caveats and Recommendations
This model would need to have the latest dataset utilized to be able to represent and make predictions based on the current population to avoid biases that are outdated. 
