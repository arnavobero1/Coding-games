//Importing the necessary libraries using #include
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int main()
{	
	//Initializing variables	
	int inputnum = 0;
	int num = 0;
	int numofguess;
	time_t t;
	
	//Initialization of random number
	srand((unsigned) time (&t));
	//Getting the random number
	num = rand() % 51;

	//Printing out the messages to make the game understandable for user.
	printf("This is a guessing game.\n");
	printf("I have chosen a number between 0 and 100.");
	printf("\nGuess the number!\n");

	//For loop is used to help perform the procedure till the user guesses the number or runs out of number of tries.
	for(numofguess = 5;numofguess>0;--numofguess)
	{
		//Telling the user how many tries he/she has left.
		printf("You have %d tr%s.",numofguess,numofguess == 1?"y":"ies");
		printf("\nEnter a guess : ");
		scanf("%d",&inputnum);

		//If else statements are used to meet the required condition. 
		if(inputnum==num)
		{
			printf("\nYou guessed the number! Well done.");
			break;
		}
		else if(inputnum < 0 || inputnum > 50)
		{
			printf("\nWhoops! Its out of range.\n");
		}
		else if(inputnum > num)
		{
			printf("\nIts lower than that!\n");
		}
		else if(inputnum < num)
		{
			printf("\nIts greater than that!\n");
		}
	}
	return 0;
}