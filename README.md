## Wordle Solver

The aim is to make an algorithm that solves wordle in a pretty optimal way, it need not be the most optimal way. This will be run and tested on my own implementation of wordle.

The wordle implementation will use the standard rules - 6 attempts, 5 letter words. The main thing which can make it slightly annoying is the word list that needs to be used. I looked into it, with [Matt Parker's Video](https://www.youtube.com/watch?v=_-AfhLQfb6w) being my starting point where he talked about how the original wordle has a finite list of word list. It was organised in two forms
- guess word list: Answers will not belong here but can be used for guesses
- answer word list: Answers will be from here and can also be used for guesses

I found the word list though a [GitHub Gist](https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93) post by 'cfreshman'. I have downloaded the list into the project. But the current wordle is operated by NY Times, and they also have a similar thing, but the issue according to 'cfreshman' is that the answer list is not definitive, and thus it can't be used on the actual thing. Thus I am downgraded the scope of the project from working on the NY Puzzle to just on my own implementation. I have also downloaded the NY Times most updated list to the project (2022-11-07, as after this date, the nature of the lists became more dynamic). 

As the NY times list is larger and belongs to the current iteration, I will mostly be using that dataset, though will allow use of original if the user ever wants to do so.