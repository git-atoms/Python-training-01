## Python 3 od Podstaw do Eksperta

*(Samokształcenie: kurs z Udemy)*


---

<br>

### Rozdział pierwszy: Podstawy Python

<br>

1. Co zrobić by wyciągnąć z kursu jak najwięcej korzyści?
2. Czym jest Python? Pierwsze uruchomienie
3. Zmienne, pierwszy skrypt oraz zmiana stanu powłoki


> Nawet gdy skrypt zakończy już swoje działanie, to nadal możemy korzystać zdefiniowane w nim zmienne, dopóki nie zrestartujemy Shell'a ponownie.

<br>

## 4. Komentarze

> CTRL / <br>
> to skrót do komentowania

```python
# komentarz w Pythonie
```

<br>

## 5. Typy zmiennych oraz nazewnictwo

> INT (integer) <br>
> FLOAT (zmiennoprzecinkowe) 4.3 <br>
> STRING (ciąg znaków) "tu wpisuję swój string" <br>
> BOOL

```python
bool = True / False
```

> Python jest CS (Case Sensitive) np.

```python
a = 5
A = 4

# i to są DWIE RÓŻNE zmienne.
```

<br>

## 6. Operatory arytmetyczne (Matematyka w Pythonie)

```python
# Po podzieleniu liczb całkowitych (INT) wynik podawany jest we FLOAT
2/2
1.0
```

<br>

## 7. Ćwiczenie z VAT'em<br>

<br>

```python
cenaNetto = float(input("Podaj cenę netto: "))
VAT = float(input("Podaj stawkę VAT: "))

obliczonyVAT = (1 + VAT/100)
cenaBrutto = cenaNetto * obliczonyVAT

print("Cena brutto: ", (cenaBrutto))
```

<br>

A link do screena z ćwiczenia [tutaj](https://github.com/git-atoms/Python-training-01/blob/master/Screeny/VAT%20exercises.jpg).

<br>

<br>
<br>



## 8. Czym jest średnik i ENTER dla interpretera? Przypisywanie kilku wartości naraz.

<br>

> ENTER to dla Pythona koniec instrukcji. Nową linię będzie chciał wykonywać od nowa, a nie jako kontynuację poprzedniej.


<br>
Można przypisać zmiennym różne wartości, np.:


```python
x = 4
y = 5
z = 7
print(x) # wyświetli wartość 4

```
<br>

A co jeśli x, y, z mają te same wartości?<br>

Można oczywiście napisać:<br>
x = 4<br>
y = 4<br>
z = 4

<br>

Ale można też napisać:<br>
x = y = z = 4<br>

<br>
<br>



## 9. Operatory przypisania


<br>

>Jeżeli do np.<br>
>x = 4 <br>
> chcemy dodać jeszcze 3, to można to zapisać tak:<br>
> x += 3
>czyli do tego co było wcześniej, dodajemy jeszcze 3.

<br>

>Inne operatory:<br>
>x += 5 <br>
>x -= 5 <br>
>x *= 5 <br>
>x /= 5 <br>
>x %= 5 (modulo)<br>
>x //= 5 (dzielenie w dół)<br>
>x **= 5 (potęgowanie)<br>
><br>


<br>
<br>


## 10. Stringi (ciągi znaków)
<br>
>Jeśli chcemy wyświetlić string, robimy to komendą PRINT
<br>

```python

imie = "Jan"
mazwisko = "Kowalski"

print(imie)


```

<br>

>Natomiast jeśli chcemy połączyć dwa stringi (imię z nazwiskiem), robimy to operatorem "+". <br>

```python
imie = "Jan"
mazwisko = "Kowalski"

print(imie + " " + nazwisko)

```

<br>


>Ale można to takie dane przechować w tylko jednej zmiennej:
<br>

```python

imie = "Jan"
nazwisko = "Kowalski"

fullName = imie + " " + nazwisko
print(fullName)

```

<br>
<br>

String wieloliniowy z kolei zapisujemy na dwa sposoby:<br>

* Za pomocą backslash'a
<br>

```python
longString = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam\
voluptate sapiente aperiam et cumque a ducimus, laudantium ipsum velit? Sint,\
nobis repellendus! Hic ipsam adipisci, amet iure repellendus quaerat veritatis!"

```

<br>

>albo za pomocą potrójnego cudzysłowia (jak długi komentarz):


```python
longString = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam
voluptate sapiente aperiam et cumque a ducimus, laudantium ipsum velit? Sint,
nobis repellendus! Hic ipsam adipisci, amet iure repellendus quaerat veritatis!"""

``` 

<br>

>Pobieranie miejsca w stringu.<br>

Pierwszym elementem jest element [0].
<br>
Ostatnim jest element [-1] (możemy go pobrać bez znania długości stringu). Przedostatnim [-2], itd.

```python
imie = "Tomek"
print(imie[-1])
# To wyświetla mi tylko ostatnią literę, bez względu na długość stringu

print(imie[:-1])
# To wyświetla cały string aż do ostatniego znaku (którego nie wyświetla)
```


Sam zresztą zobacz [tutaj](https://github.com/git-atoms/Python-training-01/blob/master/Screeny/Miejsca%20znak%C3%B3w.jpg).

<br>
Natomaist jeśli chciałbym pokazać resztę stringu bez pierwszego znaku to robię tak:

```python
imie = "Tomek"
print(imie[1:])
# To wyświetla mi wszystko od drugiej (pierwsza to zero)
```




<br>




<br>
<br>

11. Ćwiczenie z VAT'e




