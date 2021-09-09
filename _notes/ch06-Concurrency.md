# Concurrency

Concurrency is when the execution of two or more pieces of
code act **as if** they run at the same time. Parallelism is when
they **do** run at the same time.


To have concurrency, you need to run code in an environment
that can **switch** execution between different parts of your code
when it is running. This is often implemented using things such
as **fibers, threads, and processes**.

To have parallelism, you need **hardware** that can do two things
at once. This might be multiple cores in a CPU, multiple CPUs
in a computer, or multiple computers connected together.

## Topic 33 Breaking Temporal Coupling
- Tip 56 Analyze Workflow to Improve Concurrency


## Topic 34 Shared State Is Incorrect State

- Tip 56 Analyze Workflow to Improve Concurrency

- Tip 57 Shared State Is Incorrect State

- Tip 58 Random Failures Are Often Concurrency Issues


## Topic 35 Actors and Processes
An actor is an independent virtual processor with its own local (and
private) state.

A process is typically a more general-purpose virtual processor,
often implemented by the operating system to facilitate
concurrency.


- Tip 59 Use Actors For Concurrency Without Shared State

## Topic 36 Blackboards

- Tip 60 Use Blackboards to Coordinate Workflow

