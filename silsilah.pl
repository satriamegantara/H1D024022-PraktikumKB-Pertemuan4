% Silsilah Keluarga

% Fakta
% -- Hubungan Orang tua
% Predikat parent/2 (menerima dua parameter X dan Y)
% Berarti X adalah orang tua dari Y

parent(alya, bima).
parent(alya, satria).
parent(bima, david).
parent(bima, emma).
parent(satria, yunita).
parent(satria, grace).

% ATURAN

% -- Hubungan saudara kandung.
% -- Predikat sibling/2 (menerima dua parameter X dan Y)
% -- berarti X adalah saudara kandung Y apabila fakta-fakta sesuai denganaturan.

sibling(X, Y):-
parent(Z, X),
parent(Z, Y),
X \= Y.         % X tidak sama dengan Y (Garis miring adalah negasi)

% -- Hubungan kakek-nenek.
% -- Predikat grandparent/2 (menerima dua parameter X dan Y)
% -- berarti X adalah kakek/nenek dari Y apabila fakta-fakta sesuai dengan aturan.

grandparent(X, Y):-
parent(X, Z),
parent(Z, Y).

% -- Hubungan turun-temurun.
% -- Predikat ancestor/2 (menerima dua parameter X dan Y)
% -- berarti X adalah pendahulu Y apabila fakta-fakta sesuai dengan aturan.

ancestor(X, Y):-
parent(X, Y).

ancestor(X, Y):-
parent(X, Z),
ancestor(Z, Y).

parent(bima, Anak).
grandparent(alya, Cucu).
sibling(bima, satria).
ancestor(Leluhur, emma).