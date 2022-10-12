1. In the sense of machine learning, what is a model? What is the best way to train a model?

Ans: A ML model acts like program/processer to identify few pattrens which was trained and tested with given data to predict future data.Best way to make model is not to over/under fit the model and following the standareds like normal ml process like data cleaning,scaleing,model selection, training testing or corss validatoing so on.

2. In the sense of machine learning, explain the "No Free Lunch" theorem.

Ans: It is abbreviated as NFL or NFLT, is a theoretical finding that suggests all optimization algorithms perform equally well when their performance is averaged over all possible objective functions.

*In Simple Words “No Free Lunch” theorem means we can’t rely on one model to be best of all models* . We have to understand data properly and make use of ML understanding and make use of models to find best out of it.

3. Describe the K-fold cross-validation mechanism in detail.

Ans: In K-fold cross validation, total data is splited into **k**<sup>th</sup> is subsets randomly.There will k-iterations go on where **1/k<sup>th</sup>** subset of Data is always set aside for testing the data and reamaining subsets are used for training, evaluating and discarding the model. At the end of all the iterations, average of all the evaluation scores is taken and used as output.

4. Describe the bootstrap sampling method. What is the aim of it?

Ans: The bootstrap method is a statistical technique for estimating quantities about a population by averaging estimates from multiple small data samples.Samples are constructed by drawing observations from a large data sample one at a time and returning them to the data sample after they have been chosen. This allows a given observation to be included in a given small sample more than once. This approach to sampling is called sampling with replacement.

5. What is the significance of calculating the Kappa value for a classification model? Demonstrate how to measure the Kappa value of a classification model using a sample collection of results.

Ans: Kappa value or Cohen's Kappa coefficient is an evaluation metric for classification models. Its significance as an evaluation metric is that it can be used to evaluate multi class classification models and also works on models trained on imbalanced datasets(scores like accuracy scores fail for imbalanced datasets).

In simpler words It basically tells you how much better your classifier is performing over the performance of a classifier that simply guesses at random according to the frequency of each class. Cohen's kappa is always less than or equal to 1. Values of 0 or less, indicate that the classifier is useless Cohen suggested the Kappa result be interpreted as follows: values ≤ 0 as indicating no agreement and 0.01–0.20 as none to slight, 0.21–0.40 as fair, 0.41– 0.60 as moderate, 0.61–0.80 as substantial, and 0.81–1.00 as almost perfect agreement.

6. Describe the model ensemble method. In machine learning, what part does it play?

Ans: Ensemble methods or ensemble machine learning models are models where more than one models are being used spontaneously to produce better results than individually trained models.

7. What is a descriptive model's main purpose? Give examples of real-world problems that descriptive models were used to solve.

Ans: A descriptive model is used for tasks that would benefit from the insight gained from summarizing data in new and interesting ways. As opposed to predictive models that predict a target of interest, in a descriptive model, no single feature is more important than any other. In fact, because there is no target to learn, the process of training a descriptive model is called unsupervised learning.

8. Describe how to evaluate a linear regression model.

Ans: Evaluation of a linear regression model can be done using R-square. R square is calculated as the sum of squared errors in predictions made, divided by summation of all sum of squares. R square measures how much of the change in target variable can be explained by the linear regressor. Its value ranges from 0 to 1 where 0 means poor performance and 1 means good. Some other techniques which can be used to evaluate a linear regression model are:

Mean Square Error(MSE)/Root Mean Square Error(RMSE) Mean Absolute Error(MAE)

9.Distinguish :

Ans:

**Descriptive vs. predictive** models Descriptive models are built to identify trends and underlying patterns. Predictive models are built to predict a dependent variable value. Most of descriptive models are built using unsupervised machine learning. Most of predictive models are built using classification and regression models. Example for descriptive model: Finding why consumers are engaging more with a social media post. Example for predictive model: Predicting the chances of cancer in a patient.

**Underfitting vs. overfitting** The model Underfitting is a situation arising when the hypothesis is way too simple, or when the machine learning model is way too simple to produce good results. Overfitting is a situation arising when the hypothesis is way too complex, or when the machine learning model is way too complex to produce good results. Underfitting causes a model to produce poor results due to heavily simplified algorithm reacting lightly to changes in the unseen data for independent variables from the training data. Overfitting makes a model produce poor results due to slightest variations in the unseen data for independent variables from the training data Underfitting is also called High Bias. Overfitting is also called High variance.

**Bootstrapping vs cross-validation** Boostrap sampling is a method of sampling in which the repeated sampling is done with replacement using a data D in random draws over which machine learning models are trained for better performance. Cross validation is a method used to check the efficacy of the machine learning model on test data. End goal of bootstrapping is to reduce overfitting and increase performance. End goal of cross validation is only to produce test scores to check efficacy of model Bootstrapping is best employed in Random Forest Classifier. Cross Validation is best employed using K-fold cross validation technique.

10. Make quick notes on:

**LOOCV or Leave One Out Cross Validation** is a form of K-fold cross validation where only one observation is left out for validation purpose while the rest of the data is used for model training each iteration. It is computationally taxing and should only be used for data with low dimensionality.

**F-measurement or F-score** is the Harmonic mean of Precision score and recall score. It is formulated as 2 (pr re)/pr +re where pr is precision score and re is recall score.

**Width of the silhouette** is the Estimate of average inter cluster distance to give efficiency/performance of cluster algorithms. It can also be defined as how identical/similar a data point 'x' is to the data points inside the cluster to which x is assigned(value ranges from -1(bad) to 1(good)).

**Receiver Operating Characteristics curve** is the curve plotted between True Positive Rate and False Positive Rate and is used to find the area under the curve for ROC-AUC score for binary classification evaluation. True Positive Rate and False Positive Rate are calculated for different thresholds values where thresholds take values starting from the highest probability scores assigned to data points and goes up to the lowest probability score.
