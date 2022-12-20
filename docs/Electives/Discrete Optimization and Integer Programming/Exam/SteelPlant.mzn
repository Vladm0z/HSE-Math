% STEEL PLANT
% Create model of a production and inventory planning with backlogging.
% We need to schedule production and inventories for multiple
% products over time when facing limited resources such as labors,
% materials, and machine capacities in each period. The
% model should handle goals like reducing the backlogs at the end and
% reaching the target inventory levels. 
% Amount of products should be enough to satisfy demand at any period of time. 

% Features:
% 1) Bills of materials are considered.
% 2) The unit cost of production, inventory, and backlogging can change
%    over time.
% 3) Backorders are allowed.
% 4) Bounds on the ending backorder levels can be enforced.
% 5) Target ending inventory levels can be specified.

% The objective is to
% minimize the total cost of production, inventory, and backlogging.

%DATA 
% Number of time periods
int: T;
% Products
enum Products;
% Resources
enum Resources;
% Bills of materials 
array[Products, Resources] of float: ResourceReq;
% Available resources in each period 
array[Resources, 1..T] of float: Avail;
% Initial inventories
array[Products] of float: Inv0;
% Initial backorders
array[Products] of float: Backorder0;
%Bounds on ending backorder levels
array[Products] of float: EndBlg;
%Target ending inventory levels
array[Products] of float: EndInv;
% Products demand at each moment of time to be satisfied
array[Products, 1..T] of float: Demand;
%Variable production cost
array[Products, 1..T] of float: Prodcost;
%Unit inventory holding cost
array[Products, 1..T] of float: Invcost;
%Unit backorder cost
array[Products, 1..T] of float: Backlogcost;

% DATA TEST
var int: x;
solve satisfy;    
