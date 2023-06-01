Dev: *Cameron Allen*  
Date: *5.31.2023*

# Assignment 07 – Files & Exceptions #

## Intro ##
Assignment 7 was given as an open playing field to us students. After watching the lecture, we were left to our own devices to conduct more research on the topics of file pickling and ‘try-except’ statements. Then we had to create a script that demonstrated the use of these topics from scratch. 

## Pickling ##
Picking in programming is storing data to a file in bytes rather than text. One result of doing this is if you were to open the saved file you made you won’t be able to read it because it was saved as binary which is mostly un-readable to a human compared to that of a text file. A benefit to pickling your files is quick and easy serialization of data. This I hope will get explained further in our course as my understanding is limited.

Shown in Figure 1, you can even save you binary file as any extension, as long as the program that pickled it (Python in our case) is also unpickling the file, the data will be there. 

Figure 1: Saving File with extension .pkl []

## Try & Except ##
Try-except statements are like if-then statements but are more utilized toward error handling.

In figure 2 you’ll see I use a try-except statement on line 30. Here I am asking the program to ‘try’ to read data from a file. But if the file that the program is trying to read the ‘except’ statement comes into effect and provide the message ‘No Appdata.pkl found, continue making list’.

There are many different types of exceptions for the programmer to use to narrow down all the possible errors that the user may cause. This way the program can provide various feedback to the user depending on what the user did. 

Figure 2: Try-except statement starting on line 30. []

## Summary ##
There is a real difference in programming when you have existing code versus starting from scratch. But Professor Root is building us up as programmers and enabling us to strive outside of the class.

In our future programming career, we will undoubtedly need to learn a new feature or function of coding and this lesson just emphasizes how easy it is to go out and research and learn on our own to complete our coding whatever the objective may be. 

