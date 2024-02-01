include "globals.mzn";
  
predicate alldifferent_float(array[int] of var float:x) =
  forall(i,j in index_set(x) where i<j)(abs(x[i] - x[j]) >= 0.01);

% Réponses
% {15.6, 2.5, 500, 1349};
% {21.5, 2.7, 1024, 1149};
% {15, 2.3, 250, 699};
% {27, 3.1, 750, 1649};
% {13, 2.0, 320, 999};

% Déclaration des ensembles
set of int: Index = 1..5;

% Données du problème
set of int: possible_monitor = {130, 150, 156, 215, 270};
set of int: possible_processor = {20, 23, 25, 27, 31};
set of int: possible_hd = {250, 320, 500, 750, 1024};
set of int: possible_price = {699, 999, 1149, 1349, 1649};

% Variables
array[Index] of var possible_monitor: chosenMonitors;
array[Index] of var possible_processor: chosenProcessors;
array[Index] of var possible_hd: chosenHDs;
array[Index] of var possible_price: chosenPrices;

% 1. Monitors, 2.Processors, 3. HDs, 4. Prices
array [1..5, 1..4] of var int: Computers = 
[| chosenMonitors[1], chosenProcessors[1], chosenHDs[1], chosenPrices[1] |
chosenMonitors[2], chosenProcessors[2], chosenHDs[2], chosenPrices[2] |
chosenMonitors[3], chosenProcessors[3], chosenHDs[3], chosenPrices[3] |
chosenMonitors[4], chosenProcessors[4], chosenHDs[4], chosenPrices[4] |
chosenMonitors[5], chosenProcessors[5], chosenHDs[5], chosenPrices[5] |];

% Constraints
constraint alldifferent(chosenMonitors);
constraint alldifferent(chosenProcessors);
constraint alldifferent(chosenHDs);
constraint alldifferent(chosenPrices);

% Constraint 1
% On prends prends en compte que Andrew est le premier Ordinateur de Computers.
constraint exists(i, j in Index) (
  i != 1 /\ j != 1 /\
  Computers[1, 4] + 300 = Computers[i, 4]
  /\ Computers[i, 2] - 4 = Computers[j, 2]
  /\ Computers[j, 1] = 215
);

% Constraint 2
constraint exists(i,j,k,x,y in Index) (
  alldifferent([1, i, j, k, x])
  /\ Computers[1, 1] != 270
  /\ Computers[i, 2] = 20
  /\ Computers[j, 3] = 250
  /\ Computers[k, 4] = 1149
  /\ Computers[x, 1] != 150
  /\ Computers[x, 3] > Computers[1, 3]
  /\ Computers[x, 3] < Computers[y, 3]
  /\ Computers[y, 2] = 27
);

% constraint 3
constraint exists(i in Index) (
  (Computers[i, 3] = 320 /\
  (Computers[i, 2] = 20
  \/ Computers[i, 2] = 23)) 
);
  
constraint exists(i, j, k in Index) (
  Computers[i, 1] = 150
  /\ Computers[i, 2] > Computers[j, 2]
  /\ Computers[j, 4] = 999
  /\ Computers[i, 2] < Computers[k, 2]
  /\ Computers[k, 4] = 1349
);

% Constraint 4
constraint exists(i in Index) (
  Computers[i, 1] = 270
  /\ Computers[i, 3] != 320
);

constraint exists(i, j in Index) (
  i != j /\
  Computers[i, 3] = 500 /\
  Computers[i, 2] > Computers[j, 2] /\
  Computers[i, 1] > Computers[j, 1] /\
  Computers[j, 4] = 699 /\
  Computers[j, 3] != 320
);

solve satisfy;

output [ show(chosenMonitors[i]) ++ " " ++ show(chosenProcessors[i]) ++ " " ++ show(chosenHDs[i]) ++ " " ++ show(chosenPrices[i]) ++ "\n" | i in Index ]