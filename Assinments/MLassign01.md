1. What does one mean by the term "machine learning"?

   *Machine learning is defined by programming machine to learn from data to solve a specific problem.And also a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy*

2. Can you think of 4 distinct types of issues where it shines?

   *Machine learning is great for problems whose solution requires a great deal of work or a long list of rules, complex problems that are hard to get a solution of using a traditional method, fluctuating environments and getting insights about complex problems and large data.It is everywhere like on  Social Media. Transportation and Commuting. Products Recommendations. Virtual Personal Assistants. Self Driving Cars. Dynamic Pricing. Google Translate and so on.*

3. What is a labeled training set, and how does it work?

   *Labeled training set is a set of training data which has a solution to the problem or task (a.k.a. label)*.A part (60-80% mostly) of data is labeled as training set from toatl(100%) available data to train the model

4. What are the two most common supervised tasks?

   *Two most common supervised tasks are classification and regression.*

5. Can you think of four examples of unsupervised tasks?

   *Four common unsupervised tasks inclused clustering, visualization, dimensionality reduction , and association rule learning.*

6. State the machine learning model that would be best to make a robot walk through various unfamiliar terrains?

   *The best Machine Learning algorithm to allow a robot to walk in unknown terrain is Reinforced Learning, where the robot can learn from response of the terrain to optimize itself.*

7. What type of algorithm would you use to segment your customers into multiple groups?

   *The best algorithm to segment customers into multiple groups is either supervised learning (if the groups have known labels) or unsupervised learning (if there are no group labels).*

8. Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem?

   *Spam detection is a supervised learning problem because the labels are known (spam or no spam).*

9. What is an online learning system?

   *Online learning system is a learning system in which the machine learns  as data is given in small streams continuously.*

10. What is out-of-core learning system?

    *Out-of-core learning system is a system that can handle data that cannot fit into your computer memory. It uses online learning system to feed data in small bits.*

11. What kind of learning algorithm makes predictions using a similarity measure?

    *Learning algorithm that relies on a similarity measure to make predictions is instance-based algorithm.*

12. What's the difference between a model parameter and a hyperparameter in a learning algorithm? 

    *Model parameter determines how a model will predict given a new instance; model usually has more than one parameter (i.e. slope of a linear model). Hyperparameter is a parameter for the learning algorithm, not of a model.*

13. What are the criteria that model-based learning algorithms look for? What is the most popular method they use to achieve success? What method do they use to make predictions?
    
    *Model based learning algorithm search for the optimal value of parameters in a model that will give the best results for the new instances. We often use a cost function or similar to determine what the parameter value has to be in order to minimize the function. The model makes prediction by using the value of the new instance and the parameters in its function.*

14. Can you name four of the most important Machine Learning challenges? 

    *Four main challenges in Machine Learning include overfitting the data (using a model too complicated), underfitting the data (using a simple model), lacking in data and nonrepresentative data.* 

15. What happens if the model performs well on the training data but fails to generalize the results to new situations? Can you think of three different options?

    *If the model performs poorly to new instances, then it has overfit on the training data. To solve this, we can do any of the following three: get more data, implement a simpler model, or eliminate outliers or noise from the existing data set.*

16. What exactly is a test set, and why would you need one?

    *Test set is a set that you test your model (fit using training data) to see how it performs. Test set is necessary so that you can determine how good (or bad) your model performs.*

17. What is a validation set's purpose?

    *Validation set is a set used to compare between different training models.*

18. What precisely is the train-dev kit, when will you need it, how do you put it to use?

    *rank the models in term of their accuracy and helps us decide which model to proceed further with. Using Dev set we rank all our models in terms of their accuracy and pick the best performing model.* 

19. What could go wrong if you use the test set to tune hyperparameters?

    *it's like training the model with 100% of the data or more likely overfitting it !*
