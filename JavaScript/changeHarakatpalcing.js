// const { match } = require("assert")
// Create text editor app
let shaddapart
let run = "first"
fs = require("fs")
// [ء-ي]\s[ء-ي]
mystring = " ‫ُد ُرو ٌس‬ ‫‪ ‬‬ ‫‪ ‬‬ ‫َد ْر ٌس"
mystring = mystring.trim()
// console.log(mystring)
String.prototype.replaceAt = function (index, replacement) {
  return this.substring(0, index) + replacement + this.substring(index + replacement.length)
}
sometext = `
‫َثا ِم ٌن‬
 / 
 / 
 ‫َأ َما َم‬ 

 ‫َخ ْل َف‬ 

‫ُم َنا َد ْو َن‬ ‫ُم َنا َدى‬ 
‫ ـ ٌة‬/ ‫ُـو َن‬
 ‫ُم َع َّر ٌف‬ 

‫َد َّرا َجا ٌت‬ ‫ُه َنا‬ 
‫ ـ ٌة‬/ ‫ُـو َن‬ 
‫ ـ ٌة‬/ ‫ُـو َن‬ ‫َظا ِه ٌر‬ 
 
 / ‫ُم َق َّد ٌر‬ 
 
 / ‫َأ ْم ِري َكا‬ 

 / ‫َأ ْل َما ِن َيا‬ 

 / ‫ِإ ْن َك ْل َ َّتا‬ 

 ‫َف َرْن َسا‬ 

 / ‫ُس ِوي ْْ َسا‬ 
 
‫َت ْع ِب ر َتا ٌت‬ ‫َت ْع ِب ر ٌت‬ 
 
‫َس َكا ِك ر نُي‬ ‫ِس ِّك ر نٌي‬ 

‫َم َحا ِري ُب‬ ‫ِم ْح َرا ٌب‬ 
 !
 / ‫َح ِّو ْل‬ 

`
// function useRegex(input) {
//   let regex = /‬/g
//   // console.log(input)
//   let regex2 = /‫-‬‬/g
//   newString = input.replaceAll(regex, "").replaceAll(regex2, "")
//   fs.writeFile("modifi.txt", newString, function (err) {
//     if (err) return console.log(err)
//     console.log("File saved")
//   })
// }

// console.log(useRegex(sometext))

if (run === "first") {
  regfatha2x = /\u064e\u064e/g
  reglaamfatha2x = /\u0644\u064e\u064e/g
  laamfathaAlif = "\u0644\u064e\u0627"

  matchRegex = /\u0651\u064e\u0644/g
  const regex = /\u064e\u0644/g

  let modify = (text) => {
    console.log("yay")
    // console.log(stringArr.map((el) => el.replaceAll(searchRegEx, "\u0644\u0627")))
    const found = text.match(matchRegex)
    if (found) {
      console.log("Found")
      console.log(found)
      console.log(text.replaceAll(regex, "\u0644\u0627"))
      return text.replaceAll(regex, "\u0644\u0627")
    }
    return text
  }

  stringArr = sometext
    .replace(/(\n\n)/gm, "\n")
    .split("\n")
    .map((element) => element.trim())
  // .map(modify)

  // console.log("yay")
  // // console.log(stringArr.map((el) => el.replaceAll(searchRegEx, "\u0644\u0627")))
  // stringArr.forEach((element) => {
  //   const found = element.match(matchRegex)
  //   if (found) {
  //     console.log(found)
  //   }
  //   console.log(element.replaceAll(regex, "\u0644\u0627"))
  // })

  let harakats = [
    ["fatha", "\u064e"],
    ["kasra", "\u0650"],
    ["doma", "\u064f"],
    ["fatha2", "\u064b"],
    ["kasra2", "\u064d"],
    ["doma2", "\u064c"],
    ["sukun", "\u0652"],
    ["shadda", "\u0651"],
  ]
  const harakatMap = new Map(harakats)
  // console.log(harakatMap)
  let output
  let result = []

  stringArr.forEach((mystring) => {
    output = mystring
    // console.log(mystring.charAt(5))

    harakatMap.forEach(function (value, key) {
      let indexes = []
      // console.log(key)
      for (let index = 0; index < mystring.length; index++) {
        if (mystring[index] === value) {
          indexes.push(index)
        }
      }

      if (indexes.length >= 1) {
        console.log(key + " - " + indexes)

        removedstr = output.replaceAll(value, "")

        for (let i = 0; i < indexes.length; i++) {
          const index = indexes[i]
          console.log(index)
          pos1 = index
          pos2 = index + 1

          var a = removedstr
          var b = value
          var position = pos2
          output = [a.slice(0, position), b, a.slice(position)].join("")
          if (key === "shadda") {
            console.log("shadda!!!")
            shaddapart = output.charAt(index - 1)
            console.log(shaddapart)
            // output = output.replaceAt(index - 3, "")
            a = output
            b = shaddapart
            position = pos2
            output = [a.slice(0, position), b, a.slice(position)].join("")
            // console.log(shaddapart)
          }
          removedstr = output
        }

        // console.log("output")
        // console.log(removedstr)
        // console.log(mystring)
        // console.log(output)
      }
    })
    output = output.replace(/‬ ‫‪/, ",")
    // console.log(output)
    output = output.replace(/\s+/g, "")
    output = output.replaceAll(reglaamfatha2x, laamfathaAlif).replaceAll(regfatha2x, "")
    result.push(output)
  })

  console.log("result")
  towrite = result.join("\n")
  console.log(towrite)
  fs.writeFile("testi1.txt", towrite, function (err) {
    if (err) return console.log(err)
    console.log("File saved")
  })
}
