inp = [
    "....##..#........##...#.#..#.##",
    ".#.#..#....##....#...#..##.....",
    "##.#..##..#...#..........##.#..",
    ".#.##.####..#......###.........",
    "#.#.#...........#.....#...#....",
    "#.......#....#.#.##..###..##..#",
    ".#...#...##....#.........#.....",
    "..........##.#.#.....#....#.#..",
    ".......##..##...#.#.#...#......",
    ".#.#.#...#...##...#.##.##..#...",
    "........##.#.#.###.........##..",
    "#.#..#.#.#.....#...#...#......#",
    ".#.#.#...##......#...#.........",
    ".#..##.##.#...#...##....#.#....",
    ".##...#..#..#......##.###....##",
    ".....#...#.###.....#.#.........",
    "#.##..#....#.#.#.#.............",
    "........#...#......#...#..#....",
    "##..##...##.##...#...#.###...##",
    "#.#....##.#...###......#..#.#..",
    "..#.....#.##......#..........#.",
    "#.......#..#......#.....#....#.",
    ".....###...........#....#.##...",
    "#.#........##.......#.#...#.##.",
    ".#.#.#........#........#.#.....",
    "#..#..##.....#.###..#.#.#.##..#",
    "..#.#...#..##.#.#.#.......###..",
    "........#........#..#..#...#...",
    "##............#...#..##.##...#.",
    "#....#.#.....##...#............",
    "............#...#..#.#.#....#..",
    "#.#.#...##.##.#....#....#......",
    "................###.....#.....#",
    "##.#####.#..#...###..#...###...",
    "...#.....#...#.#....#...#..#...",
    ".......#....##.##.#.##.........",
    "..#..#..##.....#...#.#.....#...",
    "...#...#.#.##.#..###.......#...",
    "...#...........#.#####..##..#..",
    "#.#...#........####..#......#.#",
    "#..#.##...........#.#......#.##",
    "#.#..#....##..#..##.#..........",
    ".....#..#.....#........##..#...",
    "...###.......#.##.......#......",
    "...##..#..#...#....#.###...#...",
    "....####....#........#.##.#.#.#",
    "#....#.....#.###.##...##..##.##",
    ".##.#...#.##.#......#..##.#....",
    "...#.............#.............",
    "..##..##.#.....#........##....#",
    "#.....#....#.......####...#..#.",
    "..#...#..#...#...##.#....##....",
    ".#...##....#....#..#....#......",
    "##..#.#...##......#..#.......##",
    "..#...#.##..#.....#.#...#..#.#.",
    "#..##....#..........#..........",
    ".#........#..#......#......#.#.",
    "...##.#.........#.#....#.#...#.",
    "#.....#.#..#...#...#..#...#...#",
    "#.........#.#.........##.......",
    ".#.......#......#.........###..",
    ".#..#..##...........#.....#..#.",
    ".#....................#.....#..",
    ".##.....#....#....#.###.....#..",
    "...##.#.....#.#....#.........#.",
    ".........##.....#.....#.##..#..",
    "......#......#.#..#..###...#..#",
    "..##...#.#..#...#.#....#.......",
    "..#..##.###.#..#..#..#......#..",
    ".....##...##.........#...##...#",
    "###.#..##....##...##.#..###....",
    "#...#.#..##......##...#.#..#...",
    "..........#....###....#........",
    "#.#.#.#.#.....#..##.##.....#...",
    ".##.....#...#.....#......#.....",
    ".#..........#.#.............#..",
    ".#..##..#.#..##...#....#.##...#",
    "..#.#..........#...#..........#",
    ".#.......#.......#...#..#.....#",
    "##.#...##...#......#.#..#......",
    "#####..#....#..#...#...#.#.....",
    "....#.......#.#..#.............",
    "#..#..#.#.####...#....#....##..",
    "#..#.##.#......#...#......#....",
    "#...##.##...#....#..........##.",
    "..#..#.......##.#....#...#.#...",
    ".....#.##..............##.....#",
    "..##.##...##.....#.........#.#.",
    ".#....##...##...##..#....##..#.",
    ".#...#....#..#......#.#........",
    "#....#.#.#..............#....##",
    "..##..#..#....#####.#....#.#.##",
    "#....#...#.##..#.##.........###",
    "#..#..#....#...............#.#.",
    "#....##...##........##.##.#.##.",
    "......#......##....##.....#.###",
    "#...##..#..#.....#.#........##.",
    "..#.#.##...#...#....#..###...#.",
    "#..##..#.###..##.#.#....#......",
    "..###..#.##........###.....#...",
    "#.............#.............#..",
    ".#.##....#..##.#...#....#.#####",
    "###.....###.#......##..#..##...",
    ".#.#......##.#....#....#.#..#..",
    "###..#..#....#......###.##.....",
    "......#.......#......#..##..##.",
    "..#..#...#..#....#.##....#.#..#",
    ".......##..#........#.#.##.....",
    ".#...#..#........#..#.#..#..#.#",
    ".#..#.##.......#......#...#.#..",
    ".##..##......##.#...#......####",
    ".....#....#......#.....#......#",
    "..........#.#.#...##.#..#.#....",
    "...#.......##......#..#.#.##...",
    ".###..#.#.#....................",
    "##...#...#.##............#.....",
    "....#....#.##...#..#.#...##....",
    "..#.#....#.###...#...#.#.####.#",
    "..#..#.#...#.#......##.........",
    "#..#..####.##.#.#..###....#...#",
    "....#..........#.##.#..#.#.#.#.",
    "#.#.##.........#.....##...#..##",
    "#......#...#.##.#......#..#.#..",
    "#...#........#..#..#...##...#..",
    ".....#.####..##..#.#.##..#...#.",
    "#..#........#........#...#....#",
    "...........#..#.....#.#.#.#....",
    "....#......#....#...#....##....",
    ".#.#..#...#.#....#..#.#....##.#",
    "....#...#...#.##..#...#..##...#",
    "#######...............##.....##",
    ".#.#..............#....#..#.###",
    "#......#.#......###....###.....",
    "##..#...#.##..##..##.#....#....",
    "#....##..#..#...#.#.#...#......",
    "..........#..#.##..##.##.#..##.",
    "....#.#.#.....##........#..#...",
    "..###...#.....##.##.....##..##.",
    "....#.#..#.#.......#.......#...",
    "..##.#..#.....##...###...#...#.",
    "..#.........#...##...#...#..#..",
    "..#..#..#..#..##.#...##..#.#...",
    "...##..#..##..#..####...#.....#",
    "............#............###...",
    ".#.#.###.#.....#.#.#..#.###..#.",
    "...#.........#.....####........",
    "....##.#..##.#.............#...",
    "....#.##.....#..#.....#......##",
    "..........#.............#...##.",
    "#..#.....#.......##..###.......",
    "..##.#...........#.......#..#..",
    "...#...#.#.##.###....#.#..#....",
    "...#..........##..#..#..#...###",
    ".........#.....#..##.....#..#..",
    "#........#...#...#..#.#....##..",
    ".#.#.....####..#.##.#..........",
    "###.......##..#.##...#.....#...",
    "..###.##.#..#..#..#.....##...#.",
    ".........#.....##.#..#..##.....",
    "#..#..##...###..............#..",
    "#....#.#....#..#.....#..####...",
    "####..#.....##...#..#.#.#.#...#",
    "...#....#.....#.##.#.#.#....##.",
    "..........#...#.....###....#.##",
    "#....#.#.#....#..#..#.....#....",
    ".....#.#...#......#....#......#",
    ".####....##...#...#......##..#.",
    ".#...#..#....#..#..............",
    "##.#...##...#.##..#......#.....",
    "..####.##..#....#.#......#.#.##",
    "........#.....##...#.#..##....#",
    "....#.#.#.#.###...#.#...##...##",
    "#.....#...####.#....#.#........",
    "..#.....#...##.........###.....",
    "....#....#....#..#......#####.#",
    "###.....#..#.#.#......#.##.#...",
    "....#.##......#..#.#...........",
    ".#....#....#.#..#.......#...##.",
    "...................#.#.#..#....",
    "##...#.....#........#....#...#.",
    "........##......#...##.#..#.#.#",
    "#.#..###...#....#.#...#.......#",
    "#..........##......#..#..#.....",
    ".............#...##.#...#......",
    "#..#....##..#.........#..#.###.",
    ".....#..........#....##.#...##.",
    "###....................#.#.##..",
    "#........##...##......#....###.",
    "#....#.............#....#...#..",
    "##.......##.#.......#....#..#..",
    "##...#............#..#.#....##.",
    "..#.#..#...#####..........#....",
    "..#.........##.....#.#...####..",
    "....#..............#...........",
    "..#...#.#.#..#.......##.#.#.#..",
    "....#.##.....##..#.....#..####.",
    "#...#...#...#.......#.........#",
    "......#..#.####...###.#.#.....#",
    ".......#..#..#.....#.#..##.#..#",
    ".#......##..#............#.....",
    ".#........#.#....#....#........",
    ".....#.#..#.##.#..##....#..#...",
    "#.#...........#....##.....#....",
    "..#..#..##.###..##..#..###.#.##",
    "##.#..#...##.#.........#...#.#.",
    "......#..#..##...#....#...#.##.",
    "#.##.......................#...",
    ".......#..#..#.##..##......#...",
    "..#.#...#.....#..###....#...#..",
    "##..#.....#..#..#.##.....#...##",
    "#...##...###...#.#..###....#...",
    "...#.#.#..####.....#...##....#.",
    ".#.#..##.....#..#.....##..##..#",
    "#...#..........#.##.#.#........",
    "..##....#.##....#..##......#...",
    "....#..........###.....####..##",
    "...........###....##.#.#.#.#...",
    "...#......................####.",
    "#.#.#...#.#.#.#.#......#.....##",
    "..###...#.####...#..##..#....#.",
    "....#....#.......#...#.........",
    ".#.###.............##..#...#...",
    "....#.#....##...#.....#.##.....",
    "#.......##.....#.#.....#....##.",
    "....##.....###..#.#..#....#...#",
    "......#..##...#......#.....#.##",
    ".#.....#.##.###....#.....#..###",
    "...#..#.###.#....#..#..#...##.#",
    "...##..#...#..#.#.#..#...#.....",
    "##.####...##..#.#.#....#.......",
    "..##..#.#.......##.#......##.#.",
    "....##....#....#..#....#..##.#.",
    "..##..........##....#...#.#..#.",
    "#.#...#.#.###.#.#..##.#...#....",
    ".....#..#.............#...#...#",
    "....#.#..#...##...#....#.##....",
    "#..#...#.###.....#...#.....#.#.",
    "#####....#....#....#.......#.##",
    "#...##....##.#.#...#.....##.#..",
    "#.......#...#..#..#...#....#...",
    "....#......#.#..........#....##",
    "#.###...#.#..##..#.##........#.",
    "#..#.....##.......#..#..#.#....",
    "...#...#.##...#....#.#.#.#...#.",
    "...##..#.#....#......###......#",
    "#.#....#...#..#..#....#........",
    "..#..#.#...##..........#.###...",
    "#..........#...#..#....#....###",
    "..#..#.#....#..............#...",
    "...#........#...#.#....###.#..#",
    "....#.#.#................#..#.#",
    "..#........##.#....#.#..#......",
    "...##..#..#.......#..#......#.#",
    "..#..#....#.........#....#.##..",
    "#.....#....###.#..#..#...#...#.",
    "..#..##.###.#..##....#.###.....",
    "...#...####..#........###.#....",
    ".........#.#...#..#..#.#.......",
    ".##.........##.#..............#",
    "..#.#.#.....###........#.#.#..#",
    "....##..#....#....#.#..#.......",
    "#.#.....#...#........##........",
    ".##.#.#..#..#.#.#.........#....",
    "#.....#..#.##...#...#..........",
    "##..#....#....##.#..#.........#",
    "................#.##.#......#.#",
    "..#..#.#........##...###..#...#",
    "##........#.......#...##.##..#.",
    "##....#.....#..##....#.......#.",
    "#.#....#.#........#..#.........",
    "......##......#...#.....#.##...",
    "###....#..........##.#.#......#",
    "......#...###.........###..#...",
    ".####....#...##..#.#.....#...#.",
    ".##...#...###....#...#.#..###..",
    "#..#......##...#.###..###...#..",
    "#....#.#.#..#....##...#.##..#..",
    "..#.....#...#..........#.##.###",
    "#.....#....###.......##..##.#..",
    "#..##...#..#....#.###......#...",
    "#..#........##..#.....#.#.#....",
    "#.##.#.#..#....#.#.............",
    ".#...............#....##.......",
    ".#.##......##........#...#..#.#",
    ".#...#....#....#...#..#...##...",
    ".....#..###...##........#.#....",
    "...#.......#....##..#..#....#..",
    "...###....#........#..#.###.#..",
    "......##..##..............###.#",
    ".......#.####..##....#.#....#..",
    "#...#......#...#..#.....##....#",
    ".#..#..###....#..##.##.#.......",
    "#......##......#..##....#..##..",
    ".....#..#.#......##.##..##.....",
    "...#..#.......#......#.........",
    "....#..####......#..#....#...#.",
    "..#.#..#...#....#....#.......#.",
    "####..#........#.###...##.#.#.#",
    ".......##........#.#.#...##....",
    "...#.........#..#.#..##....#...",
    ".....#..#...#.#....#...#.#.##.#",
    "#..##.....#.....##.......#...#.",
    ".......##.#.#.....#....#......#",
    "...#...#.##...#......#....#....",
    "..#..#.#...#..#.....#...###.#..",
    ".........#...#..#.......##.....",
    "..##...................#..#.###",
    ".##.##..#.#...#.#....#.....##..",
    "#.#...##...#...#...##..#......#",
    "....#..#...#.....##.#.....#..##",
    "##.#..........###..#...#..#....",
    "...##....#.##....#......#......",
    ".....#.........#....#.#.......#",
    ".......#............#.#.....#..",
    "..#..#...#..#####..#....##.....",
    "...##......##...#.#........##..",
    ".....#..###...##.#.#.##.#...#..",
    "..#.#.#..##..#.##...##.#.#.....",
    "......##...#..##......#.#......",
    "......................#........",
    "#...#..#....#..#.#.##.#.....#.#",
    ".#......#.#....#.#.#..#....#...",
    ".#..#.#.#..#....#.............."
]

