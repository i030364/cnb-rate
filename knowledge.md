# sandbox_resilience
Various Resilience snippets

# Python packages
* https://pypi.org/project/circuitbreaker/
* https://github.com/zacernst/circuit_breaker 
    * very simple implementation
    * no persistence
    * utilizing decorator and threading module (dependency is called in separate thread)
    * ASSESSMENT: not good for productive use
 * https://github.com/fabfuel/circuitbreaker
    * more sophisticated implementation
    * utilizing @wrap instead of threading
    * central monitor of all registered circuit breakers
    * no persistence 
    * ASSESSMENT: Can be taken over; but relays on exceptions not status codes
  * https://pypi.org/project/healthcheck/0.2/
    * Flash with wrapped health-checks - needs to review how is this implemented
