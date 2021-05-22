
console.log(module);
module.exports.getDate = function() {
  const options = { weekday: 'long', year: '2-digit', month: 'long', day: '2-digit' };
  const today  = new Date();

  // console.log(today.toLocaleDateString("en-US")); // 9/17/2016
  // console.log(today.toLocaleDateString("en-US", options)); // Saturday, September 17, 2016
  // console.log(today.toLocaleDateString("hi-IN", options)); // शनिवार, 17 सितंबर 2016
  // day = today.toLocaleDateString("zh-TW", options);
  const day = today.toLocaleDateString("ja-JP", options);
  return day
}


module.exports.getDay = function() {
  const options = { weekday: 'long'};
  const today  = new Date();
  const day = today.toLocaleDateString("ja-JP", options);
  return day
}
