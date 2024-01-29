include "globals.mzn";

% Déclaration des ensembles
set of int: Index = 1..5; 


% Données du problème
array[Index] of string: Day= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
array[Index] of int: Times = [1175,1180,1220,1230,1245];
array[Index] of string: Names = ["Sally", "Mark", "Jessica", "Laurie", "Mary"];
array[Index] of string: Films = ["Scarface", "Scarecrow", "Donnie_Brasco", "eighty_eight_Minutes", "The_Recruit"];


set of int: Films2000 = {4, 5}; 
set of int: Films1900 = {1, 2, 3};

% Variables
array[Index] of var Index: ChosenFilm;
array[Index] of var Index: ChosenDay;
array[Index] of var Index: ChosenTime;

% Contraintes

constraint alldifferent(ChosenFilm);
constraint alldifferent(ChosenDay);
constraint alldifferent(ChosenTime);

% Indice 1
% Of the 20-hundreds releases, neither of which was Jessica's choice, one opened the week and one closed the week.

% changer ca pour remplacer "3" par "jessica"???
constraint
  forall(i in Index where i != 3) (
    (ChosenFilm[i] in Films2000) ->
    (
      (ChosenDay[i] = 1) \/ (ChosenDay[i] = 5)
    )
  );



% Indice 2
% The latest of the 19-hundreds releases was shown at 30 minutes past the hour.

var int: Latest1900 = 3;

constraint forall(i in Index where ChosenFilm[i] = Latest1900) (
    Times[ChosenTime[i]] mod 60 = 30
  );

% Indice 3 
% The releases shown before 8:00 were on consecutive days, as were the releases shown after 8:00

% Contrainte pour les sorties avant 8:00
constraint
  forall(i in Index where Times[ChosenTime[i]] < 1200) (
    (i < 5 /\ ChosenDay[i] + 1 = ChosenDay[i+1]) \/ (i > 1 /\ ChosenDay[i] - 1 = ChosenDay[i-1])
  );

% Contrainte pour les sorties après 8:00
constraint
  forall(i in Index where Times[ChosenTime[i]] > 1200) (
    (i < 5 /\ ChosenDay[i] + 1 = ChosenDay[i+1]) \/ (i > 1 /\ ChosenDay[i] - 1 = ChosenDay[i-1])
  );
  
% Indice 4 
% One of the men and one of the women had a showing before 800, but neither was mid-week

set of int: MenIndex = {2, 4};  % Mark et Laurie
set of int: WomenIndex = {1, 3, 5};  % Sally, Jessica, et Mary

constraint
  exists(i in MenIndex)  (Times[ChosenTime[i]] < 1200 /\ ChosenDay[i] != 3  )
  /\
  exists(j in WomenIndex)(Times[ChosenTime[j]] < 1200 /\ ChosenDay[j] != 3  );
  
% Indice 5 
% Mark, whose choice was Scarecrow, had a showing at a time of one hour and five minutes after that of Scarface


constraint
  forall(i in Index where ChosenFilm[i] = 1) (
    exists(j in Index where ChosenFilm[j] = 2) (
      Times[ChosenTime[j]] =Times[ChosenTime[i]] + 65
      /\
      ChosenFilm[2] = 2
    )
  );
  
% Indice 6
% Neither Miss Farmer nor Miss Peters had a showing on an even-numbered day

set of int: MissFarmerIndex = {3};  % Jessica Farmer
set of int: MissPetersIndex = {5};  % Mary Peters

constraint
  forall(i in MissFarmerIndex) (
    ChosenDay[i] mod 2 != 0
  ) /\
  forall(j in MissPetersIndex) (
    ChosenDay[j] mod 2 != 0
  );

% Indice 7
% 88_Minutes showed at a time both 40 minutes to the hour and 40 minutes after the thursday showing


constraint
  (exists(i in Index where ChosenFilm[i] = 4) (
    (Times[ChosenTime[i]] mod 60 = 20)
    /\
    (exists ( j in Index where ChosenDay[j] = 4) 
      (Times[ChosenTime[i]] = Times[ChosenTime[j]] + 40)
    
  )));
  
  


% Résolution
solve satisfy;

% Output section
output [ Names[i] ++ " a choisi le film " ++ show(ChosenFilm[i]) ++ " le " ++ show(ChosenDay[i]) ++ " à " ++ show(Times[ChosenTime[i]]) ++ "\n" | i in Index];


