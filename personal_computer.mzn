include "globals.mzn";

set of float: MonitorSizes = [13, 15, 15.6, 21.5, 27];
set of float: ProcessorPowers = [2.0, 2.3, 2.5, 2.7, 3.1];
set of float: HardDriveCapacities = [250, 320, 500, 750, 1024];
set of float: Prices = [699, 999, 1149, 1349, 1649];

array [1..4] of float: Computer;

array [MonitorSizes, ProcessorPowers, HardDriveCapacities, Prices] of var Computer: Computers;

constraint
all_different(Computers)
  /\ all_different(ProcessorPowers)
  /\ all_different(HardDriveCapacities)
  /\ all_different(Prices);

% Solve the puzzle
solve satisfy;

% Output the results
output [show(Computers)];