inp = [
    "....!!..!........!!...!.!..!.!!",
    ".!.!..!....!!....!...!..!!.....",
    "!!.!..!!..!...!..........!!.!..",
    ".!.!!.!!!!..!......!!!.........",
    "!.!.!...........!.....!...!....",
    "!.......!....!.!.!!..!!!..!!..!",
    ".!...!...!!....!.........!.....",
    "..........!!.!.!.....!....!.!..",
    ".......!!..!!...!.!.!...!......",
    ".!.!.!...!...!!...!.!!.!!..!...",
    "........!!.!.!.!!!.........!!..",
    "!.!..!.!.!.....!...!...!......!",
    ".!.!.!...!!......!...!.........",
    ".!..!!.!!.!...!...!!....!.!....",
    ".!!...!..!..!......!!.!!!....!!",
    ".....!...!.!!!.....!.!.........",
    "!.!!..!....!.!.!.!.............",
    "........!...!......!...!..!....",
    "!!..!!...!!.!!...!...!.!!!...!!",
    "!.!....!!.!...!!!......!..!.!..",
    "..!.....!.!!......!..........!.",
    "!.......!..!......!.....!....!.",
    ".....!!!...........!....!.!!...",
    "!.!........!!.......!.!...!.!!.",
    ".!.!.!........!........!.!.....",
    "!..!..!!.....!.!!!..!.!.!.!!..!",
    "..!.!...!..!!.!.!.!.......!!!..",
    "........!........!..!..!...!...",
    "!!............!...!..!!.!!...!.",
    "!....!.!.....!!...!............",
    "............!...!..!.!.!....!..",
    "!.!.!...!!.!!.!....!....!......",
    "................!!!.....!.....!",
    "!!.!!!!!.!..!...!!!..!...!!!...",
    "...!.....!...!.!....!...!..!...",
    ".......!....!!.!!.!.!!.........",
    "..!..!..!!.....!...!.!.....!...",
    "...!...!.!.!!.!..!!!.......!...",
    "...!...........!.!!!!!..!!..!..",
    "!.!...!........!!!!..!......!.!",
    "!..!.!!...........!.!......!.!!",
    "!.!..!....!!..!..!!.!..........",
    ".....!..!.....!........!!..!...",
    "...!!!.......!.!!.......!......",
    "...!!..!..!...!....!.!!!...!...",
    "....!!!!....!........!.!!.!.!.!",
    "!....!.....!.!!!.!!...!!..!!.!!",
    ".!!.!...!.!!.!......!..!!.!....",
    "...!.............!.............",
    "..!!..!!.!.....!........!!....!",
    "!.....!....!.......!!!!...!..!.",
    "..!...!..!...!...!!.!....!!....",
    ".!...!!....!....!..!....!......",
    "!!..!.!...!!......!..!.......!!",
    "..!...!.!!..!.....!.!...!..!.!.",
    "!..!!....!..........!..........",
    ".!........!..!......!......!.!.",
    "...!!.!.........!.!....!.!...!.",
    "!.....!.!..!...!...!..!...!...!",
    "!.........!.!.........!!.......",
    ".!.......!......!.........!!!..",
    ".!..!..!!...........!.....!..!.",
    ".!....................!.....!..",
    ".!!.....!....!....!.!!!.....!..",
    "...!!.!.....!.!....!.........!.",
    ".........!!.....!.....!.!!..!..",
    "......!......!.!..!..!!!...!..!",
    "..!!...!.!..!...!.!....!.......",
    "..!..!!.!!!.!..!..!..!......!..",
    ".....!!...!!.........!...!!...!",
    "!!!.!..!!....!!...!!.!..!!!....",
    "!...!.!..!!......!!...!.!..!...",
    "..........!....!!!....!........",
    "!.!.!.!.!.....!..!!.!!.....!...",
    ".!!.....!...!.....!......!.....",
    ".!..........!.!.............!..",
    ".!..!!..!.!..!!...!....!.!!...!",
    "..!.!..........!...!..........!",
    ".!.......!.......!...!..!.....!",
    "!!.!...!!...!......!.!..!......",
    "!!!!!..!....!..!...!...!.!.....",
    "....!.......!.!..!.............",
    "!..!..!.!.!!!!...!....!....!!..",
    "!..!.!!.!......!...!......!....",
    "!...!!.!!...!....!..........!!.",
    "..!..!.......!!.!....!...!.!...",
    ".....!.!!..............!!.....!",
    "..!!.!!...!!.....!.........!.!.",
    ".!....!!...!!...!!..!....!!..!.",
    ".!...!....!..!......!.!........",
    "!....!.!.!..............!....!!",
    "..!!..!..!....!!!!!.!....!.!.!!",
    "!....!...!.!!..!.!!.........!!!",
    "!..!..!....!...............!.!.",
    "!....!!...!!........!!.!!.!.!!.",
    "......!......!!....!!.....!.!!!",
    "!...!!..!..!.....!.!........!!.",
    "..!.!.!!...!...!....!..!!!...!.",
    "!..!!..!.!!!..!!.!.!....!......",
    "..!!!..!.!!........!!!.....!...",
    "!.............!.............!..",
    ".!.!!....!..!!.!...!....!.!!!!!",
    "!!!.....!!!.!......!!..!..!!...",
    ".!.!......!!.!....!....!.!..!..",
    "!!!..!..!....!......!!!.!!.....",
    "......!.......!......!..!!..!!.",
    "..!..!...!..!....!.!!....!.!..!",
    ".......!!..!........!.!.!!.....",
    ".!...!..!........!..!.!..!..!.!",
    ".!..!.!!.......!......!...!.!..",
    ".!!..!!......!!.!...!......!!!!",
    ".....!....!......!.....!......!",
    "..........!.!.!...!!.!..!.!....",
    "...!.......!!......!..!.!.!!...",
    ".!!!..!.!.!....................",
    "!!...!...!.!!............!.....",
    "....!....!.!!...!..!.!...!!....",
    "..!.!....!.!!!...!...!.!.!!!!.!",
    "..!..!.!...!.!......!!.........",
    "!..!..!!!!.!!.!.!..!!!....!...!",
    "....!..........!.!!.!..!.!.!.!.",
    "!.!.!!.........!.....!!...!..!!",
    "!......!...!.!!.!......!..!.!..",
    "!...!........!..!..!...!!...!..",
    ".....!.!!!!..!!..!.!.!!..!...!.",
    "!..!........!........!...!....!",
    "...........!..!.....!.!.!.!....",
    "....!......!....!...!....!!....",
    ".!.!..!...!.!....!..!.!....!!.!",
    "....!...!...!.!!..!...!..!!...!",
    "!!!!!!!...............!!.....!!",
    ".!.!..............!....!..!.!!!",
    "!......!.!......!!!....!!!.....",
    "!!..!...!.!!..!!..!!.!....!....",
    "!....!!..!..!...!.!.!...!......",
    "..........!..!.!!..!!.!!.!..!!.",
    "....!.!.!.....!!........!..!...",
    "..!!!...!.....!!.!!.....!!..!!.",
    "....!.!..!.!.......!.......!...",
    "..!!.!..!.....!!...!!!...!...!.",
    "..!.........!...!!...!...!..!..",
    "..!..!..!..!..!!.!...!!..!.!...",
    "...!!..!..!!..!..!!!!...!.....!",
    "............!............!!!...",
    ".!.!.!!!.!.....!.!.!..!.!!!..!.",
    "...!.........!.....!!!!........",
    "....!!.!..!!.!.............!...",
    "....!.!!.....!..!.....!......!!",
    "..........!.............!...!!.",
    "!..!.....!.......!!..!!!.......",
    "..!!.!...........!.......!..!..",
    "...!...!.!.!!.!!!....!.!..!....",
    "...!..........!!..!..!..!...!!!",
    ".........!.....!..!!.....!..!..",
    "!........!...!...!..!.!....!!..",
    ".!.!.....!!!!..!.!!.!..........",
    "!!!.......!!..!.!!...!.....!...",
    "..!!!.!!.!..!..!..!.....!!...!.",
    ".........!.....!!.!..!..!!.....",
    "!..!..!!...!!!..............!..",
    "!....!.!....!..!.....!..!!!!...",
    "!!!!..!.....!!...!..!.!.!.!...!",
    "...!....!.....!.!!.!.!.!....!!.",
    "..........!...!.....!!!....!.!!",
    "!....!.!.!....!..!..!.....!....",
    ".....!.!...!......!....!......!",
    ".!!!!....!!...!...!......!!..!.",
    ".!...!..!....!..!..............",
    "!!.!...!!...!.!!..!......!.....",
    "..!!!!.!!..!....!.!......!.!.!!",
    "........!.....!!...!.!..!!....!",
    "....!.!.!.!.!!!...!.!...!!...!!",
    "!.....!...!!!!.!....!.!........",
    "..!.....!...!!.........!!!.....",
    "....!....!....!..!......!!!!!.!",
    "!!!.....!..!.!.!......!.!!.!...",
    "....!.!!......!..!.!...........",
    ".!....!....!.!..!.......!...!!.",
    "...................!.!.!..!....",
    "!!...!.....!........!....!...!.",
    "........!!......!...!!.!..!.!.!",
    "!.!..!!!...!....!.!...!.......!",
    "!..........!!......!..!..!.....",
    ".............!...!!.!...!......",
    "!..!....!!..!.........!..!.!!!.",
    ".....!..........!....!!.!...!!.",
    "!!!....................!.!.!!..",
    "!........!!...!!......!....!!!.",
    "!....!.............!....!...!..",
    "!!.......!!.!.......!....!..!..",
    "!!...!............!..!.!....!!.",
    "..!.!..!...!!!!!..........!....",
    "..!.........!!.....!.!...!!!!..",
    "....!..............!...........",
    "..!...!.!.!..!.......!!.!.!.!..",
    "....!.!!.....!!..!.....!..!!!!.",
    "!...!...!...!.......!.........!",
    "......!..!.!!!!...!!!.!.!.....!",
    ".......!..!..!.....!.!..!!.!..!",
    ".!......!!..!............!.....",
    ".!........!.!....!....!........",
    ".....!.!..!.!!.!..!!....!..!...",
    "!.!...........!....!!.....!....",
    "..!..!..!!.!!!..!!..!..!!!.!.!!",
    "!!.!..!...!!.!.........!...!.!.",
    "......!..!..!!...!....!...!.!!.",
    "!.!!.......................!...",
    ".......!..!..!.!!..!!......!...",
    "..!.!...!.....!..!!!....!...!..",
    "!!..!.....!..!..!.!!.....!...!!",
    "!...!!...!!!...!.!..!!!....!...",
    "...!.!.!..!!!!.....!...!!....!.",
    ".!.!..!!.....!..!.....!!..!!..!",
    "!...!..........!.!!.!.!........",
    "..!!....!.!!....!..!!......!...",
    "....!..........!!!.....!!!!..!!",
    "...........!!!....!!.!.!.!.!...",
    "...!......................!!!!.",
    "!.!.!...!.!.!.!.!......!.....!!",
    "..!!!...!.!!!!...!..!!..!....!.",
    "....!....!.......!...!.........",
    ".!.!!!.............!!..!...!...",
    "....!.!....!!...!.....!.!!.....",
    "!.......!!.....!.!.....!....!!.",
    "....!!.....!!!..!.!..!....!...!",
    "......!..!!...!......!.....!.!!",
    ".!.....!.!!.!!!....!.....!..!!!",
    "...!..!.!!!.!....!..!..!...!!.!",
    "...!!..!...!..!.!.!..!...!.....",
    "!!.!!!!...!!..!.!.!....!.......",
    "..!!..!.!.......!!.!......!!.!.",
    "....!!....!....!..!....!..!!.!.",
    "..!!..........!!....!...!.!..!.",
    "!.!...!.!.!!!.!.!..!!.!...!....",
    ".....!..!.............!...!...!",
    "....!.!..!...!!...!....!.!!....",
    "!..!...!.!!!.....!...!.....!.!.",
    "!!!!!....!....!....!.......!.!!",
    "!...!!....!!.!.!...!.....!!.!..",
    "!.......!...!..!..!...!....!...",
    "....!......!.!..........!....!!",
    "!.!!!...!.!..!!..!.!!........!.",
    "!..!.....!!.......!..!..!.!....",
    "...!...!.!!...!....!.!.!.!...!.",
    "...!!..!.!....!......!!!......!",
    "!.!....!...!..!..!....!........",
    "..!..!.!...!!..........!.!!!...",
    "!..........!...!..!....!....!!!",
    "..!..!.!....!..............!...",
    "...!........!...!.!....!!!.!..!",
    "....!.!.!................!..!.!",
    "..!........!!.!....!.!..!......",
    "...!!..!..!.......!..!......!.!",
    "..!..!....!.........!....!.!!..",
    "!.....!....!!!.!..!..!...!...!.",
    "..!..!!.!!!.!..!!....!.!!!.....",
    "...!...!!!!..!........!!!.!....",
    ".........!.!...!..!..!.!.......",
    ".!!.........!!.!..............!",
    "..!.!.!.....!!!........!.!.!..!",
    "....!!..!....!....!.!..!.......",
    "!.!.....!...!........!!........",
    ".!!.!.!..!..!.!.!.........!....",
    "!.....!..!.!!...!...!..........",
    "!!..!....!....!!.!..!.........!",
    "................!.!!.!......!.!",
    "..!..!.!........!!...!!!..!...!",
    "!!........!.......!...!!.!!..!.",
    "!!....!.....!..!!....!.......!.",
    "!.!....!.!........!..!.........",
    "......!!......!...!.....!.!!...",
    "!!!....!..........!!.!.!......!",
    "......!...!!!.........!!!..!...",
    ".!!!!....!...!!..!.!.....!...!.",
    ".!!...!...!!!....!...!.!..!!!..",
    "!..!......!!...!.!!!..!!!...!..",
    "!....!.!.!..!....!!...!.!!..!..",
    "..!.....!...!..........!.!!.!!!",
    "!.....!....!!!.......!!..!!.!..",
    "!..!!...!..!....!.!!!......!...",
    "!..!........!!..!.....!.!.!....",
    "!.!!.!.!..!....!.!.............",
    ".!...............!....!!.......",
    ".!.!!......!!........!...!..!.!",
    ".!...!....!....!...!..!...!!...",
    ".....!..!!!...!!........!.!....",
    "...!.......!....!!..!..!....!..",
    "...!!!....!........!..!.!!!.!..",
    "......!!..!!..............!!!.!",
    ".......!.!!!!..!!....!.!....!..",
    "!...!......!...!..!.....!!....!",
    ".!..!..!!!....!..!!.!!.!.......",
    "!......!!......!..!!....!..!!..",
    ".....!..!.!......!!.!!..!!.....",
    "...!..!.......!......!.........",
    "....!..!!!!......!..!....!...!.",
    "..!.!..!...!....!....!.......!.",
    "!!!!..!........!.!!!...!!.!.!.!",
    ".......!!........!.!.!...!!....",
    "...!.........!..!.!..!!....!...",
    ".....!..!...!.!....!...!.!.!!.!",
    "!..!!.....!.....!!.......!...!.",
    ".......!!.!.!.....!....!......!",
    "...!...!.!!...!......!....!....",
    "..!..!.!...!..!.....!...!!!.!..",
    ".........!...!..!.......!!.....",
    "..!!...................!..!.!!!",
    ".!!.!!..!.!...!.!....!.....!!..",
    "!.!...!!...!...!...!!..!......!",
    "....!..!...!.....!!.!.....!..!!",
    "!!.!..........!!!..!...!..!....",
    "...!!....!.!!....!......!......",
    ".....!.........!....!.!.......!",
    ".......!............!.!.....!..",
    "..!..!...!..!!!!!..!....!!.....",
    "...!!......!!...!.!........!!..",
    ".....!..!!!...!!.!.!.!!.!...!..",
    "..!.!.!..!!..!.!!...!!.!.!.....",
    "......!!...!..!!......!.!......",
    "......................!........",
    "!...!..!....!..!.!.!!.!.....!.!",
    ".!......!.!....!.!.!..!....!...",
    ".!..!.!.!..!....!.............."
]
inp_l = """....##..#........##...#.#..#.##.#.#..#....##....#...#..##.....##.#..##..#...#..........##.#...#.##.####..#......###.........#.#.#...........#.....#...#....#.......#....#.#.##..###..##..#.#...#...##....#.........#...............##.#.#.....#....#.#.........##..##...#.#.#...#.......#.#.#...#...##...#.##.##..#...........##.#.#.###.........##..#.#..#.#.#.....#...#...#......#.#.#.#...##......#...#..........#..##.##.#...#...##....#.#.....##...#..#..#......##.###....##.....#...#.###.....#.#.........#.##..#....#.#.#.#.....................#...#......#...#..#....##..##...##.##...#...#.###...###.#....##.#...###......#..#.#....#.....#.##......#..........#.#.......#..#......#.....#....#......###...........#....#.##...#.#........##.......#.#...#.##..#.#.#........#........#.#.....#..#..##.....#.###..#.#.#.##..#..#.#...#..##.#.#.#.......###..........#........#..#..#...#...##............#...#..##.##...#.#....#.#.....##...#........................#...#..#.#.#....#..#.#.#...##.##.#....#....#......................###.....#.....###.#####.#..#...###..#...###......#.....#...#.#....#...#..#..........#....##.##.#.##...........#..#..##.....#...#.#.....#......#...#.#.##.#..###.......#......#...........#.#####..##..#..#.#...#........####..#......#.##..#.##...........#.#......#.###.#..#....##..#..##.#...............#..#.....#........##..#......###.......#.##.......#.........##..#..#...#....#.###...#.......####....#........#.##.#.#.##....#.....#.###.##...##..##.##.##.#...#.##.#......#..##.#.......#.............#...............##..##.#.....#........##....##.....#....#.......####...#..#...#...#..#...#...##.#....##.....#...##....#....#..#....#......##..#.#...##......#..#.......##..#...#.##..#.....#.#...#..#.#.#..##....#..........#...........#........#..#......#......#.#....##.#.........#.#....#.#...#.#.....#.#..#...#...#..#...#...##.........#.#.........##........#.......#......#.........###...#..#..##...........#.....#..#..#....................#.....#...##.....#....#....#.###.....#.....##.#.....#.#....#.........#..........##.....#.....#.##..#........#......#.#..#..###...#..#..##...#.#..#...#.#....#.........#..##.###.#..#..#..#......#.......##...##.........#...##...####.#..##....##...##.#..###....#...#.#..##......##...#.#..#.............#....###....#........#.#.#.#.#.....#..##.##.....#....##.....#...#.....#......#......#..........#.#.............#...#..##..#.#..##...#....#.##...#..#.#..........#...#..........#.#.......#.......#...#..#.....###.#...##...#......#.#..#......#####..#....#..#...#...#.#.........#.......#.#..#.............#..#..#.#.####...#....#....##..#..#.##.#......#...#......#....#...##.##...#....#..........##...#..#.......##.#....#...#.#........#.##..............##.....#..##.##...##.....#.........#.#..#....##...##...##..#....##..#..#...#....#..#......#.#........#....#.#.#..............#....##..##..#..#....#####.#....#.#.###....#...#.##..#.##.........####..#..#....#...............#.#.#....##...##........##.##.#.##.......#......##....##.....#.####...##..#..#.....#.#........##...#.#.##...#...#....#..###...#.#..##..#.###..##.#.#....#........###..#.##........###.....#...#.............#.............#...#.##....#..##.#...#....#.########.....###.#......##..#..##....#.#......##.#....#....#.#..#..###..#..#....#......###.##...........#.......#......#..##..##...#..#...#..#....#.##....#.#..#.......##..#........#.#.##......#...#..#........#..#.#..#..#.#.#..#.##.......#......#...#.#...##..##......##.#...#......####.....#....#......#.....#......#..........#.#.#...##.#..#.#.......#.......##......#..#.#.##....###..#.#.#....................##...#...#.##............#.........#....#.##...#..#.#...##......#.#....#.###...#...#.#.####.#..#..#.#...#.#......##.........#..#..####.##.#.#..###....#...#....#..........#.##.#..#.#.#.#.#.#.##.........#.....##...#..###......#...#.##.#......#..#.#..#...#........#..#..#...##...#.......#.####..##..#.#.##..#...#.#..#........#........#...#....#...........#..#.....#.#.#.#........#......#....#...#....##.....#.#..#...#.#....#..#.#....##.#....#...#...#.##..#...#..##...########...............##.....##.#.#..............#....#..#.####......#.#......###....###.....##..#...#.##..##..##.#....#....#....##..#..#...#.#.#...#................#..#.##..##.##.#..##.....#.#.#.....##........#..#.....###...#.....##.##.....##..##.....#.#..#.#.......#.......#.....##.#..#.....##...###...#...#...#.........#...##...#...#..#....#..#..#..#..##.#...##..#.#......##..#..##..#..####...#.....#............#............###....#.#.###.#.....#.#.#..#.###..#....#.........#.....####............##.#..##.#.............#.......#.##.....#..#.....#......##..........#.............#...##.#..#.....#.......##..###.........##.#...........#.......#..#.....#...#.#.##.###....#.#..#.......#..........##..#..#..#...###.........#.....#..##.....#..#..#........#...#...#..#.#....##...#.#.....####..#.##.#..........###.......##..#.##...#.....#.....###.##.#..#..#..#.....##...#..........#.....##.#..#..##.....#..#..##...###..............#..#....#.#....#..#.....#..####...####..#.....##...#..#.#.#.#...#...#....#.....#.##.#.#.#....##...........#...#.....###....#.###....#.#.#....#..#..#.....#.........#.#...#......#....#......#.####....##...#...#......##..#..#...#..#....#..#..............##.#...##...#.##..#......#.......####.##..#....#.#......#.#.##........#.....##...#.#..##....#....#.#.#.#.###...#.#...##...###.....#...####.#....#.#..........#.....#...##.........###.........#....#....#..#......#####.####.....#..#.#.#......#.##.#.......#.##......#..#.#............#....#....#.#..#.......#...##....................#.#.#..#....##...#.....#........#....#...#.........##......#...##.#..#.#.##.#..###...#....#.#...#.......##..........##......#..#..#..................#...##.#...#......#..#....##..#.........#..#.###......#..........#....##.#...##.###....................#.#.##..#........##...##......#....###.#....#.............#....#...#..##.......##.#.......#....#..#..##...#............#..#.#....##...#.#..#...#####..........#......#.........##.....#.#...####......#..............#.............#...#.#.#..#.......##.#.#.#......#.##.....##..#.....#..####.#...#...#...#.......#.........#......#..#.####...###.#.#.....#.......#..#..#.....#.#..##.#..#.#......##..#............#......#........#.#....#....#.............#.#..#.##.#..##....#..#...#.#...........#....##.....#......#..#..##.###..##..#..###.#.####.#..#...##.#.........#...#.#.......#..#..##...#....#...#.##.#.##.......................#..........#..#..#.##..##......#.....#.#...#.....#..###....#...#..##..#.....#..#..#.##.....#...###...##...###...#.#..###....#......#.#.#..####.....#...##....#..#.#..##.....#..#.....##..##..##...#..........#.##.#.#..........##....#.##....#..##......#.......#..........###.....####..##...........###....##.#.#.#.#......#......................####.#.#.#...#.#.#.#.#......#.....##..###...#.####...#..##..#....#.....#....#.......#...#..........#.###.............##..#...#.......#.#....##...#.....#.##.....#.......##.....#.#.....#....##.....##.....###..#.#..#....#...#......#..##...#......#.....#.##.#.....#.##.###....#.....#..###...#..#.###.#....#..#..#...##.#...##..#...#..#.#.#..#...#.....##.####...##..#.#.#....#.........##..#.#.......##.#......##.#.....##....#....#..#....#..##.#...##..........##....#...#.#..#.#.#...#.#.###.#.#..##.#...#.........#..#.............#...#...#....#.#..#...##...#....#.##....#..#...#.###.....#...#.....#.#.#####....#....#....#.......#.###...##....##.#.#...#.....##.#..#.......#...#..#..#...#....#.......#......#.#..........#....###.###...#.#..##..#.##........#.#..#.....##.......#..#..#.#.......#...#.##...#....#.#.#.#...#....##..#.#....#......###......##.#....#...#..#..#....#..........#..#.#...##..........#.###...#..........#...#..#....#....###..#..#.#....#..............#......#........#...#.#....###.#..#....#.#.#................#..#.#..#........##.#....#.#..#.........##..#..#.......#..#......#.#..#..#....#.........#....#.##..#.....#....###.#..#..#...#...#...#..##.###.#..##....#.###........#...####..#........###.#.............#.#...#..#..#.#........##.........##.#..............#..#.#.#.....###........#.#.#..#....##..#....#....#.#..#.......#.#.....#...#........##.........##.#.#..#..#.#.#.........#....#.....#..#.##...#...#..........##..#....#....##.#..#.........#................#.##.#......#.#..#..#.#........##...###..#...###........#.......#...##.##..#.##....#.....#..##....#.......#.#.#....#.#........#..#...............##......#...#.....#.##...###....#..........##.#.#......#......#...###.........###..#....####....#...##..#.#.....#...#..##...#...###....#...#.#..###..#..#......##...#.###..###...#..#....#.#.#..#....##...#.##..#....#.....#...#..........#.##.####.....#....###.......##..##.#..#..##...#..#....#.###......#...#..#........##..#.....#.#.#....#.##.#.#..#....#.#..............#...............#....##........#.##......##........#...#..#.#.#...#....#....#...#..#...##........#..###...##........#.#.......#.......#....##..#..#....#.....###....#........#..#.###.#........##..##..............###.#.......#.####..##....#.#....#..#...#......#...#..#.....##....#.#..#..###....#..##.##.#.......#......##......#..##....#..##.......#..#.#......##.##..##........#..#.......#......#.............#..####......#..#....#...#...#.#..#...#....#....#.......#.####..#........#.###...##.#.#.#.......##........#.#.#...##.......#.........#..#.#..##....#........#..#...#.#....#...#.#.##.##..##.....#.....##.......#...#........##.#.#.....#....#......#...#...#.##...#......#....#......#..#.#...#..#.....#...###.#...........#...#..#.......##.......##...................#..#.###.##.##..#.#...#.#....#.....##..#.#...##...#...#...##..#......#....#..#...#.....##.#.....#..####.#..........###..#...#..#.......##....#.##....#......#...........#.........#....#.#.......#.......#............#.#.....#....#..#...#..#####..#....##........##......##...#.#........##.......#..###...##.#.#.##.#...#....#.#.#..##..#.##...##.#.#...........##...#..##......#.#............................#........#...#..#....#..#.#.##.#.....#.#.#......#.#....#.#.#..#....#....#..#.#.#..#....#.............."""

