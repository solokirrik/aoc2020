inp = ["""LLLLLL.LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LL
LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.L.LLLLLL.LL.LLLLLL
LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLL.LL.LLLLLLLLLLLLLL.LL.LLLLLLLLL
LLLLLL.LLLLL..LLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.L.LLLLL.L
LLLLLL.LLLLLL.LLL.L.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLL..LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL.LLL
.LLLLLLLLLLLL.LLL.L.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLL.L.L.LLLLLLLLLLLLL.L.LLLLLLLLL
LLLLLL.LLLLLL.LLLLL.LLLLLLL..LLLLLLLLLL..LLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLL.LLLL..LLLLLLLL
..........LL....L..LL..L.....L...L....L............L.LL...L.......L.L.LL...L.L...L....L.L....LLL..
LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLL.L.LLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LL..LLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLL.LLLLL.LLLLLLL.LLL.L.LLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL.LLL
.LLLLL..LL.LL..LLL.LLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL
L.LLLL.LLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLL.LLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL
LLLLLL.LLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLL.L.LLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLL.L.LLLLLLLL.LLLLLLLL.LLLLLLLLL
...LLLLL.......L.LL..L..LL...LL..L.....L...L...LLL.L.L.....L.L....L.L......LL..L.L.L..LL.L.....LL.
LLLLLLLLLLL.L.LLL.LLLLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLLL.L.LL.LLLLLLLLLLLLLLL
LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLL.LLL.LLLLLLLL.LLLLLLLL..LLLLLLLLLLLLLL.LL
LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLL.L.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLL..LL.L.LLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLL
L.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLL.LL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL
.LLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.L.LLL.LLLLLLLL.LLL..LLLLLLL.LL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.L.LLLLLL.LLLLLLLLLLLLLLLLL.
L.LL..LLL.L.........L.L....L...LL.L......L..LL.......L.....L.LL.....L..L.L.....L.....L.L...L.L....
LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL..LLLL..LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLL.L..LLLL.L.LLLLLLLLLLLLL.LLLLL.LLLLL.L.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLL
LLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLL..LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL
LL.LLLLLLLLLLLLLLL..LLLLLLLLLLLL..LLLLLLLLL.LLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLL
LLLLLL..LLLLLLLLLLLLLLLLL.L.LLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL
..L...L...L..L..LL...L..........L.....L......L....L.L..L.L.L..L.LL....L..L...L...L......L.....L..L
LLLLLLLLLLLL..LLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LL.LLLLLLLLLLLLL.L.LLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.L.LLLLL.LLLLLLLLLLLLLLLLL..LLLLLLL.LLLLLLLLL
LLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLL.LLLLLLLLL
LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLL.LLLL.LLLLLLLL.LLLLL.LLLLLLLLLL.L
LLLLLLLLLLLLL.L.LLL.LLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL..LLLLLLLLL
LLL..L..LLLL.LLL.L......L...LL.L..L.L...L...LL....L.L.L.L................L....L..L...L......LLL.L.
LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL..LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLL..LLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLLL.LLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LL.LLLLLLLL.LLLLLL.LLLLLLLLLL.LLLLLLLLL
.LLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL
LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLL..LLLLLLLL.LLLLLLLL.LLLLLLLL.L.LLLLLLL
LLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLL.LL.LLLLLLLLLLLLLLLLLL
LLLLLL.LLLLLL.LLLLL.LLLL.LL.LLLLL.LLLLL.LLLLLLLL..LLL.LLLLL.L.LLLLLLLLLLLLLLLLL.LLL.LLLL.LLLLLLLLL
LL.LLL.LLLLLL.LLLLL.LLLLLLLLLLLLL.LL.LLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLL.L.LL.LLLLLLLLLLL.LLLLLL
LLLLLLLLLLLLL.LLLLL..LLLLLLLLLLLLLLLLLL.L.LLLLLL.LLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL
.LLLLL..L.L.L...L...L..LL.L.L.LL.L...L.L.L...................LL..L...L......L..L.........L.....LL.
LLLL.LLLLLLLL.LLLLL.LLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLL.L.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLL.LLLLLL.L.LLLL.LLLLL.LLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLL.LL..LLLL.
.LLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLL.L.LLLL.LLLLLLLLLLLLLL.LLLLLLL..LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLL...LLLLL.LLLLLLL.LLLL.LLLLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLLL.LLLLLLL.LLLLLLLL..L.LLLLL.LLLLLLLL.LLLLLLLLL
LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LL.LLLLLLLLLLLLLL.
LLL.LL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLL.LLL..L.LLLLL.LLLLLLLLLLLLLLLLL.L.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL
L.LL.L.L...L.LL.L.LLL...L.......LLL.L.LL..LLLL.L.L...L..LL.L..LL..L.L..LLLL.L.L..L.L....L....L...L
LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLL.LLLL.L.LLLLLLL
LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL
LLLLLL.L.LLLL.LLLLL.LLL.LLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLL..LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLL.LLLLLLLL.LLLLL..LLLLLLLLLLLL.LL.LL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.L.LLLLLL.LLLLLLLLLLLLLLLLLL
LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL..LLLLLLL.LL.LLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLL.LLLLL
L.L..L................L..LL.....LL...L............L....LL..LL.LLL.L.............L..L...L.....LLL..
LLLLLLLLLLLLLLLL.LL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLL.LLLLLL.LLLLLLL.LLLLL.LLL.LLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.
LLLLLL.LLLLLLLLLLLLLL.LLLLL.LLLLL.LL.LL.LLLLLLLL.LLLL.LLLLLLL.LL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL
LLLL.LL.LLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLL..LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLL.LLL.LLLL.LLLLLL.L.LLLLLLLL.LLLLLLLLL
L.L..L...LL.L.....LL..LL.L.....L.L..L....L..L.L...L.LLLL....L...LL......L..L....LL..L..L........LL
LLLLLLLLLLLLLLLLLLL.LLLL.LL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLL.LLLL.LLLLLLLL.LLLLL.LLL
LLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LL.LLLLLL.LLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLL.LLLLL.LLLLLL.LLLLLLL.LLLLLLLLLLL..LLLLLLL.L.LL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL..LLLLLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLL.LLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLLLLLLLLLLLLL.LL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLL.L.LLLLLLLLLLLLL.LLLLLLLLL.L.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLL..LLLLLLLL.LLLLLLLLL
LLLLL..LLLL.L.LLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLL..LLLLLLLL.LLLLLLLLL
L.LLLLLLLLLLLLLLLLL.LLLLLLL.LL.LL.LLLLL.LLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL
LL.L......L......L...L..LLL.....L.L..L.L...L......L..L..L.....L...LL.L.LL.L.LLL....L.LLL....L..L..
LLLLLLLLLL.LLLLLLLLLL.LL.LL.LLLLLLLLLLL.L..LLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLL.LL..LLL.LLLLLLL.LLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL..LL.LL.LLLLL.LLLLLLL.L.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLL.LLL.LLLL.LLLLLLLLLLLLLLLL..LLLLLLLLL
LLLLLLLLLLL.LLLLLLL.LLL.LLLLLLLLL.LLLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLLLLLLL.L.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.L.LLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLL..LLLL.LLLLLLLLLLLLLLLL.LL.LLLL.LLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.L.L.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LL.LLLLLLLLL.LLLLLLL.LLLLLL
L..L.LL......LLL....LLLL.......L.L..L..L....LLLLL..LLLLL..L..L.L.L........LLL...LL.L......LLL.....
LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL..LLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LL.LLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLL.LLLL.LLLLLLLL..LLLLLL.LLLLL.LLLL...LLLLL.L.LLLL.LLLLLLL..LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL
LLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLL.LLL
LLLLLLLLLLLLL.LLLLL.L.LLLLL.LLLLLLLLLLL.LLLLLLLLLL.LL.LLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL
LLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL
LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.L.LLLLLL.LLLLLLLLLLLLLLLLL.
LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL
"""]

