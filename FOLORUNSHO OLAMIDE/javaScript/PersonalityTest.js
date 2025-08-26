const prompt = require('prompt-sync')();
let optionA = []
let optionB = []
let invalid = []
let countA = 0
let countB = 0
let count = 0 

let name = prompt("What is your fullname: ")



console.log("QUESTION 1. You regularly make new friends.\n")
let noOneQuestion =prompt("A.Agree        B.DisAgree:").toUpperCase();
if(noOneQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noOneQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}

console.log("QUESTION 2. Complex and novel ideas excite you more than simple and straightforward ones.\n")
let noTwoQuestion =prompt("A. Agree        B. DisAgree: ").toUpperCase();
if(noTwoQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noTwoQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 3. You usually feel more persuaded by what resonates emotionally with you than by factual arguments.\n")
let noThreeQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noThreeQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noThreeQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 4. Your living and working spaces are clean and organized.\n")
let noFourQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noFourQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noFourQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 5. You usually stay calm, even under a lot of pressure.\n")
let noFiveQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noFiveQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noFiveQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 6. You find the idea of networking or promoting yourself to strangers very daunting.\n")
let noSixQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noSixQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noSixQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 7. You prioritize and plan tasks effectively, often completing them well before the deadline.\n")
let noSevenQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noSevenQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noSevenQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 8. People’s stories and emotions speak louder to you than numbers or data.\n")
let noEightQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noEightQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noEightQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 9. You like to use organizing tools like schedules and lists.\n")
let noNineQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noNineQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noNineQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 10. Even a small mistake can cause you to doubt your overall abilities and knowledge.\n")
let noTenQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noTenQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noTenQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 11. You feel comfortable just walking up to someone you find interesting and striking up a conversation.\n")
let noElevenQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noElevenQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noElevenQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 12. You are not too interested in discussions about various interpretations of creative works.\n")
let noTwelveQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noTwelveQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noTwelveQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 13. You prioritize facts over people’s feelings when determining a course of action.\n")
let noThirteenQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noThirteenQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noThirteenQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 14. Even a small mistake can cause you to doubt your overall abilities and knowledge.\n")
let noForteenQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noForteenQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noForteenQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 15. You often allow the day to unfold without any schedule at all.\n")
let noFifteenQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noFifteenQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noFifteenQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 16. You rarely worry about whether you make a good impression on people you meet.\n")
let noSixteenQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noSixteenQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noSixteenQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 17. You enjoy participating in team-based activities.\n")
let noSeventeenQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noSeventeenQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noSeventeenQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 18. You enjoy experimenting with new and untested approaches.\n")
let noEighteenQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noEighteenQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noEighteenQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 19. You prioritize being sensitive over being completely honest.\n")
let noNineteenQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noNineteenQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noNineteenQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log("QUESTION 20. You actively seek out new experiences and knowledge areas to explore.\n")
let noTwentyQuestion =prompt("A.Agree        B.DisAgree: ").toUpperCase();
if(noTwentyQuestion == "A") {
	optionA.push("A.Agree")
	countA++
}
else if(noTwentyQuestion == "B"){
	optionB.push("B.DisAgree")
	countB++
}else {
	invalid.push("invalid input")
	count++
}
console.log(name)
console.log(optionA)
console.log(optionB) 
console.log(invalid)
console.log("Total 'Agree' responses:", countA++)
console.log( "Total 'DsAgree' responses:" , countB++)
console.log("Total 'invalid input' responses:", count++)	


