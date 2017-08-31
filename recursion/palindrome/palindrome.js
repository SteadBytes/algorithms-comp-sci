// Returns the first character of the string str
function firstCharacter(str) {
    return str.slice(0, 1);
};

// Returns the last character of a string str
function lastCharacter(str) {
    return str.slice(-1);
};

// Returns the string that results from removing the first
//  and last characters from str
function middleCharacters(str) {
    return str.slice(1, -1);
};

function isPalindrome(str) {
    // base case #1
    if (str.length <= 1) {
        return true;
    }
    // base case #2
    if (firstCharacter(str) !== lastCharacter(str)) {
        return false;
    }
    // recursive case
    return isPalindrome(middleCharacters(str));
};

function checkPalindrome(str) {
    console.log("Is this word a palindrome? " + str);
    console.log(isPalindrome(str));
};

checkPalindrome("a");
console.assert(isPalindrome("a") === true);
checkPalindrome("motor");
console.assert(isPalindrome("motor") === false);
checkPalindrome("rotor");
console.assert(isPalindrome("rotor") === true);
console.assert(isPalindrome("hello") === false);
console.assert(isPalindrome("hannah") === true);