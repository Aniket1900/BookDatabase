% Author: Bartosz Modrzy�ski
% Date: 2016-04-25

%Baza danych
%author- id, imie, nazwisko
%book - id, tytul, autor, rodzaj, indeks
%type - id rodzaju, nazwa

go:- dynamic(author/3), dynamic(book/5), dynamic(type/2), program.


program :-  new(BDatabase, dialog('Menu')),
            send(BDatabase, append, text('Baza Danych ksi��ek')),
            send(BDatabase, append, button('Dodawanie autora',message(@prolog,add_author)),below),
            send(BDatabase, append, button('Dodawanie ksiazki',message(@prolog,add_book)),below),
            send(BDatabase, append, button('Dodanie gatunku',message(@prolog,add_type)),below),
            send(BDatabase, append, button('Usuniecie autora',message(@prolog,remove_author)),below),
            send(BDatabase, append, button('Usuniecie ksiazki',message(@prolog,remove_book)),below),
            send(BDatabase, append, button('Usuniecie gatunku', message(@prolog,remove_type)),below),
            send(BDatabase, append, button(exit, message(BDatabase, destroy)), below),
       send(BDatabase, open).

add_author:-
        new(Window,dialog('Dodawanie autora')),
        send_list(Window,append,[ text('Wpisz imie, nazwisko oraz miasto'),
                  new(Id_autora,text_item('Id autora')),
                  new(Imie, text_item('Imie autora')),
                  new(Nazwisko,text_item('Nazwisko autora')),
                  button('Dodaj autora',and(message(@prolog,add_new_author,Id_autora?selection, Imie?selection, Nazwisko?selection),message(Window,destroy)))
                                ]),
                  send(Window,open).

add_new_author(Id_autora, Imie, Nazwisko):-assert(author(Id_autora,Imie,Nazwisko)).

%book - id, tytul, autor, rodzaj, indeks

add_book :-
        new(Window,dialog('Dodawanie autora')),
        send_list(Window,append,[ text('Wpisz imie, nazwisko oraz miasto'),
                  new(Id_ksiazki,text_item('Id ksiazki')),
                  new(Tytul, text_item('Tytul')),
                  new(text('Autor:')),
                  new(Id_autora,text_item('Id autora')),
                  new(Imie, text_item('Imie autora')),
                  new(Nazwisko,text_item('Nazwisko autora')),
                  new(Typ, text_item('Rodzaj ksiazki')),
                  new(Indeks, text_item('Indeks')),
                  button('Dodaj autora',
                    and(
                      message(@prolog,add_new_author,Id_autora?selection, Imie?selection, Nazwisko?selection),
                      message(@prolog, add_new_book, Id_ksiazki?selection, Tytul?selection, Typ?selection, Indeks?selection),
                      message(Window,destroy)))
                                ]),
                  send(Window,open).

add_new_book(Id_ksiazki, Tytul, Typ, Indeks) :-
  assert(book(Id_ksiazki,Tytul,Typ,Indeks)).
