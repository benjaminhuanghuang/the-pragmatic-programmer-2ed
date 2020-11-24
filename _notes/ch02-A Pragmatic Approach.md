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

## Topic 14. Domain Languages 

## Topic 15. Estimating 