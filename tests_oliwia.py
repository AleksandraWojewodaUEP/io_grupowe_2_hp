from main import *

fundusz = {
    "knut": [1,2,3],
    "sykl": [1,2,4],
    "galeon": [4,5,6]
}

assert(licz_sume(fundusz) == {
    "knut": 6,
    "sykl": 7,
    "galeon": 15
})

fundusz = {
    "knut": [1,2,3],
    "sykl": [0],
    "galeon": [4,5,6]
}

assert(licz_sume(fundusz) == {
    "knut": 6,
    "sykl": 0,
    "galeon": 15
})

fundusz = {
    "knut": [4,6,11],
    "sykl": [1,2,15],
    "galeon": [7,3]
}

assert(licz_sume(fundusz) == {
    "knut": 0,
    "sykl": 2,
    "galeon": 11
})

fundusz = {
    "knut": [0],
    "sykl": [34,2],
    "galeon": [0]
}

assert(licz_sume(fundusz) == {
    "knut": 0,
    "sykl": 2,
    "galeon": 2
})


