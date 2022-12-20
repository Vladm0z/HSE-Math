% FACTORY PLANNING

% An engineering factory makes seven products (PROD 1 to PROD 7) on the
% following machines: four grinders, two vertical drills, three horizontal drills, one
% borer and one planer. Each product yields a certain contribution to profit (defined
% as $/unit selling price minus cost of raw materials). These quantities (in $/unit)
% together with the unit production times (hours) required on each process are given.
% Targeted number of machines should be taken down for maintenance.
% We want to find the optimal mix of products to manufacture and sell subject to given production capacities and marketing
% limitations. 
% The objective function is: (Total profit from selling)  - (Hodling cost) 


%DATA
% Number of considered months
int: NbMonths;
% 2 eight hour shifts per day, 24 working days per month;
float: HoursMonth;
% Cost of holding inventory at the end of month
float: CostHold;
% Starting inventory
float: StartHold;
% Ending inventory
float: EndHold;
% Max amount of inventory at any month
float: MaxHold;

% products
enum Prod;
% machines
enum Process;

% profitProd[j] is profit per unit for product j
array[Prod] of float: ProfitProd;
% processProd[i,j] gives hours of process i required by product j
array[Process, Prod] of float: ProcessProd;
% marketProd[i,j] gives marketing limitation on product j for month i
array[1..NbMonths, Prod] of float: MarketProd;
% number of each type of machine
array[Process] of int: NumProcess;
% how many machines must be down over 6 month period
array[Process] of int: NumDown;

%TEST DATA
var int: x;
solve satisfy;