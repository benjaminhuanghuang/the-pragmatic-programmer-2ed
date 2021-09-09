# Ch05 Bend or Break

write code that bends and doesn’t break.

## Topic 28 Decoupling
- Tip 44 Decoupled Code Is Easier to Change

- Tip 45 Tell, Don’t Ask
This principle says that you shouldn’t make decisions based on
the internal state of an object and then update that object.
Doing so totally destroys the benefits of encapsulation


- Tip 46 Don’t Chain Method Calls

- Tip 47 Avoid Global Data

- Tip 48 If It’s Important Enough to Be Global, Wrap It in an API


## Topic 29 Juggling the Real World
Strategy for event:
    1. Finite State Machines (FSM)
    2. The Observer Pattern
    3. Publish/Subscribe
    4. Reactive Programming and Streams


## Topic 30 Transforming Programming
All programs transform data, converting an input into an output.
```
    $ find . -type f | xargs wc -l | sort -n | tail -5
```

- Tip 49 Programming Is About Code, But Programs Are About Data

- Tip 50 Don’t Hoard State; Pass It Around


## Topic 31 Inheritance Tax
- Tip 51 Don’t Pay Inheritance Tax
    - Interfaces and protocols
    - Delegation
    - Mixins and traits

- Tip 52 Prefer Interfaces to Express Polymorphism   
If a parent class has 20 methods, and the subclass wants to make use of just two of them, its objects will still have the other 18 just lying around and callable


- Tip 53 Delegate to Services: Has-A Trumps Is-A


- Tip 54 Use Mixins to Share Functionality

## Topic 32 Configuration

- Tip 55 Parameterize Your App Using External Configuration
    - Credentials for external services (database, third party APIs, and so on)
    - Logging levels and destinations
    - Port, IP address, machine, and cluster names the app uses
    - Environment-specific validation parameters
    - Externally set parameters, such as tax rates
    - Site-specific formatting details
    - License keys

