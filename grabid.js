const currentUrl = window.location.href;
console.log(currentUrl);
var preemID = currentUrl.split("=").pop()
console.log(preemID)
reemID = preemID.replace(/[a-zA-Z]/g,function(c){return String.fromCharCode((c<="Z"?90:122)>=(c=c.charCodeAt(0)+13)?c:c-26);});
console.log(reemID);
function makeid(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
      counter += 1;
    }
    return result;
};
eemID = makeid(2);
emID = reemID.concat(eemID);

console.log(makeid(5));
