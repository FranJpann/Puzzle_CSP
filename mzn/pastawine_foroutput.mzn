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


test check_1() =
  forall(i in Index where chosenShirts[i] = white) (
    check((i<5 /\ chosenWhines[i+1] = Italian) \/ ( i>1 /\ chosenWhines[i-1] = Italian), "1")
  );

test check_2() =
  exists (m in Index, d in Index, b in Index where chosenSurnames[m] = Miller /\ chosenSurnames[d] = Davis /\ chosenSurnames[b] = Brown) (
      d < m /\ m < b
    );

test check_3() =
  chosenAges[3] = min(chosenAges);
  
test check_4() =
  exists ( i, r in Index where chosenAges[i]= 45 /\ chosenShirts[r] = red) (
      i > r
        );
  
test check_5() =
  exists (i in Index where chosenWhines[i]= Chilean) (
        chosenPastas[i] = farfalle
        );
        
test check_6() =
  chosenWhines[1] = Argentine;
  
test check_7() =
  exists (i in Index where chosenNames[i] = Andrea) (
     i>1 /\ chosenAges[i-1] = 35
    );
    
test check_8() =
  exists (b in Index, d in Index, h in Index where chosenShirts[b] = blue /\ chosenSurnames[d]= Davis /\ chosenNames[h] = Holly) (
    d < b /\ b < h
  );
  
test check_9() =
  exists (v in Index where chosenNames[v] = Victoria ) (
    ( v<5 /\ chosenNames[v+1] = Leslie) \/ ( v>1 /\ chosenNames[v-1] = Leslie)
    );
    
test check_10() =
  exists ( r in Index, a in Index where chosenShirts[r] = red /\ chosenWhines[a]= Australian) (
    r<a
  );
  
test check_11() =
  exists (i in Index where chosenSurnames[i] = Wilson) (
      ( i<5 /\ chosenAges[i+1] = 30) \/( i>1 /\ chosenAges[i-1] = 30)
    );
    
test check_12() =
  exists (i in Index where chosenNames[i] = Leslie) (
    i< 5 /\ chosenAges[i+1] = 30
    );
    
test check_13() = 
  exists (h in Index,r in Index where chosenNames[h] = Holly /\ chosenShirts[r]=red) (
      r<h
    );
    
test check_14() =
  exists (b in Index where chosenSurnames[b] = Brown) (
     b<5 /\ chosenNames[b+1] = Julie
   );
   
test check_15() =
  exists (i in Index where chosenAges[i] = min(Ages)) (
    chosenPastas[i] = penne
    );
    
test check_16() =
  exists (i in Index) (
  chosenSurnames[i] = Wilson /\ chosenShirts[i] = white
  );
  
test check_17() =
  exists (l in Index, i in Index,s in Index where chosenPastas[l] = lasagne /\ chosenWhines[i]= Italian /\ chosenPastas[s] = spaghetti) (
    i < l /\ l < s 
  );
  
test check_18() = chosenShirts[2] = blue;

test check_19() =
  exists (i in Index) (
    chosenAges[i] = 40 /\ chosenPastas[i] = lasagne
    );
    
test check_20() = chosenSurnames[5] = Lopes;   

test check_21() =
  exists (a in Index, v in Index,f in Index where chosenWhines[a] = Australian /\ chosenNames[v] = Victoria /\ chosenWhines[f] = French) (
    v < a /\ a < f 
  );
  
test check_22() =
  exists ( y in Index where chosenShirts[y] = yellow) (
     y<5 /\ chosenAges[y+1] = 35
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

