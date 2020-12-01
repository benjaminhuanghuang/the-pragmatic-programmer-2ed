
## Topic 16. The Power of Plain Text 

keep the basic tool set sharp and ready to use.

good reasons:
- Insurance against obsolescence
- Leverage existing tools
- Easier testing


## Topic 17. Shell Games 
Using GUI, You won’t be able to automate common tasks
- Setting color themes
- Configuring a prompt
- Aliases and shell functions
```
  alias apt-up='sudo apt-get update && sudo apt-get upgrade'
```
- Command completion



## Topic 18. Power Editing 
Do everything without using a mouse/trackpad

Consciously look for opportunities to use your new superpower, ideally many times a day

Find extensions of the editor


## Topic 19. Version Control 

## Topic 20. Debugging 
Beware of myopia when debugging. Resist the urge to fix just the symptoms

Always try to discover the root cause of a problem, not just this particular appearance of it.

It doesn’t make sense to waste time trying to find a problem that the computer could find for you


- You may need to interview the user who reported the bug in order to
gather more data than you were initially given.

- Artificial tests don’t exercise enough of an application. You must brutally test both boundary conditions and realistic end-user usage patterns. You
need to do this systematically


The best way to start fixing a bug is to make it reproducible
we want a bug that can be reproduced with a single command.

isolate the circumstances that display the bug

Get a copy of the dataset and feed it through a locally running copy of the app


Even if the problem does lie with a third party, you’ll still have to eliminate your code before submitting the bug report.

sit down and read the documentation 

If it took a long time to fix this bug, ask yourself why. Is there anything you
can do to make fixing this bug easier the next time around

amend the unit or other tests so that they would have caught it

Debugging Checklist
• Is the problem being reported a direct result of the underlying bug, or
merely a symptom?
• Is the bug really in the framework you’re using? Is it in the OS? Or is it
in your code?
• If you explained this problem in detail to a coworker, what would you
say?
• If the suspect code passes its unit tests, are the tests complete enough?
What happens if you run the tests with this data?
• Do the conditions that caused this bug exist anywhere else in the system?
Are there other bugs still in the larval stage, just waiting to hatch?

## Topic 21. Text Manipulation 
Unix shell awk and sed
Python or Ruby


converts each .yaml file into a corresponding .json file

Change camelCase names for variables to snake_case


## Topic 22. Engineering Daybooks 
- It is more reliable than memory
- It gives you a place to store ideas that aren’t immediately relevant to the
task at hand
- It acts as a kind of rubber duck

