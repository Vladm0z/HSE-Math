% BUDGETING
% There are is a set of projects can be invested by the firm
% over time period. Each of the projects brings a reward in each period
% once chosen. The objective is to maximizes the total net present
% value of the initial investment and final revenue. The model enables
% restrictions on selection of projects, such as that one project must
% be chosen among a set of mutually exclusive projects. The solution
% to the model indicates the projects that will be selected and when
% to invest in them. Each period has a constraint on the minimum balance.

%DATA 
% Time periods
int: T;
% Number of 
int: NumMustTakeOne;
% Initial balance
float: InitBal;

%Discount rate (interest rate)
float: Rate;
%List of projects 
enum Projects;
% Set of projects to choose only one from them
set of Projects: MustTakeOne;
% Setup cost of projects 
array[Projects, 1..T] of float: SetupCost; 

% Rewards (= Revenue - Cost) of projects in each period 
array[Projects, 1..T] of float: Reward;    

% Minimum balance at the end of each period
array[1..T] of float: MinBal;

%TEST DATA 
var int: x;
solve satisfy;