inp_m = """....................................................................................................
.LLLLLL.LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LL.
.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.L.LLLLLL.LL.LLLLLL.
.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLL.LL.LLLLLLLLLLLLLL.LL.LLLLLLLLL.
.LLLLLL.LLLLL..LLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.L.LLLLL.L.
.LLLLLL.LLLLLL.LLL.L.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLL..LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL.LLL.
..LLLLLLLLLLLL.LLL.L.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLL.L.L.LLLLLLLLLLLLL.L.LLLLLLLLL.
.LLLLLL.LLLLLL.LLLLL.LLLLLLL..LLLLLLLLLL..LLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLL.LLLL..LLLLLLLL.
...........LL....L..LL..L.....L...L....L............L.LL...L.......L.L.LL...L.L...L....L.L....LLL...
.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLL.L.LLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LL..LLLLLLL.LLLLLLLLLL.
.LLLLLLLLLLLLL.LLLLL.LLLLLLL.LLL.L.LLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL.LLL.
..LLLLL..LL.LL..LLL.LLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.
.L.LLLL.LLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLL.LLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL.
.LLLLLL.LLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLL.L.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLL.L.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
....LLLLL.......L.LL..L..LL...LL..L.....L...L...LLL.L.L.....L.L....L.L......LL..L.L.L..LL.L.....LL..
.LLLLLLLLLLL.L.LLL.LLLLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLLL.L.LL.LLLLLLLLLLLLLLL.
.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLL.LLL.LLLLLLLL.LLLLLLLL..LLLLLLLLLLLLLL.LL.
.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLL.L.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLL..LL.L.LLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLL.
.L.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLL.LL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.
..LLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.L.LLL.LLLLLLLL.LLL..LLLLLLL.LL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.L.LLLLLL.LLLLLLLLLLLLLLLLL..
.L.LL..LLL.L.........L.L....L...LL.L......L..LL.......L.....L.LL.....L..L.L.....L.....L.L...L.L.....
.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL..LLLL..LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.
.LLL.L..LLLL.L.LLLLLLLLLLLLL.LLLLL.LLLLL.L.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLL.
.LLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLL..LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.
.LL.LLLLLLLLLLLLLLL..LLLLLLLLLLLL..LLLLLLLLL.LLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLL.
.LLLLLL..LLLLLLLLLLLLLLLLL.L.LLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
...L...L...L..L..LL...L..........L.....L......L....L.L..L.L.L..L.LL....L..L...L...L......L.....L..L.
.LLLLLLLLLLLL..LLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LL.LLLLLLLLLLLLL.L.LLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.L.LLLLL.LLLLLLLLLLLLLLLLL..LLLLLLL.LLLLLLLLL.
.LLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLL.LLLLLLLLL.
.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLL.LLLL.LLLLLLLL.LLLLL.LLLLLLLLLL.L.
.LLLLLLLLLLLLL.L.LLL.LLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL..LLLLLLLLL.
.LLL..L..LLLL.LLL.L......L...LL.L..L.L...L...LL....L.L.L.L................L....L..L...L......LLL.L..
.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL..LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLL..LLLLLLL.LLLLLLLLLLLLLLLLLL.
.LLLLLL.LLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LL.LLLLLLLL.LLLLLL.LLLLLLLLLL.LLLLLLLLL.
..LLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.
.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLL..LLLLLLLL.LLLLLLLL.LLLLLLLL.L.LLLLLLL.
.LLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLL.LL.LLLLLLLLLLLLLLLLLL.
.LLLLLL.LLLLLL.LLLLL.LLLL.LL.LLLLL.LLLLL.LLLLLLLL..LLL.LLLLL.L.LLLLLLLLLLLLLLLLL.LLL.LLLL.LLLLLLLLL.
.LL.LLL.LLLLLL.LLLLL.LLLLLLLLLLLLL.LL.LLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLL.L.LL.LLLLLLLLLLL.LLLLLL.
.LLLLLLLLLLLLL.LLLLL..LLLLLLLLLLLLLLLLLL.L.LLLLLL.LLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL.
..LLLLL..L.L.L...L...L..LL.L.L.LL.L...L.L.L...................LL..L...L......L..L.........L.....LL..
.LLLL.LLLLLLLL.LLLLL.LLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLL.L.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLL.LLLLLL.L.LLLL.LLLLL.LLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLL.LL..LLLL..
..LLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLL.L.LLLL.LLLLLLLLLLLLLL.LLLLLLL..LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLL...LLLLL.LLLLLLL.LLLL.LLLLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.
.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLLL.LLLLLLL.LLLLLLLL..L.LLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LL.LLLLLLLLLLLLLL..
.LLL.LL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.
.LLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.
.LLLLLL.LLL..L.LLLLL.LLLLLLLLLLLLLLLLL.L.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
.L.LL.L.L...L.LL.L.LLL...L.......LLL.L.LL..LLLL.L.L...L..LL.L..LL..L.L..LLLL.L.L..L.L....L....L...L.
.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLL.LLLL.L.LLLLLLL.
.LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.
.LLLLLL.L.LLLL.LLLLL.LLL.LLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLL..LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLL.LLLLLLLL.LLLLL..LLLLLLLLLLLL.LL.LL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.L.LLLLLL.LLLLLLLLLLLLLLLLLL.
.LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL..LLLLLLL.LL.LLLLLL.
.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLL.LLLLL.
.L.L..L................L..LL.....LL...L............L....LL..LL.LLL.L.............L..L...L.....LLL...
.LLLLLLLLLLLLLLLL.LL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLL.LLLLLL.LLLLLLL.LLLLL.LLL.LLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL..
.LLLLLL.LLLLLLLLLLLLLL.LLLLL.LLLLL.LL.LL.LLLLLLLL.LLLL.LLLLLLL.LL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.
.LLLL.LL.LLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLL..LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLL.LLL.LLLL.LLLLLL.L.LLLLLLLL.LLLLLLLLL.
.L.L..L...LL.L.....LL..LL.L.....L.L..L....L..L.L...L.LLLL....L...LL......L..L....LL..L..L........LL.
.LLLLLLLLLLLLLLLLLLL.LLLL.LL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLL.LLLL.LLLLLLLL.LLLLL.LLL.
.LLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LL.LLLLLL.LLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.
.LLLLLL.LLLLL.LLLLLL.LLLLLLL.LLLLLLLLLLL..LLLLLLL.L.LL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL..LLLLLLLLL.
.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLL.LLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLLLLLLLLLLLLL.LL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLL.L.LLLLLLLLLLLLL.LLLLLLLLL.L.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLL..LLLLLLLL.LLLLLLLLL.
.LLLLL..LLLL.L.LLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLL..LLLLLLLL.LLLLLLLLL.
.L.LLLLLLLLLLLLLLLLL.LLLLLLL.LL.LL.LLLLL.LLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LL.L......L......L...L..LLL.....L.L..L.L...L......L..L..L.....L...LL.L.LL.L.LLL....L.LLL....L..L...
.LLLLLLLLLL.LLLLLLLLLL.LL.LL.LLLLLLLLLLL.L..LLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLL.LL..LLL.LLLLLLL.LLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL..LL.LL.LLLLL.LLLLLLL.L.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLL.LLL.LLLL.LLLLLLLLLLLLLLLL..LLLLLLLLL.
.LLLLLLLLLLL.LLLLLLL.LLL.LLLLLLLLL.LLLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLLLLLLL.L.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.L.LLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLL..LLLL.LLLLLLLLLLLLLLLL.LL.LLLL.LLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.L.L.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LL.LLLLLLLLL.LLLLLLL.LLLLLL.
.L..L.LL......LLL....LLLL.......L.L..L..L....LLLLL..LLLLL..L..L.L.L........LLL...LL.L......LLL......
.LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL..LLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LL.LLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLL.LLLL.LLLLLLLL..LLLLLL.LLLLL.LLLL...LLLLL.L.LLLL.LLLLLLL..LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL.
.LLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLL.LLL.
.LLLLLLLLLLLLL.LLLLL.L.LLLLL.LLLLLLLLLLL.LLLLLLLLLL.LL.LLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL.
.LLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.
.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.L.LLLLLL.LLLLLLLLLLLLLLLLL..
.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.
...................................................................................................."""

