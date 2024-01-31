include "globals.mzn";

% Déclaration des ensembles
set of int: Index = 1..5; 


% Données du problème
enum Shirts= {blue, green,red, white, yellow};
enum Names= {Andrea, Holly, Julie,Leslie, Victoria};
enum Surnames= {Brown, Davis, Lopes, Miller, Wilson};
enum Pastas= {farfalle, lasagne, penne, spaghetti, ravioli};
enum Whines= {Australian, Argentine, Chilean, French, Italian};
set of int: Ages= {30,35,40,45,50};


% Variables (FAIRE PAREIL POUR AL PACINO !!!!!!! )
array[Index] of var Shirts: chosenShirts ;
array[Index] of var Names: chosenNames ;
array[Index] of var Surnames: chosenSurnames ;
array[Index] of var Pastas: chosenPastas ;
array[Index] of var Whines: chosenWhines ;
array[Index] of var Ages: chosenAges ;



constraint alldifferent(chosenShirts);
constraint alldifferent(chosenNames);
constraint alldifferent(chosenSurnames);
constraint alldifferent(chosenPastas);
constraint alldifferent(chosenWhines);
constraint alldifferent(chosenAges);

% The woman wearing the White shirt is next to the woman who likes Lombardian wines.
constraint 
  forall(i in Index where chosenShirts[i] = white) (
    ( i<5 /\ chosenWhines[i+1] = Italian) \/ ( i>1 /\ chosenWhines[i-1] = Italian)
);

% Ms Miller is somewhere between Ms Davis and Ms Brown, in that order.
constraint
  exists (m in Index, d in Index, b in Index where chosenSurnames[m] = Miller /\ chosenSurnames[d] = Davis /\ chosenSurnames[b] = Brown) (
    d < m /\ m < b
  );
  
% The youngest woman is at the third position.
constraint chosenAges[3] = min(chosenAges);

%The 45-year-old woman is somewhere to the right of the woman wearing the Red shirt.
constraint 
  exists ( i, r in Index where chosenAges[i]= 45 /\ chosenShirts[r] = red) (
      i > r
      );
      
% The woman who likes Chilean wines also likes Farfalle.
constraint
  exists (i in Index where chosenWhines[i]= Chilean) (
        chosenPastas[i] = farfalle
        );

% At the first position is the woman that likes Argentine wines.
constraint chosenWhines[1] = Argentine;

%Andrea is exactly to the right of the 35-year-old woman.
constraint 
   exists (i in Index where chosenNames[i] = Andrea) (
     i>1 /\ chosenAges[i-1] = 35
    );
    
%The woman wearing the Blue shirt is somewhere between Ms Davis and Holly, in that order.

constraint
  exists (b in Index, d in Index, h in Index where chosenShirts[b] = blue /\ chosenSurnames[d]= Davis /\ chosenNames[h] = Holly) (
    d < b /\ b < h
  );
  
%  Victoria is next to Leslie.
constraint
  exists (v in Index where chosenNames[v] = Victoria ) (
    ( v<5 /\ chosenNames[v+1] = Leslie) \/ ( v>1 /\ chosenNames[v-1] = Leslie)
    );
    
% The woman wearing the Red shirt is somewhere to the left of the woman who likes Australian wines. 
constraint
  exists ( r in Index, a in Index where chosenShirts[r] = red /\ chosenWhines[a]= Australian) (
  r<a
  ); 
  
% Ms Wilson is next to the 30-year-old woman.   
constraint 
   exists (i in Index where chosenSurnames[i] = Wilson) (
    ( i<5 /\ chosenAges[i+1] = 30) \/( i>1 /\ chosenAges[i-1] = 30)
    );
    
% Leslie is exactly to the left of the 30-year-old woman.
 constraint 
   exists (i in Index where chosenNames[i] = Leslie) (
    i< 5 /\ chosenAges[i+1] = 30
    );
    
% Holly is somewhere to the right of the woman wearing the Red shirt.
constraint 
   exists (h in Index,r in Index where chosenNames[h] = Holly /\ chosenShirts[r]=red) (
    r<h
    );
    
% Ms Brown is exactly to the left of Julie.
constraint 
  exists (b in Index where chosenSurnames[b] = Brown) (
     b<5 /\ chosenNames[b+1] = Julie
   );
   
% The youngest woman likes Penne.
constraint 
  exists (i in Index where chosenAges[i] = min(Ages)) (
    chosenPastas[i] = penne
    );
    
% Ms Wilson is wearing the White shirt.
constraint
  exists (i in Index) (
  chosenSurnames[i] = Wilson /\ chosenShirts[i] = white
  );
  
% The woman who likes Lasagne is somewhere between the woman who likes Italian wines and the woman who likes Spaghetti, in that order.
constraint
  exists (l in Index, i in Index,s in Index where chosenPastas[l] = lasagne /\ chosenWhines[i]= Italian /\ chosenPastas[s] = spaghetti) (
    i < l /\ l < s 
  );
  
% At the second position is the woman wearing the Blue shirt.
constraint chosenShirts[2] = blue;

% The 40-year-old woman likes Lasagne.
constraint 
  exists (i in Index) (
    chosenAges[i] = 40 /\ chosenPastas[i] = lasagne
    );
    
% Ms Lopes is at the fifth position.
constraint chosenSurnames[5] = Lopes;   

 % The woman that likes Australian wines is somewhere between Victoria and the woman who likes wines from Bordeaux, in that order. 
constraint
  exists (a in Index, v in Index,f in Index where chosenWhines[a] = Australian /\ chosenNames[v] = Victoria /\ chosenWhines[f] = French) (
    v < a /\ a < f 
  );
  
% The woman wearing the Yellow shirt is exactly to the left of the 35-year-old woman.
constraint 
  exists ( y in Index where chosenShirts[y] = yellow) (
     y<5 /\ chosenAges[y+1] = 35
    );

solve satisfy;

