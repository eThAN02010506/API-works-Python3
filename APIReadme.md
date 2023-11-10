

## Key Features

* Rank - Look up the toefl score and rank of specific person

* List - checks all the partcipants.
  


## How To Use

Here is a list of current API keys:

1. 060212
2. 060501

Then, use that API key to properly load these paths listed below.

Directions for using the API key are included in the Note at the bottom
```
# check for all participants
/class_pass_chance
```
```
# Get the stats of a specific participant from the list
/class_pass_chance/{participant_name}/fail_chance

# parameter {participant_name}: this is where you put your name of choice
```
```
# Get the age of the participant
/class_pass_chance/{participant_name}/age

# parameter {last_name}: this is where you put your name of choice
```

## Example:
```
http://10.6.20.246:8000/class_pass_chance/a/age?api_key=060212


# Will return with:

The participant a is 18 years old
```

‎
> **Note**
> 
>Be sure to end your route with the API key like this: ?api_key={API_KEY}
>* If you do not use one of the API keys provided, the API will not work.