matr = [[c for c in x] for x in inp_m.splitlines()]
row_len = len(matr[0])
col_high = len(matr)
i, j = 0, 0


def neibours_c(inp_m, i, j):
    neibours = [
        (i - 1, j),  # низ
        (i, j - 1),  # слева
        (i - 1, j - 1),  # низ слева
        (i + 1, j),  # верх
        (i, j + 1),  # справа
        (i + 1, j + 1),  # верх справа
        (i - 1, j + 1),  # низ право
        (i + 1, j - 1),  # низ лево
    ]
    neibours_count = 0
    for k in neibours:
        #         print(k)
        #         print(i, j, k[0], k[1])
        #         print(inp_m)
        #         print(inp_m[k[0]])
        #         print(inp_m[k[0]][k[1]])
        if inp_m[k[0]][k[1]] == "#":
            neibours_count += 1
    return neibours_count


def occupy(inp_m):
    row_len = len(inp_m[0]) - 1
    col_high = len(inp_m) - 1

    new_m = inp_m[:]
    occupied = []
    for i in range(1, col_high):
        for j in range(1, row_len):
            if new_m[i][j] == ".":
                continue
            neibours = neibours_c(new_m, i, j)
            #             print(i, j, neibours)
            if neibours == 0:
                occupied.append((i, j))
    #                 new_m[i][j] = "#"
    #     print(len(occupied))
    for o in occupied:
        new_m[o[0]][o[1]] = "#"
    return new_m, len(occupied)


