#!/usr/bin/env python

players_list = [
    {
        "appearances": "963",
        "first_name": "Ryan",
        "goals": "168",
        "last_name": "Giggs",
        "nationality": "Wales"
    },
    {
        "appearances": "758",
        "first_name": "Bobby",
        "goals": "249",
        "last_name": "Charlton",
        "nationality": "England"
    },
    {
        "appearances": "718",
        "first_name": "Paul",
        "goals": "155",
        "last_name": "Scholes",
        "nationality": "England"
    },
    {
        "appearances": "688",
        "first_name": "Bill",
        "goals": "9",
        "last_name": "Foulkes",
        "nationality": "England"
    },
    {
        "appearances": "602",
        "first_name": "Gary",
        "goals": "7",
        "last_name": "Neville",
        "nationality": "England"
    },
    {
        "appearances": "559",
        "first_name": "Wayne",
        "goals": "253",
        "last_name": "Rooney",
        "nationality": "England"
    },
    {
        "appearances": "545",
        "first_name": "David",
        "goals": "0",
        "last_name": "de Gea",
        "nationality": "Spain"
    },
    {
        "appearances": "539",
        "first_name": "Alex",
        "goals": "2",
        "last_name": "Stepney",
        "nationality": "England"
    },
    {
        "appearances": "535",
        "first_name": "Tony",
        "goals": "2",
        "last_name": "Dunne",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "529",
        "first_name": "Denis",
        "goals": "33",
        "last_name": "Irwin",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "510",
        "first_name": "Joe",
        "goals": "168",
        "last_name": "Spence",
        "nationality": "England"
    },
    {
        "appearances": "485",
        "first_name": "Arthur",
        "goals": "7",
        "last_name": "Albiston",
        "nationality": "Scotland"
    },
    {
        "appearances": "480",
        "first_name": "Roy",
        "goals": "51",
        "last_name": "Keane",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "471",
        "first_name": "Brian",
        "goals": "127",
        "last_name": "McClair",
        "nationality": "Scotland"
    },
    {
        "appearances": "470",
        "first_name": "George",
        "goals": "179",
        "last_name": "Best",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "467",
        "first_name": "Mark",
        "goals": "163",
        "last_name": "Hughes",
        "nationality": "Wales"
    },
    {
        "appearances": "464",
        "first_name": "Michael",
        "goals": "24",
        "last_name": "Carrick",
        "nationality": "England"
    },
    {
        "appearances": "461",
        "first_name": "Bryan",
        "goals": "99",
        "last_name": "Robson",
        "nationality": "England"
    },
    {
        "appearances": "456",
        "first_name": "Martin",
        "goals": "4",
        "last_name": "Buchan",
        "nationality": "Scotland"
    },
    {
        "appearances": "455",
        "first_name": "Rio",
        "goals": "8",
        "last_name": "Ferdinand",
        "nationality": "England"
    },
    {
        "appearances": "449",
        "first_name": "Jack",
        "goals": "2",
        "last_name": "Silcock",
        "nationality": "England"
    },
    {
        "appearances": "437",
        "first_name": "Gary",
        "goals": "15",
        "last_name": "Pallister",
        "nationality": "England"
    },
    {
        "appearances": "426",
        "first_name": "Marcus",
        "goals": "138",
        "last_name": "Rashford",
        "nationality": "England"
    },
    {
        "appearances": "424",
        "first_name": "Jack",
        "goals": "211",
        "last_name": "Rowley",
        "nationality": "England"
    },
    {
        "appearances": "419",
        "first_name": "Sammy",
        "goals": "71",
        "last_name": "McIlroy",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "414",
        "first_name": "Steve",
        "goals": "51",
        "last_name": "Bruce",
        "nationality": "England"
    },
    {
        "appearances": "404",
        "first_name": "Denis",
        "goals": "237",
        "last_name": "Law",
        "nationality": "Scotland"
    },
    {
        "appearances": "401",
        "first_name": "Lou",
        "goals": "97",
        "last_name": "Macari",
        "nationality": "Scotland"
    },
    {
        "appearances": "398",
        "first_name": "Peter",
        "goals": "1",
        "last_name": "Schmeichel",
        "nationality": "Denmark"
    },
    {
        "appearances": "397",
        "first_name": "Paddy",
        "goals": "15",
        "last_name": "Crerand",
        "nationality": "Scotland"
    },
    {
        "appearances": "396",
        "first_name": "Steve",
        "goals": "70",
        "last_name": "Coppell",
        "nationality": "England"
    },
    {
        "appearances": "395",
        "first_name": "Nobby",
        "goals": "19",
        "last_name": "Stiles",
        "nationality": "England"
    },
    {
        "appearances": "394",
        "first_name": "David",
        "goals": "85",
        "last_name": "Beckham",
        "nationality": "England"
    },
    {
        "appearances": "393",
        "first_name": "John",
        "goals": "15",
        "last_name": "O'Shea",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "391",
        "first_name": "Allenby",
        "goals": "3",
        "last_name": "Chilton",
        "nationality": "England"
    },
    {
        "appearances": "387",
        "first_name": "Nicky",
        "goals": "26",
        "last_name": "Butt",
        "nationality": "England"
    },
    {
        "appearances": "386",
        "first_name": "Phil",
        "goals": "8",
        "last_name": "Neville",
        "nationality": "England"
    },
    {
        "appearances": "379",
        "first_name": "Patrice",
        "goals": "10",
        "last_name": "Evra",
        "nationality": "France"
    },
    {
        "appearances": "378",
        "first_name": "Mike",
        "goals": "7",
        "last_name": "Duxbury",
        "nationality": "England"
    },
    {
        "appearances": "375",
        "first_name": "Gary",
        "goals": "0",
        "last_name": "Bailey",
        "nationality": "England"
    },
    {
        "appearances": "366",
        "first_name": "Ole",
        "goals": "126",
        "last_name": "Gunnar Solskj\u00e6r",
        "nationality": "Norway"
    },
    {
        "appearances": "362",
        "first_name": "Wes",
        "goals": "5",
        "last_name": "Brown",
        "nationality": "England"
    },
    {
        "appearances": "361",
        "first_name": "Mika\u00ebl",
        "goals": "10",
        "last_name": "Silvestre",
        "nationality": "France"
    },
    {
        "appearances": "359",
        "first_name": "Shay",
        "goals": "6",
        "last_name": "Brennan",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "346",
        "first_name": "Cristiano",
        "goals": "145",
        "last_name": "Ronaldo",
        "nationality": "Portugal"
    },
    {
        "appearances": "344",
        "first_name": "Johnny",
        "goals": "17",
        "last_name": "Carey",
        "nationality": "Ireland\n Republic of Ireland"
    },
    {
        "appearances": "343",
        "first_name": "Stan",
        "goals": "148",
        "last_name": "Pearson",
        "nationality": "England"
    },
    {
        "appearances": "342",
        "first_name": "Darren",
        "goals": "24",
        "last_name": "Fletcher",
        "nationality": "Scotland"
    },
    {
        "appearances": "339",
        "first_name": "Antonio",
        "goals": "25",
        "last_name": "Valencia",
        "nationality": "Ecuador"
    },
    {
        "appearances": "335",
        "first_name": "Billy",
        "goals": "36",
        "last_name": "Meredith",
        "nationality": "Wales"
    },
    {
        "appearances": "335",
        "first_name": "David",
        "goals": "27",
        "last_name": "Sadler",
        "nationality": "England"
    },
    {
        "appearances": "328",
        "first_name": "Charlie",
        "goals": "0",
        "last_name": "Moore",
        "nationality": "England"
    },
    {
        "appearances": "326",
        "first_name": "Alf",
        "goals": "0",
        "last_name": "Steward",
        "nationality": "England"
    },
    {
        "appearances": "323",
        "first_name": "Chris",
        "goals": "18",
        "last_name": "Smalling",
        "nationality": "England"
    },
    {
        "appearances": "322",
        "first_name": "Lal",
        "goals": "7",
        "last_name": "Hilditch",
        "nationality": "England"
    },
    {
        "appearances": "319",
        "first_name": "George",
        "goals": "100",
        "last_name": "Wall",
        "nationality": "England"
    },
    {
        "appearances": "318",
        "first_name": "Anthony",
        "goals": "90",
        "last_name": "Martial",
        "nationality": "France"
    },
    {
        "appearances": "310",
        "first_name": "Fred",
        "goals": "9",
        "last_name": "Erentz",
        "nationality": "Scotland"
    },
    {
        "appearances": "309",
        "first_name": "Alex",
        "goals": "10",
        "last_name": "Bell",
        "nationality": "Scotland"
    },
    {
        "appearances": "302",
        "first_name": "Charlie",
        "goals": "23",
        "last_name": "Roberts",
        "nationality": "England"
    },
    {
        "appearances": "301",
        "first_name": "Ray",
        "goals": "3",
        "last_name": "Bennion",
        "nationality": "Wales"
    },
    {
        "appearances": "301",
        "first_name": "Bruno",
        "goals": "100",
        "last_name": "Fernandes",
        "nationality": "Portugal"
    },
    {
        "appearances": "300",
        "first_name": "Nemanja",
        "goals": "21",
        "last_name": "Vidi\u0107",
        "nationality": "Serbia and Montenegro\n Serbia"
    },
    {
        "appearances": "296",
        "first_name": "Willie",
        "goals": "34",
        "last_name": "Morgan",
        "nationality": "Scotland"
    },
    {
        "appearances": "296",
        "first_name": "Luke",
        "goals": "4",
        "last_name": "Shaw",
        "nationality": "England"
    },
    {
        "appearances": "293",
        "first_name": "Dennis",
        "goals": "179",
        "last_name": "Viollet",
        "nationality": "England"
    },
    {
        "appearances": "289",
        "first_name": "Kevin",
        "goals": "24",
        "last_name": "Moran",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "288",
        "first_name": "Frank",
        "goals": "78",
        "last_name": "Stapleton",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "285",
        "first_name": "Juan",
        "goals": "51",
        "last_name": "Mata",
        "nationality": "Spain"
    },
    {
        "appearances": "284",
        "first_name": "John",
        "goals": "30",
        "last_name": "Aston Sr.",
        "nationality": "England"
    },
    {
        "appearances": "284",
        "first_name": "Victor",
        "goals": "4",
        "last_name": "Lindel\u00f6f",
        "nationality": "Sweden"
    },
    {
        "appearances": "281",
        "first_name": "Paul",
        "goals": "29",
        "last_name": "Ince",
        "nationality": "England"
    },
    {
        "appearances": "280",
        "first_name": "Roger",
        "goals": "20",
        "last_name": "Byrne",
        "nationality": "England"
    },
    {
        "appearances": "276",
        "first_name": "Johnny",
        "goals": "45",
        "last_name": "Berry",
        "nationality": "England"
    },
    {
        "appearances": "275",
        "first_name": "Henry",
        "goals": "4",
        "last_name": "Cockburn",
        "nationality": "England"
    },
    {
        "appearances": "275",
        "first_name": "Andy",
        "goals": "121",
        "last_name": "Cole",
        "nationality": "England"
    },
    {
        "appearances": "274",
        "first_name": "Norman",
        "goals": "67",
        "last_name": "Whiteside",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "271",
        "first_name": "Brian",
        "goals": "17",
        "last_name": "Greenhoff",
        "nationality": "England"
    },
    {
        "appearances": "270",
        "first_name": "George",
        "goals": "9",
        "last_name": "Stacey",
        "nationality": "England"
    },
    {
        "appearances": "266",
        "first_name": "Harry",
        "goals": "0",
        "last_name": "Moger",
        "nationality": "England"
    },
    {
        "appearances": "266",
        "first_name": "Brian",
        "goals": "70",
        "last_name": "Kidd",
        "nationality": "England"
    },
    {
        "appearances": "266",
        "first_name": "Edwin",
        "goals": "0",
        "last_name": "van der Sar",
        "nationality": "Netherlands"
    },
    {
        "appearances": "265",
        "first_name": "David",
        "goals": "145",
        "last_name": "Herd",
        "nationality": "Scotland"
    },
    {
        "appearances": "263",
        "first_name": "Lee",
        "goals": "36",
        "last_name": "Sharpe",
        "nationality": "England"
    },
    {
        "appearances": "261",
        "first_name": "Ashley",
        "goals": "19",
        "last_name": "Young",
        "nationality": "England"
    },
    {
        "appearances": "257",
        "first_name": "Walter",
        "goals": "8",
        "last_name": "Cartwright",
        "nationality": "England"
    },
    {
        "appearances": "255",
        "first_name": "Scott",
        "goals": "29",
        "last_name": "McTominay",
        "nationality": "Scotland"
    },
    {
        "appearances": "254",
        "first_name": "Dick",
        "goals": "11",
        "last_name": "Duckworth",
        "nationality": "England"
    },
    {
        "appearances": "253",
        "first_name": "Harry",
        "goals": "17",
        "last_name": "Maguire",
        "nationality": "England"
    },
    {
        "appearances": "250",
        "first_name": "Stewart",
        "goals": "16",
        "last_name": "Houston",
        "nationality": "Scotland"
    },
    {
        "appearances": "248",
        "first_name": "Jimmy",
        "goals": "6",
        "last_name": "Nicholl",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "247",
        "first_name": "Sandy",
        "goals": "101",
        "last_name": "Turnbull",
        "nationality": "Scotland"
    },
    {
        "appearances": "247",
        "first_name": "Harry",
        "goals": "0",
        "last_name": "Gregg",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "245",
        "first_name": "Clayton",
        "goals": "26",
        "last_name": "Blackmore",
        "nationality": "Wales"
    },
    {
        "appearances": "241",
        "first_name": "Jonny",
        "goals": "8",
        "last_name": "Evans",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "233",
        "first_name": "Paul",
        "goals": "39",
        "last_name": "Pogba",
        "nationality": "France"
    },
    {
        "appearances": "232",
        "first_name": "Jesse",
        "goals": "35",
        "last_name": "Lingard",
        "nationality": "England"
    },
    {
        "appearances": "230",
        "first_name": "Mr.",
        "goals": "40",
        "last_name": "Nani",
        "nationality": "Portugal"
    },
    {
        "appearances": "229",
        "first_name": "Gordon",
        "goals": "26",
        "last_name": "McQueen",
        "nationality": "Scotland"
    },
    {
        "appearances": "229",
        "first_name": "Phil",
        "goals": "6",
        "last_name": "Jones",
        "nationality": "England"
    },
    {
        "appearances": "219",
        "first_name": "Ruud",
        "goals": "150",
        "last_name": "van Nistelrooy",
        "nationality": "Netherlands"
    },
    {
        "appearances": "217",
        "first_name": "Diogo",
        "goals": "9",
        "last_name": "Dalot",
        "nationality": "Portugal"
    },
    {
        "appearances": "213",
        "first_name": "Mr.",
        "goals": "14",
        "last_name": "Fred",
        "nationality": "Brazil"
    },
    {
        "appearances": "212",
        "first_name": "Jack",
        "goals": "0",
        "last_name": "Crompton",
        "nationality": "England"
    },
    {
        "appearances": "209",
        "first_name": "George",
        "goals": "1",
        "last_name": "Vose",
        "nationality": "England"
    },
    {
        "appearances": "208",
        "first_name": "Ray",
        "goals": "0",
        "last_name": "Wood",
        "nationality": "England"
    },
    {
        "appearances": "205",
        "first_name": "John",
        "goals": "8",
        "last_name": "Grimwood",
        "nationality": "England"
    },
    {
        "appearances": "205",
        "first_name": "Park",
        "goals": "27",
        "last_name": "Ji-sung",
        "nationality": "South Korea"
    },
    {
        "appearances": "201",
        "first_name": "Gordon",
        "goals": "38",
        "last_name": "Strachan",
        "nationality": "Scotland"
    },
    {
        "appearances": "200",
        "first_name": "Harry",
        "goals": "1",
        "last_name": "Stafford",
        "nationality": "England"
    },
    {
        "appearances": "200",
        "first_name": "Tom",
        "goals": "0",
        "last_name": "Jones",
        "nationality": "Wales"
    },
    {
        "appearances": "199",
        "first_name": "Jack",
        "goals": "0",
        "last_name": "Mew",
        "nationality": "England"
    },
    {
        "appearances": "199",
        "first_name": "Remi",
        "goals": "12",
        "last_name": "Moses",
        "nationality": "England"
    },
    {
        "appearances": "199",
        "first_name": "Paul",
        "goals": "16",
        "last_name": "McGrath",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "197",
        "first_name": "Frank",
        "goals": "5",
        "last_name": "Mann",
        "nationality": "England"
    },
    {
        "appearances": "195",
        "first_name": "Tom",
        "goals": "41",
        "last_name": "Manley",
        "nationality": "England"
    },
    {
        "appearances": "194",
        "first_name": "Maurice",
        "goals": "14",
        "last_name": "Setters",
        "nationality": "England"
    },
    {
        "appearances": "194",
        "first_name": "Ray",
        "goals": "10",
        "last_name": "Wilkins",
        "nationality": "England"
    },
    {
        "appearances": "191",
        "first_name": "Alex",
        "goals": "14",
        "last_name": "Downie",
        "nationality": "Scotland"
    },
    {
        "appearances": "191",
        "first_name": "Tommy",
        "goals": "131",
        "last_name": "Taylor",
        "nationality": "England"
    },
    {
        "appearances": "190",
        "first_name": "Aaron",
        "goals": "2",
        "last_name": "Wan-Bissaka",
        "nationality": "DR Congo"
    },
    {
        "appearances": "189",
        "first_name": "Ander",
        "goals": "20",
        "last_name": "Herrera",
        "nationality": "Spain"
    },
    {
        "appearances": "189",
        "first_name": "Nemanja",
        "goals": "4",
        "last_name": "Mati\u0107",
        "nationality": "Serbia"
    },
    {
        "appearances": "187",
        "first_name": "John",
        "goals": "27",
        "last_name": "Aston Jr.",
        "nationality": "England"
    },
    {
        "appearances": "185",
        "first_name": "Eric",
        "goals": "82",
        "last_name": "Cantona",
        "nationality": "France"
    },
    {
        "appearances": "184",
        "first_name": "Jimmy",
        "goals": "28",
        "last_name": "Delaney",
        "nationality": "Scotland"
    },
    {
        "appearances": "184",
        "first_name": "Albert",
        "goals": "56",
        "last_name": "Quixall",
        "nationality": "England"
    },
    {
        "appearances": "182",
        "first_name": "Bill",
        "goals": "15",
        "last_name": "McKay",
        "nationality": "Scotland"
    },
    {
        "appearances": "181",
        "first_name": "Enoch",
        "goals": "80",
        "last_name": "West",
        "nationality": "England"
    },
    {
        "appearances": "181",
        "first_name": "Mr.",
        "goals": "9",
        "last_name": "Anderson",
        "nationality": "Brazil"
    },
    {
        "appearances": "180",
        "first_name": "Harry",
        "goals": "55",
        "last_name": "Rowley",
        "nationality": "England"
    },
    {
        "appearances": "180",
        "first_name": "Stuart",
        "goals": "66",
        "last_name": "Pearson",
        "nationality": "England"
    },
    {
        "appearances": "179",
        "first_name": "Alf",
        "goals": "35",
        "last_name": "Schofield",
        "nationality": "England"
    },
    {
        "appearances": "177",
        "first_name": "Duncan",
        "goals": "21",
        "last_name": "Edwards",
        "nationality": "England"
    },
    {
        "appearances": "177",
        "first_name": "Marouane",
        "goals": "22",
        "last_name": "Fellaini",
        "nationality": "Belgium"
    },
    {
        "appearances": "176",
        "first_name": "Jesper",
        "goals": "24",
        "last_name": "Olsen",
        "nationality": "Denmark"
    },
    {
        "appearances": "175",
        "first_name": "Billy",
        "goals": "30",
        "last_name": "Griffiths",
        "nationality": "England"
    },
    {
        "appearances": "175",
        "first_name": "Frank",
        "goals": "52",
        "last_name": "McPherson",
        "nationality": "England"
    },
    {
        "appearances": "174",
        "first_name": "Joe",
        "goals": "100",
        "last_name": "Cassidy",
        "nationality": "Scotland"
    },
    {
        "appearances": "173",
        "first_name": "Jack",
        "goals": "1",
        "last_name": "Griffiths",
        "nationality": "England"
    },
    {
        "appearances": "170",
        "first_name": "Mr.",
        "goals": "5",
        "last_name": "Rafael",
        "nationality": "Brazil"
    },
    {
        "appearances": "162",
        "first_name": "Charlie",
        "goals": "61",
        "last_name": "Mitten",
        "nationality": "England"
    },
    {
        "appearances": "161",
        "first_name": "Steve",
        "goals": "4",
        "last_name": "James",
        "nationality": "England"
    },
    {
        "appearances": "161",
        "first_name": "Andrei",
        "goals": "36",
        "last_name": "Kanchelskis",
        "nationality": "Soviet Union\n CIS\n Russia"
    },
    {
        "appearances": "160",
        "first_name": "Teddy",
        "goals": "18",
        "last_name": "Partridge",
        "nationality": "England"
    },
    {
        "appearances": "157",
        "first_name": "James",
        "goals": "12",
        "last_name": "McNaught",
        "nationality": "Scotland"
    },
    {
        "appearances": "157",
        "first_name": "Billy",
        "goals": "42",
        "last_name": "Bryant",
        "nationality": "England"
    },
    {
        "appearances": "157",
        "first_name": "Javier",
        "goals": "59",
        "last_name": "Hern\u00e1ndez",
        "nationality": "Mexico"
    },
    {
        "appearances": "156",
        "first_name": "Francis",
        "goals": "7",
        "last_name": "Burns",
        "nationality": "Scotland"
    },
    {
        "appearances": "155",
        "first_name": "Bob",
        "goals": "66",
        "last_name": "Donaldson",
        "nationality": "Scotland"
    },
    {
        "appearances": "153",
        "first_name": "Arthur",
        "goals": "50",
        "last_name": "Lochhead",
        "nationality": "Scotland"
    },
    {
        "appearances": "153",
        "first_name": "Teddy",
        "goals": "46",
        "last_name": "Sheringham",
        "nationality": "England"
    },
    {
        "appearances": "152",
        "first_name": "Billy",
        "goals": "7",
        "last_name": "Morgan",
        "nationality": "England"
    },
    {
        "appearances": "152",
        "first_name": "Frank",
        "goals": "4",
        "last_name": "Barson",
        "nationality": "England"
    },
    {
        "appearances": "152",
        "first_name": "Dwight",
        "goals": "66",
        "last_name": "Yorke",
        "nationality": "Trinidad and Tobago"
    },
    {
        "appearances": "150",
        "first_name": "David",
        "goals": "28",
        "last_name": "Pegg",
        "nationality": "England"
    },
    {
        "appearances": "150",
        "first_name": "Ronny",
        "goals": "9",
        "last_name": "Johnsen",
        "nationality": "Norway"
    },
    {
        "appearances": "149",
        "first_name": "Dimitar",
        "goals": "56",
        "last_name": "Berbatov",
        "nationality": "Bulgaria"
    },
    {
        "appearances": "147",
        "first_name": "Jimmy",
        "goals": "52",
        "last_name": "Hanson",
        "nationality": "England"
    },
    {
        "appearances": "147",
        "first_name": "John",
        "goals": "10",
        "last_name": "Fitzpatrick",
        "nationality": "Scotland"
    },
    {
        "appearances": "146",
        "first_name": "Noel",
        "goals": "8",
        "last_name": "Cantwell",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "146",
        "first_name": "Mike",
        "goals": "3",
        "last_name": "Phelan",
        "nationality": "England"
    },
    {
        "appearances": "146",
        "first_name": "Paul",
        "goals": "2",
        "last_name": "Parker",
        "nationality": "England"
    },
    {
        "appearances": "144",
        "first_name": "Alejandro",
        "goals": "26",
        "last_name": "Garnacho",
        "nationality": "Argentina"
    },
    {
        "appearances": "142",
        "first_name": "Gerry",
        "goals": "32",
        "last_name": "Daly",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "142",
        "first_name": "Danny",
        "goals": "29",
        "last_name": "Welbeck",
        "nationality": "England"
    },
    {
        "appearances": "141",
        "first_name": "Daley",
        "goals": "6",
        "last_name": "Blind",
        "nationality": "Netherlands"
    },
    {
        "appearances": "140",
        "first_name": "Jack",
        "goals": "3",
        "last_name": "Wilson",
        "nationality": "England"
    },
    {
        "appearances": "139",
        "first_name": "Fabien",
        "goals": "0",
        "last_name": "Barthez",
        "nationality": "France"
    },
    {
        "appearances": "136",
        "first_name": "Frank",
        "goals": "0",
        "last_name": "Barrett",
        "nationality": "Scotland"
    },
    {
        "appearances": "135",
        "first_name": "Harry",
        "goals": "13",
        "last_name": "Thomas",
        "nationality": "Wales"
    },
    {
        "appearances": "134",
        "first_name": "Bob",
        "goals": "3",
        "last_name": "Bonthron",
        "nationality": "Scotland"
    },
    {
        "appearances": "134",
        "first_name": "Gordon",
        "goals": "51",
        "last_name": "Hill",
        "nationality": "England"
    },
    {
        "appearances": "134",
        "first_name": "Mr.",
        "goals": "20",
        "last_name": "Casemiro",
        "nationality": "Brazil"
    },
    {
        "appearances": "130",
        "first_name": "Mason",
        "goals": "35",
        "last_name": "Greenwood",
        "nationality": "England"
    },
    {
        "appearances": "128",
        "first_name": "Vince",
        "goals": "2",
        "last_name": "Hayes",
        "nationality": "England"
    },
    {
        "appearances": "127",
        "first_name": "William",
        "goals": "33",
        "last_name": "Bryant",
        "nationality": "England"
    },
    {
        "appearances": "127",
        "first_name": "Albert",
        "goals": "35",
        "last_name": "Scanlon",
        "nationality": "England"
    },
    {
        "appearances": "127",
        "first_name": "Jaap",
        "goals": "1",
        "last_name": "Stam",
        "nationality": "Netherlands"
    },
    {
        "appearances": "126",
        "first_name": "Joe",
        "goals": "41",
        "last_name": "Jordan",
        "nationality": "Scotland"
    },
    {
        "appearances": "126",
        "first_name": "Quinton",
        "goals": "11",
        "last_name": "Fortune",
        "nationality": "South Africa"
    },
    {
        "appearances": "125",
        "first_name": "Harold",
        "goals": "56",
        "last_name": "Halse",
        "nationality": "England"
    },
    {
        "appearances": "124",
        "first_name": "Louis",
        "goals": "42",
        "last_name": "Saha",
        "nationality": "France"
    },
    {
        "appearances": "123",
        "first_name": "Jimmy",
        "goals": "36",
        "last_name": "Greenhoff",
        "nationality": "England"
    },
    {
        "appearances": "122",
        "first_name": "Jack",
        "goals": "46",
        "last_name": "Picken",
        "nationality": "Scotland"
    },
    {
        "appearances": "122",
        "first_name": "Jack",
        "goals": "0",
        "last_name": "Mellor",
        "nationality": "England"
    },
    {
        "appearances": "122",
        "first_name": "Billy",
        "goals": "2",
        "last_name": "McGlen",
        "nationality": "England"
    },
    {
        "appearances": "122",
        "first_name": "Marcos",
        "goals": "2",
        "last_name": "Rojo",
        "nationality": "Argentina"
    },
    {
        "appearances": "121",
        "first_name": "Jack",
        "goals": "58",
        "last_name": "Peddie",
        "nationality": "Scotland"
    },
    {
        "appearances": "121",
        "first_name": "Mark",
        "goals": "1",
        "last_name": "Jones",
        "nationality": "England"
    },
    {
        "appearances": "120",
        "first_name": "George",
        "goals": "49",
        "last_name": "Mutch",
        "nationality": "Scotland"
    },
    {
        "appearances": "120",
        "first_name": "John",
        "goals": "4",
        "last_name": "Gidman",
        "nationality": "England"
    },
    {
        "appearances": "119",
        "first_name": "David",
        "goals": "0",
        "last_name": "Gaskell",
        "nationality": "England"
    },
    {
        "appearances": "119",
        "first_name": "Alex",
        "goals": "5",
        "last_name": "Forsyth",
        "nationality": "Scotland"
    },
    {
        "appearances": "119",
        "first_name": "Mal",
        "goals": "0",
        "last_name": "Donaghy",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "118",
        "first_name": "David",
        "goals": "8",
        "last_name": "May",
        "nationality": "England"
    },
    {
        "appearances": "117",
        "first_name": "Dick",
        "goals": "0",
        "last_name": "Holden",
        "nationality": "England"
    },
    {
        "appearances": "117",
        "first_name": "Jackie",
        "goals": "27",
        "last_name": "Blanchflower",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "116",
        "first_name": "Hugh",
        "goals": "12",
        "last_name": "McLenahan",
        "nationality": "England"
    },
    {
        "appearances": "116",
        "first_name": "George",
        "goals": "4",
        "last_name": "McLachlan",
        "nationality": "Scotland"
    },
    {
        "appearances": "116",
        "first_name": "Johnny",
        "goals": "37",
        "last_name": "Downie",
        "nationality": "Scotland"
    },
    {
        "appearances": "115",
        "first_name": "Jack",
        "goals": "2",
        "last_name": "Warner",
        "nationality": "Wales"
    },
    {
        "appearances": "115",
        "first_name": "Don",
        "goals": "0",
        "last_name": "Gibson",
        "nationality": "England"
    },
    {
        "appearances": "115",
        "first_name": "Johnny",
        "goals": "13",
        "last_name": "Giles",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "113",
        "first_name": "John",
        "goals": "35",
        "last_name": "Connelly",
        "nationality": "England"
    },
    {
        "appearances": "113",
        "first_name": "Eric",
        "goals": "1",
        "last_name": "Bailly",
        "nationality": "Ivory Coast"
    },
    {
        "appearances": "112",
        "first_name": "Bobby",
        "goals": "0",
        "last_name": "Beale",
        "nationality": "England"
    },
    {
        "appearances": "110",
        "first_name": "James",
        "goals": "1",
        "last_name": "Brown",
        "nationality": "Scotland"
    },
    {
        "appearances": "110",
        "first_name": "David",
        "goals": "8",
        "last_name": "McCreery",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "110",
        "first_name": "Mickey",
        "goals": "15",
        "last_name": "Thomas",
        "nationality": "Wales"
    },
    {
        "appearances": "110",
        "first_name": "Graeme",
        "goals": "1",
        "last_name": "Hogg",
        "nationality": "Scotland"
    },
    {
        "appearances": "110",
        "first_name": "Neil",
        "goals": "11",
        "last_name": "Webb",
        "nationality": "England"
    },
    {
        "appearances": "109",
        "first_name": "Tommy",
        "goals": "57",
        "last_name": "Bamford",
        "nationality": "Wales"
    },
    {
        "appearances": "109",
        "first_name": "Lee",
        "goals": "2",
        "last_name": "Martin",
        "nationality": "England"
    },
    {
        "appearances": "108",
        "first_name": "Eddie",
        "goals": "2",
        "last_name": "Colman",
        "nationality": "England"
    },
    {
        "appearances": "107",
        "first_name": "Freddie",
        "goals": "8",
        "last_name": "Goodwin",
        "nationality": "England"
    },
    {
        "appearances": "107",
        "first_name": "Ashley",
        "goals": "11",
        "last_name": "Grimes",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "107",
        "first_name": "Christian",
        "goals": "8",
        "last_name": "Eriksen",
        "nationality": "Denmark"
    },
    {
        "appearances": "106",
        "first_name": "Arthur",
        "goals": "6",
        "last_name": "Whalley",
        "nationality": "England"
    },
    {
        "appearances": "106",
        "first_name": "Ronnie",
        "goals": "2",
        "last_name": "Cope",
        "nationality": "England"
    },
    {
        "appearances": "106",
        "first_name": "Peter",
        "goals": "26",
        "last_name": "Davenport",
        "nationality": "England"
    },
    {
        "appearances": "105",
        "first_name": "Robin",
        "goals": "58",
        "last_name": "van Persie",
        "nationality": "Netherlands"
    },
    {
        "appearances": "103",
        "first_name": "Henning",
        "goals": "3",
        "last_name": "Berg",
        "nationality": "Norway"
    },
    {
        "appearances": "102",
        "first_name": "George",
        "goals": "0",
        "last_name": "Perrins",
        "nationality": "England"
    },
    {
        "appearances": "102",
        "first_name": "Andr\u00e9",
        "goals": "0",
        "last_name": "Onana",
        "nationality": "Cameroon"
    },
    {
        "appearances": "101",
        "first_name": "Dick",
        "goals": "37",
        "last_name": "Smith",
        "nationality": "England"
    },
    {
        "appearances": "101",
        "first_name": "Tommy",
        "goals": "67",
        "last_name": "Reid",
        "nationality": "Scotland"
    },
    {
        "appearances": "99",
        "first_name": "Carlos",
        "goals": "34",
        "last_name": "Tevez",
        "nationality": "Argentina"
    },
    {
        "appearances": "98",
        "first_name": "Billy",
        "goals": "52",
        "last_name": "Whelan",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "98",
        "first_name": "Arnold",
        "goals": "18",
        "last_name": "M\u00fchren",
        "nationality": "Netherlands"
    },
    {
        "appearances": "98",
        "first_name": "Diego",
        "goals": "17",
        "last_name": "Forl\u00e1n",
        "nationality": "Uruguay"
    },
    {
        "appearances": "97",
        "first_name": "Tony",
        "goals": "1",
        "last_name": "Young",
        "nationality": "England"
    },
    {
        "appearances": "96",
        "first_name": "Charlie",
        "goals": "1",
        "last_name": "Radford",
        "nationality": "England"
    },
    {
        "appearances": "96",
        "first_name": "Hubert",
        "goals": "4",
        "last_name": "Redwood",
        "nationality": "England"
    },
    {
        "appearances": "96",
        "first_name": "Romelu",
        "goals": "42",
        "last_name": "Lukaku",
        "nationality": "Belgium"
    },
    {
        "appearances": "96",
        "first_name": "Mr.",
        "goals": "12",
        "last_name": "Antony",
        "nationality": "Brazil"
    },
    {
        "appearances": "95",
        "first_name": "Billy",
        "goals": "6",
        "last_name": "Draycott",
        "nationality": "England"
    },
    {
        "appearances": "95",
        "first_name": "Jeff",
        "goals": "0",
        "last_name": "Whitefoot",
        "nationality": "England"
    },
    {
        "appearances": "95",
        "first_name": "Colin",
        "goals": "9",
        "last_name": "Gibson",
        "nationality": "England"
    },
    {
        "appearances": "95",
        "first_name": "Rapha\u00ebl",
        "goals": "2",
        "last_name": "Varane",
        "nationality": "France"
    },
    {
        "appearances": "95",
        "first_name": "Rasmus",
        "goals": "26",
        "last_name": "H\u00f8jlund",
        "nationality": "Denmark"
    },
    {
        "appearances": "94",
        "first_name": "Jim",
        "goals": "0",
        "last_name": "Leighton",
        "nationality": "Scotland"
    },
    {
        "appearances": "93",
        "first_name": "Johnny",
        "goals": "35",
        "last_name": "Morris",
        "nationality": "England"
    },
    {
        "appearances": "93",
        "first_name": "Alex",
        "goals": "54",
        "last_name": "Dawson",
        "nationality": "Scotland"
    },
    {
        "appearances": "93",
        "first_name": "Alan",
        "goals": "12",
        "last_name": "Smith",
        "nationality": "England"
    },
    {
        "appearances": "92",
        "first_name": "George",
        "goals": "0",
        "last_name": "Roughton",
        "nationality": "England"
    },
    {
        "appearances": "92",
        "first_name": "Matteo",
        "goals": "1",
        "last_name": "Darmian",
        "nationality": "Italy"
    },
    {
        "appearances": "91",
        "first_name": "Lisandro",
        "goals": "3",
        "last_name": "Mart\u00ednez",
        "nationality": "Argentina"
    },
    {
        "appearances": "90",
        "first_name": "Tom",
        "goals": "16",
        "last_name": "Smith",
        "nationality": "England"
    },
    {
        "appearances": "89",
        "first_name": "Matthew",
        "goals": "21",
        "last_name": "Gillespie",
        "nationality": "Scotland"
    },
    {
        "appearances": "87",
        "first_name": "Willie",
        "goals": "5",
        "last_name": "Stewart",
        "nationality": "Scotland"
    },
    {
        "appearances": "87",
        "first_name": "Alan",
        "goals": "21",
        "last_name": "Gowling",
        "nationality": "England"
    },
    {
        "appearances": "86",
        "first_name": "Jimmy",
        "goals": "2",
        "last_name": "Hodge",
        "nationality": "Scotland"
    },
    {
        "appearances": "86",
        "first_name": "George",
        "goals": "39",
        "last_name": "Anderson",
        "nationality": "England"
    },
    {
        "appearances": "85",
        "first_name": "Wilf",
        "goals": "2",
        "last_name": "McGuinness",
        "nationality": "England"
    },
    {
        "appearances": "83",
        "first_name": "Gabriel",
        "goals": "4",
        "last_name": "Heinze",
        "nationality": "Argentina"
    },
    {
        "appearances": "83",
        "first_name": "Jadon",
        "goals": "12",
        "last_name": "Sancho",
        "nationality": "England"
    },
    {
        "appearances": "82",
        "first_name": "Juan",
        "goals": "11",
        "last_name": "Sebasti\u00e1n Ver\u00f3n",
        "nationality": "Argentina"
    },
    {
        "appearances": "81",
        "first_name": "Kieran",
        "goals": "11",
        "last_name": "Richardson",
        "nationality": "England"
    },
    {
        "appearances": "80",
        "first_name": "Reg",
        "goals": "0",
        "last_name": "Allen",
        "nationality": "England"
    },
    {
        "appearances": "80",
        "first_name": "Mark",
        "goals": "14",
        "last_name": "Pearson",
        "nationality": "England"
    },
    {
        "appearances": "80",
        "first_name": "Kobbie",
        "goals": "7",
        "last_name": "Mainoo",
        "nationality": "England"
    },
    {
        "appearances": "79",
        "first_name": "Colin",
        "goals": "31",
        "last_name": "Webster",
        "nationality": "Wales"
    },
    {
        "appearances": "79",
        "first_name": "Chris",
        "goals": "0",
        "last_name": "Turner",
        "nationality": "England"
    },
    {
        "appearances": "79",
        "first_name": "Tom",
        "goals": "5",
        "last_name": "Cleverley",
        "nationality": "England"
    },
    {
        "appearances": "78",
        "first_name": "Jimmy",
        "goals": "45",
        "last_name": "Turnbull",
        "nationality": "Scotland"
    },
    {
        "appearances": "77",
        "first_name": "Billy",
        "goals": "27",
        "last_name": "Johnston",
        "nationality": "Scotland"
    },
    {
        "appearances": "77",
        "first_name": "Tim",
        "goals": "0",
        "last_name": "Howard",
        "nationality": "United States"
    },
    {
        "appearances": "76",
        "first_name": "Stanley",
        "goals": "20",
        "last_name": "Gallimore",
        "nationality": "England"
    },
    {
        "appearances": "75",
        "first_name": "Ian",
        "goals": "0",
        "last_name": "Greaves",
        "nationality": "England"
    },
    {
        "appearances": "75",
        "first_name": "Laurent",
        "goals": "4",
        "last_name": "Blanc",
        "nationality": "France"
    },
    {
        "appearances": "75",
        "first_name": "Andreas",
        "goals": "4",
        "last_name": "Pereira",
        "nationality": "Brazil"
    },
    {
        "appearances": "74",
        "first_name": "John",
        "goals": "23",
        "last_name": "Clarkin",
        "nationality": "Scotland"
    },
    {
        "appearances": "74",
        "first_name": "Fred",
        "goals": "8",
        "last_name": "Hopkin",
        "nationality": "England"
    },
    {
        "appearances": "74",
        "first_name": "Daniel",
        "goals": "9",
        "last_name": "James",
        "nationality": "Wales"
    },
    {
        "appearances": "73",
        "first_name": "Jack",
        "goals": "0",
        "last_name": "Hall",
        "nationality": "England"
    },
    {
        "appearances": "73",
        "first_name": "Russell",
        "goals": "4",
        "last_name": "Beardsmore",
        "nationality": "England"
    },
    {
        "appearances": "72",
        "first_name": "Roy",
        "goals": "0",
        "last_name": "Carroll",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "72",
        "first_name": "Amad",
        "goals": "15",
        "last_name": "Diallo",
        "nationality": "Ivory Coast"
    },
    {
        "appearances": "71",
        "first_name": "Jimmy",
        "goals": "17",
        "last_name": "Collinson",
        "nationality": "England"
    },
    {
        "appearances": "71",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Breen",
        "nationality": "Ireland\n Republic of Ireland"
    },
    {
        "appearances": "71",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Carolan",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "71",
        "first_name": "Danny",
        "goals": "11",
        "last_name": "Wallace",
        "nationality": "England"
    },
    {
        "appearances": "70",
        "first_name": "Mark",
        "goals": "17",
        "last_name": "Robins",
        "nationality": "England"
    },
    {
        "appearances": "69",
        "first_name": "Jimmy",
        "goals": "22",
        "last_name": "Hanlon",
        "nationality": "England"
    },
    {
        "appearances": "69",
        "first_name": "Jim",
        "goals": "5",
        "last_name": "Holton",
        "nationality": "Scotland"
    },
    {
        "appearances": "69",
        "first_name": "Viv",
        "goals": "4",
        "last_name": "Anderson",
        "nationality": "England"
    },
    {
        "appearances": "68",
        "first_name": "Charlie",
        "goals": "25",
        "last_name": "Rennox",
        "nationality": "Scotland"
    },
    {
        "appearances": "68",
        "first_name": "Billy",
        "goals": "0",
        "last_name": "Dale",
        "nationality": "England"
    },
    {
        "appearances": "68",
        "first_name": "Jimmy",
        "goals": "6",
        "last_name": "Nicholson",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "68",
        "first_name": "Paul",
        "goals": "1",
        "last_name": "Edwards",
        "nationality": "England"
    },
    {
        "appearances": "68",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "O'Neil",
        "nationality": "England"
    },
    {
        "appearances": "67",
        "first_name": "Warren",
        "goals": "21",
        "last_name": "Bradley",
        "nationality": "England"
    },
    {
        "appearances": "67",
        "first_name": "Pat",
        "goals": "0",
        "last_name": "Dunne",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "65",
        "first_name": "Ernest",
        "goals": "1",
        "last_name": "Vincent",
        "nationality": "England"
    },
    {
        "appearances": "65",
        "first_name": "Billy",
        "goals": "0",
        "last_name": "Porter",
        "nationality": "England"
    },
    {
        "appearances": "65",
        "first_name": "Ian",
        "goals": "1",
        "last_name": "Ure",
        "nationality": "Scotland"
    },
    {
        "appearances": "64",
        "first_name": "William",
        "goals": "14",
        "last_name": "Jackson",
        "nationality": "Wales"
    },
    {
        "appearances": "64",
        "first_name": "Jimmy",
        "goals": "0",
        "last_name": "Whitehouse",
        "nationality": "England"
    },
    {
        "appearances": "64",
        "first_name": "Garry",
        "goals": "12",
        "last_name": "Birtles",
        "nationality": "England"
    },
    {
        "appearances": "63",
        "first_name": "Jimmy",
        "goals": "8",
        "last_name": "Bannister",
        "nationality": "England"
    },
    {
        "appearances": "63",
        "first_name": "Gary",
        "goals": "0",
        "last_name": "Walsh",
        "nationality": "England"
    },
    {
        "appearances": "63",
        "first_name": "Adnan",
        "goals": "5",
        "last_name": "Januzaj",
        "nationality": "Belgium"
    },
    {
        "appearances": "63",
        "first_name": "Henrikh",
        "goals": "13",
        "last_name": "Mkhitaryan",
        "nationality": "Armenia"
    },
    {
        "appearances": "62",
        "first_name": "Henry",
        "goals": "35",
        "last_name": "Boyd",
        "nationality": "Scotland"
    },
    {
        "appearances": "62",
        "first_name": "Donny",
        "goals": "2",
        "last_name": "van de Beek",
        "nationality": "Netherlands"
    },
    {
        "appearances": "61",
        "first_name": "Andrew",
        "goals": "0",
        "last_name": "Mitchell",
        "nationality": "Scotland"
    },
    {
        "appearances": "61",
        "first_name": "Alf",
        "goals": "28",
        "last_name": "Farman",
        "nationality": "England"
    },
    {
        "appearances": "61",
        "first_name": "Wilf",
        "goals": "21",
        "last_name": "Woodcock",
        "nationality": "England"
    },
    {
        "appearances": "61",
        "first_name": "Tomasz",
        "goals": "0",
        "last_name": "Kuszczak",
        "nationality": "Poland"
    },
    {
        "appearances": "61",
        "first_name": "Sergio",
        "goals": "0",
        "last_name": "Romero",
        "nationality": "Argentina"
    },
    {
        "appearances": "60",
        "first_name": "Mickey",
        "goals": "2",
        "last_name": "Hamill",
        "nationality": "Ireland"
    },
    {
        "appearances": "60",
        "first_name": "Jack",
        "goals": "18",
        "last_name": "Cape",
        "nationality": "England"
    },
    {
        "appearances": "60",
        "first_name": "Raimond",
        "goals": "0",
        "last_name": "van der Gouw",
        "nationality": "Netherlands"
    },
    {
        "appearances": "60",
        "first_name": "Darron",
        "goals": "10",
        "last_name": "Gibson",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "59",
        "first_name": "Oscar",
        "goals": "0",
        "last_name": "Linkson",
        "nationality": "England"
    },
    {
        "appearances": "59",
        "first_name": "Thomas",
        "goals": "0",
        "last_name": "McNulty",
        "nationality": "England"
    },
    {
        "appearances": "59",
        "first_name": "Edinson",
        "goals": "19",
        "last_name": "Cavani",
        "nationality": "Uruguay"
    },
    {
        "appearances": "59",
        "first_name": "Noussair",
        "goals": "0",
        "last_name": "Mazraoui",
        "nationality": "Morocco"
    },
    {
        "appearances": "58",
        "first_name": "Jordi",
        "goals": "8",
        "last_name": "Cruyff",
        "nationality": "Netherlands"
    },
    {
        "appearances": "57",
        "first_name": "William",
        "goals": "0",
        "last_name": "Douglas",
        "nationality": "Scotland"
    },
    {
        "appearances": "57",
        "first_name": "Harry",
        "goals": "8",
        "last_name": "McShane",
        "nationality": "Scotland"
    },
    {
        "appearances": "57",
        "first_name": "Shinji",
        "goals": "6",
        "last_name": "Kagawa",
        "nationality": "Japan"
    },
    {
        "appearances": "56",
        "first_name": "Carlo",
        "goals": "6",
        "last_name": "Sartori",
        "nationality": "Italy"
    },
    {
        "appearances": "56",
        "first_name": "Les",
        "goals": "0",
        "last_name": "Sealey",
        "nationality": "England"
    },
    {
        "appearances": "56",
        "first_name": "Mr.",
        "goals": "3",
        "last_name": "F\u00e1bio",
        "nationality": "Brazil"
    },
    {
        "appearances": "55",
        "first_name": "Anthony",
        "goals": "4",
        "last_name": "Elanga",
        "nationality": "Sweden"
    },
    {
        "appearances": "54",
        "first_name": "Herbert",
        "goals": "0",
        "last_name": "Burgess",
        "nationality": "England"
    },
    {
        "appearances": "54",
        "first_name": "Manuel",
        "goals": "2",
        "last_name": "Ugarte",
        "nationality": "Uruguay"
    },
    {
        "appearances": "53",
        "first_name": "George",
        "goals": "17",
        "last_name": "Sapsford",
        "nationality": "England"
    },
    {
        "appearances": "53",
        "first_name": "Tommy",
        "goals": "6",
        "last_name": "Meehan",
        "nationality": "England"
    },
    {
        "appearances": "53",
        "first_name": "Samuel",
        "goals": "12",
        "last_name": "Hopkinson",
        "nationality": "England"
    },
    {
        "appearances": "53",
        "first_name": "Ernie",
        "goals": "12",
        "last_name": "Hine",
        "nationality": "England"
    },
    {
        "appearances": "53",
        "first_name": "Harry",
        "goals": "18",
        "last_name": "Baird",
        "nationality": "Ireland"
    },
    {
        "appearances": "53",
        "first_name": "Paddy",
        "goals": "0",
        "last_name": "Roche",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "53",
        "first_name": "Memphis",
        "goals": "7",
        "last_name": "Depay",
        "nationality": "Netherlands"
    },
    {
        "appearances": "53",
        "first_name": "Zlatan",
        "goals": "29",
        "last_name": "Ibrahimovi\u0107",
        "nationality": "Sweden"
    },
    {
        "appearances": "53",
        "first_name": "Joshua",
        "goals": "7",
        "last_name": "Zirkzee",
        "nationality": "Netherlands"
    },
    {
        "appearances": "53",
        "first_name": "Matthijs",
        "goals": "2",
        "last_name": "de Ligt",
        "nationality": "Netherlands"
    },
    {
        "appearances": "52",
        "first_name": "Tommy",
        "goals": "4",
        "last_name": "Frame",
        "nationality": "Scotland"
    },
    {
        "appearances": "52",
        "first_name": "Arthur",
        "goals": "7",
        "last_name": "Graham",
        "nationality": "Scotland"
    },
    {
        "appearances": "52",
        "first_name": "Michael",
        "goals": "17",
        "last_name": "Owen",
        "nationality": "England"
    },
    {
        "appearances": "52",
        "first_name": "Mason",
        "goals": "4",
        "last_name": "Mount",
        "nationality": "England"
    },
    {
        "appearances": "51",
        "first_name": "Jack",
        "goals": "14",
        "last_name": "Peters",
        "nationality": "England"
    },
    {
        "appearances": "51",
        "first_name": "Dick",
        "goals": "20",
        "last_name": "Pegg",
        "nationality": "England"
    },
    {
        "appearances": "51",
        "first_name": "Dick",
        "goals": "3",
        "last_name": "Wombwell",
        "nationality": "England"
    },
    {
        "appearances": "51",
        "first_name": "Hugh",
        "goals": "0",
        "last_name": "Edmonds",
        "nationality": "Scotland"
    },
    {
        "appearances": "51",
        "first_name": "John",
        "goals": "0",
        "last_name": "Moody",
        "nationality": "England"
    },
    {
        "appearances": "51",
        "first_name": "Billy",
        "goals": "0",
        "last_name": "Garton",
        "nationality": "England"
    },
    {
        "appearances": "51",
        "first_name": "Brandon",
        "goals": "1",
        "last_name": "Williams",
        "nationality": "England"
    },
    {
        "appearances": "50",
        "first_name": "John",
        "goals": "6",
        "last_name": "Dow",
        "nationality": "Scotland"
    },
    {
        "appearances": "50",
        "first_name": "Jack",
        "goals": "18",
        "last_name": "Ball",
        "nationality": "England"
    },
    {
        "appearances": "50",
        "first_name": "William",
        "goals": "1",
        "last_name": "Robertson",
        "nationality": "Scotland"
    },
    {
        "appearances": "50",
        "first_name": "Alex",
        "goals": "1",
        "last_name": "Telles",
        "nationality": "Brazil"
    },
    {
        "appearances": "49",
        "first_name": "Frank",
        "goals": "2",
        "last_name": "Harris",
        "nationality": "England"
    },
    {
        "appearances": "49",
        "first_name": "William",
        "goals": "7",
        "last_name": "Stewart",
        "nationality": "Scotland"
    },
    {
        "appearances": "48",
        "first_name": "Charlie",
        "goals": "0",
        "last_name": "Spencer",
        "nationality": "England"
    },
    {
        "appearances": "48",
        "first_name": "Jackie",
        "goals": "6",
        "last_name": "Wassall",
        "nationality": "England"
    },
    {
        "appearances": "48",
        "first_name": "Karel",
        "goals": "6",
        "last_name": "Poborsk\u00fd",
        "nationality": "Czech Republic"
    },
    {
        "appearances": "47",
        "first_name": "Caesar",
        "goals": "6",
        "last_name": "Jenkyns",
        "nationality": "Wales"
    },
    {
        "appearances": "47",
        "first_name": "Frank",
        "goals": "1",
        "last_name": "Knowles",
        "nationality": "England"
    },
    {
        "appearances": "47",
        "first_name": "Phil",
        "goals": "10",
        "last_name": "Chisnall",
        "nationality": "England"
    },
    {
        "appearances": "47",
        "first_name": "Morgan",
        "goals": "1",
        "last_name": "Schneiderlin",
        "nationality": "France"
    },
    {
        "appearances": "47",
        "first_name": "Tyrell",
        "goals": "0",
        "last_name": "Malacia",
        "nationality": "Netherlands"
    },
    {
        "appearances": "46",
        "first_name": "Tommy",
        "goals": "15",
        "last_name": "Leigh",
        "nationality": "England"
    },
    {
        "appearances": "46",
        "first_name": "James",
        "goals": "3",
        "last_name": "Fisher",
        "nationality": "Scotland"
    },
    {
        "appearances": "46",
        "first_name": "George",
        "goals": "14",
        "last_name": "Livingstone",
        "nationality": "Scotland"
    },
    {
        "appearances": "46",
        "first_name": "Billy",
        "goals": "5",
        "last_name": "Harrison",
        "nationality": "England"
    },
    {
        "appearances": "46",
        "first_name": "Jimmy",
        "goals": "0",
        "last_name": "Rimmer",
        "nationality": "England"
    },
    {
        "appearances": "46",
        "first_name": "George",
        "goals": "2",
        "last_name": "Graham",
        "nationality": "Scotland"
    },
    {
        "appearances": "45",
        "first_name": "Ian",
        "goals": "5",
        "last_name": "Moir",
        "nationality": "Scotland"
    },
    {
        "appearances": "45",
        "first_name": "Alexis",
        "goals": "5",
        "last_name": "S\u00e1nchez",
        "nationality": "Chile"
    },
    {
        "appearances": "44",
        "first_name": "Will",
        "goals": "2",
        "last_name": "Davidson",
        "nationality": "Scotland"
    },
    {
        "appearances": "44",
        "first_name": "Jack",
        "goals": "1",
        "last_name": "Banks",
        "nationality": "England"
    },
    {
        "appearances": "44",
        "first_name": "Bill",
        "goals": "14",
        "last_name": "Ridding",
        "nationality": "England"
    },
    {
        "appearances": "44",
        "first_name": "Nobby",
        "goals": "6",
        "last_name": "Lawton",
        "nationality": "England"
    },
    {
        "appearances": "43",
        "first_name": "Neil",
        "goals": "2",
        "last_name": "McBain",
        "nationality": "Scotland"
    },
    {
        "appearances": "43",
        "first_name": "Ian",
        "goals": "12",
        "last_name": "Storey-Moore",
        "nationality": "England"
    },
    {
        "appearances": "43",
        "first_name": "Mick",
        "goals": "2",
        "last_name": "Martin",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "43",
        "first_name": "Leny",
        "goals": "1",
        "last_name": "Yoro",
        "nationality": "France"
    },
    {
        "appearances": "42",
        "first_name": "John",
        "goals": "0",
        "last_name": "Clements",
        "nationality": "England"
    },
    {
        "appearances": "42",
        "first_name": "Bert",
        "goals": "0",
        "last_name": "Read",
        "nationality": "England"
    },
    {
        "appearances": "42",
        "first_name": "George",
        "goals": "10",
        "last_name": "Bissett",
        "nationality": "Scotland"
    },
    {
        "appearances": "42",
        "first_name": "Lance",
        "goals": "0",
        "last_name": "Richardson",
        "nationality": "England"
    },
    {
        "appearances": "42",
        "first_name": "Jack",
        "goals": "15",
        "last_name": "Smith",
        "nationality": "England"
    },
    {
        "appearances": "42",
        "first_name": "Andy",
        "goals": "13",
        "last_name": "Ritchie",
        "nationality": "England"
    },
    {
        "appearances": "41",
        "first_name": "Jim",
        "goals": "17",
        "last_name": "Brown",
        "nationality": "United States"
    },
    {
        "appearances": "41",
        "first_name": "Alan",
        "goals": "12",
        "last_name": "Brazil",
        "nationality": "Scotland"
    },
    {
        "appearances": "40",
        "first_name": "John",
        "goals": "2",
        "last_name": "Anderson",
        "nationality": "England"
    },
    {
        "appearances": "40",
        "first_name": "David",
        "goals": "8",
        "last_name": "Bellion",
        "nationality": "France"
    },
    {
        "appearances": "39",
        "first_name": "Arthur",
        "goals": "10",
        "last_name": "Warburton",
        "nationality": "England"
    },
    {
        "appearances": "39",
        "first_name": "Bert",
        "goals": "0",
        "last_name": "Whalley",
        "nationality": "England"
    },
    {
        "appearances": "39",
        "first_name": "Luke",
        "goals": "2",
        "last_name": "Chadwick",
        "nationality": "England"
    },
    {
        "appearances": "39",
        "first_name": "Eric",
        "goals": "2",
        "last_name": "Djemba-Djemba",
        "nationality": "Cameroon"
    },
    {
        "appearances": "39",
        "first_name": "Owen",
        "goals": "2",
        "last_name": "Hargreaves",
        "nationality": "England"
    },
    {
        "appearances": "38",
        "first_name": "Billy",
        "goals": "6",
        "last_name": "Hood",
        "nationality": "England"
    },
    {
        "appearances": "38",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Blackstock",
        "nationality": "Scotland"
    },
    {
        "appearances": "38",
        "first_name": "Billy",
        "goals": "0",
        "last_name": "Redman",
        "nationality": "England"
    },
    {
        "appearances": "38",
        "first_name": "Jim",
        "goals": "7",
        "last_name": "McCalliog",
        "nationality": "Scotland"
    },
    {
        "appearances": "38",
        "first_name": "Mark",
        "goals": "0",
        "last_name": "Bosnich",
        "nationality": "Australia"
    },
    {
        "appearances": "38",
        "first_name": "Jesper",
        "goals": "1",
        "last_name": "Blomqvist",
        "nationality": "Sweden"
    },
    {
        "appearances": "37",
        "first_name": "Billy",
        "goals": "14",
        "last_name": "Grassam",
        "nationality": "Scotland"
    },
    {
        "appearances": "37",
        "first_name": "Tony",
        "goals": "0",
        "last_name": "Donnelly",
        "nationality": "England"
    },
    {
        "appearances": "37",
        "first_name": "Joe",
        "goals": "3",
        "last_name": "Norton",
        "nationality": "England"
    },
    {
        "appearances": "37",
        "first_name": "Billy",
        "goals": "10",
        "last_name": "Wrigglesworth",
        "nationality": "England"
    },
    {
        "appearances": "37",
        "first_name": "Axel",
        "goals": "0",
        "last_name": "Tuanzebe",
        "nationality": "DR Congo"
    },
    {
        "appearances": "36",
        "first_name": "Tommy",
        "goals": "8",
        "last_name": "Morrison",
        "nationality": "Ireland"
    },
    {
        "appearances": "36",
        "first_name": "Jack",
        "goals": "22",
        "last_name": "Allan",
        "nationality": "England"
    },
    {
        "appearances": "36",
        "first_name": "Henry",
        "goals": "8",
        "last_name": "Williams",
        "nationality": "England"
    },
    {
        "appearances": "36",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Forster",
        "nationality": "England"
    },
    {
        "appearances": "36",
        "first_name": "Bill",
        "goals": "17",
        "last_name": "Henderson",
        "nationality": "Scotland"
    },
    {
        "appearances": "36",
        "first_name": "Bill",
        "goals": "19",
        "last_name": "Rawlings",
        "nationality": "England"
    },
    {
        "appearances": "36",
        "first_name": "Neil",
        "goals": "14",
        "last_name": "Dewar",
        "nationality": "Scotland"
    },
    {
        "appearances": "36",
        "first_name": "Liam",
        "goals": "2",
        "last_name": "O'Brien",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "36",
        "first_name": "Federico",
        "goals": "5",
        "last_name": "Macheda",
        "nationality": "Italy"
    },
    {
        "appearances": "35",
        "first_name": "Alexander",
        "goals": "1",
        "last_name": "Robertson",
        "nationality": "Scotland"
    },
    {
        "appearances": "35",
        "first_name": "Patrick",
        "goals": "2",
        "last_name": "O'Connell",
        "nationality": "Ireland"
    },
    {
        "appearances": "35",
        "first_name": "Rees",
        "goals": "2",
        "last_name": "Williams",
        "nationality": "Wales"
    },
    {
        "appearances": "35",
        "first_name": "Stewart",
        "goals": "1",
        "last_name": "Chalmers",
        "nationality": "Scotland"
    },
    {
        "appearances": "35",
        "first_name": "Jack",
        "goals": "0",
        "last_name": "Breedon",
        "nationality": "England"
    },
    {
        "appearances": "35",
        "first_name": "Ronnie",
        "goals": "23",
        "last_name": "Burke",
        "nationality": "England"
    },
    {
        "appearances": "35",
        "first_name": "Bastian",
        "goals": "2",
        "last_name": "Schweinsteiger",
        "nationality": "Germany"
    },
    {
        "appearances": "34",
        "first_name": "Jimmy",
        "goals": "10",
        "last_name": "Coupar",
        "nationality": "Scotland"
    },
    {
        "appearances": "34",
        "first_name": "Stephen",
        "goals": "14",
        "last_name": "Preston",
        "nationality": "England"
    },
    {
        "appearances": "34",
        "first_name": "Sandy",
        "goals": "10",
        "last_name": "Robertson",
        "nationality": "Scotland"
    },
    {
        "appearances": "34",
        "first_name": "Clem",
        "goals": "15",
        "last_name": "Beddow",
        "nationality": "England"
    },
    {
        "appearances": "34",
        "first_name": "Joe",
        "goals": "8",
        "last_name": "Myerscough",
        "nationality": "England"
    },
    {
        "appearances": "34",
        "first_name": "Jack",
        "goals": "0",
        "last_name": "Hacking",
        "nationality": "England"
    },
    {
        "appearances": "34",
        "first_name": "Chris",
        "goals": "1",
        "last_name": "McGrath",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "34",
        "first_name": "John",
        "goals": "1",
        "last_name": "Siveb\u00e6k",
        "nationality": "Denmark"
    },
    {
        "appearances": "33",
        "first_name": "William",
        "goals": "12",
        "last_name": "Kennedy",
        "nationality": "Scotland"
    },
    {
        "appearances": "33",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Arkesden",
        "nationality": "England"
    },
    {
        "appearances": "33",
        "first_name": "Charlie",
        "goals": "24",
        "last_name": "Sagar",
        "nationality": "England"
    },
    {
        "appearances": "33",
        "first_name": "Tommy",
        "goals": "7",
        "last_name": "Bogan",
        "nationality": "Scotland"
    },
    {
        "appearances": "33",
        "first_name": "Bobby",
        "goals": "0",
        "last_name": "Noble",
        "nationality": "England"
    },
    {
        "appearances": "32",
        "first_name": "Jack",
        "goals": "8",
        "last_name": "Peden",
        "nationality": "Ireland"
    },
    {
        "appearances": "32",
        "first_name": "Eric",
        "goals": "7",
        "last_name": "Sweeney",
        "nationality": "England"
    },
    {
        "appearances": "32",
        "first_name": "\u00c1ngel",
        "goals": "4",
        "last_name": "Di Mar\u00eda",
        "nationality": "Argentina"
    },
    {
        "appearances": "31",
        "first_name": "David",
        "goals": "0",
        "last_name": "Fitzsimmons",
        "nationality": "Scotland"
    },
    {
        "appearances": "31",
        "first_name": "Wout",
        "goals": "2",
        "last_name": "Weghorst",
        "nationality": "Netherlands"
    },
    {
        "appearances": "30",
        "first_name": "Tommy",
        "goals": "6",
        "last_name": "Fitzsimmons",
        "nationality": "Scotland"
    },
    {
        "appearances": "30",
        "first_name": "Herbert",
        "goals": "0",
        "last_name": "Birchenough",
        "nationality": "England"
    },
    {
        "appearances": "30",
        "first_name": "John",
        "goals": "0",
        "last_name": "Hodge",
        "nationality": "Scotland"
    },
    {
        "appearances": "30",
        "first_name": "Cyril",
        "goals": "0",
        "last_name": "Barlow",
        "nationality": "England"
    },
    {
        "appearances": "30",
        "first_name": "Ernie",
        "goals": "16",
        "last_name": "Goldthorpe",
        "nationality": "England"
    },
    {
        "appearances": "30",
        "first_name": "Chris",
        "goals": "7",
        "last_name": "Taylor",
        "nationality": "England"
    },
    {
        "appearances": "30",
        "first_name": "Ernie",
        "goals": "4",
        "last_name": "Taylor",
        "nationality": "England"
    },
    {
        "appearances": "30",
        "first_name": "Ralph",
        "goals": "3",
        "last_name": "Milne",
        "nationality": "Scotland"
    },
    {
        "appearances": "30",
        "first_name": "Darren",
        "goals": "0",
        "last_name": "Ferguson",
        "nationality": "Scotland"
    },
    {
        "appearances": "30",
        "first_name": "Mr.",
        "goals": "2",
        "last_name": "Kl\u00e9berson",
        "nationality": "Brazil"
    },
    {
        "appearances": "30",
        "first_name": "Timothy",
        "goals": "0",
        "last_name": "Fosu-Mensah",
        "nationality": "Netherlands"
    },
    {
        "appearances": "30",
        "first_name": "Sofyan",
        "goals": "0",
        "last_name": "Amrabat",
        "nationality": "Morocco"
    },
    {
        "appearances": "30",
        "first_name": "Patrick",
        "goals": "0",
        "last_name": "Dorgu",
        "nationality": "Denmark"
    },
    {
        "appearances": "29",
        "first_name": "Arthur",
        "goals": "5",
        "last_name": "Potts",
        "nationality": "England"
    },
    {
        "appearances": "29",
        "first_name": "Walter",
        "goals": "2",
        "last_name": "McMillen",
        "nationality": "Ireland"
    },
    {
        "appearances": "29",
        "first_name": "Anders",
        "goals": "0",
        "last_name": "Lindegaard",
        "nationality": "Denmark"
    },
    {
        "appearances": "29",
        "first_name": "Radamel",
        "goals": "4",
        "last_name": "Falcao",
        "nationality": "Colombia"
    },
    {
        "appearances": "29",
        "first_name": "Dean",
        "goals": "0",
        "last_name": "Henderson",
        "nationality": "England"
    },
    {
        "appearances": "28",
        "first_name": "Herbert",
        "goals": "0",
        "last_name": "Rothwell",
        "nationality": "England"
    },
    {
        "appearances": "28",
        "first_name": "John",
        "goals": "0",
        "last_name": "Willie Sutcliffe",
        "nationality": "England"
    },
    {
        "appearances": "28",
        "first_name": "George",
        "goals": "1",
        "last_name": "Gladwin",
        "nationality": "England"
    },
    {
        "appearances": "28",
        "first_name": "Ronnie",
        "goals": "0",
        "last_name": "Wallwork",
        "nationality": "England"
    },
    {
        "appearances": "28",
        "first_name": "Gabriel",
        "goals": "1",
        "last_name": "Obertan",
        "nationality": "France"
    },
    {
        "appearances": "28",
        "first_name": "Alexander",
        "goals": "2",
        "last_name": "B\u00fcttner",
        "nationality": "Netherlands"
    },
    {
        "appearances": "27",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Fall",
        "nationality": "England"
    },
    {
        "appearances": "27",
        "first_name": "Harry",
        "goals": "4",
        "last_name": "Lappin",
        "nationality": "England"
    },
    {
        "appearances": "27",
        "first_name": "James",
        "goals": "1",
        "last_name": "Montgomery",
        "nationality": "England"
    },
    {
        "appearances": "27",
        "first_name": "Tom",
        "goals": "8",
        "last_name": "Miller",
        "nationality": "Scotland"
    },
    {
        "appearances": "27",
        "first_name": "George",
        "goals": "0",
        "last_name": "Haslam",
        "nationality": "England"
    },
    {
        "appearances": "27",
        "first_name": "Willie",
        "goals": "4",
        "last_name": "McDonald",
        "nationality": "Scotland"
    },
    {
        "appearances": "27",
        "first_name": "Walter",
        "goals": "0",
        "last_name": "Winterbottom",
        "nationality": "England"
    },
    {
        "appearances": "27",
        "first_name": "Jimmy",
        "goals": "4",
        "last_name": "Ryan",
        "nationality": "Scotland"
    },
    {
        "appearances": "27",
        "first_name": "Terry",
        "goals": "1",
        "last_name": "Gibson",
        "nationality": "England"
    },
    {
        "appearances": "27",
        "first_name": "Jonathan",
        "goals": "0",
        "last_name": "Greening",
        "nationality": "England"
    },
    {
        "appearances": "27",
        "first_name": "Paddy",
        "goals": "0",
        "last_name": "McNair",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "26",
        "first_name": "Jackie",
        "goals": "0",
        "last_name": "Sheldon",
        "nationality": "England"
    },
    {
        "appearances": "26",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Haywood",
        "nationality": "England"
    },
    {
        "appearances": "26",
        "first_name": "Billy",
        "goals": "0",
        "last_name": "Chapman",
        "nationality": "England"
    },
    {
        "appearances": "26",
        "first_name": "John",
        "goals": "7",
        "last_name": "Doherty",
        "nationality": "England"
    },
    {
        "appearances": "26",
        "first_name": "Nikola",
        "goals": "4",
        "last_name": "Jovanovi\u0107",
        "nationality": "Yugoslavia"
    },
    {
        "appearances": "25",
        "first_name": "Alex",
        "goals": "4",
        "last_name": "Menzies",
        "nationality": "Scotland"
    },
    {
        "appearances": "25",
        "first_name": "Tom",
        "goals": "14",
        "last_name": "Homer",
        "nationality": "England"
    },
    {
        "appearances": "25",
        "first_name": "Scott",
        "goals": "3",
        "last_name": "McGarvey",
        "nationality": "Scotland"
    },
    {
        "appearances": "25",
        "first_name": "Peter",
        "goals": "5",
        "last_name": "Barnes",
        "nationality": "England"
    },
    {
        "appearances": "25",
        "first_name": "Facundo",
        "goals": "0",
        "last_name": "Pellistri",
        "nationality": "Uruguay"
    },
    {
        "appearances": "24",
        "first_name": "John",
        "goals": "0",
        "last_name": "Scott",
        "nationality": "Scotland"
    },
    {
        "appearances": "24",
        "first_name": "Ted",
        "goals": "7",
        "last_name": "Buckle",
        "nationality": "England"
    },
    {
        "appearances": "24",
        "first_name": "Eddie",
        "goals": "11",
        "last_name": "Lewis",
        "nationality": "England"
    },
    {
        "appearances": "24",
        "first_name": "Michael",
        "goals": "0",
        "last_name": "Clegg",
        "nationality": "England"
    },
    {
        "appearances": "23",
        "first_name": "Hugh",
        "goals": "4",
        "last_name": "Morgan",
        "nationality": "Scotland"
    },
    {
        "appearances": "23",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Gipps",
        "nationality": "England"
    },
    {
        "appearances": "23",
        "first_name": "George",
        "goals": "2",
        "last_name": "Hunter",
        "nationality": "England"
    },
    {
        "appearances": "23",
        "first_name": "David",
        "goals": "9",
        "last_name": "Bain",
        "nationality": "Scotland"
    },
    {
        "appearances": "23",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Walton",
        "nationality": "England"
    },
    {
        "appearances": "23",
        "first_name": "John",
        "goals": "0",
        "last_name": "Ball",
        "nationality": "England"
    },
    {
        "appearances": "23",
        "first_name": "Kenny",
        "goals": "0",
        "last_name": "Morgans",
        "nationality": "Wales"
    },
    {
        "appearances": "23",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Jackson",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "23",
        "first_name": "Gerard",
        "goals": "2",
        "last_name": "Piqu\u00e9",
        "nationality": "Spain"
    },
    {
        "appearances": "23",
        "first_name": "Ben",
        "goals": "0",
        "last_name": "Foster",
        "nationality": "England"
    },
    {
        "appearances": "23",
        "first_name": "Odion",
        "goals": "5",
        "last_name": "Ighalo",
        "nationality": "Nigeria"
    },
    {
        "appearances": "22",
        "first_name": "Jimmy",
        "goals": "0",
        "last_name": "Warner",
        "nationality": "England"
    },
    {
        "appearances": "22",
        "first_name": "Tommy",
        "goals": "4",
        "last_name": "Jones",
        "nationality": "Wales"
    },
    {
        "appearances": "22",
        "first_name": "Liam",
        "goals": "2",
        "last_name": "Miller",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "21",
        "first_name": "Daniel",
        "goals": "4",
        "last_name": "Hurst",
        "nationality": "England"
    },
    {
        "appearances": "21",
        "first_name": "George",
        "goals": "4",
        "last_name": "Travers",
        "nationality": "England"
    },
    {
        "appearances": "21",
        "first_name": "James",
        "goals": "3",
        "last_name": "Robinson",
        "nationality": "Ireland"
    },
    {
        "appearances": "21",
        "first_name": "Ernie",
        "goals": "4",
        "last_name": "Bond",
        "nationality": "England"
    },
    {
        "appearances": "20",
        "first_name": "John",
        "goals": "1",
        "last_name": "McCartney",
        "nationality": "Scotland"
    },
    {
        "appearances": "20",
        "first_name": "Frank",
        "goals": "4",
        "last_name": "Hodges",
        "nationality": "England"
    },
    {
        "appearances": "20",
        "first_name": "Stan",
        "goals": "0",
        "last_name": "Crowther",
        "nationality": "England"
    },
    {
        "appearances": "20",
        "first_name": "Arnie",
        "goals": "0",
        "last_name": "Sidebottom",
        "nationality": "England"
    },
    {
        "appearances": "20",
        "first_name": "Simon",
        "goals": "1",
        "last_name": "Davies",
        "nationality": "Wales"
    },
    {
        "appearances": "20",
        "first_name": "James",
        "goals": "4",
        "last_name": "Wilson",
        "nationality": "England"
    },
    {
        "appearances": "19",
        "first_name": "Sam",
        "goals": "2",
        "last_name": "Blott",
        "nationality": "England"
    },
    {
        "appearances": "19",
        "first_name": "Leslie",
        "goals": "0",
        "last_name": "Hofton",
        "nationality": "England"
    },
    {
        "appearances": "19",
        "first_name": "Ron",
        "goals": "4",
        "last_name": "Ferrier",
        "nationality": "England"
    },
    {
        "appearances": "19",
        "first_name": "Graham",
        "goals": "5",
        "last_name": "Moore",
        "nationality": "Wales"
    },
    {
        "appearances": "19",
        "first_name": "Trevor",
        "goals": "2",
        "last_name": "Anderson",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "19",
        "first_name": "John",
        "goals": "0",
        "last_name": "Curtis",
        "nationality": "England"
    },
    {
        "appearances": "18",
        "first_name": "Jack",
        "goals": "1",
        "last_name": "Fitchett",
        "nationality": "England"
    },
    {
        "appearances": "18",
        "first_name": "Fred",
        "goals": "4",
        "last_name": "Kennedy",
        "nationality": "England"
    },
    {
        "appearances": "18",
        "first_name": "Albert",
        "goals": "5",
        "last_name": "Pape",
        "nationality": "England"
    },
    {
        "appearances": "18",
        "first_name": "Dick",
        "goals": "1",
        "last_name": "Gardner",
        "nationality": "England"
    },
    {
        "appearances": "18",
        "first_name": "Ted",
        "goals": "5",
        "last_name": "MacDougall",
        "nationality": "Scotland"
    },
    {
        "appearances": "18",
        "first_name": "Phil",
        "goals": "0",
        "last_name": "Bardsley",
        "nationality": "England"
    },
    {
        "appearances": "18",
        "first_name": "Marcel",
        "goals": "3",
        "last_name": "Sabitzer",
        "nationality": "Austria"
    },
    {
        "appearances": "17",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Ridgway",
        "nationality": "England"
    },
    {
        "appearances": "17",
        "first_name": "John",
        "goals": "2",
        "last_name": "Cunningham",
        "nationality": "Scotland"
    },
    {
        "appearances": "17",
        "first_name": "Stockport",
        "goals": "0",
        "last_name": "Smith",
        "nationality": "England"
    },
    {
        "appearances": "17",
        "first_name": "Tommy",
        "goals": "6",
        "last_name": "Boyle",
        "nationality": "England"
    },
    {
        "appearances": "17",
        "first_name": "Thomas",
        "goals": "0",
        "last_name": "Parker",
        "nationality": "England"
    },
    {
        "appearances": "17",
        "first_name": "Bill",
        "goals": "1",
        "last_name": "Owen",
        "nationality": "England"
    },
    {
        "appearances": "17",
        "first_name": "Wyn",
        "goals": "4",
        "last_name": "Davies",
        "nationality": "Wales"
    },
    {
        "appearances": "17",
        "first_name": "Dion",
        "goals": "3",
        "last_name": "Dublin",
        "nationality": "England"
    },
    {
        "appearances": "17",
        "first_name": "Chris",
        "goals": "1",
        "last_name": "Eagles",
        "nationality": "England"
    },
    {
        "appearances": "17",
        "first_name": "Altay",
        "goals": "0",
        "last_name": "Bay\u0131nd\u0131r",
        "nationality": "Turkey"
    },
    {
        "appearances": "16",
        "first_name": "Tom",
        "goals": "4",
        "last_name": "Nuttall",
        "nationality": "England"
    },
    {
        "appearances": "16",
        "first_name": "John",
        "goals": "1",
        "last_name": "Wood",
        "nationality": "Scotland"
    },
    {
        "appearances": "16",
        "first_name": "Charlie",
        "goals": "3",
        "last_name": "Ramsden",
        "nationality": "England"
    },
    {
        "appearances": "16",
        "first_name": "Norman",
        "goals": "0",
        "last_name": "Tapken",
        "nationality": "England"
    },
    {
        "appearances": "16",
        "first_name": "Tahith",
        "goals": "0",
        "last_name": "Chong",
        "nationality": "Netherlands"
    },
    {
        "appearances": "15",
        "first_name": "Bob",
        "goals": "7",
        "last_name": "Parkinson",
        "nationality": "England"
    },
    {
        "appearances": "15",
        "first_name": "Ted",
        "goals": "2",
        "last_name": "Connor",
        "nationality": "England"
    },
    {
        "appearances": "15",
        "first_name": "Len",
        "goals": "0",
        "last_name": "Langford",
        "nationality": "England"
    },
    {
        "appearances": "15",
        "first_name": "Roy",
        "goals": "0",
        "last_name": "John",
        "nationality": "Wales"
    },
    {
        "appearances": "15",
        "first_name": "Brian",
        "goals": "5",
        "last_name": "Birch",
        "nationality": "England"
    },
    {
        "appearances": "15",
        "first_name": "Frank",
        "goals": "2",
        "last_name": "Clempson",
        "nationality": "England"
    },
    {
        "appearances": "15",
        "first_name": "Sammy",
        "goals": "6",
        "last_name": "McMillan",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "14",
        "first_name": "Bill",
        "goals": "1",
        "last_name": "Berry",
        "nationality": "England"
    },
    {
        "appearances": "14",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Curry",
        "nationality": "England"
    },
    {
        "appearances": "14",
        "first_name": "Billy",
        "goals": "4",
        "last_name": "Toms",
        "nationality": "Ireland"
    },
    {
        "appearances": "14",
        "first_name": "Bill",
        "goals": "1",
        "last_name": "Inglis",
        "nationality": "Scotland"
    },
    {
        "appearances": "14",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Lowrie",
        "nationality": "Scotland"
    },
    {
        "appearances": "14",
        "first_name": "Sonny",
        "goals": "0",
        "last_name": "Feehan",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "14",
        "first_name": "Willie",
        "goals": "0",
        "last_name": "Watson",
        "nationality": "Scotland"
    },
    {
        "appearances": "14",
        "first_name": "Tony",
        "goals": "2",
        "last_name": "Gill",
        "nationality": "England"
    },
    {
        "appearances": "14",
        "first_name": "Keith",
        "goals": "2",
        "last_name": "Gillespie",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "14",
        "first_name": "Ben",
        "goals": "0",
        "last_name": "Thornley",
        "nationality": "England"
    },
    {
        "appearances": "14",
        "first_name": "Michael",
        "goals": "0",
        "last_name": "Stewart",
        "nationality": "Scotland"
    },
    {
        "appearances": "14",
        "first_name": "Giuseppe",
        "goals": "4",
        "last_name": "Rossi",
        "nationality": "Italy"
    },
    {
        "appearances": "14",
        "first_name": "Cameron",
        "goals": "0",
        "last_name": "Borthwick-Jackson",
        "nationality": "England"
    },
    {
        "appearances": "13",
        "first_name": "Adam",
        "goals": "3",
        "last_name": "Carson",
        "nationality": "Scotland"
    },
    {
        "appearances": "13",
        "first_name": "James",
        "goals": "0",
        "last_name": "Saunders",
        "nationality": "England"
    },
    {
        "appearances": "13",
        "first_name": "William",
        "goals": "1",
        "last_name": "McCartney",
        "nationality": "Scotland"
    },
    {
        "appearances": "13",
        "first_name": "Sam",
        "goals": "0",
        "last_name": "Cookson",
        "nationality": "Wales"
    },
    {
        "appearances": "13",
        "first_name": "Walter",
        "goals": "0",
        "last_name": "Spratt",
        "nationality": "England"
    },
    {
        "appearances": "13",
        "first_name": "James",
        "goals": "0",
        "last_name": "McCrae",
        "nationality": "Scotland"
    },
    {
        "appearances": "13",
        "first_name": "Herbert",
        "goals": "2",
        "last_name": "Mann",
        "nationality": "England"
    },
    {
        "appearances": "13",
        "first_name": "Reg",
        "goals": "1",
        "last_name": "Chester",
        "nationality": "England"
    },
    {
        "appearances": "13",
        "first_name": "Tommy",
        "goals": "1",
        "last_name": "Lang",
        "nationality": "Scotland"
    },
    {
        "appearances": "13",
        "first_name": "Sammy",
        "goals": "0",
        "last_name": "Lynn",
        "nationality": "England"
    },
    {
        "appearances": "13",
        "first_name": "Cliff",
        "goals": "2",
        "last_name": "Birkett",
        "nationality": "England"
    },
    {
        "appearances": "13",
        "first_name": "Willie",
        "goals": "0",
        "last_name": "Anderson",
        "nationality": "England"
    },
    {
        "appearances": "13",
        "first_name": "Henrik",
        "goals": "3",
        "last_name": "Larsson",
        "nationality": "Sweden"
    },
    {
        "appearances": "13",
        "first_name": "Hannibal",
        "goals": "1",
        "last_name": "Mejbri",
        "nationality": "Tunisia"
    },
    {
        "appearances": "13",
        "first_name": "Toby",
        "goals": "0",
        "last_name": "Collyer",
        "nationality": "England"
    },
    {
        "appearances": "12",
        "first_name": "William",
        "goals": "0",
        "last_name": "Dunn",
        "nationality": "England"
    },
    {
        "appearances": "12",
        "first_name": "Arthur",
        "goals": "2",
        "last_name": "Beadsworth",
        "nationality": "England"
    },
    {
        "appearances": "12",
        "first_name": "Arthur",
        "goals": "0",
        "last_name": "Allman",
        "nationality": "England"
    },
    {
        "appearances": "12",
        "first_name": "Richard",
        "goals": "0",
        "last_name": "Gibson",
        "nationality": "England"
    },
    {
        "appearances": "12",
        "first_name": "Louis",
        "goals": "0",
        "last_name": "Page",
        "nationality": "England"
    },
    {
        "appearances": "12",
        "first_name": "Henry",
        "goals": "1",
        "last_name": "Topping",
        "nationality": "England"
    },
    {
        "appearances": "12",
        "first_name": "Arthur",
        "goals": "2",
        "last_name": "Fitton",
        "nationality": "England"
    },
    {
        "appearances": "12",
        "first_name": "Geoff",
        "goals": "0",
        "last_name": "Bent",
        "nationality": "England"
    },
    {
        "appearances": "12",
        "first_name": "Frank",
        "goals": "0",
        "last_name": "Kopel",
        "nationality": "Scotland"
    },
    {
        "appearances": "12",
        "first_name": "Tom",
        "goals": "0",
        "last_name": "Sloan",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "12",
        "first_name": "Tyler",
        "goals": "0",
        "last_name": "Blackett",
        "nationality": "England"
    },
    {
        "appearances": "12",
        "first_name": "Sergio",
        "goals": "0",
        "last_name": "Reguil\u00f3n",
        "nationality": "Spain"
    },
    {
        "appearances": "11",
        "first_name": "Samuel",
        "goals": "0",
        "last_name": "Parker",
        "nationality": "Scotland"
    },
    {
        "appearances": "11",
        "first_name": "James",
        "goals": "1",
        "last_name": "Vance",
        "nationality": "England"
    },
    {
        "appearances": "11",
        "first_name": "Edwin",
        "goals": "5",
        "last_name": "Lee",
        "nationality": "England"
    },
    {
        "appearances": "11",
        "first_name": "Jack",
        "goals": "3",
        "last_name": "Grundy",
        "nationality": "England"
    },
    {
        "appearances": "11",
        "first_name": "Charlie",
        "goals": "2",
        "last_name": "Richards",
        "nationality": "England"
    },
    {
        "appearances": "11",
        "first_name": "Edward",
        "goals": "0",
        "last_name": "Hudson",
        "nationality": "England"
    },
    {
        "appearances": "11",
        "first_name": "David",
        "goals": "0",
        "last_name": "Ellis",
        "nationality": "Scotland"
    },
    {
        "appearances": "11",
        "first_name": "Charlie",
        "goals": "0",
        "last_name": "Hannaford",
        "nationality": "England"
    },
    {
        "appearances": "11",
        "first_name": "Charlie",
        "goals": "2",
        "last_name": "Craven",
        "nationality": "England"
    },
    {
        "appearances": "11",
        "first_name": "Bobby",
        "goals": "0",
        "last_name": "Harrop",
        "nationality": "England"
    },
    {
        "appearances": "11",
        "first_name": "Peter",
        "goals": "0",
        "last_name": "Jones",
        "nationality": "England"
    },
    {
        "appearances": "11",
        "first_name": "Ronnie",
        "goals": "0",
        "last_name": "Briggs",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "11",
        "first_name": "Guillermo",
        "goals": "0",
        "last_name": "Varela",
        "nationality": "Uruguay"
    },
    {
        "appearances": "11",
        "first_name": "Bryan",
        "goals": "5",
        "last_name": "Mbeumo",
        "nationality": "Cameroon"
    },
    {
        "appearances": "11",
        "first_name": "Benjamin",
        "goals": "2",
        "last_name": "\u0160e\u0161ko",
        "nationality": "Slovenia"
    },
    {
        "appearances": "10",
        "first_name": "James",
        "goals": "1",
        "last_name": "Colville",
        "nationality": "unknown"
    },
    {
        "appearances": "10",
        "first_name": "John",
        "goals": "0",
        "last_name": "Davies",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "William",
        "goals": "2",
        "last_name": "Mathieson",
        "nationality": "Scotland"
    },
    {
        "appearances": "10",
        "first_name": "Bogie",
        "goals": "2",
        "last_name": "Roberts",
        "nationality": "unknown"
    },
    {
        "appearances": "10",
        "first_name": "Alfred",
        "goals": "1",
        "last_name": "Ambler",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Alexander",
        "goals": "0",
        "last_name": "Higgins",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Lawrence",
        "goals": "1",
        "last_name": "Smith",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Fred",
        "goals": "4",
        "last_name": "Williams",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Bob",
        "goals": "0",
        "last_name": "Valentine",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Harry",
        "goals": "5",
        "last_name": "Leonard",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Frank",
        "goals": "0",
        "last_name": "Brett",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Jimmy",
        "goals": "3",
        "last_name": "Bullock",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Matt",
        "goals": "0",
        "last_name": "Robinson",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Ron",
        "goals": "0",
        "last_name": "Davies",
        "nationality": "Wales"
    },
    {
        "appearances": "10",
        "first_name": "Steve",
        "goals": "0",
        "last_name": "Paterson",
        "nationality": "Scotland"
    },
    {
        "appearances": "10",
        "first_name": "Alan",
        "goals": "1",
        "last_name": "Davies",
        "nationality": "Wales"
    },
    {
        "appearances": "10",
        "first_name": "Mark",
        "goals": "0",
        "last_name": "Wilson",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Angel",
        "goals": "0",
        "last_name": "Gomes",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Willy",
        "goals": "0",
        "last_name": "Kambwala",
        "nationality": "DR Congo"
    },
    {
        "appearances": "10",
        "first_name": "Matheus",
        "goals": "1",
        "last_name": "Cunha",
        "nationality": "Brazil"
    },
    {
        "appearances": "9",
        "first_name": "Harry",
        "goals": "0",
        "last_name": "Erentz",
        "nationality": "Scotland"
    },
    {
        "appearances": "9",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Clark",
        "nationality": "Scotland"
    },
    {
        "appearances": "9",
        "first_name": "Gilbert",
        "goals": "4",
        "last_name": "Godsmark",
        "nationality": "England"
    },
    {
        "appearances": "9",
        "first_name": "Billy",
        "goals": "1",
        "last_name": "Richards",
        "nationality": "England"
    },
    {
        "appearances": "9",
        "first_name": "Harry",
        "goals": "0",
        "last_name": "Wilkinson",
        "nationality": "England"
    },
    {
        "appearances": "9",
        "first_name": "Herbert",
        "goals": "0",
        "last_name": "Broomfield",
        "nationality": "England"
    },
    {
        "appearances": "9",
        "first_name": "Ken",
        "goals": "2",
        "last_name": "MacDonald",
        "nationality": "Scotland"
    },
    {
        "appearances": "9",
        "first_name": "Arthur",
        "goals": "0",
        "last_name": "Chesters",
        "nationality": "England"
    },
    {
        "appearances": "9",
        "first_name": "Eddie",
        "goals": "4",
        "last_name": "Green",
        "nationality": "England"
    },
    {
        "appearances": "9",
        "first_name": "Charlie",
        "goals": "0",
        "last_name": "McGillivray",
        "nationality": "Scotland"
    },
    {
        "appearances": "9",
        "first_name": "Don",
        "goals": "1",
        "last_name": "Givens",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "9",
        "first_name": "Nick",
        "goals": "1",
        "last_name": "Powell",
        "nationality": "England"
    },
    {
        "appearances": "9",
        "first_name": "Ayden",
        "goals": "0",
        "last_name": "Heaven",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Roger",
        "goals": "1",
        "last_name": "Doughty",
        "nationality": "Wales"
    },
    {
        "appearances": "8",
        "first_name": "Frank",
        "goals": "0",
        "last_name": "Pepper",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Heathcote",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Ralph",
        "goals": "0",
        "last_name": "Gaudie",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Proctor",
        "goals": "2",
        "last_name": "Hall",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "John",
        "goals": "1",
        "last_name": "Ferguson",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Dick",
        "goals": "3",
        "last_name": "Black",
        "nationality": "Scotland"
    },
    {
        "appearances": "8",
        "first_name": "Charlie",
        "goals": "0",
        "last_name": "Hillam",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Jeff",
        "goals": "0",
        "last_name": "Wealands",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Mark",
        "goals": "0",
        "last_name": "Higgins",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Giuliano",
        "goals": "0",
        "last_name": "Maiorana",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Kevin",
        "goals": "0",
        "last_name": "Pilkington",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Terry",
        "goals": "1",
        "last_name": "Cooke",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Jonathan",
        "goals": "0",
        "last_name": "Spector",
        "nationality": "United States"
    },
    {
        "appearances": "8",
        "first_name": "Danny",
        "goals": "0",
        "last_name": "Simpson",
        "nationality": "England"
    },
    {
        "appearances": "8",
        "first_name": "Rodrigo",
        "goals": "0",
        "last_name": "Possebon",
        "nationality": "Italy"
    },
    {
        "appearances": "8",
        "first_name": "Mame",
        "goals": "1",
        "last_name": "Biram Diouf",
        "nationality": "Senegal"
    },
    {
        "appearances": "8",
        "first_name": "Chido",
        "goals": "0",
        "last_name": "Obi",
        "nationality": "Denmark"
    },
    {
        "appearances": "7",
        "first_name": "James",
        "goals": "0",
        "last_name": "Brown",
        "nationality": "Scotland"
    },
    {
        "appearances": "7",
        "first_name": "Herbert",
        "goals": "0",
        "last_name": "Stone",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "George",
        "goals": "5",
        "last_name": "Millar",
        "nationality": "Scotland"
    },
    {
        "appearances": "7",
        "first_name": "Rimmer",
        "goals": "2",
        "last_name": "Brown",
        "nationality": "unknown"
    },
    {
        "appearances": "7",
        "first_name": "George",
        "goals": "1",
        "last_name": "Foley",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Charles",
        "goals": "4",
        "last_name": "Mackie",
        "nationality": "Scotland"
    },
    {
        "appearances": "7",
        "first_name": "Arthur",
        "goals": "1",
        "last_name": "Hooper",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Ezra",
        "goals": "0",
        "last_name": "Royals",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Billy",
        "goals": "1",
        "last_name": "Goodwin",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "George",
        "goals": "2",
        "last_name": "Nicol",
        "nationality": "Scotland"
    },
    {
        "appearances": "7",
        "first_name": "Cliff",
        "goals": "0",
        "last_name": "Collinson",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Bill",
        "goals": "0",
        "last_name": "Fielding",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Peter",
        "goals": "0",
        "last_name": "Fletcher",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Clive",
        "goals": "0",
        "last_name": "Griffiths",
        "nationality": "Wales"
    },
    {
        "appearances": "7",
        "first_name": "Garth",
        "goals": "2",
        "last_name": "Crooks",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Chris",
        "goals": "0",
        "last_name": "Casper",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "John",
        "goals": "0",
        "last_name": "O'Kane",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Danny",
        "goals": "0",
        "last_name": "Higginbotham",
        "nationality": "Gibraltar"
    },
    {
        "appearances": "7",
        "first_name": "Danny",
        "goals": "0",
        "last_name": "Pugh",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Ben",
        "goals": "0",
        "last_name": "Amos",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Mr.",
        "goals": "2",
        "last_name": "Beb\u00e9",
        "nationality": "Cape Verde"
    },
    {
        "appearances": "7",
        "first_name": "James",
        "goals": "0",
        "last_name": "Garner",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Omari",
        "goals": "0",
        "last_name": "Forson",
        "nationality": "England"
    },
    {
        "appearances": "7",
        "first_name": "Harry",
        "goals": "0",
        "last_name": "Amass",
        "nationality": "England"
    },
    {
        "appearances": "6",
        "first_name": "Jack",
        "goals": "0",
        "last_name": "Owen",
        "nationality": "Wales"
    },
    {
        "appearances": "6",
        "first_name": "Arthur",
        "goals": "0",
        "last_name": "Henrys",
        "nationality": "Scotland"
    },
    {
        "appearances": "6",
        "first_name": "Thomas",
        "goals": "0",
        "last_name": "Sawyer",
        "nationality": "unknown"
    },
    {
        "appearances": "6",
        "first_name": "James",
        "goals": "0",
        "last_name": "Garvey",
        "nationality": "England"
    },
    {
        "appearances": "6",
        "first_name": "Arthur",
        "goals": "0",
        "last_name": "Marshall",
        "nationality": "England"
    },
    {
        "appearances": "6",
        "first_name": "James",
        "goals": "1",
        "last_name": "Thomson",
        "nationality": "Scotland"
    },
    {
        "appearances": "6",
        "first_name": "Sidney",
        "goals": "2",
        "last_name": "Evans",
        "nationality": "England"
    },
    {
        "appearances": "6",
        "first_name": "Billy",
        "goals": "4",
        "last_name": "Boyd",
        "nationality": "Scotland"
    },
    {
        "appearances": "6",
        "first_name": "Harry",
        "goals": "0",
        "last_name": "Worrall",
        "nationality": "England"
    },
    {
        "appearances": "6",
        "first_name": "Frank",
        "goals": "0",
        "last_name": "Haydock",
        "nationality": "England"
    },
    {
        "appearances": "6",
        "first_name": "Ian",
        "goals": "0",
        "last_name": "Donald",
        "nationality": "Scotland"
    },
    {
        "appearances": "6",
        "first_name": "David",
        "goals": "0",
        "last_name": "Wilson",
        "nationality": "England"
    },
    {
        "appearances": "6",
        "first_name": "Ritchie",
        "goals": "0",
        "last_name": "De Laet",
        "nationality": "Belgium"
    },
    {
        "appearances": "6",
        "first_name": "Zeki",
        "goals": "0",
        "last_name": "Fryers",
        "nationality": "England"
    },
    {
        "appearances": "5",
        "first_name": "William",
        "goals": "1",
        "last_name": "Campbell",
        "nationality": "Scotland"
    },
    {
        "appearances": "5",
        "first_name": "James",
        "goals": "1",
        "last_name": "Higson",
        "nationality": "England"
    },
    {
        "appearances": "5",
        "first_name": "George",
        "goals": "0",
        "last_name": "Lyons",
        "nationality": "Scotland"
    },
    {
        "appearances": "5",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Ford",
        "nationality": "England"
    },
    {
        "appearances": "5",
        "first_name": "Harry",
        "goals": "2",
        "last_name": "Williams",
        "nationality": "England"
    },
    {
        "appearances": "5",
        "first_name": "Albert",
        "goals": "1",
        "last_name": "Smith",
        "nationality": "Scotland"
    },
    {
        "appearances": "5",
        "first_name": "Arthur",
        "goals": "1",
        "last_name": "Thomson",
        "nationality": "England"
    },
    {
        "appearances": "5",
        "first_name": "Jimmy",
        "goals": "1",
        "last_name": "McClelland",
        "nationality": "Scotland"
    },
    {
        "appearances": "5",
        "first_name": "Ted",
        "goals": "0",
        "last_name": "Savage",
        "nationality": "England"
    },
    {
        "appearances": "5",
        "first_name": "Laurie",
        "goals": "2",
        "last_name": "Cunningham",
        "nationality": "England"
    },
    {
        "appearances": "5",
        "first_name": "Stephen",
        "goals": "0",
        "last_name": "Pears",
        "nationality": "England"
    },
    {
        "appearances": "5",
        "first_name": "Erik",
        "goals": "1",
        "last_name": "Nevland",
        "nationality": "Norway"
    },
    {
        "appearances": "5",
        "first_name": "Mr.",
        "goals": "0",
        "last_name": "Ricardo",
        "nationality": "Spain"
    },
    {
        "appearances": "5",
        "first_name": "Ritchie",
        "goals": "0",
        "last_name": "Jones",
        "nationality": "England"
    },
    {
        "appearances": "5",
        "first_name": "Zoran",
        "goals": "0",
        "last_name": "To\u0161i\u0107",
        "nationality": "Serbia"
    },
    {
        "appearances": "5",
        "first_name": "Michael",
        "goals": "0",
        "last_name": "Keane",
        "nationality": "England"
    },
    {
        "appearances": "5",
        "first_name": "Shola",
        "goals": "0",
        "last_name": "Shoretire",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Jack",
        "goals": "0",
        "last_name": "Powell",
        "nationality": "Wales"
    },
    {
        "appearances": "4",
        "first_name": "John",
        "goals": "0",
        "last_name": "Slater",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "John",
        "goals": "0",
        "last_name": "Graham",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "James",
        "goals": "1",
        "last_name": "Connachan",
        "nationality": "Scotland"
    },
    {
        "appearances": "4",
        "first_name": "Bill",
        "goals": "0",
        "last_name": "Williams",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Billy",
        "goals": "0",
        "last_name": "Ball",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "William",
        "goals": "0",
        "last_name": "Hartwell",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Ernest",
        "goals": "0",
        "last_name": "Thomson",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Aaron",
        "goals": "0",
        "last_name": "Hulme",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "John",
        "goals": "0",
        "last_name": "McGillivray",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Harold",
        "goals": "0",
        "last_name": "Hardman",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Tom",
        "goals": "0",
        "last_name": "Chorlton",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "John",
        "goals": "0",
        "last_name": "Howarth",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Jack",
        "goals": "2",
        "last_name": "Barber",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "James",
        "goals": "1",
        "last_name": "Miller",
        "nationality": "Scotland"
    },
    {
        "appearances": "4",
        "first_name": "Jimmy",
        "goals": "0",
        "last_name": "Bain",
        "nationality": "Scotland"
    },
    {
        "appearances": "4",
        "first_name": "Tom",
        "goals": "1",
        "last_name": "Harris",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Danny",
        "goals": "0",
        "last_name": "Ferguson",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "David",
        "goals": "3",
        "last_name": "Byrne",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "4",
        "first_name": "Herbert",
        "goals": "2",
        "last_name": "Heywood",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "George",
        "goals": "0",
        "last_name": "Nevin",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Reg",
        "goals": "1",
        "last_name": "Halton",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Robert",
        "goals": "0",
        "last_name": "Murray",
        "nationality": "Scotland"
    },
    {
        "appearances": "4",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Dougan",
        "nationality": "Scotland"
    },
    {
        "appearances": "4",
        "first_name": "Berry",
        "goals": "0",
        "last_name": "Brown",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Laurie",
        "goals": "0",
        "last_name": "Cassidy",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Lancaster",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Mike",
        "goals": "0",
        "last_name": "Pinner",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "George",
        "goals": "0",
        "last_name": "Buchan",
        "nationality": "Scotland"
    },
    {
        "appearances": "4",
        "first_name": "Paul",
        "goals": "0",
        "last_name": "Bielby",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Colin",
        "goals": "0",
        "last_name": "Waldron",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Nicky",
        "goals": "0",
        "last_name": "Wood",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Deiniol",
        "goals": "1",
        "last_name": "Graham",
        "nationality": "Wales"
    },
    {
        "appearances": "4",
        "first_name": "Phil",
        "goals": "0",
        "last_name": "Mulryne",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "4",
        "first_name": "Massimo",
        "goals": "0",
        "last_name": "Taibi",
        "nationality": "Italy"
    },
    {
        "appearances": "4",
        "first_name": "Daniel",
        "goals": "0",
        "last_name": "Nardiello",
        "nationality": "Wales"
    },
    {
        "appearances": "4",
        "first_name": "David",
        "goals": "0",
        "last_name": "Jones",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Fraizer",
        "goals": "0",
        "last_name": "Campbell",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Richard",
        "goals": "0",
        "last_name": "Eckersley",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Scott",
        "goals": "0",
        "last_name": "Wootton",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Wilfried",
        "goals": "0",
        "last_name": "Zaha",
        "nationality": "England\n Ivory Coast2"
    },
    {
        "appearances": "4",
        "first_name": "Ethan",
        "goals": "0",
        "last_name": "Wheatley",
        "nationality": "England"
    },
    {
        "appearances": "4",
        "first_name": "Senne",
        "goals": "0",
        "last_name": "Lammens",
        "nationality": "Belgium"
    },
    {
        "appearances": "3",
        "first_name": "Jack",
        "goals": "3",
        "last_name": "Doughty",
        "nationality": "Wales"
    },
    {
        "appearances": "3",
        "first_name": "John",
        "goals": "0",
        "last_name": "Mitchell",
        "nationality": "unknown"
    },
    {
        "appearances": "3",
        "first_name": "Alf",
        "goals": "3",
        "last_name": "Edge",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Bob",
        "goals": "0",
        "last_name": "McFarlane",
        "nationality": "Scotland"
    },
    {
        "appearances": "3",
        "first_name": "John",
        "goals": "1",
        "last_name": "Sneddon",
        "nationality": "Scotland"
    },
    {
        "appearances": "3",
        "first_name": "William",
        "goals": "0",
        "last_name": "Thompson",
        "nationality": "Scotland"
    },
    {
        "appearances": "3",
        "first_name": "Charles",
        "goals": "3",
        "last_name": "Rothwell",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Walter",
        "goals": "0",
        "last_name": "Whittaker",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "John",
        "goals": "0",
        "last_name": "Whitney",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "James",
        "goals": "1",
        "last_name": "Carman",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "William",
        "goals": "3",
        "last_name": "Brooks",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "John",
        "goals": "0",
        "last_name": "Turner",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Wilson",
        "goals": "0",
        "last_name": "Greenwood",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Reg",
        "goals": "0",
        "last_name": "Lawson",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Ernest",
        "goals": "0",
        "last_name": "Street",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Robertson",
        "nationality": "Scotland"
    },
    {
        "appearances": "3",
        "first_name": "Bernard",
        "goals": "0",
        "last_name": "Donaghey",
        "nationality": "Ireland"
    },
    {
        "appearances": "3",
        "first_name": "Archie",
        "goals": "0",
        "last_name": "Montgomery",
        "nationality": "Scotland"
    },
    {
        "appearances": "3",
        "first_name": "Frank",
        "goals": "0",
        "last_name": "Buckley",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "William",
        "goals": "0",
        "last_name": "Yates",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Joe",
        "goals": "1",
        "last_name": "Williams",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "William",
        "goals": "2",
        "last_name": "Hunter",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Arthur",
        "goals": "0",
        "last_name": "Cashmore",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Bert",
        "goals": "0",
        "last_name": "Cartman",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "David",
        "goals": "0",
        "last_name": "Lyner",
        "nationality": "Ireland"
    },
    {
        "appearances": "3",
        "first_name": "Wilfred",
        "goals": "0",
        "last_name": "Lievesley",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Billy",
        "goals": "0",
        "last_name": "Dennis",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Jack",
        "goals": "0",
        "last_name": "Hall",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Frank",
        "goals": "0",
        "last_name": "Williams",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "George",
        "goals": "0",
        "last_name": "Lydon",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Leslie",
        "goals": "0",
        "last_name": "Lievesley",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Ernie",
        "goals": "1",
        "last_name": "Thompson",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Jackie",
        "goals": "0",
        "last_name": "Scott",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "3",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Heron",
        "nationality": "Scotland"
    },
    {
        "appearances": "3",
        "first_name": "John",
        "goals": "0",
        "last_name": "Connaughton",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Alan",
        "goals": "0",
        "last_name": "Foggon",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "David",
        "goals": "0",
        "last_name": "Healy",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "3",
        "first_name": "Paul",
        "goals": "0",
        "last_name": "Rachubka",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Danny",
        "goals": "0",
        "last_name": "Webber",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Lee",
        "goals": "0",
        "last_name": "Roche",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Lee",
        "goals": "0",
        "last_name": "Martin",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Kieran",
        "goals": "1",
        "last_name": "Lee",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Dong",
        "goals": "0",
        "last_name": "Fangzhuo",
        "nationality": "China"
    },
    {
        "appearances": "3",
        "first_name": "Mr.",
        "goals": "0",
        "last_name": "Manucho",
        "nationality": "Angola"
    },
    {
        "appearances": "3",
        "first_name": "Ravel",
        "goals": "0",
        "last_name": "Morrison",
        "nationality": "Jamaica"
    },
    {
        "appearances": "3",
        "first_name": "Will",
        "goals": "0",
        "last_name": "Keane",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "3",
        "first_name": "Joel",
        "goals": "0",
        "last_name": "Castro Pereira",
        "nationality": "Portugal"
    },
    {
        "appearances": "3",
        "first_name": "Tom",
        "goals": "0",
        "last_name": "Heaton",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Tyler",
        "goals": "0",
        "last_name": "Fredricson",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Davies",
        "nationality": "Wales"
    },
    {
        "appearances": "2",
        "first_name": "Thomas",
        "goals": "1",
        "last_name": "Craig",
        "nationality": "unknown"
    },
    {
        "appearances": "2",
        "first_name": "William",
        "goals": "0",
        "last_name": "Sharpe",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "James",
        "goals": "1",
        "last_name": "Hendry",
        "nationality": "Scotland"
    },
    {
        "appearances": "2",
        "first_name": "S",
        "goals": "0",
        "last_name": "Prince",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "John",
        "goals": "1",
        "last_name": "Aitken",
        "nationality": "Scotland"
    },
    {
        "appearances": "2",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Wetherell",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Frank",
        "goals": "2",
        "last_name": "Wedge",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Owen",
        "goals": "0",
        "last_name": "Jones",
        "nationality": "Wales"
    },
    {
        "appearances": "2",
        "first_name": "Robert",
        "goals": "0",
        "last_name": "Turner",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Robert",
        "goals": "0",
        "last_name": "Walker",
        "nationality": "unknown"
    },
    {
        "appearances": "2",
        "first_name": "James",
        "goals": "1",
        "last_name": "Bain",
        "nationality": "Scotland"
    },
    {
        "appearances": "2",
        "first_name": "Peter",
        "goals": "0",
        "last_name": "Blackmore",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "William",
        "goals": "0",
        "last_name": "Booth",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "William",
        "goals": "0",
        "last_name": "Bunce",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Hugh",
        "goals": "0",
        "last_name": "Kerr",
        "nationality": "Scotland"
    },
    {
        "appearances": "2",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Schofield",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Arthur",
        "goals": "0",
        "last_name": "Young",
        "nationality": "Scotland"
    },
    {
        "appearances": "2",
        "first_name": "David",
        "goals": "0",
        "last_name": "Christie",
        "nationality": "Scotland"
    },
    {
        "appearances": "2",
        "first_name": "Tom",
        "goals": "0",
        "last_name": "Wilcox",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Ernest",
        "goals": "1",
        "last_name": "Payne",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Jack",
        "goals": "0",
        "last_name": "Quin",
        "nationality": "Scotland"
    },
    {
        "appearances": "2",
        "first_name": "Elijah",
        "goals": "0",
        "last_name": "Round",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Robert",
        "goals": "0",
        "last_name": "Roberts",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "John",
        "goals": "0",
        "last_name": "Williamson",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "James",
        "goals": "0",
        "last_name": "Pugh",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Richard",
        "goals": "0",
        "last_name": "Iddon",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Astley",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Ron",
        "goals": "0",
        "last_name": "Haworth",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Harold",
        "goals": "0",
        "last_name": "Dean",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Percy",
        "goals": "0",
        "last_name": "Newton",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Alf",
        "goals": "0",
        "last_name": "Ainsworth",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Tom",
        "goals": "0",
        "last_name": "Manns",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Len",
        "goals": "1",
        "last_name": "Bradbury",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "John",
        "goals": "0",
        "last_name": "Roach",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Dale",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Jimmy",
        "goals": "0",
        "last_name": "Pegg",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Ed",
        "goals": "0",
        "last_name": "McIlvenny",
        "nationality": "United States"
    },
    {
        "appearances": "2",
        "first_name": "John",
        "goals": "0",
        "last_name": "Walton",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Les",
        "goals": "0",
        "last_name": "Olive",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Gordon",
        "goals": "0",
        "last_name": "Clayton",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Baldwin",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Tony",
        "goals": "0",
        "last_name": "Grimshaw",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Peter",
        "goals": "1",
        "last_name": "Coyne",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Tom",
        "goals": "0",
        "last_name": "Connell",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "2",
        "first_name": "Mark",
        "goals": "0",
        "last_name": "Dempsey",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Derek",
        "goals": "0",
        "last_name": "Brazil",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "2",
        "first_name": "Paul",
        "goals": "0",
        "last_name": "Wratten",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Graeme",
        "goals": "0",
        "last_name": "Tomlinson",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "William",
        "goals": "0",
        "last_name": "Prunier",
        "nationality": "France"
    },
    {
        "appearances": "2",
        "first_name": "Michael",
        "goals": "0",
        "last_name": "Appleton",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Michael",
        "goals": "0",
        "last_name": "Twiss",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Andy",
        "goals": "0",
        "last_name": "Goram",
        "nationality": "Scotland"
    },
    {
        "appearances": "2",
        "first_name": "Bojan",
        "goals": "0",
        "last_name": "Djordjic",
        "nationality": "Sweden"
    },
    {
        "appearances": "2",
        "first_name": "Sylvan",
        "goals": "1",
        "last_name": "Ebanks-Blake",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Ryan",
        "goals": "0",
        "last_name": "Shawcross",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Joshua",
        "goals": "0",
        "last_name": "King",
        "nationality": "Norway"
    },
    {
        "appearances": "2",
        "first_name": "Marnick",
        "goals": "0",
        "last_name": "Vermijl",
        "nationality": "Belgium"
    },
    {
        "appearances": "2",
        "first_name": "Ryan",
        "goals": "0",
        "last_name": "Tunnicliffe",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "V\u00edctor",
        "goals": "0",
        "last_name": "Vald\u00e9s",
        "nationality": "Spain"
    },
    {
        "appearances": "2",
        "first_name": "Donald",
        "goals": "0",
        "last_name": "Love",
        "nationality": "Scotland"
    },
    {
        "appearances": "2",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Riley",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Lee",
        "goals": "0",
        "last_name": "Grant",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Ethan",
        "goals": "0",
        "last_name": "Laird",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Teden",
        "goals": "0",
        "last_name": "Mengi",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Martin",
        "goals": "0",
        "last_name": "D\u00fabravka",
        "nationality": "Slovakia"
    },
    {
        "appearances": "2",
        "first_name": "Dan",
        "goals": "0",
        "last_name": "Gore",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Robert",
        "goals": "0",
        "last_name": "Beckett",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Tom",
        "goals": "0",
        "last_name": "Burke",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Heber",
        "goals": "0",
        "last_name": "Davies",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "John",
        "goals": "0",
        "last_name": "Earp",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "James",
        "goals": "0",
        "last_name": "Gotheridge",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Edward",
        "goals": "0",
        "last_name": "Howles",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "A",
        "goals": "0",
        "last_name": "Longton",
        "nationality": "unknown"
    },
    {
        "appearances": "1",
        "first_name": "Charlie",
        "goals": "0",
        "last_name": "Harrison",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Tom",
        "goals": "0",
        "last_name": "Hay",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "George",
        "goals": "0",
        "last_name": "Owen",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Edgar",
        "goals": "0",
        "last_name": "Wilson",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "George",
        "goals": "1",
        "last_name": "Evans",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Bob",
        "goals": "0",
        "last_name": "Milarvie",
        "nationality": "Scotland"
    },
    {
        "appearances": "1",
        "first_name": "Bob",
        "goals": "0",
        "last_name": "Ramsay",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Herbert",
        "goals": "0",
        "last_name": "Dale",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "John",
        "goals": "0",
        "last_name": "Donnelly",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Charles",
        "goals": "0",
        "last_name": "Felton",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "William",
        "goals": "0",
        "last_name": "Gyves",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Thomas",
        "goals": "0",
        "last_name": "O'Shaughnessy",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "William",
        "goals": "0",
        "last_name": "Rattigan",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "William",
        "goals": "0",
        "last_name": "Turner",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Joseph",
        "goals": "0",
        "last_name": "Denman",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Joe",
        "goals": "0",
        "last_name": "Kinloch",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "William",
        "goals": "0",
        "last_name": "Brady",
        "nationality": "Scotland"
    },
    {
        "appearances": "1",
        "first_name": "David",
        "goals": "0",
        "last_name": "McFetteridge",
        "nationality": "Scotland"
    },
    {
        "appearances": "1",
        "first_name": "William",
        "goals": "0",
        "last_name": "Longair",
        "nationality": "Scotland"
    },
    {
        "appearances": "1",
        "first_name": "James",
        "goals": "0",
        "last_name": "Cairns",
        "nationality": "unknown"
    },
    {
        "appearances": "1",
        "first_name": "Robert",
        "goals": "1",
        "last_name": "Stephenson",
        "nationality": "unknown"
    },
    {
        "appearances": "1",
        "first_name": "James",
        "goals": "0",
        "last_name": "Cairns",
        "nationality": "unknown"
    },
    {
        "appearances": "1",
        "first_name": "William",
        "goals": "0",
        "last_name": "Owen",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "George",
        "goals": "0",
        "last_name": "Radcliffe",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "John",
        "goals": "0",
        "last_name": "Gourlay",
        "nationality": "Scotland"
    },
    {
        "appearances": "1",
        "first_name": "James",
        "goals": "0",
        "last_name": "Hopkins",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Edward",
        "goals": "1",
        "last_name": "Holt",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Samuel",
        "goals": "0",
        "last_name": "Johnson",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "George",
        "goals": "0",
        "last_name": "O'Brien",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "John",
        "goals": "0",
        "last_name": "Christie",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Harry",
        "goals": "0",
        "last_name": "Cleaver",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Jimmy",
        "goals": "0",
        "last_name": "Dyer",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Horace",
        "goals": "0",
        "last_name": "Blew",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Ted",
        "goals": "0",
        "last_name": "Dalton",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Kerr",
        "goals": "0",
        "last_name": "Whiteside",
        "nationality": "Scotland"
    },
    {
        "appearances": "1",
        "first_name": "Tommy",
        "goals": "0",
        "last_name": "Wilson",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Freddy",
        "goals": "0",
        "last_name": "Capper",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Pat",
        "goals": "0",
        "last_name": "McCarthy",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Jocelyn",
        "goals": "0",
        "last_name": "Rowe",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Albert",
        "goals": "0",
        "last_name": "Prince",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "John",
        "goals": "0",
        "last_name": "Prentice",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "George",
        "goals": "0",
        "last_name": "Schofield",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "George",
        "goals": "0",
        "last_name": "Albinson",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Percy",
        "goals": "0",
        "last_name": "Schofield",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Walter",
        "goals": "0",
        "last_name": "Taylor",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "William",
        "goals": "0",
        "last_name": "Sarvis",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Albert",
        "goals": "0",
        "last_name": "Broome",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Syd",
        "goals": "0",
        "last_name": "Tyler",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "John",
        "goals": "0",
        "last_name": "Whittle",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Andy",
        "goals": "0",
        "last_name": "Mitchell",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Billy",
        "goals": "0",
        "last_name": "Behan",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "1",
        "first_name": "Ben",
        "goals": "0",
        "last_name": "Morton",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "David",
        "goals": "0",
        "last_name": "Robbie",
        "nationality": "Scotland"
    },
    {
        "appearances": "1",
        "first_name": "David",
        "goals": "0",
        "last_name": "Jones",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Beaumont",
        "goals": "0",
        "last_name": "Asquith",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Bill",
        "goals": "1",
        "last_name": "Bainbridge",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Noel",
        "goals": "0",
        "last_name": "McFarlane",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "1",
        "first_name": "Paddy",
        "goals": "0",
        "last_name": "Kennedy",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "1",
        "first_name": "Walter",
        "goals": "0",
        "last_name": "Whitehurst",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Tony",
        "goals": "0",
        "last_name": "Hawksworth",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Reg",
        "goals": "0",
        "last_name": "Hunter",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Harold",
        "goals": "0",
        "last_name": "Bratt",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Dennis",
        "goals": "0",
        "last_name": "Walker",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Wilf",
        "goals": "0",
        "last_name": "Tranter",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Albert",
        "goals": "1",
        "last_name": "Kinsey",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Jimmy",
        "goals": "0",
        "last_name": "Kelly",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Jonathan",
        "goals": "0",
        "last_name": "Clark",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Martyn",
        "goals": "0",
        "last_name": "Rogers",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Anto",
        "goals": "0",
        "last_name": "Whelan",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "1",
        "first_name": "Peter",
        "goals": "0",
        "last_name": "Beardsley",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Neil",
        "goals": "0",
        "last_name": "Whitworth",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Ian",
        "goals": "0",
        "last_name": "Wilkinson",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Colin",
        "goals": "0",
        "last_name": "McKee",
        "nationality": "Scotland"
    },
    {
        "appearances": "1",
        "first_name": "Pat",
        "goals": "0",
        "last_name": "McGibbon",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "1",
        "first_name": "Alex",
        "goals": "0",
        "last_name": "Notman",
        "nationality": "Scotland"
    },
    {
        "appearances": "1",
        "first_name": "Nick",
        "goals": "0",
        "last_name": "Culkin",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Richie",
        "goals": "0",
        "last_name": "Wellens",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Jimmy",
        "goals": "0",
        "last_name": "Davis",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Mads",
        "goals": "0",
        "last_name": "Timm",
        "nationality": "Denmark"
    },
    {
        "appearances": "1",
        "first_name": "Mark",
        "goals": "0",
        "last_name": "Lynch",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Paul",
        "goals": "0",
        "last_name": "Tierney",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Eddie",
        "goals": "0",
        "last_name": "Johnson",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Adam",
        "goals": "0",
        "last_name": "Eckersley",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "David",
        "goals": "0",
        "last_name": "Gray",
        "nationality": "Scotland"
    },
    {
        "appearances": "1",
        "first_name": "Michael",
        "goals": "0",
        "last_name": "Barnes",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Phil",
        "goals": "0",
        "last_name": "Marsh",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "James",
        "goals": "0",
        "last_name": "Chester",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Larnell",
        "goals": "0",
        "last_name": "Cole",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Robbie",
        "goals": "0",
        "last_name": "Brady",
        "nationality": "Republic of Ireland"
    },
    {
        "appearances": "1",
        "first_name": "Tom",
        "goals": "0",
        "last_name": "Lawrence",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Saidy",
        "goals": "0",
        "last_name": "Janko",
        "nationality": "Gambia"
    },
    {
        "appearances": "1",
        "first_name": "Reece",
        "goals": "0",
        "last_name": "James",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Tom",
        "goals": "0",
        "last_name": "Thorpe",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Regan",
        "goals": "0",
        "last_name": "Poole",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "James",
        "goals": "0",
        "last_name": "Weir",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Demetri",
        "goals": "0",
        "last_name": "Mitchell",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Josh",
        "goals": "1",
        "last_name": "Harrop",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Di'Shon",
        "goals": "0",
        "last_name": "Bernard",
        "nationality": "Jamaica"
    },
    {
        "appearances": "1",
        "first_name": "Dylan",
        "goals": "0",
        "last_name": "Levitt",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "D'Mani",
        "goals": "0",
        "last_name": "Mellor",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Largie",
        "goals": "0",
        "last_name": "Ramazani",
        "nationality": "Belgium"
    },
    {
        "appearances": "1",
        "first_name": "Ethan",
        "goals": "0",
        "last_name": "Galbraith",
        "nationality": "Northern Ireland"
    },
    {
        "appearances": "1",
        "first_name": "Will",
        "goals": "0",
        "last_name": "Fish",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Zidane",
        "goals": "0",
        "last_name": "Iqbal",
        "nationality": "Iraq"
    },
    {
        "appearances": "1",
        "first_name": "Charlie",
        "goals": "0",
        "last_name": "Savage",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Charlie",
        "goals": "0",
        "last_name": "McNeill",
        "nationality": "England"
    },
    {
        "appearances": "201",
        "first_name": "Ella",
        "goals": "63",
        "last_name": "Toone",
        "nationality": "England"
    },
    {
        "appearances": "178",
        "first_name": "Millie",
        "goals": "11",
        "last_name": "Turner",
        "nationality": "England"
    },
    {
        "appearances": "164",
        "first_name": "Leah",
        "goals": "44",
        "last_name": "Galton",
        "nationality": "England"
    },
    {
        "appearances": "161",
        "first_name": "Katie",
        "goals": "32",
        "last_name": "Zelem",
        "nationality": "England"
    },
    {
        "appearances": "125",
        "first_name": "Mary",
        "goals": "0",
        "last_name": "Earps",
        "nationality": "England"
    },
    {
        "appearances": "110",
        "first_name": "Hayley",
        "goals": "11",
        "last_name": "Ladd",
        "nationality": "Wales"
    },
    {
        "appearances": "108",
        "first_name": "Maya",
        "goals": "11",
        "last_name": "Le Tissier",
        "nationality": "England"
    },
    {
        "appearances": "92",
        "first_name": "Hannah",
        "goals": "3",
        "last_name": "Blundell",
        "nationality": "England"
    },
    {
        "appearances": "90",
        "first_name": "Kirsty",
        "goals": "16",
        "last_name": "Hanson",
        "nationality": "Scotland"
    },
    {
        "appearances": "85",
        "first_name": "Rachel",
        "goals": "21",
        "last_name": "Williams",
        "nationality": "England"
    },
    {
        "appearances": "77",
        "first_name": "Ona",
        "goals": "3",
        "last_name": "Batlle",
        "nationality": "Spain"
    },
    {
        "appearances": "68",
        "first_name": "Melvine",
        "goals": "18",
        "last_name": "Malard",
        "nationality": "France"
    },
    {
        "appearances": "67",
        "first_name": "Amy",
        "goals": "4",
        "last_name": "Turner",
        "nationality": "England"
    },
    {
        "appearances": "66",
        "first_name": "Jessica",
        "goals": "26",
        "last_name": "Sigsworth",
        "nationality": "England"
    },
    {
        "appearances": "60",
        "first_name": "Jackie",
        "goals": "0",
        "last_name": "Groenen",
        "nationality": "Netherlands"
    },
    {
        "appearances": "60",
        "first_name": "Luc\u00eda",
        "goals": "16",
        "last_name": "Garc\u00eda",
        "nationality": "Spain"
    },
    {
        "appearances": "59",
        "first_name": "Alessia",
        "goals": "27",
        "last_name": "Russo",
        "nationality": "England"
    },
    {
        "appearances": "58",
        "first_name": "Kirsty",
        "goals": "1",
        "last_name": "Smith",
        "nationality": "Scotland"
    },
    {
        "appearances": "58",
        "first_name": "Hinata",
        "goals": "3",
        "last_name": "Miyazawa",
        "nationality": "Japan"
    },
    {
        "appearances": "57",
        "first_name": "Nikita",
        "goals": "25",
        "last_name": "Parris",
        "nationality": "England"
    },
    {
        "appearances": "57",
        "first_name": "Jayde",
        "goals": "1",
        "last_name": "Riviere",
        "nationality": "Canada"
    },
    {
        "appearances": "56",
        "first_name": "Lauren",
        "goals": "28",
        "last_name": "James",
        "nationality": "England"
    },
    {
        "appearances": "55",
        "first_name": "Aoife",
        "goals": "1",
        "last_name": "Mannion",
        "nationality": "Ireland"
    },
    {
        "appearances": "53",
        "first_name": "Martha",
        "goals": "8",
        "last_name": "Thomas",
        "nationality": "Scotland"
    },
    {
        "appearances": "52",
        "first_name": "Lisa",
        "goals": "6",
        "last_name": "Naalsund",
        "nationality": "Norway"
    },
    {
        "appearances": "49",
        "first_name": "Martha",
        "goals": "1",
        "last_name": "Harris",
        "nationality": "England"
    },
    {
        "appearances": "47",
        "first_name": "Phallon",
        "goals": "0",
        "last_name": "Tullis-Joyce",
        "nationality": "United States"
    },
    {
        "appearances": "45",
        "first_name": "Maria",
        "goals": "1",
        "last_name": "Thorisdottir",
        "nationality": "Norway"
    },
    {
        "appearances": "44",
        "first_name": "Vilde",
        "goals": "8",
        "last_name": "B\u00f8e Risa",
        "nationality": "Norway"
    },
    {
        "appearances": "42",
        "first_name": "Dominique",
        "goals": "2",
        "last_name": "Janssen",
        "nationality": "Netherlands"
    },
    {
        "appearances": "40",
        "first_name": "Lucy",
        "goals": "3",
        "last_name": "Staniforth",
        "nationality": "England"
    },
    {
        "appearances": "40",
        "first_name": "Elisabeth",
        "goals": "21",
        "last_name": "Terland",
        "nationality": "Norway"
    },
    {
        "appearances": "39",
        "first_name": "Mr.",
        "goals": "3",
        "last_name": "Geyse",
        "nationality": "Brazil"
    },
    {
        "appearances": "38",
        "first_name": "Gabby",
        "goals": "1",
        "last_name": "George",
        "nationality": "England"
    },
    {
        "appearances": "37",
        "first_name": "Celin",
        "goals": "7",
        "last_name": "Bizet D\u00f8nnum",
        "nationality": "Norway"
    },
    {
        "appearances": "34",
        "first_name": "Lizzie",
        "goals": "9",
        "last_name": "Arnot",
        "nationality": "Scotland"
    },
    {
        "appearances": "34",
        "first_name": "Jane",
        "goals": "7",
        "last_name": "Ross",
        "nationality": "Scotland"
    },
    {
        "appearances": "34",
        "first_name": "Anna",
        "goals": "1",
        "last_name": "Sandberg",
        "nationality": "Sweden"
    },
    {
        "appearances": "29",
        "first_name": "Mollie",
        "goals": "16",
        "last_name": "Green",
        "nationality": "England"
    },
    {
        "appearances": "28",
        "first_name": "Grace",
        "goals": "9",
        "last_name": "Clinton",
        "nationality": "England"
    },
    {
        "appearances": "27",
        "first_name": "Siobhan",
        "goals": "0",
        "last_name": "Chamberlain",
        "nationality": "England"
    },
    {
        "appearances": "27",
        "first_name": "Alex",
        "goals": "5",
        "last_name": "Greenwood",
        "nationality": "England"
    },
    {
        "appearances": "25",
        "first_name": "Abbie",
        "goals": "2",
        "last_name": "McManus",
        "nationality": "England"
    },
    {
        "appearances": "21",
        "first_name": "Charlie",
        "goals": "6",
        "last_name": "Devlin",
        "nationality": "England"
    },
    {
        "appearances": "21",
        "first_name": "Ivana",
        "goals": "2",
        "last_name": "Fuso",
        "nationality": "Brazil"
    },
    {
        "appearances": "19",
        "first_name": "Gemma",
        "goals": "0",
        "last_name": "Evans",
        "nationality": "Wales"
    },
    {
        "appearances": "19",
        "first_name": "Simi",
        "goals": "0",
        "last_name": "Awujo",
        "nationality": "Canada"
    },
    {
        "appearances": "17",
        "first_name": "Christen",
        "goals": "4",
        "last_name": "Press",
        "nationality": "United States"
    },
    {
        "appearances": "15",
        "first_name": "Aimee",
        "goals": "1",
        "last_name": "Palmer",
        "nationality": "England"
    },
    {
        "appearances": "13",
        "first_name": "Julia",
        "goals": "0",
        "last_name": "Zigiotti Olme",
        "nationality": "Sweden"
    },
    {
        "appearances": "11",
        "first_name": "Tobin",
        "goals": "4",
        "last_name": "Heath",
        "nationality": "United States"
    },
    {
        "appearances": "10",
        "first_name": "Lotta",
        "goals": "0",
        "last_name": "\u00d6kvist",
        "nationality": "Sweden"
    },
    {
        "appearances": "10",
        "first_name": "Carrie",
        "goals": "0",
        "last_name": "Jones",
        "nationality": "Wales"
    },
    {
        "appearances": "10",
        "first_name": "Sophie",
        "goals": "0",
        "last_name": "Baggaley",
        "nationality": "England"
    },
    {
        "appearances": "10",
        "first_name": "Jess",
        "goals": "4",
        "last_name": "Park",
        "nationality": "England"
    },
    {
        "appearances": "9",
        "first_name": "Jade",
        "goals": "2",
        "last_name": "Moore",
        "nationality": "England"
    },
    {
        "appearances": "9",
        "first_name": "Adriana",
        "goals": "3",
        "last_name": "Leon",
        "nationality": "Canada"
    },
    {
        "appearances": "9",
        "first_name": "Fridolina",
        "goals": "1",
        "last_name": "Rolf\u00f6",
        "nationality": "Sweden"
    },
    {
        "appearances": "7",
        "first_name": "Signe",
        "goals": "0",
        "last_name": "Bruun",
        "nationality": "Denmark"
    },
    {
        "appearances": "7",
        "first_name": "Irene",
        "goals": "0",
        "last_name": "Guerrero",
        "nationality": "Spain"
    },
    {
        "appearances": "6",
        "first_name": "Emily",
        "goals": "0",
        "last_name": "Ramsey",
        "nationality": "England"
    },
    {
        "appearances": "6",
        "first_name": "Diane",
        "goals": "0",
        "last_name": "Caldwell",
        "nationality": "Ireland"
    },
    {
        "appearances": "5",
        "first_name": "A\u00efssatou",
        "goals": "0",
        "last_name": "Tounkara",
        "nationality": "France"
    },
    {
        "appearances": "3",
        "first_name": "Naomi",
        "goals": "0",
        "last_name": "Hartley",
        "nationality": "England"
    },
    {
        "appearances": "3",
        "first_name": "Emma",
        "goals": "1",
        "last_name": "Watson",
        "nationality": "Scotland"
    },
    {
        "appearances": "2",
        "first_name": "Fran",
        "goals": "0",
        "last_name": "Bentley",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Keira",
        "goals": "0",
        "last_name": "Barry",
        "nationality": "England"
    },
    {
        "appearances": "2",
        "first_name": "Estelle",
        "goals": "0",
        "last_name": "Cascarino",
        "nationality": "France"
    },
    {
        "appearances": "1",
        "first_name": "Aurora",
        "goals": "0",
        "last_name": "Mikalsen",
        "nationality": "Norway"
    },
    {
        "appearances": "1",
        "first_name": "Rebecca",
        "goals": "0",
        "last_name": "May",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Tara",
        "goals": "0",
        "last_name": "Bourne",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Karna",
        "goals": "0",
        "last_name": "Solskj\u00e6r",
        "nationality": "Norway"
    },
    {
        "appearances": "1",
        "first_name": "Alyssa",
        "goals": "0",
        "last_name": "Aherne",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Evie",
        "goals": "0",
        "last_name": "Rabjohn",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Jess",
        "goals": "0",
        "last_name": "Simpson",
        "nationality": "England"
    },
    {
        "appearances": "1",
        "first_name": "Safia",
        "goals": "0",
        "last_name": "Middleton-Patel",
        "nationality": "Wales"
    },
    {
        "appearances": "1",
        "first_name": "Mared",
        "goals": "2",
        "last_name": "Griffiths",
        "nationality": "Wales"
    }
]