# Lela

### [You can use Lela by clicking here.](https://lela-dietician.herokuapp.com)

## ABSTRACT
This application provides the user with a complex algorithm which can provide the user with a diet plan based on his/her characteristics like height, weight, BMI etc. In Today's busy life everyone can just dream of having a proper balanced diet. A balanced diet is important because your organs and tissues need proper nutrition to work effectively. Without good nutrition, your body is more prone to disease, infection, fatigue, and poor performance. Children with a poor diet run the risk of growth and developmental problems and poor academic performance, and bad eating habits can persist for the rest of their lives. At the core of a balanced diet are foods that are low in unnecessary fats and sugars and high in vitamins, minerals, and other nutrients. The following food groups are essential parts of a balanced diet. Calories play a vital role in our growth and energy. A good diet can help you manipulate calorie intake based on your requirements. The proposed application will provide the user with a user-friendly User-Interface where they can create an account, manage their account and get the diet by the click of just one button. This webpage will save a lot of user’s time by not actually visiting a dietitian and getting everything done on their phone/laptop.

## INTRODUCTION
Smart dietitian application is a web page that provides a generic diet to its users. It acts as a diet consultant similar to a real Dietitian. This system acts in a similar way as that of a dietitian. A person in order to know his/her diet plan needs to give some information to the dietitian such as its body type, weight, height and working hour details. A similar way this system also provides the diet plan according to the information entered by the user. The system asks for all his data from the user and processes it to provide the diet plan to the user. Thus, the user does not need to visit any dietitian which also saves time and the user can get the required diet plan in just a click. The system will give more accurate results as it accepts the data entered by the user and processes it depending on some metrics already known to the application on the basis of which a diet plan is generated and asks the user if the user accepts the diet plan. The Application also has a card for preparing healthy food at home and also provides all the general knowledge and some amazing facts on our foods. This Application can be a vital part of a user if he wishes to maintain his health and body perfectly and follow the diet plan & the workout plan provided to the user.

## DESIGN & IMPLEMENTATION.
In this, we designed the overview and implementation of the project was discussed. The modules discussed to be implemented are listed with some details.  
* Home page.
* Recipes.
* My diet.
* About me.
In the Design Process, we first designed the flow of events in which the application would work, which can be seen in the flowchart below. 

The Formulas used for calculating the BMI (Body mass Index) and to calculate the total calories to intake was found on the internet on some research. 
Formula for BMI: BMI = Weight / (Height*2/100) 
Where weight is in kilograms, height is in centimeters. 
Formula for calculating Maintenance Calories: 
Calories = (Weight * 22) * Activity Multiplier 
Where weight is in kilograms, activity multiplies refers to the amount of activity done. 

### Calculating Diet & Providing Diet: 
The Maintenance calories of the users has to be calculated on the basis of his height, weight, and age. The Maintenance Calories are calculated with the help of the formula given above, once the calories are calculated then the system decides if the user is in an under-weight, healthy or overweight category based on his BMI. Then, the user is  suggested which type of diet program he / she should start, the user is still given the option to opt for the diet category like, gain weight, maintain weight or lose weight. Based on the category selected the diet is provided by the application to the user. The diet is calculated using the calories tracker with the use of NLP and basic for and if statements. We have added the contacts of dieticians if any user want to consult a physical dietitian if he / she has some issues with the diet provided or has some food allergies or irritations, for example some people are lactose intolerant, so the dietitian will suggest some replacement for the lactose-based products in the diet. in a day; it ranges from 1.2 for moderate work to 2.0 for extreme work done. But in the future scope, we add all the details of allergies and make our website more user friendly.

### Acknowledgements
I would like to thank [Chidhambararajan R](https://github.com/TheSeriousProgrammer) and [Dhiraj Suthar](https://github.com/Dhiraj5789) for helping me in this project.