def run(inp_m):
    row_len = len(inp_m[0]) - 1
    col_high = len(inp_m) - 1

    new_m = inp_m[:]
    left = []
    for i in range(1, col_high):
        for j in range(1, row_len):
            if new_m[i][j] == ".":
                continue
            neibours = neibours_c(new_m, i, j)
            #             print(i, j, neibours)
            if neibours >= 4:
                left.append((i, j))
    for l in left:
        new_m[l[0]][l[1]] = "L"
    #     print(len(left))
    return new_m, len(left)


def print_m(inp_m):
    return ["".join(x) for x in inp_m]


import copy

FLOOR = "."
EMPTY_SEAT = "L"
TAKEN = "#"


def print_map(map):
    for row in map:
        for column in row:
            print(column, end="")
        print("")
    print("")


def process_until_stable_star1(new_map):
    # first iteration
    old_map = copy.deepcopy(new_map)
    # print_map(old_map)

    new_map = process_star1(new_map)
    # print_map(new_map)

    while (not are_identical(old_map, new_map)):
        old_map = copy.deepcopy(new_map)

        new_map = process_star1(new_map)

        # print_map(new_map)

    return new_map


def are_identical(old_map, new_map):
    for i in range(0, len(new_map)):
        # print(f"{old_map[i]} - {new_map[i]}")
        if old_map[i] != new_map[i]:
            # print("stop")
            return False

    return True


