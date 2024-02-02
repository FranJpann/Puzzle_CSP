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


% Variables
array[Index] of Shirts: chosenShirts ;
array[Index] of Names: chosenNames ;
array[Index] of Surnames: chosenSurnames ;
array[Index] of Pastas: chosenPastas ;
array[Index] of Whines: chosenWhines ;
array[Index] of Ages: chosenAges ;


constraint alldifferent(chosenShirts) ;
constraint alldifferent(chosenNames) ;
constraint alldifferent(chosenSurnames) ;
constraint alldifferent(chosenPastas) ;
constraint alldifferent(chosenWhines) ;
constraint alldifferent(chosenAges) ;


test check_1() =
  forall(i in Index where chosenShirts[i] = white) (
    check((i<5 /\ chosenWhines[i+1] = Italian) \/ ( i>1 /\ chosenWhines[i-1] = Italian), "1 marche po")
  );
  
output[if
  check_1()
  then
    "CORRECT: All constraints hold"
  else       
    "INCORRECT"
  endif];

test check(bool: b,string: s) =
  if b then true else trace_stdout("ERROR: "++s++"\n",false) endif;

