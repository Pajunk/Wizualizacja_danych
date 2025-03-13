# Wizualizacja_danych
Projekt zawiera wizualizację danych w 2D, 3D, średnią, medianę, odchylenie standardowe z podziałem na współrzędne y, funkcję interpolacyjną, funkcję aproksymacyjną, pole powierzchni funkcji, całki z funkcji interpolacyjne i aproksymacyjnej ,pochodne cząstkowe i monotoniczność wybranego wiersza.
-wizualizacja danych w formie mapy 2D, kolory dla współrzędnej Z
Funkcja wczytuje dane z pliku do zmiennych x i y, tworzy zmienne X i Y które zawierają min i max ze zmiennych x i y. Tworzy zmienną Z która przetwarza dane z X i Y w celu późniejszego wyświetlenia. Na koniec wyświetla obraz.

- wizualizacja danych w formie powierzchni 3D
Funkcja wczytuje dane z pliku do zmiennych x, y i z. Tworzy zmienną ax która będzie odnosić się do obrazka 3D, wyświetla obrazek.

- wyznaczyć średnią, medianę, odchylenie standardowe z podziałem na współrzędne y
Funkcja na podstawie wartości y wyznacza średnia dla danego przedziału dla funkcji F(x,y).
 
Funkcja sortuje wartości dla funkcji med. Funkcja med oblicza medianę która następnie jest wyświetlana.
Funkcja war oblicza wariancję która jest potem wyświetlana.
 
- wyznaczyć funkcje interpolacyjną
Została wybrana interpolacja Lagrange’a ze względu na osobiste chęci autora.
Najpierw funkcja interp_lag oblicza interpolacje po czym dane są dzielone na fragmenty w celu późniejszego wyświetlenia.
 
- wyznaczyć funkcje aproksymacyjną
Została wybrana Aproksymacja liniowa ze względu na prostotę działania.
Najpierw liczona jest eliminacja Gaussa. Następnie używana jest w funkcji obliczającej aproksymację liniową która jest na koniec wyświetlana
 
- obliczyć pole powierzchni funkcji
Funkcja najpierw oblicza odległość między punktami które zostaną użyte do obliczania pola powierzchni funkcji.
 
- obliczyć całkę z funkcji interpolacyjnych i aproksymacyjnych
Całki obliczane metodą trapezów wybranej ze względu na wysoką dokładność wyników. Funkcja całki oblicza całkę metodą trapezów po czym jest zastosowana do interpolacji Lagrange’a i aproksymacji liniowej 
 
- wyznaczyć pochodne cząstkowe wybranego wiersza
Funkcja poch oblicza pochodną która jest potem wyświetlana.
 
- określić monotoniczność  wybranego wiersza
Funkcja sprawdza dla jakich punktów wartości są dodatnie a które ujemne. Po czym wyświetla wykres reprezentujący tą zależność i wartości y dla których pochodna była dodatnia lub ujemna.