def process_star1(map):
    new_map = copy.deepcopy(map)

    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            # print(f"x:{x} y:{y}")
            new_map[y][x] = calculate_new_state_star1(map, y, x)
            # print("")

    return new_map


def get_occupied_neighbours_star1(map, x, y):
    occupied_seats = 0

    for dy in [-1, 0, 1]:
        if (0 <= (dy + y) < len(map)):
            for dx in [-1, 0, 1]:
                # check that we dont exceed boundaries

                if (0 <= (dx + x) < len(map[y])) and not ((dx == 0) and (dy == 0)):
                    # print(f"dx {dx} : dy {dy} : {map[y + dy][dx + x]}")
                    if map[y + dy][dx + x] == TAKEN:
                        occupied_seats += 1
    # print(f"occupied seats: {occupied_seats}")
    return occupied_seats


def calculate_new_state_star1(map, y, x):
    if map[y][x] == FLOOR:
        return FLOOR

    if map[y][x] == EMPTY_SEAT:
        if get_occupied_neighbours_star1(map, x, y) == 0:
            return TAKEN
        else:
            return EMPTY_SEAT

    if map[y][x] == TAKEN:
        # print(get_occupied_neighbours(map, x ,y))

        if get_occupied_neighbours_star1(map, x, y) >= 4:
            return EMPTY_SEAT
        else:
            return TAKEN
    # umfeld abfahren und zustaende zaehlen
    return EMPTY_SEAT


