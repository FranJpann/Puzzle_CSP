include "globals.mzn";



set of int: Index = 1..5; 


% Données du problème
enum Day= {Monday, Tuesday, Wednesday, Thursday, Friday};
set of int: Times = {1175,1180,1220,1230,1245};
enum Names = {Mary, Laurie,Jessica, Mark, Sally};
enum Films = {Scarface, Scarecrow, Donnie_Brasco, eighty_eight_Minutes, The_Recruit};


% Variables
array[Index] of var Names: ChosenNames;
array[Index] of var Films: ChosenFilm;
array[Index] of var Day: ChosenDay;
array[Index] of var Times: ChosenTime;

% Contraintes
constraint alldifferent(ChosenNames);
constraint alldifferent(ChosenFilm);
constraint alldifferent(ChosenDay);
constraint alldifferent(ChosenTime);


%fonction pour récuperer un index dans un array de string


% Indice 1 
% Of the 20-hundreds releases, neither of which was Jessica's choice, one opened the week and one closed the week.

set of Films: Films2000 = {eighty_eight_Minutes,The_Recruit}; 

constraint
  forall(i in Index where i != 3 /\ ChosenFilm[i] in Films2000) (
    ChosenDay[i] = Monday \/ ChosenDay[i] = Friday
  );
  


% Indice 2
% The latest of the 19-hundreds releases was shown at 30 minutes past the hour.


constraint forall(i in Index where ChosenFilm[i] = Donnie_Brasco) (
    ChosenTime[i] mod 60 = 30
  );

% Indice 3 
% The releases shown before 8:00 were on consecutive days, as were the releases shown after 8:00


constraint
  (exists(i, j in Index where ChosenTime[i] < 1200 /\ ChosenTime[j] < 1200) (
    (ChosenDay[i] + 1 = ChosenDay[j] \/ ChosenDay[i] = ChosenDay[j] + 1)) 
    /\
  exists(i, j, k in Index where ChosenTime[i] > 1200 /\ ChosenTime[j] > 1200 /\ ChosenTime[k] > 1200) (
    (ChosenDay[i] + 1 = ChosenDay[j] /\ ChosenDay[j] + 1 = ChosenDay[k]))
  )
   
  \/
        
  (exists(i, j in Index where ChosenTime[i] > 1200 /\ ChosenTime[j] > 1200) (
    (ChosenDay[i] + 1 = ChosenDay[j] \/ ChosenDay[i] = ChosenDay[j] + 1)) 
    /\
   exists(i, j, k in Index where ChosenTime[i] < 1200 /\ ChosenTime[j] < 1200 /\ ChosenTime[k] < 1200) (
    (ChosenDay[i] + 1 = ChosenDay[j] /\ ChosenDay[j] + 1 = ChosenDay[k]))
  );

  
% Indice 4 
% One of the men and one of the women had a showing before 800, but neither was mid-week

set of Names: MenIndex = {Mark,Laurie};  % Mark et Laurie
set of Names: WomenIndex = {Sally, Jessica,Mary};  % Sally, Jessica, et Mary

constraint
  exists(i in MenIndex)  (ChosenTime[i] < 1200 /\ ChosenDay[i] !=Wednesday  );
 
constraint 
  exists(j in WomenIndex)(ChosenTime[j] < 1200 /\ ChosenDay[j] != Wednesday );
  
% Indice 5 
% Mark, whose choice was Scarecrow, had a showing at a time of one hour and five minutes after that of Scarface

constraint   
  ChosenFilm[Mark] = Scarecrow;

constraint
  exists(j in Index where ChosenFilm[j] = Scarface) (
    ChosenTime[Mark] =  ChosenTime[j] + 65
);
 
% Indice 6
% Neither Miss Farmer nor Miss Peters had a showing on an even-numbered day
  
constraint ChosenDay[3] mod 2 !=0 ;
constraint ChosenDay[5] mod 2 !=0 ;

% Indice 7
% 88_Minutes showed at a time both 40 minutes to the hour and 40 minutes after the thursday showing


constraint
  exists(i in Index where ChosenFilm[i] = eighty_eight_Minutes) (
    (ChosenTime[i] mod 60 = 20) /\
    exists(j in Index where ChosenDay[j] = Thursday) (
      ChosenTime[i] = ChosenTime[j] + 40
    )
  );
  


% Résolution
solve satisfy;

/*

% Output section
output [ Names[i] ++ " a choisi le film " ++ show(ChosenFilm[i]) ++ " le " ++ show(ChosenDay[i]) ++ " à " ++ show(Times[ChosenTime[i]]) ++ "\n" | i in Index];


*/