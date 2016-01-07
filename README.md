# DegreEfficient

Get rid of your Academic Advisors! You can plan your own degree(s) with ease now.

Take all the courses you want to take, and as many per semester as you wish.
DegreEfficient will help you graduate as early as possible, keeping these preferences in mind.

## Usage

`python main.py filepath maxHrsPerSem`

`filepath` is the path to the (properly formatted) course list. `maxHrsPerSem` is the maximum number of credit hours per semester. 

## Format of Course List

A text file containing data in this format:

`CourseName: #CreditHours: PrereqName1, PrereqName2, ...`

## To do

 - [ ] Support for co-requisites (both weak and strict).
 - [ ] Support for courses that can't be taken before a given semester. 

## License

The MIT License (MIT)