def process_until_stable_star2(new_map):
    # first iteration
    old_map = copy.deepcopy(new_map)
    # print_map(old_map)

    new_map = process_star2(new_map)
    # print_map(new_map)

    while (not are_identical(old_map, new_map)):
        old_map = copy.deepcopy(new_map)

        new_map = process_star2(new_map)

        # print_map(new_map)

    return new_map


def process_star2(map):
    new_map = copy.deepcopy(map)

    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            # print(f"x:{x} y:{y}")
            new_map[y][x] = calculate_new_state_star2(map, y, x)
            # print("")

    return new_map


def calculate_new_state_star2(map, y, x):
    if map[y][x] == FLOOR:
        return FLOOR

    if map[y][x] == EMPTY_SEAT:
        if get_occupied_neighbours_star2(map, x, y) == 0:
            return TAKEN
        else:
            return EMPTY_SEAT

    if map[y][x] == TAKEN:
        # print(get_occupied_neighbours(map, x ,y))

        if get_occupied_neighbours_star2(map, x, y) >= 5:
            return EMPTY_SEAT
        else:
            return TAKEN

    return EMPTY_SEAT


def get_occupied_neighbours_star2(map, x, y):
    occupied_seats = 0

    for dy in [-1, 0, 1]:
        if (0 <= (dy + y) < len(map)):
            for dx in [-1, 0, 1]:
                # check that we dont exceed boundaries

                if (0 <= (dx + x) < len(map[y])) and not ((dx == 0) and (dy == 0)):
                    # print(f"dx {dx} : dy {dy} : {map[y + dy][dx + x]}")
                    # scan every of the eight directions around the seat
                    occupied_seats += scan(map, x, y, dx, dy)
    # print(f"x:{x} y:{y} occu: {occupied_seats}")
    return occupied_seats


def scanner_in_map(map, scanner_x, scanner_y):
    # check if scanner beam is still within the map
    if 0 <= scanner_x and 0 <= scanner_y and scanner_x < len(map[0]) and scanner_y < len(map):
        return True
    else:
        return False


def scan(map, x, y, dx, dy):
    # shots a scan beam across the beam until a occupied seatis found or the end the map is reached
    scanner_y = y + dy
    scanner_x = x + dx

    while (scanner_in_map(map, scanner_x, scanner_y)):
        if map[scanner_y][scanner_x] == TAKEN:
            return 1
        if map[scanner_y][scanner_x] == EMPTY_SEAT:
            return 0
        scanner_x += dx
        scanner_y += dy

    return 0


def count_occupied_seats(map):
    occupied_seats = 0
    for row in map:
        for seat in row:
            if seat == TAKEN:
                occupied_seats += 1

    return occupied_seats


if __name__ == '__main__':
    map1 = matr
    map1 = process_until_stable_star1(map1)
    print(f"Star 1: {count_occupied_seats(map1)} seats are taken")

    map2 = matr
    map2 = process_until_stable_star2(map2)
    print(f"Star 2: {count_occupied_seats(map2)} seats are taken")
