% STUFFING
% A restaurant runs from 8am - 8pm on Monday - Friday. Each working day is
% divided into three 4-hr shifts:
% Breakfast:  8am - 12pm
% Lunch:     12pm -  4pm
% Dinner:     4pm -  8pm

% Each shift demands three types of personnel: cook, cashier, and cleaner.
% Each of its personnel is capable of performing a subset of these tasks.
% If scheduled, each person works 8 hours a day (2 shifts in this case), 
% and prefers the shifts to be consecutive. Also, if she works on a night shift, she
% prefers not to work on the morning shift the next day.

% Objective:
% The first criterion is to find a schedule with minimal number of unfilled slots. 
% Second criterion is balancing personnel workload: min (Max shifts of person) - (Min shifts of person)
% We want to find schedule with the best second criterion over all schedules which are optimal subject to the first criterion. 
 

%DATA
%Total # of shifts in a day
int: Totalshifts;
%Total # shifts a person should work in a day
int: Nbshifts; 
%Type of skills required
enum Skills;    
%Set of work days 
enum Weekdays;  
%Set of personnel
enum People;    
%Number of personnel of skill requested at day and shift
array[Weekdays, 1..Totalshifts, Skills] of int: Req;
% 0-1 matrix HasSkill[i,j] defines if person i have skill s
array[People, Skills] of 0..1: HasSkill;         

% TEST DATA  
var int: x;
solve satisfy;    
