# Predict-Titanic-Survival
This is a logistic regression algorithm that predicts whether or not someone on the Titanic would've survived. The code is written in Python and uses the Sikit-Learn library.

# Data cleaning
The data was split into multiple csv files which made it neccesary to combine them into one merged csv file. Column "Sex", which referred to the gender of that individual, had to be converted to an integer, which is either be a 0(female) or a 1(male). Additionally, some of the data for the column "age" was missing. In order to fix that problem, I took the mean value of the "age" column and input that value into any empty positions. 

# Algorithm training
Columns such as "Cabin", "Embarked" or "Ticket" were purposely ignored during this process, as these columns had very little to no correlation to the expected output. For example, where you got on the Titanic would have very little correlation to whether or not you survived. However, your gender and age would have a very strong correlation to the output, as women and children would be the first ones allowed on the lifeboats. 

# Conclusion
The accuracy of this algorithm was 85.49%.