def count_trees(i_step, j_step, inp):
    i, j, trees = 0, 0, 0
    row_len = len(inp[0])

    while i < len(inp):
        with_tree = False

        if row_len - j < j_step:
            j = j_step - (row_len - j) - j_step
        if inp[i][j] == "!":
            with_tree = True
            trees += 1

        #         print_tree(with_tree, j, inp[i])
        i += i_step
        j += j_step
    return trees

def print_tree(with_tree, j, inp):
    char = "+"
    if with_tree:
        char = "X"
    out = inp[:j] + char
    if j + 1 < len(inp):
        out += inp[j + 1:]
    print(out[:len(inp)])

if __name__=='__main__':
    i, trees = 0, 0
    i_step, j_step = 1, 3

    while i < len(inp_l):
        if inp_l[i] == "#":
            trees += 1
            print(i)
        i += i_step*31 + j_step

    print(trees)

    print(count_trees(1, 1, inp))
    print(count_trees(1, 3, inp))
    print(count_trees(1, 5, inp))
    print(count_trees(1, 7, inp))
    print(count_trees(2, 1, inp))
    print(93*164*82*91*44)

    print(inp[0])
    print_tree(True, 2, "....##..#........##...#.#..#.##")
    print_tree(False, 2, "....##..#........##...#.#..#.##")