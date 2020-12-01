There are certain tips and tricks that apply at all levels of software development.

## Topic 8. The Essence of Good Design 
Easier to Change
- decoupling: isolating concerns and make each easier to change.
- single responsibility principle : change in requirements is mirrored by a change in just one module.

deliberately asking yourself "did the thing I just did make the overall system easier
or harder to change?"

try to make what you write replaceable

develop instincts by taking daily notes

## Topic 9. DRY（Don’t Repeat Yourself）–The Evils of Duplication 

DRY is about the duplication of knowledge, of intent

Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

- Duplication in code, in code and comments, in data, data srouce, API, Interdeveloper

– Not All Code Duplication Is Knowledge Duplication

## Topic 10. Orthogonality 
signify a kind of independence or decoupling.
Two or more things are **orthogonal** if changes in one do not affect
any of the others. 
The database code will be orthogonal to the user interface

There is no local fix in Nonorthogonal System.

2 major benefits in orthogonal systems: 
- increased productivity, M × N things
- reduced risk

How to
- Design
- Toolkits and Libraries
- Coding: decoupled, avoid gobal data, advoid similar function
- Testing:  orthogonal system is easier to test


It’s time to refactor.


## Topic 11. Reversibility 
Change

flexibility in code, architecture, deployment, and vendor integration.

## Topic 12. Tracer Bullets 
when you’re building something that hasn’t been built before. We use the term tracer bullet development to visually illustrate the need for immediate feedback under actual conditions with a moving goal

very first tracer bullet is simply create the "hello world" project

## Topic 13. Prototypes and Post-it Notes 
The reason: to analyze and expose risk, and to offer chances for correction at a
greatly reduced cost. 

Anything you aren’t comfortable with. You can prototype:
- Architecture
- New functionality in an existing system
- Structure or contents of external data
- Third-party tools or components
- Performance issues
- User interface design

Prototyping is a learning experience

what details can you ignore
- Correctness
- Completeness
- Robustness
- Style

architectural prototype:
- Are the responsibilities of the major areas well defined and appropriate?
- Are the collaborations between major components well defined?
- Is coupling minimized?
- Can you identify potential sources of duplication?
- Are interface definitions and constraints acceptable?
- Does every module have an access path to the data it needs during execution?

Remember: prototype is disposable code

## Topic 14. Domain Languages 
The language of the problem domain may also suggest a programming solution.

The downside of internal domain languages is that you’re bound by the syntax
and semantics of that language. 
External languages have no such restrictions.


## Topic 15. Estimating 

When you’re coding, you’ll be able to know which subsystems need optimizing and which ones can be left alone.

Where Do Estimates Come From?
- Understand What’s Being Asked
- Build a Model of the System
- Break the Model into Components
- Give Each Parameter a Value 
- Calculate the Answers
- Keep Track of Your Estimating Prowess

ask someone who’s already done it.


Program Evaluation Review Technique, or PERT.
Every PERT task has an optimistic, a most likely, and a pessimistic estimate.
The tasks are arranged into a dependency network, and then you use some
simple statistics to identify likely best and worst times for the overall project.

Repeating the following steps with very thin slices of functionality:
- Check requirements
- Analyze risk (and prioritize riskiest items earlier)
- Design, implement, integrate
- Validate with the users

Practice
Start keeping a log of your estimates. Track how accurate you turned out to be. If your error was greater than 50%, try to find out where your estimate went wrong.
