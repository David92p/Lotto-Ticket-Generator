# This is the first step to start playing.

## The first branch will have inside a packcage called "lottoproject" which will take care of dividing the code:
### 1 [basic:](https://github.com/David92p/Lotto-Ticket-Generator/blob/learning-path-1/lottoproject/basic.py)
      - This script introduces a Class named BasicGame that checks and instantiates an object of 
        type city and form.

### 2 [game:](https://github.com/David92p/Lotto-Ticket-Generator/blob/learning-path-1/lottoproject/game.py)
      - This script introduces a sub-class named Lotto which instantiates a list of randomly drawn numbers.
      - The extraction of the numbers is performed on the basis of a logic of form transmitted 
        by the BasicGame Class.
        
### 3 [header:](https://github.com/David92p/Lotto-Ticket-Generator/blob/learning-path-1/lottoproject/header.py)
      - This script introduces the Header Class which takes care of printing a header 
        on the screen of our ticket.

### 4 [ticket:](https://github.com/David92p/Lotto-Ticket-Generator/blob/learning-path-1/lottoproject/ticket.py)
      - This script introduces the Ticket Class.
        It builds the body of our ticket using instances inherited from the Lotto Class.
         
### 5 [test:](https://github.com/David92p/Lotto-Ticket-Generator/blob/learning-path-1/lottoproject/test.py)
      - This is a momentary test script useful for testing our program.
