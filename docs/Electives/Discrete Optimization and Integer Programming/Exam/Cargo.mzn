% TRUCK CARGO
% A shipping company has a hub and spoke system. The shipments to be
% delivered are specified by an originating spoke, a destination spoke,
% and a shipment volume. The trucks have different types defined by a
% maximum capacity, a speed, and a cost per km. The model is to assign
% right number of trucks to each route in order to minimize the cost of
% transshipment and meet the volume requirements. There is a minimum
% departure time and a maximum return time for trucks at a spoke, and an
% load and unload time at the hub. Trucks of different types travel in
% different speeds. Therefore, shipments are available at each hub in a
% timely manner. Volume availability constraints are considered, that
% is ,the shipments that will be carried back from a hub to a spoke by a
% truck must be available for loading before the truck leaves.

% The assumptions are:
% - exactly the same number of trucks that go from spoke to hub return from hub
%   to spoke;
% - the shipments can be broken arbitrarily into smaller packages and
%   shipped through different paths.

% The objective is minimize total cost paid for truck distance covering

%DATA 
% Number of spokes
int: NumSpokes;
% Number of hubs
int: NumHubs;
% Truck types
enum TruckTypes;
% Earliest departure time at spoke 
array[1..NumSpokes] of int: MinDepTime;
% Latest arrive time at spoke
array[1..NumSpokes] of int: MaxArrTime;
%% Truck info
  % capacity
array[TruckTypes] of int: Capacity;
  % distance covering cost
array[TruckTypes] of int: CostPerKm;
  % speed
array[TruckTypes] of int: KmPerHour;
% Load time at hubs
array[1..NumHubs, TruckTypes] of int: LoadTime;
% Hubs to spoke distances -1 if route is not available
array[1..NumSpokes, 1..NumHubs] of int: Routes;
% Shipments to deliver from spoke to spoke
array[1..NumSpokes, 1..NumSpokes] of int: Shipments;

%TEST DATA
var int: x;
solve satisfy;   

